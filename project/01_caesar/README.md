# Caesar Shift

For this exercise, we'll write a program to implement the Caesar Shift, one of the earliest known secret codes. To encode using a Caesar Shift, you shift each letter in your message to the right a certain number of spaces in the alphabet.

## Program Description 

Write a Python program called `caesar.py` to encode or decode a secret message from a file using the Caesar Shift. Specifically, if the user provides the option `--number 3` take `"H"` - start there and count three more letters in the alphabet, `"I"`, `"J"`, `"K"`.  So `"H"` becomes `"K"`. To keep things simple, we will print the message back to the user in all uppercase. However, you will need to encode only the letters and leave all of the rest of the text alone.

Think back to the exercise called "jump_the_five". Can you create a substitution table on the fly based on the `--number` the user provides (or the default = 3)? Be sure to do this for both encoding and decoding the caesar shift and provide the correct dictionary based on the `--decode` option. Note, this can get a little tricky at the end of the alphabet, how might you do this?

Here is an example alphabet string you can use:

```
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
```

Here is an example substitution table for --number 3:

```
A => D
B => E
C => F
D => G
...
```

## Usage

The program should take the following arguments:

* An input file as a positional argument
* An optional `-n` or `--number` argument for the number of positions to shift (default = 3)
* An optional `-d` or `--decode` argument for decoding the file (default = False)
* An optional output file `-o` or `--output ` argument (default = std.out)

When run with no arguments, it should print a brief usage:

```
$ ./caesar.py
usage: caesar.py [-h] [-n NUMBER] [-d] [-o FILE] FILE
caesar.py: error: the following arguments are required: FILE
```

When run with the `-h` or `--help` flag, it should print a longer usage:

```
usage: caesar.py [-h] [-n NUMBER] [-d] [-o FILE] FILE

caesar shift

positional arguments:
  FILE                  Input file

optional arguments:
  -h, --help            show this help message and exit
  -n NUMBER, --number NUMBER
                        A number to shift (default: 3)
  -d, --decode          A boolean flag (default: False)
  -o FILE, --outfile FILE
                        Output file (default: std.out)
```

## Argument Validation

The program should use `argparse` to validate the file argument and generate errors for a file that cannot be opened.
For instance, _blargh_ in the following example represents a nonexistent file:

```
$ ./caesar.py blargh
usage: caesar.py [-h] [-n] [-d] FILE
caesar.py: error: argument FILE: can't open 'blargh': 
[Errno 2] No such file or directory: 'blargh'
```
 
## Output

When run with a valid file, your program should print the lines of each file.
For instance, the _inputs/hello.txt_ file has one line:

```
$ ./caesar.py -n 5 ./inputs/hello.txt
MJQQTBTWQI
```