import sys
sys.path.append("..")
from game import *
import pytest


def test_choose_word():
    game = Game()
    word = game.word
    assert word in WORDS

def test_draw_word():
    game = Game()
    game.word = 'pytest'
    game.correct_letters = ['p', 'y']
    assert game.draw_word() == 'py____'

def test_check_correct_letter():
    game = Game()
    game.word = 'pytest'
    assert game.check_letter('p') == 0

def test_check_wrong_letter():
    game = Game()
    game.word = 'pytest'
    assert game.check_letter('q') == 1

def test_check_correct_used_letter():
    game = Game()
    game.word = 'pytest'
    game.correct_letters = ['p']
    assert game.check_letter('p') == -1