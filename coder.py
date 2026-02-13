"""
Welcome to libary \033[1m coder \033[0m !!
This is encodes and decodes text, uses key
"""

class InvaildError(Exception): pass

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
    
class TwoTimeKey:
    """
    Generates Encode-Decode Random key
    Used only once for Encode-Decode Pattern
    Example:
        user1 = TwoTimeKey()
        user2 = TwoTimeKey()
        var1 = user1.encoder("Example password: Pass1234") # send to user2
        var2 = user2.encoder(var1) # send to user1
        var3 = user1.decoder(var2) # send to user2
        var4 = user2.decoder(var3) # User2 gets message: 'Example password: Pass1234'
        print(var4)
    """
    def __init__(self):
        self.used = 0
        self.done = False
        self.genkey()

    def __repr__(self):
        return "Used" if self.done else "Not used"

    def genkey(self, to=10**8):
        from random import randint as k
        self.key = k(-to, to)
        self.done = False
        self.used = 0

    def encoder(self, text):
        """Encodes text: Use first"""
        if self.used != 0 or self.done:
            raise InvaildError("Already used!")
        self.used = 1
        return encoder(text, key)

    def decoder(self, text):
        """Decodes text: Use last"""
        if self.used != 1 or self.done:
            raise InvaildError("Not used!")
        self.done = True
        self.used = 2
        yes = decoder(text, key)
        del self.key
        return yes

    def __getattr__(self, name):
        if name == "decoder":
            return self.decoder
        if name == "encoder":
            return self.encoder
        if name == "key":
            return self.key
        raise AttributeError("Safe mode is on for " + str(name))

__version__ = "V1.0"
__all_dict__ = {
  "encoder": encoder,
  "decoder": decoder,
  "TwoTimeKey": TwoTimeKey
}
__all__ = list(__all_dict__.keys())
