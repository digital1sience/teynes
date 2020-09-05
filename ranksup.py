# Version 1.0.0

import os
from sys import platform
import time
# Create <clear> function
clear = None
if platform == "win32" :
    clear = lambda: os.system("cls")
else:
    clear = lambda: os.system("clear")

class Player:
    """ Player data.
    """
    pass

class Crypt:
    """ Encrypt and Decrypt logic.
    """
    def encrypt(self, text):
        """ Returns Encrypted text.
        """
        a_byte_array = bytearray(text, "utf-8")
        byte_list = []
        for byte in a_byte_array:
            byte_list.append(bin(byte))
        return ' '.join(byte_list)
    def decrypt(self, text):
        """ Returns Decrypted text.
        """
        binary_values = text.split()
        rstring = ""
        for binary_value in binary_values:
            an_integer = int(binary_value, 2)
            rstring += chr(an_integer)
        return rstring

class Game:
    """ Main Game Logic
    """
    def __init__(self):
        self.player = Player()

    def check_data_file(self):
        """ Check data file. When exists returns True, else False.
        """
        for i in os.listdir():
            if i == "data.bin":
                return True
        return False

    def save_data_file(self):
        pass

    def welcome(self):
        """ Send to player welcome message.
        """
        clear()
        print("WELCOME TO")
        time.sleep(0.2)
        print(" ____             _        _   _ ____  ")
        time.sleep(0.2)
        print("|  _ \ __ _ _ __ | | _____| | | |  _ \ ")
        time.sleep(0.2)
        print("| |_) / _` | '_ \| |/ / __| | | | |_) |")
        time.sleep(0.2)
        print("|  _ < (_| | | | |   <\__ \ |_| |  __/ ")
        time.sleep(0.2)
        print("|_| \_\__,_|_| |_|_|\_\___/\___/|_|   ")
        time.sleep(0.2)
        print("")

    def run(self):
        if (self.check_data_file()):
            self.start()
        else:
            self.start(True)
            
    def start(self, new=False):
        if (new):
            self.welcome()
            self.player.name = input("Введи своё имя, рядовой: ")
        else:
            self.welcome()
            print("Добро пожаловать, " + name + "!")



if __name__ == "__main__":
    _game = Game()
    _game.run()
