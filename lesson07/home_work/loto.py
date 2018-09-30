#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11      
      16 49    55 88    77    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""
import random

class Loto:
    def __init__(self):
        """
        state - статус игры (0 - игры нет, 1 - ход, 2 - game over)
        """
        self.barrels = Barrel()
        self.players = Players(2)
        self.state = 0

    def start_game(self):
        self.state = 1
        while self.state == 1:
            self.choice_barrel()
            self.take_barrel_computer()
            GameDrawer(self)
            self.take_barrel_human()
        GameDrawer(self)

    def take_barrel_human(self):
        take_barrel = input("Зачеркнуть цифру? (y/n): ").lower() == 'y'
        if take_barrel:
            if self.barrels.current in self.players.human.card:
                self.players.human.card_print = self.players.human.card_print.replace(str(self.barrels.current) + " ", "x ")
                self.players.human.card.remove(self.barrels.current)
                if len(self.players.human.card) == 0:
                    self.state = 2
                    self.players.winner = "Вы"
            else:
                self.state = 2
                self.players.winner = "Компьютер"
        else:
            if self.barrels.current in self.players.human.card:
                self.state = 2
                self.players.winner = "Компьютер"

    def take_barrel_computer(self):
        if self.barrels.current in self.players.computer.card:
            self.players.computer.card_print = self.players.computer.card_print.replace(str(self.barrels.current) + " ", "x ")
            self.players.computer.card.remove(self.barrels.current)
            if len(self.players.human.card) == 0:
                self.state = 2
                self.players.winner = "Компьютер"

    def choice_barrel(self):
        if len(self.barrels.bucket) > 0:
            barrel = random.choice(self.barrels.bucket)
            self.barrels.bucket.remove(barrel)
            self.barrels.current = barrel
        else:
            self.state = 0


class Barrel:
    def __init__(self):
        self.bucket = list(range(1,91))
        self.current = 0


class GameDrawer:
    def __init__(self,loto_game):
        if loto_game.state == 1:
            print('Новый бочонок: {} (осталось {}) \n'.format(loto_game.barrels.current, len(loto_game.barrels.bucket)))
            print(loto_game.players.human.card_print)
            print(loto_game.players.computer.card_print)
        if loto_game.state == 2:
            print('Игра окончена, победитель {}'.format(loto_game.players.winner))
        if loto_game.state == 0:
            print("эм")

    @staticmethod
    def print_card(card, player_title):
        str_card = f'{player_title} \n'
        row = 1
        card_idx = 0
        while row <= 3:
            empty_column_indx = random.sample(range(1, 10), k=4)
            col = 1
            str_card += "  "
            while col <= 9:
                if col in empty_column_indx:
                    str_card += "_ "
                else:
                    str_card += f'{card[card_idx]} '
                    card_idx += 1
                col += 1
            str_card += "\n"
            row += 1
        str_card += "-------------------------- \n"
        return str_card



class PlayerCardIterObj:
    def __init__(self, count_players=2):
        self.i = 0
        self.count_players = count_players

    def __next__(self):
        self.i += 1
        if self.i <= self.count_players:
            return random.sample(range(1, 91), k=15)
        else:
            raise StopIteration


class PlayerCardIter:

    def __init__(self, count_players=2):
        self.count_players = count_players

    def __iter__(self):
        return PlayerCardIterObj(self.count_players)







class Human:
    def __init__(self, card):
        self.card = card
        self.card_print = GameDrawer.print_card(card, "------ Ваша карточка -----")

class Computer:
    def __init__(self, card):
        self.card = card
        self.card_print = GameDrawer.print_card(card, "-- Карточка компьютера ---")

class Players:
    def __init__(self, count_players):
        self.cards = []
        self.winner = ""
        self.gen_cards(count_players)
        self.human = Human(self.cards[0])
        self.computer = Computer(self.cards[1])

    def gen_cards(self, count_players):
        for idx, el in enumerate(PlayerCardIter(2)):
            self.cards.append(el)


loto = Loto()

loto.start_game()

