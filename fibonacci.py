#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)

def get_num_terms():
  while True:
    num = input("How many Fibonacci terms do you want? ")
    if num.isdigit() and int(num) > 0:
      return int(num)
    else:
      print("Please enter a positive number!")


def make_fibonacci(n):
  sequence = [0, 1]
  if n == 1:
    return [0]
  elif n == 2:
    return[0, 1]
    for i in range(2, n):
      next_num = sequence[i - 1] + sequence[i - 2]
      sequence.append(next_num)
    return sequence 



def show_fibonacci(sequence):
  print("\nFibonacci Sequence:")
  for num in sequence:
    print(num, end= " ")
  print()

def main():
  terms = get_num_terms()
  result = make_fibonacci(terms)
  show_fibonacci(result)
