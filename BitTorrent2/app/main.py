
import sys
import json
import tempfile
from torrent import print_info, download, download_piece
from network import get_peers, split_peers, init_handshake
from utils import decode_bencode


def bytes_to_str(data):
    if isinstance(data, bytes):
        return data.decode()
    raise TypeError(f"Type not serializable: {type(data)}")


def main():
    command = sys.argv[1]
    if command == "decode":
        bencoded_value = sys.argv[2].encode()
        decoded_value, remainder = decode_bencode(bencoded_value)
        if remainder:
            raise ValueError("Undecoded remainder.")
        print(json.dumps(decoded_value, default=bytes_to_str))
    elif command == "info":
        if len(sys.argv) != 3:
            raise NotImplementedError(f"Usage: {sys.argv[0]} info filename")
        filename = sys.argv[2]
        print_info(filename)
    elif command == "peers":
        if len(sys.argv) != 3:
            raise NotImplementedError(f"Usage: {sys.argv[0]} peers filename")
        filename = sys.argv[2]
        peers = split_peers(get_peers(filename))
        for p in peers:
            print(p)
    elif command == "handshake":
        if len(sys.argv) != 4:
            raise NotImplementedError(
                f"Usage: {sys.argv[0]} handshake filename <peer_ip>:<peer_port>")
        filename = sys.argv[2]
        peer = sys.argv[3]
        peer_socket, received_message = init_handshake(filename, peer)
        received_id = received_message[48:68].hex()
        print("Peer ID:", received_id)
        peer_socket.close()
    elif command == "download_piece":
        if len(sys.argv) != 6:
            raise NotImplementedError(
                f"Usage: {sys.argv[0]} download_piece -o output filename piececount")
        outputfile = sys.argv[3]
        filename = sys.argv[4]
        piececount = int(sys.argv[5])
        p, o = download_piece(outputfile, filename,
                              piececount, tempfile.gettempdir())
        print("Piece %i downloaded to %s" % (p, o))
    elif command == "download":
        if len(sys.argv) != 5:
            raise NotImplementedError(
                f"Usage: {sys.argv[0]} download -o output filename")
        outputfile = sys.argv[3]
        filename = sys.argv[4]
        download(outputfile, filename)
        print("Download %s to %s" % (filename, outputfile))
    else:
        raise NotImplementedError(f"Unknown command {command}")


if __name__ == "__main__":
    main()
