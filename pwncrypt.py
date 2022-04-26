from pystyle import Colorate, Colors
import pwncryption
from colorama import Fore
import os
import sys

os.system("cls")

def crypter(file, mode, file_key="pwncryption.key", strength=16):
    if mode == "encrypt":
        print(f'{Fore.LIGHTBLACK_EX}[{Fore.GREEN}*{Fore.LIGHTBLACK_EX}] {Fore.WHITE}Encrypting file "{file}"\n')
        pwncryption.encrypt(file, strength)
        print(f"{Fore.GREEN}Done.{Fore.RESET}")

    if mode == "decrypt":
        print(f'{Fore.LIGHTBLACK_EX}[{Fore.GREEN}*{Fore.LIGHTBLACK_EX}] {Fore.WHITE}Decrypting file "{file}"\n')
        pwncryption.decrypt(file, file_key)
        print(f"{Fore.GREEN}Done.{Fore.RESET}")
            

try:
    file = sys.argv[1]
    mode = sys.argv[2]
    if mode == "decrypt":
        try:
            file_key = sys.argv[3]
        except:
            print(f'{Fore.LIGHTBLACK_EX}[{Fore.YELLOW}-{Fore.LIGHTBLACK_EX}] {Fore.WHITE}Decrypting with default file : "pwncryption.pwn"')
    
    if mode == "encrypt":
        try:
            strength = sys.argv[3]
        except:
            print(f'{Fore.LIGHTBLACK_EX}[{Fore.YELLOW}-{Fore.LIGHTBLACK_EX}] {Fore.WHITE}Encrypting with default strength : 16')


    crypter(file, mode)
except:
    print(f"{Fore.LIGHTBLACK_EX}[{Fore.RED}x{Fore.LIGHTBLACK_EX}] {Fore.YELLOW}Usage {Fore.LIGHTBLACK_EX}:{Fore.YELLOW} pwncrypt {Fore.LIGHTBLACK_EX}[{Fore.YELLOW}file{Fore.LIGHTBLACK_EX}] [{Fore.YELLOW}mode{Fore.LIGHTBLACK_EX} -{Fore.YELLOW} decrypt{Fore.LIGHTBLACK_EX}/{Fore.YELLOW}encrypt{Fore.LIGHTBLACK_EX}] {Fore.LIGHTBLACK_EX}[{Fore.MAGENTA}Third Argument{Fore.LIGHTBLACK_EX}]\n\n{Fore.YELLOW}Third Argument{Fore.LIGHTBLACK_EX} -{Fore.MAGENTA} encrypt{Fore.LIGHTBLACK_EX} : {Fore.YELLOW}supply {Fore.MAGENTA}encryption strength{Fore.YELLOW} as the third argument or one will be supplied for you\nThird Argument {Fore.LIGHTBLACK_EX}-{Fore.MAGENTA} decrypt{Fore.LIGHTBLACK_EX} :{Fore.YELLOW} supply a {Fore.MAGENTA}file key{Fore.YELLOW} as the third argument or the default will be used{Fore.RESET}")
    





