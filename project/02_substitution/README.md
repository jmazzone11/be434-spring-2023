# Substitution Cipher

For this exercise, we'll write a program to implement a Substitution Cipher, that creates a substitution table by randomly scambling the alphabet. 

## Program Description 

The Caesar Shift wasn't a great secret code; for one thing, there are only a few different possibilities (only as many letters as you have in your alphabet).

We can make a code that is much harder to break by scrambling the alphabet completely instead of just shifting to one side.

Define a substitution cipher by scrambling the entire alphabet.  Say, for example, `"WJKUXVBMIYDTPLHZGONCRSAEFQ"`.

Then, imagine writing it out underneath the normal alphabet, in the normal order, like so:

```
ABCDEFGHIJKLMNOPQRSTUVWXYZ
WJKUXVBMIYDTPLHZGONCRSAEFQ
```

To encode a message, replace each letter in the message with the matching letter in the cipher alphabet.  In this case, `"HELLO"` would be encoded as `"MXTTH"`, since M is directly under H, etc. To keep things simple, we will print the message back to the user in all uppercase letters. And you will need to simply print any characters that are not letters.

Think back to the exercise `ransom`, and consider how you might create a function to randomly get a letter from the alphabet. But, be sure to choose the letter without replacement (or you might get letters that encode the same letter). Also, be sure to use a random seed so we can make the code reproducible and testable. You should also be able to re-use some of the code you wrote for substitution.py.

## Usage

The program should take the following arguments:

* An input file as a positional argument
* An optional `-s` or `--seed` argument for a random seed (default = 3)
* An optional `-d` or `--decode` argument for decoding the file (default = False)
* An optional output file `-o` or `--output ` argument (default = std.out)


When run with no arguments, it should print a brief usage:

```
$ ./substitution.py   
usage: substitution.py [-h] [-s SEED] [-d] [-o FILE] FILE
substitution.py: error: the following arguments are required: FILE
```

When run with the `-h` or `--help` flag, it should print a longer usage:

```
$ ./substitution.py  -h
usage: substitution.py [-h] [-s SEED] [-d] [-o FILE] FILE

substitution cipher

positional arguments:
  FILE                  Input file

optional arguments:
  -h, --help            show this help message and exit
  -s SEED, --seed SEED  A random seed (default: 3)
  -d, --decode          A boolean flag (default: False)
  -o FILE, --outfile FILE Output file (default: std.out)
```

## Argument Validation

The program should use `argparse` to validate the file argument and generate errors for a file that cannot be opened.
For instance, _blargh_ in the following example represents a nonexistent file:

```
$ ./substitution.py blargh
usage: substitution.py [-h] [-n] [-d] FILE
substitution.py: error: argument FILE: can't open 'blargh': 
[Errno 2] No such file or directory: 'blargh'
```
 
## Output

When run with a valid file, your program should print the lines of each file.
For instance, the _inputs/hello.txt_ file has one line:

```
$ ./substitution.py -s 5 ./inputs/hello.txt
OUVVDMDSVL
```
