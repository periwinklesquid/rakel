#!/usr/bin/python
from exercise import return_string, divides_by, even_numbers
#from cheat_sheet import return_string, divides_by, even_numbers #uncomment this line if you want to cheet
from random import randint
from sys import exit
from time import sleep

def test_1():
   print("Testing return_string()")
   success = 1
   if type(return_string()) is not str:
       print("return_string() returned {}. {} was expected".format(type(return_string()),type("")))
       success = 0
   if not success:
       print("return_string() FAILED\n")
   else:
       print("return_string() SUCCESS\n")

def test_2():
   print("Testing divides_by(n,d)")
   success = 1
   if not divides_by(2,1):
      print("divides_by(2,1) didn't return True")
      success = 0 
   if divides_by(1,2):
      print("1 divided by 2 returns True")
      success = 0
   for _ in range(100):
      i = randint(2,100)
      j = i * randint(2,100)   
      if not divides_by(j, i):
         print("divides_by({},{}) didn't return True".format(j, i))
         success = 0 
         break
      if divides_by(i,j):
         print("divides_by({},{}) returned False".format(i, j))
         success = 0 
         break
   if not success:
      print("divides_by(n,d) FAILED\n")
   else:
      print("divides_by(n,d) SUCCESS\n")

def test_3():
   print("Testing even_numbers(n)")
   success = 1
   if not even_numbers(4) == [0,2,4]:
      success = 0
   for _ in range(100):
      rand_int = randint(1,100)
      answer = [ i for i in range(rand_int + 1) if not i % 2 ]
      if even_numbers(rand_int) != answer:
         success = 0
         print("even_numbers({}) returned {} was expecting {}".format(
             rand_int,
             even_numbers(rand_int),
             answer
         ))
         break 
   if not success:
      print("even_numbers(n) FAILED\n")
   else:
      print("even_numbers(n) SUCCESS\n")

def main():
   print("")
   test_1()
   sleep(1)
   test_2()
   sleep(1)
   test_3()
   sleep(1)

if __name__ == "__main__":
   main()
