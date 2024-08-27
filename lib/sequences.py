#!/usr/bin/env python3

def print_fibonacci(length):
    #pass
    if length < 0:
      print('Invalid length')
      return
    elif length == 0:
         print([])
         return
    elif length == 1:
         print([0])
         return
      
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < length:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    print(fibonacci_sequence)  
print_fibonacci(2)  