"""
Sample:
Use it sample
"""
def encoder(item, key):
    result = []
    limit = 1114112
    for char in item:
        new_val = (ord(char) + key) % limit
        result.append(chr(new_val))
    return "".join(result)

def decoder(item, key):
    result = []
    limit = 1114112
    for char in item:
        new_val = (ord(char) - key) % limit
        result.append(chr(new_val))
    return "".join(result)

if __name__ == '__main__':
  run = "Y"
  while run == "Y":
    code = input("Item to encode: ")
    key = int(input("Key: ")
    print(encoder(code, key))
    run = input("Want to run again (Y/n)? ")

  runs = "Y"
  while runs == "Y":
    code = input("Item to decode: ")
    key = int(input("Key: ")
    print(decoder(code, key))
    runs = input("Want to run again (Y/n)? ")

print("Ended sample!")
