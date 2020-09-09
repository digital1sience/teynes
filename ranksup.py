import os
from sys import platform
import time
import random
# Create <clear> function
clear = None
if platform == "win32" :
    clear = lambda: os.system("cls")
else:
    clear = lambda: os.system("clear")

class Item:
    """ Item in shop
    """
    def __init__(self, name, cost, item_code):
        self.name = name
        self.cost = cost
        self.item_code = item_code

class Shop:
    """ Items in shop
    """
    items = []
    def __init__(self):
        self.items.append(Item("+20 exp", 10, 0))
        self.items.append(Item("+60 энергии", 30, 1))
        self.items.append(Item("поменять имя", 10, 2))
        self.items.append(Item("VIP на 10 ходов", 30, 3))
    def get_item(self, id):
        return self.items[id]

class Task:
    """ Generate task
    """
    def __init__(self, player):
        self.chance = random.randint(1, 100)
        self.exp = random.randint(1, 5)
        self.is_done = False
        self.add_chance_cost = int(random.randint(2, 5) * self.exp)
        if (player.is_vip):
            self.exp += random.randint(0, 3)
    def done(self):
        self.is_done = True
        return self.exp
    def skip(self):
        return int(self.exp / 2)

class Player:
    """ Player data.
    """
    def __init__(self):
        self.name = ""
        self.level = 1
        self.rank_number = 0
        self.exp_to_next_level = 4
        self.up_rank = 0
        self.completed_tasks = 0
        self.money = 0
        self.is_vip = False
        self.stamina = 100
        self.exp = 0
        self.task_to_end_vip = 0

    def add_exp(self, exp):
        for i in range(exp):
            self.exp += 1
            if self.exp_to_next_level == self.exp:
                self.add_level()
    def add_level(self):
        self.level += 1
        self.exp_to_next_level += 4
        self.exp = 0
        if self.stamina < 100:
            self.stamina = 100
        money = random.randint(5, 25)
        self.money += money
        if self.level % 5 == 0 and self.rank_number < len(_game.ranks):
            self.rank_number += 1
        clear()
        print(f"Поздравляю, новый уровень! Вы получили {money}")
        time.sleep(1)

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

class View:
    """ Contains functions to print messages.
    """
    def welcome_message(self):
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
        time.sleep(1)
        print("")
    def main_message(self, player, ranks):
        """ Send to player main message.
        """
        clear()
        print("*=========================*")
        print(f"Имя : {player.name}")
        print(f"Ранг : {ranks[player.rank_number]} [{player.rank_number}]")
        print(f"Уровень : {player.level} [{player.exp}/{player.exp_to_next_level} exp.]")
        print(f"Выполнено заданий: {player.completed_tasks}")
        print(f"Энергия : {player.stamina}")
        print(f"Деньги : {player.money} $")
        if player.is_vip:
            print(f"VIP Окончание через : {player.task_to_end_vip}\n\tВ 1.5 раза увеличивает награду и в 2 раза уменьшает сумму проигрыша и энергии")
        print("*=========================*")
    def menu(self, task, vip):
        """ Send menu to player
        """
        if vip:
            print(f"\n[1] - отправится на задание. Шанс на успех : {task.chance} %. При успешном прохождении ты получишь : {int(task.exp * 1.5)}")
        else:
            print(f"\n[1] - отправится на задание. Шанс на успех : {task.chance} %. При успешном прохождении ты получишь : {task.exp}")
        print(f"[2] - отправится на задание с шансом +15% за {task.add_chance_cost}$")
        print(f"[3] - магазин")
        print(f"[4] - сохранить и выйти\n")
    def complete_task(self, task, vip):
        clear()
        if vip:
            print(f"Вы выполнили задание и получили {int(task.exp * 1.5)}")
        else:
            print(f"Вы выполнили задание и получили {task.exp}")
        time.sleep(1)   
    def failed_task(self, task, vip):
        clear()
        if vip:
            print(f"Вы провалили задание и потеряли {task.exp}$")
        else:
            print(f"Вы провалили задание и потеряли {task.exp * 2}$")
        time.sleep(1)
    def shop_menu(self, shop):
        clear()
        for i in range(len(shop.items)):
            print(f"[{i+1}] - Купить {shop.get_item(i).name} за {shop.get_item(i).cost}$")

class Game:
    """ Main Game Logic.
    """
    def __init__(self):
        self.player = Player()
        self.crypt = Crypt()
        self.view = View()
        self.task = Task(self.player)
        self.shop = Shop()
        self.version = "1.0.3"
        self.ranks = ["Рядовой", "Ефрейтор", "Мл. Сержант", "Сержант", "Ст. Сержант", "Старшина", "Прапорщик", "Ст. Прапорщик", "Мл. Лейтенант", "Лейтенант", "Ст. Лейтенант", "Капитан", "Майор", "Подполковник", "Полковник", "Генерал майор", "Генерал лейтенант", "Генерал полковник", "Генерал армии", "Маршал России"]

    def check_data_file(self):
        """ Check data file. When exists returns True, else False.
        """
        for i in os.listdir():
            if i == "data.bin":
                return True
        return False

    def save_data_file(self):
        text = [self.player.name, self.player.level, self.player.rank_number, \
                self.player.exp_to_next_level, self.player.up_rank, \
                self.player.completed_tasks, self.player.money, self.player.is_vip, self.player.stamina, \
                self.player.exp, self.player.task_to_end_vip
            ]
        for i, el in enumerate(text):
            text[i] = str(el)
        with open("data.bin", "w") as f:
            f.write(self.crypt.encrypt('|'.join(text)))

    def load_data_file(self):
        with open("data.bin", "r") as f:
            text = self.crypt.decrypt(f.read()) # Строка из "value|value"
        text_lines = text.split("|") # Список из "value"
        self.player.name = text_lines[0]
        self.player.level = int(text_lines[1])
        self.player.rank_number = int(text_lines[2])
        self.player.exp_to_next_level = int(text_lines[3])
        self.player.up_rank = int(text_lines[4])
        self.player.completed_tasks = int(text_lines[5])
        self.player.money = int(text_lines[6])
        if (text_lines[7] == "True"):
            self.player.is_vip = True
        else:
            self.player.is_vip = False
        self.player.stamina = int(text_lines[8])
        self.player.exp = int(text_lines[9])
        self.player.task_to_end_vip = int(text_lines[10])

    def run(self):
        """ Run app.
        """
        if (self.check_data_file()):
            self.start()
        else:
            self.start(True)
            
    def start(self, new=False):
        """ Start game.
        """
        self.view.welcome_message()
        if (new):
            while self.player.name == "":
                self.player.name = input("Введи своё имя, рядовой: ")
        else:
            self.load_data_file()
            print("Добро пожаловать, " + self.player.name + "!")
        while True:
            if (self.task.is_done):
                self.task = Task(self.player)
            if (self.player.task_to_end_vip == 0):
                self.player.is_vip = False
            choosed_number = ""
            while type(choosed_number) != int:
                try:
                    self.view.main_message(self.player, self.ranks)
                    self.view.menu(self.task, self.player.is_vip)
                    choosed_number = int(input(">>> "))
                except:
                    pass
            if choosed_number == 1:
                self.player.stamina -= 5
                if (self.player.is_vip):
                    self.player.stamina += 2
                    self.player.task_to_end_vip -= 1
                    if self.task.chance >= random.randint(1,100):
                        self.player.add_exp(int(self.task.done() * 1.5))
                        self.player.completed_tasks += 1
                        self.view.complete_task(self.task, self.player.is_vip)
                    else:
                        self.player.money -= self.task.done()
                        self.view.failed_task(self.task, self.player.is_vip)
                else:
                    if self.task.chance >= random.randint(1,100):
                        self.player.add_exp(self.task.done())
                        self.player.completed_tasks += 1
                        self.view.complete_task(self.task, self.player.is_vip)
                    else:
                        self.player.money -= self.task.done() * 2
                        self.view.failed_task(self.task, self.player.is_vip)
            elif choosed_number == 2:
                if self.player.money < self.task.add_chance_cost:
                    print("У вас нехватает денег")
                    time.sleep(1)
                    continue
                else:
                    self.player.money -= self.task.add_chance_cost
                self.player.stamina -= 5
                if (self.player.is_vip):
                    self.player.stamina += 2
                    self.player.task_to_end_vip -= 1
                    if self.task.chance + 15 >= random.randint(1,100):
                        self.player.add_exp(int(self.task.done() * 1.5))
                        self.player.completed_tasks += 1
                        self.view.complete_task(self.task, self.player.is_vip)
                    else:
                        self.player.money -= self.task.done()
                        self.view.failed_task(self.task, self.player.is_vip)
                else:
                    if self.task.chance + 15 >= random.randint(1,100):
                        self.player.add_exp(self.task.done())
                        self.player.completed_tasks += 1
                        self.view.complete_task(self.task, self.player.is_vip)
                    else:
                        self.player.money -= self.task.done() * 2
                        self.view.failed_task(self.task, self.player.is_vip)
            elif choosed_number == 3:
                item_id = ""
                while type(item_id) != int:
                    try:
                        self.view.shop_menu(self.shop)
                        item_id = int(input(">>> "))
                        item_id -= 1
                        if item_id >= len(self.shop.items):
                            item_id = ""
                    except:
                        pass
                    if self.shop.get_item(item_id).cost > self.player.money:
                        print("Недостаточно денег")
                        time.sleep(1)
                        break
                    if item_id == 0:
                        self.player.money -= self.shop.get_item(item_id).cost
                        self.player.add_exp(20)
                    elif item_id == 1:
                        self.player.money -= self.shop.get_item(item_id).cost
                        self.player.stamina += 60
                    elif item_id == 2:
                        self.player.money -= self.shop.get_item(item_id).cost
                        self.player.name = input("Введите новое имя: ")
                    elif item_id == 3:
                        self.player.money -= self.shop.get_item(item_id).cost
                        self.player.is_vip = True
                        self.player.task_to_end_vip += 10
                    else:
                        break
                    print(f"Вы купили {self.shop.get_item(item_id).name} за {self.shop.get_item(item_id).cost}")
            elif choosed_number == 4:
                break
            else:
                print("Данного варианта нет в меню.")
                time.sleep(1)
  
        self.save_data_file()



if __name__ == "__main__":
    _game = Game()
    _game.run()