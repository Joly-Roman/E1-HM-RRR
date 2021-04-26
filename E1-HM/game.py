import random
import sys

WORDS = ['skillfactory', 'testing', 'blackbox', 'pytest', 'unittest', 'coverage']



class Game():
    def __init__(self):
        self.word = random.choice(WORDS)
        self.false_tries = 0
        self.correct_letters = []


    def start(self):
        self.__init__()
        print(f'Привет,это игра в Виселицу , попробуй угадать слово ({self.word}), у тебя 4 права на ошибку')
        self.step()


    def step(self):
        if self.draw_word() == self.word:
            self.win()

        if self.false_tries >= 4:
            self.lose()

        print(f'{self.draw_word()}  (неверных ответов - {self.false_tries})')
        tried_letter = self.get_letter()
        if self.check_letter(tried_letter) == -1:
            print('Буква уже отгадана')
            self.step()
        if self.check_letter(tried_letter) == 1:
            print('Такой буквы нет')
            self.false_tries += 1
            self.step()
        else:
            print('Такая буква есть!!')
            self.correct_letters.append(tried_letter)
            self.step()


    def win(self):
        print(f'Поздравляю,ты отгадал(а) слово -- {self.word}')
        answer = str(input('Сыграем еще раз? (да/нет): '))
        if answer == 'да':
            self.start()
        else:
            print("Never gonna give you up\n"
                  "Never gonna let you down\n"
                  "Never gonna run around and desert you\n"
                  "Never gonna make you cry\n"
                  "Never gonna say goodbye\n"
                  "Never gonna tell a lie and hurt you")
            sys.exit()

    def lose(self):
            print('Ты проиграл!!!')
            answer = str(input('Сыграем еще раз? (да/нет): '))
            if answer == 'да':
                self.start()
            else:
                sys.exit()

    def get_letter(self):
        tried_letter = str(input('Введи букву: '))
        return tried_letter


    def check_letter(self, letter):
        if letter in list(self.word):
            if letter in self.correct_letters:
                return -1
            else:
                return 0
        else:
            return 1


    def draw_word(self):
        word_condition = []
        for letter in self.word:
            if letter in self.correct_letters:
                word_condition.append(letter)
            else:
                word_condition.append('_')
        return ''.join(word_condition)



game = Game()
if __name__ == '__main__':
    game.start()
