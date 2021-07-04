import random
#import os

def game_summary(rand,trys) :
  n=1
  for i in trys:
    if i>rand:
      print("Your {0} guess was {guess} which is greater than {num}".format(n,guess=i,num=rand))
    else:
      print("Your {0} guess was {guess} which is less than {num}".format(n, guess=i, num=rand))
    n+=1


def num_input():
  try:
    num = int(input())
    assert 0 < num < 101, "Invalid input"

  except AssertionError as ae:
    print("Invalid input . Enter integers between 1 - 100 : ",end="")
    num_input()
  except ValueError:
    print("Invalid input . Enter integers between 1 - 100 : ",end="")
    num_input()
  return num

def game():
  num = 0
  trys=[]
  rand=random.randint(1, 101)
  print("Enter your guess between 1-100 : ",end="")
  num = num_input()

  while (num != rand):
    trys.append(num)
    if num<rand:
      print("It lies above the number")
    else:
      print("It lies below the number")
    print("Enter your next guess : ",end="")
    num = num_input()
  print("Congratulations ! you guessed the right answer (",rand,") in",len(trys),"trys");
  game_summary(rand,trys)


def main():
  ch='y'
  while(ch=='y' or ch=='Y'):
    #os.system('cls')
    #clear=lambda: os.system('cls')
    #clear()
    game()
    print("If you want to play another game enter 'y' else 'n' without quotes : ",end="")
    ch=input()
  print("Hope you have fun thanks for playing :)")
main()
