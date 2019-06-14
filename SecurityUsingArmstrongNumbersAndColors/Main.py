from Encryptor import  Encryption
from Decryptor import  Decryption
from Colors import ColorManager


def main():
    key = "how old is my computer"
    enc = Encryption(key)

    enc.encrypt("f:/a.txt", "f:/aa.txt")

    dec = Decryption(key)
    dec.decrypt("f:/aa.txt", "f:/aaa.txt")

    print("DONE")

main()