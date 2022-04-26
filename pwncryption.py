import random
import string

def encrypt(file, strength=16):
    encrypted_data = []
    encryption_strength = strength
    encryption_characters = string.ascii_letters + string.digits + "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    encryption_map = {} 
    for char in encryption_characters:
        key = ''.join(random.choice(encryption_characters)for _ in range(encryption_strength))
        encryption_map[char] = key  
    encryption_map['%'] = ''.join(random.choice(encryption_characters)for _ in range(encryption_strength))
    encryption_map["^"] = ''.join(random.choice(encryption_characters)for _ in range(encryption_strength))
    f=open(file, "r")
    for line in f:
        for letter in line:
            if letter == " ":
                encrypted_data.append(encryption_map['%'])
            elif letter == "\n":
                encrypted_data.append(encryption_map['^'])

            else:
                encrypted_data.append(encryption_map[letter]) 



    f.close()
    f=open(file, "w")
    for data in encrypted_data:
        f.write(data)
    f=open("pwncryption.key", "w+")
    for value in encryption_map:
        f.write(f"{value} : {encryption_map[value]}\n")
    

def decrypt(file, file_key="pwncryption.key"):
    decryption_key = {}
    f=open(file_key, "r")
    for line in f:
        key = line[:1]
        decryption_key[key] = line[4:].removesuffix("\n")
    decryption_key1 = {v: k for k, v in decryption_key.items()}
    f.close()
    f = open(file, "r")
    data = str(f.read())
    data = str(data)
    x = len(decryption_key['a'])
    n=x
    msg = [data[i:i+n] for i in range(0, len(data), n)]
    decrypted_msg = []
    for letter in msg:
        for l in decryption_key:
            if decryption_key[l] == letter:
                if decryption_key1[decryption_key[l]] == '%':
                    decrypted_msg.append(" ")
                elif decryption_key1[decryption_key[l]] == "^":
                    decrypted_msg.append("\n")
                else:
                    decrypted_msg.append(decryption_key1[decryption_key[l]])

    
    print(''.join(decrypted_msg))
