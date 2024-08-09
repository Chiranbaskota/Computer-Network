# utils.py
import hashlib
import json
import os
import struct
import tempfile
from bencode import decode_bencode, bencode

def decode_torrentfile(filename):
    try:
        with open(filename, "rb") as f:              
            bencoded_content = f.read()           ## open and read file in binary read mode
            if not bencoded_content:
                raise ValueError(f"The file {filename} is empty.")
            decoded_value, remainder = decode_bencode(bencoded_content)             
            if remainder:
                raise ValueError("Undecoded remainder.")
            return decoded_value
    except FileNotFoundError:
        raise FileNotFoundError(f"File {filename} not found.")
    except Exception as e:
        raise ValueError(f"Error reading or decoding file {filename}: {e}")

def piece_hashes(pieces):
    n = 20                       # standard length for SHA-1
    if len(pieces) % n != 0:
        raise ValueError("Piece hashes do not add up to a multiple of 20 bytes.")
    return [pieces[i: i + n] for i in range(0, len(pieces), n)]                    #(start=0, stop= total_length_of_piece , step=20)
