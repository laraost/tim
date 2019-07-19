#!/usr/bin/env python3

"""
Read a code-matrix from a file, start at the top left and interpret the symbols:
<, >, v, ^: go left, right, down, up
+, -:       increment the current register
.:          do nothing
[,]:        move the register pointer left, right; wraps around if the pointer moves past the first or last register
/,\:        change the direction of motion if the value of the current register is non-zero

                  .                     .
                  .                     .
                ../     /..     ..\     \..
                        .         .
                        .         .

p:          print all registers (as ascii characters) from the register pointer until the first 0
d:          print the value of the current register
x:          exit
"""

import sys

matrix = []

if len(sys.argv) < 2:
    print("Usage: machine.py FILE [registers]")
    print("'registers' (optional) is the number of registers. Default is 100.")
    print("The initial content of registers is read from standard input. If no value is provided the registers are initialized with 0.")
    sys.exit(1)

with open(sys.argv[1], 'r') as inputfile:
    for line in inputfile:
        chars = [x for x in line if x is not '\n']
        matrix.append(chars)

if len(sys.argv) == 3:
    numberofregisters = int(sys.argv[2])
    if numberofregisters < 1:
        print("There needs to be at least 1 register")
        sys.exit(1)
else:
    numberofregisters = 100

registers = [0]*numberofregisters

regptr = 0
for line in sys.stdin:
    line = line.strip();
    for x in line.split(" "):
        registers[regptr] = int(x)
        regptr = regptr + 1    

regptr = 0
row = 0
col = 0

# direction of motion (row, col)
# we start by moving right
motion_dir = (0, 1)

done = False
while not done:
    symbol = matrix[row][col]
    # move left, right, down or up
    if symbol in '<>v^':
        if symbol == '<':
            motion_dir = (0, -1)
        elif symbol == '>':
            motion_dir = (0,  1)
        elif symbol == 'v':
            motion_dir = ( 1, 0)
        elif symbol == '^':
            motion_dir = (-1, 0)
    # increment/decrement register
    elif symbol in '+-':
        if symbol == '+':
            registers[regptr] = registers[regptr] + 1;
        elif symbol == '-':
            registers[regptr] = registers[regptr] - 1;
    # move pointer
    elif symbol in '[]':
        if symbol == '[':
            regptr = (regptr - 1) % len(registers)
        elif symbol == ']':
            regptr = (regptr + 1) % len(registers)
    # branch
    elif symbol in '/\\':
        if symbol == '/':
            if registers[regptr] != 0:
                if motion_dir == (0, 1):
                    new_dir = (-1, 0)
                if motion_dir == (0, -1):
                    new_dir = (1, 0)
                if motion_dir == (1, 0):
                    new_dir = (0, -1)
                if motion_dir == (-1, 0):
                    new_dir = (0, 1)
                motion_dir = new_dir
        elif symbol == '\\':
            if registers[regptr] != 0:
                if motion_dir == (0, 1):
                    new_dir = (1, 0)
                if motion_dir == (0, -1):
                    new_dir = (-1, 0)
                if motion_dir == (1, 0):
                    new_dir = (0, 1)
                if motion_dir == (-1, 0):
                    new_dir = (0, -1)
                motion_dir = new_dir
    # print (as ascii)
    elif symbol == 'p':
        output = ''
        for idx in range(regptr, len(registers)):
            output = output + chr(registers[idx])
            idx = idx + 1
            if registers[idx] == 0:
                break
        print(output)
    elif symbol == 'd':
        print(repr(registers[regptr]))
    # quit
    elif symbol == 'x':
        break
    # move after reading all instructions
    col = (col + motion_dir[1]) % len(matrix[row])
    row = (row + motion_dir[0]) % len(matrix)
