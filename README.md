# useless

This is a computing machine controlled by a 2-dimensional input language. Here's an example (```examples/multiply```):

```
v               This program multiplies numbers in the first and second register and stores the result in the third register
.               This program cannot handle negative numbers. If one of the inputs is negative, the program enters an infinite loop.
.
>+++++v         Write 5 into the first register
v.....<
]               Move to the second register
>+++v           Write 3 into the second register
v...<
.
.       Now go through a loop until the first register is 0.
.       In the loop:
.                       - decrement the first register
.                       - add the second register onto the third
.
.    Test the first register here
.    |              Print the third register (the result)
.    |              |
.    v              v
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

It's written in Python 3. Just run ```./machine.py /path/to/input/file``` to be amazed.
