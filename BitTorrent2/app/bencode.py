
def decode_bencode(bencoded_value):
    if not bencoded_value:
        raise ValueError("Empty bencoded value.")
    if chr(bencoded_value[0]).isdigit():
        return decode_string(bencoded_value)
    elif chr(bencoded_value[0]) == "i":
        return decode_int(bencoded_value)
    elif chr(bencoded_value[0]) == "l":
        return decode_list(bencoded_value)
    elif chr(bencoded_value[0]) == "d":
        return decode_dict(bencoded_value)
    else:
        raise NotImplementedError("We only support strings, integers, lists, and dicts.")


def decode_string(bencoded_value):  ## format   b"5:Hello3:foo"
    first_colon_index = bencoded_value.find(b":")       
    if first_colon_index == -1:
        raise ValueError("Not a string")
    length_string = int(bencoded_value[:first_colon_index])
    decoded_string = bencoded_value[first_colon_index + 1: first_colon_index + 1 + length_string]
    bencoded_remainder = bencoded_value[first_colon_index + 1 + length_string:]
    return decoded_string, bencoded_remainder

def decode_int(bencoded_value):  # format b'i32e'
    if chr(bencoded_value[0]) != "i":            ## starts with i?
        raise ValueError("Not an integer")
    end_int = bencoded_value.find(b"e")           ## ends with e?
    if end_int == -1:
        raise ValueError("Not an integer")
    decoded_int = int(bencoded_value[1:end_int])
    bencoded_remainder = bencoded_value[end_int + 1:]
    return decoded_int, bencoded_remainder

def decode_list(bencoded_value):       # format b'l 5:helloi32e e '
    if chr(bencoded_value[0]) != "l":      ## starts with l?
        raise ValueError("Not a list")
    bencoded_remainder = bencoded_value[1:]             ## 5:helloi32e e
    decoded_list = []
    while chr(bencoded_remainder[0]) != "e":      ## perform until it finds e?
        decoded_value, bencoded_remainder = decode_bencode(bencoded_remainder)
        decoded_list.append(decoded_value)
    return decoded_list, bencoded_remainder[1:]

def decode_dict(bencoded_value):    # format b'd 3:foo3:bar 5:helloi32e e'
    if chr(bencoded_value[0]) != "d":
        raise ValueError("Not a dict")
    bencoded_remainder = bencoded_value[1:]
    decoded_dict = {}
    while chr(bencoded_remainder[0]) != "e":
        decoded_key, bencoded_remainder = decode_string(bencoded_remainder)   #decoded key =foo
        decoded_value, bencoded_remainder = decode_bencode(bencoded_remainder) ## bencoded remainder = 3:bar5:helloi32ee
        decoded_dict[decoded_key.decode()] = decoded_value                       #converted to string using .decode
    return decoded_dict, bencoded_remainder[1:]



def bencode_string(unencoded_value):
    length = len(unencoded_value)
    return (str(length) + ":" + unencoded_value).encode()

def bencode_bytes(unencoded_value):
    length = len(unencoded_value)
    return str(length).encode() + b":" + unencoded_value

def bencode_int(unencoded_value):
    return ("i" + str(unencoded_value) + "e").encode()

def bencode_list(unencoded_value):
    result = b"l"
    for i in unencoded_value:
        result += bencode(i)
    return result + b"e"

def bencode_dict(unencoded_value):
    result = b"d"
    for k in unencoded_value:
        result += bencode(k) + bencode(unencoded_value[k])
    return result + b"e"

def bencode(unencoded_value):
    if isinstance(unencoded_value, str):
        return bencode_string(unencoded_value)
    elif isinstance(unencoded_value, bytes):
        return bencode_bytes(unencoded_value)
    elif isinstance(unencoded_value, int):
        return bencode_int(unencoded_value)
    elif isinstance(unencoded_value, list):
        return bencode_list(unencoded_value)
    elif isinstance(unencoded_value, dict):
        return bencode_dict(unencoded_value)
    else:
        raise ValueError("Can only bencode strings, ints, lists, or dicts.")
