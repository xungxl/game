# -*- coding: utf-8 -*-
"""기말과제_윤수빈정준길이윤지.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1r_w3-yGpVNPaT_cp1KB4VyJpcciFaC-P
"""

import random as rd

class Monstergame:
  def __init__(self):
    self.player_health = 50
    self.monster_health = 50
    self.attempts = 5

  def random_number(self):
      return rd.randint(1,3)

  def user_input(self):
    while True:
      try:
        user_number = int(input('1부터 3 사이의 숫자를 입력하시오.:'))

        if user_number >=1 and user_number <=3 :
          return user_number
        else :
          print('\n알맞은 숫자를 입력하시오.\n')

      except ValueError:
        print('\n알맞은 숫자를 입력하시오.\n')

  def round(self, user_number):
    if user_number == self.random_number():
      print('\n정확합니다! monster의 체력을 10 깎습니다.\n')
      self.monster_health -= 10
      self.attempts += 2
      self.player_health += 10

    else:
      print('\n틀렸습니다. player의 체력을 10 깎습니다.\n')
      self.player_health -= 10
    self.attempts -= 1
    print('monster : {}, 내 체력: {}, 남은 시도 횟수: {}\n'.format(self.monster_health, self.player_health, self.attempts))


  def game(self):
    while self.attempts >= 0:
      if self.monster_health == 0:
        print('\n몬스터를 물리쳤습니다! 축하드립니다!')
        break

      if self.player_health == 0:
        print('\n플레이어의 체력이 0이 되어 게임을 종료합니다.')
        break

      if self.attempts == 0 :
        print('\n시도 횟수가 소진되어 게임을 종료합니다.')
      user_number = self.user_input()
      self.round(user_number)

if __name__ == "__main__":
  x = Monstergame()
  x.game()

