#!/usr/bin/env python3

"""
Read a code-matrix from a file, start at the top left and interpret the symbols:
0-9:        select the active tape. Each tape has its own register pointer. Tape 0 is active at the start (the 'input'-tape)
<, >, v, ^: go left, right, down, up
+, -:       increment the current register
.:          do nothing
[,]:        move the register pointer left, right; wraps around if the pointer moves past the first or last register
/,\:        change the direction of motion if the value of the current register is greater than zero

                  .                     .
                  .                     .
                ../     /..     ..\     \..
                        .         .
                        .         .

!:          flip the sign of the current register
c:          clear the current register to 0
p:          print all registers (as ascii characters) from the register pointer until the first 0
d:          print the value of the current register
x:          exit
"""

import sys

numtapes = 10

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

registers = [[0]*numberofregisters for i in range(10)]

# start on the 'input'-tape
tape = 0

regptr = [0]*numtapes
for line in sys.stdin:
    line = line.strip();
    for x in line.split(" "):
        registers[tape][regptr[tape]] = int(x)
        regptr[tape] = regptr[tape] + 1    

regptr[tape] = 0
row = 0
col = 0

# direction of motion (row, col)
# we start by moving right
motion_dir = (0, 1)

done = False
while not done:
    # print(row, col, registers[tape][regptr[tape]], tape, regptr[tape])
    symbol = matrix[row][col]
    # select a tape
    if symbol in '0123456789':
        tape = int(symbol)
    # move left, right, down or up
    elif symbol in '<>v^':
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
            registers[tape][regptr[tape]] = registers[tape][regptr[tape]] + 1;
        elif symbol == '-':
            registers[tape][regptr[tape]] = registers[tape][regptr[tape]] - 1;
    # move pointer
    elif symbol in '[]':
        if symbol == '[':
            regptr[tape] = (regptr[tape] - 1) % numberofregisters
        elif symbol == ']':
            regptr[tape] = (regptr[tape] + 1) % numberofregisters
    # branch
    elif symbol in '/\\':
        if symbol == '/':
            if registers[tape][regptr[tape]] > 0:
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
            if registers[tape][regptr[tape]] > 0:
                if motion_dir == (0, 1):
                    new_dir = (1, 0)
                if motion_dir == (0, -1):
                    new_dir = (-1, 0)
                if motion_dir == (1, 0):
                    new_dir = (0, 1)
                if motion_dir == (-1, 0):
                    new_dir = (0, -1)
                motion_dir = new_dir
    # flip sign
    elif symbol == '!':
        registers[tape][regptr[tape]] = -registers[tape][regptr[tape]]
    # clear to zero
    elif symbol == 'c':
        registers[tape][regptr[tape]] = 0
    # print (as ascii)
    elif symbol == 'p':
        output = ''
        for idx in range(regptr[tape], numberofregisters):
            output = output + chr(registers[tape][idx])
            idx = idx + 1
            if registers[tape][idx] == 0:
                break
        print(output)
    elif symbol == 'd':
        print(repr(registers[tape][regptr[tape]]))
    # quit
    elif symbol == 'x':
        break
    # move after reading all instructions
    col = (col + motion_dir[1]) % len(matrix[row])
    row = (row + motion_dir[0]) % len(matrix)
