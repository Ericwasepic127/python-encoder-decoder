"""
Welcome to libary \033[1m coder \033[0m !!
This is encodes and decodes
"""
def encoder(item, key):
    """
    Encoder function.
    Arguments:
    - item: Item to encode
    - key: Key to encode with
    """
    result = []
    limit = 1114112
    for char in item:
        new_val = (ord(char) + key) % limit
        result.append(chr(new_val))
    return "".join(result)

def decoder(item, key):
    """
    Decoder function.
    Arguments:
    - item: Item to decode
    - key: Key to decode with
    """
    result = []
    limit = 1114112
    for char in item:
        new_val = (ord(char) - key) % limit
        result.append(chr(new_val))
    return "".join(result)

__version__ = "V1.0"
__all_dict__ = {
  "encoder": encoder,
  "decoder": decoder
}
__all__ = list(__all_dict__.keys())
