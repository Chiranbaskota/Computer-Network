# torrent.py
import hashlib
import os
import tempfile
from network import construct_message, get_peers, init_handshake, receive_message, request_block, verify_message
from network import split_peers
from bencode import bencode
from utils import decode_torrentfile, piece_hashes

def print_info(filename):
    decoded_value = decode_torrentfile(filename)
    print("Tracker URL:", decoded_value["announce"].decode())
    print("Length:", decoded_value["info"]["length"])
    info_hash = hashlib.sha1(bencode(decoded_value["info"])).hexdigest()
    print("Info Hash:", info_hash)
    print("Piece Length:", decoded_value["info"]["piece length"])
    print("Piece Hashes:")
    hashes = piece_hashes(decoded_value["info"]["pieces"])
    for h in hashes:
        print(h.hex())
        
def download_piece(outputfile, filename, piececount, tempdir):
    decoded_value = decode_torrentfile(filename)
    peers = split_peers(get_peers(filename))
    # For the sake of simplicity, at this stage, just use the first peer:
    peer = peers[0]
    s, received_message = init_handshake(filename, peer)
    # Wait for bitfield message:
    bitfield = receive_message(s)
    verify_message(bitfield, 5)
    # Build and send interested message
    interested = construct_message(2, b"")
    s.send(interested)
    # Wait for unchoke message
    unchoke = receive_message(s)
    while unchoke[4] != 1:
        unchoke = receive_message(s)
    verify_message(unchoke, 1)
    # Calculate number of blocks, figuring out if we are the last piece
    last_piece_remainder = (
        decoded_value["info"]["length"] % decoded_value["info"]["piece length"]
    )
    total_pieces = len(piece_hashes(decoded_value["info"]["pieces"]))
    if piececount + 1 == total_pieces and last_piece_remainder > 0:
        length = last_piece_remainder
    else:
        length = decoded_value["info"]["piece length"]
    block_size = 16 * 1024
    full_blocks = length // block_size
    final_block = length % block_size
    # Send request for a block. This is painfully duplicated at the moment
    # to handle corner case where only have a small block.
    piece = b""
    sha1hash = hashlib.sha1()
    if full_blocks == 0:
        block = request_block(s, piececount, 0, final_block)
        piece += block
        sha1hash.update(block)
    else:
        for i in range(full_blocks):
            block = request_block(s, piececount, i, block_size)
            piece += block
            sha1hash.update(block)
        if final_block > 0:
            block = request_block(s, piececount, i + 1, final_block)
            piece += block
            sha1hash.update(block)
    # Verify piece hash
    piece_hash = piece_hashes(decoded_value["info"]["pieces"])[piececount]
    local_hash = sha1hash.digest()
    if piece_hash != local_hash:
        raise ValueError("Piece hash mismatch.")
    # Write piece to disk
    piece_path = os.path.join(tempdir, f"test-{piececount}")
    with open(piece_path, "wb") as piece_file:
        piece_file.write(piece)
    # Clean up
    s.close()
    # Return piece completed and location
    return piececount, piece_path
    pass

def download(outputfile, filename):
    decoded_value = decode_torrentfile(filename)
    total_pieces = len(piece_hashes(decoded_value["info"]["pieces"]))
    piecefiles = []
    with tempfile.TemporaryDirectory() as tempdir:
        for piece in range(total_pieces):
            p, o = download_piece("/tmp/test-" + str(piece),
                                  filename, piece, tempdir)
            piecefiles.append(o)
        with open(outputfile, "ab") as result_file:
            for piecefile in piecefiles:
                with open(piecefile, "rb") as piece_file:
                    result_file.write(piece_file.read())
                os.remove(piecefile)
    pass
