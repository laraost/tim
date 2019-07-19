# useless

This is a computing machine controlled by a 2-dimensional input language. Here's an example (```examples/multiply```):

```
v This program multiplies numbers in the first and second register and stores the result in the third register
. This program cannot handle negative numbers. If one of the inputs is negative, the program enters an infinite loop.
.
. Now go through a loop until the first register is 0.
. In the loop:
.       - decrement the first register
.       - add the second register onto the third
.
.   Test the first register here
.   |            Print the third register (the result) and exit
.   |            |
.   v            v
>.[.\............]]dx
.   -
.   >].>.\.]].>.\.[[.v
.      . .    . .    .
.      . .    . .    .
.      . -    . -    .
.      [ ]    ] [    .
.      . +    . .    .
.      [ ]    ] [    .
.      . +    . +    .
.      . .    . .    .
.      ^.<    ^.<    .
.                    .
^....................<
```

Here's another example. This one prints and decrements the first register until it is zero:
```
d-\x>
  >.^
```

The initial values for the registers are read from standard input (or set to zero if none are provided).

It's written in Python 3. Run ```machine.py``` with the argument ```/path/to/input/file``` to be amazed.

We can chain multiple programs together, for example:
```
echo "3 5" | ./multiply.py examples/multiply | ./multiply.py examples/loop
```
