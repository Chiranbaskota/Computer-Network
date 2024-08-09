import socket
import struct
import hashlib
import requests
from utils import decode_torrentfile, piece_hashes
from bencode import decode_bencode, bencode

def get_peers(filename):
    decoded_value = decode_torrentfile(filename)          ## generally decoded_value in dict {key : value}pairs
    tracker_url = decoded_value["announce"].decode()
    info_hash = hashlib.sha1(bencode(decoded_value["info"])).digest()
    peer_id = "00112233445566778899"
    port = 6881
    uploaded = 0
    downloaded = 0
    left = decoded_value["info"]["length"]    ## total size of file ,client needs to download initally, length of file
    compact = 1                                ## compact=0  (verbose)human readable form 
    params = dict(
        info_hash=info_hash,
        peer_id=peer_id,
        port=port,
        uploaded=uploaded,
        downloaded=downloaded,
        left=left,
        compact=compact,
    )
    result = requests.get(tracker_url, params=params)
    decoded_result = decode_bencode(result.content)[0]
    return decoded_result["peers"]             ##compacted

def split_peers(peers):
    if len(peers) % 6 != 0:     #(6 bytes : 4 bytes for ip and 2 for port)
        raise ValueError("Peer list from tracker does not divide into 6 bytes; did you use compact?")
    uncompacted_peers = []
    for peer in [peers[i: i + 6] for i in range(0, len(peers), 6)]:   #(start, stop, step) and insert in list peers
        ip = str(peer[0]) + "." + str(peer[1]) + "." + str(peer[2]) + "." + str(peer[3])
        port = str(int.from_bytes(peer[4:], byteorder="big", signed=False)) #converting last two bytes in int from bytes
        uncompacted_peers.append(ip + ":" + port)
    return uncompacted_peers

def init_handshake(filename, peer):
    decoded_value = decode_torrentfile(filename)
    peer_colon = peer.find(":")
    ip = peer[:peer_colon]
    port = int(peer[peer_colon + 1:])
    length_prefix = struct.pack(">B", 19)
    protocol_string = b"BitTorrent protocol"
    reserved_bytes = b"\x00" * 8
    info_hash = hashlib.sha1(bencode(decoded_value["info"])).digest()
    peer_id = b"00112233445566778899"
    message = length_prefix + protocol_string + reserved_bytes + info_hash + peer_id   #68 byte
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                             ## ipv4 for addressing and TCp as transport
    s.connect((ip, port))
    s.send(message)
    received_message = s.recv(68)
    return s, received_message

def construct_message(message_id, payload):              ##message_id=6 (request a piece of data)
    message_id = message_id.to_bytes(1, byteorder='big')
    message = message_id + payload
    length = len(message)
    length_prefix = length.to_bytes(4, byteorder='big')
    message = length_prefix + message
    return message

def verify_message(message, message_id):  ##message_id = 7 send piece of data
    if message[4] != message_id:
        raise ValueError("Expected message of id %s, but received id %s" % (message_id, message[4]))
    if int.from_bytes(message[:4], byteorder='big') != len(message[4:]):
        raise ValueError("Message wrong length.")

def request_block(s, piece_index, block_index, length):
    index = piece_index
    begin = block_index * 2**14                     #16kb
    payload = struct.pack(">I", index) + struct.pack(">I", begin) + struct.pack(">I", length)      ##each 4 byte
    message = construct_message(6, payload)     ##(message_id , payload)
    s.send(message)
    piece_message = receive_message(s)
    while piece_message[4] != 7:                        ##receive until messade_id=7 , 5th index of piece_message= message_id
        piece_message = receive_message(s)
    verify_message(piece_message, 7)
    received_index = int.from_bytes(piece_message[5:9], byteorder='big')
    received_begin = int.from_bytes(piece_message[9:13], byteorder='big')
    if received_index != index or received_begin != begin:
        raise ValueError("Piece message does not have expected payload.")
    block = piece_message[13:]
    return block

def receive_message(s):
    length = s.recv(4)
    while len(length) < 4:
        length += s.recv(4 - len(length))
    message_length = int.from_bytes(length, byteorder='big')
    message = s.recv(message_length)
    while len(message) < message_length:
        message += s.recv(message_length - len(message))
    return length + message
