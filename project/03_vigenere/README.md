# Vigenere Ciphers

For this exercise, we'll write a program to implement a Vigenere Cipher, that encrypts alphabetic text by using a series of interwoven Caesar ciphers, based on the letters of a keyword.

## Program Description 

It turns out that the Substitution Cipher wasn't a great cipher either; in fact, most newspapers carry a daily puzzle about solving a vigenere cipher.  Anything that someone can figure out for fun in an afternoon is not a very secure secret code!

In 1553, a new way of writing secret codes became the new state of the art and stayed that way for centuries.  For about 300 years, there was a secret code called "le chiffre indechiffrable" (the indecipherable cipher) - the Vigenere Cipher.  It wasn't cracked until mathematicians began to study it in the mid-1800s, applying sophisticated statistical analysis tools.

Here's how the Vigenere Cipher works.  First, pick a key word; let's say "TEST".  Then, pick a message you want to encode; let's say "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG".  Imagine writing out the message, and then writing the key word over and over underneath it.  Like this:

```
THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG
TESTTESTTESTTESTTESTTESTTESTTESTTEST
```

To encode the message, go column by column.  Take the two letters in each column and convert them to indices in the alphabet (like Python does, starting with "A" = 0).  Add the two numbers together.  Then, wrapping around if necessary, convert back to a letter.

For example, the first column contains "T" and another "T".  In a zero-indexed alphabet, "T" is index 19.  So, the first colum becomes 19 + 19 = 38.  There are only 26 letters in the alphabet, so imagine counting 0 to 25 and then starting over at the beginning again, where 26 goes back to A.  Counting to 38 ends on M.  (Another way to think about this is that 38 - 26 = 12, and the letter at index 12 is M.)  So, the first column is encoded to the letter M.

The second column is H + E, or 7 + 4, or 11, or L.

In total, the full message encodes this way:

```
THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG
TESTTESTTESTTESTTESTTESTTESTTESTTEST
------------------------------------
MLWJNMUDUVGPGJGQCYEIXHGOXVLAXPSSRHGZ
```

## Usage

The program should take the following arguments:

* An input file as a positional argument
* An optional `-k` or `--keyword` argument for a keyword (default = CIPHER)
* An optional `-d` or `--decode` argument for decoding the file (default = False)
* An optional output file `-o` or `--output ` argument (default = std.out)

When run with no arguments, it should print a brief usage:

```
$ ./vigenere.py
usage: vigenere.py [-h] [-k KEYWORD] [-d] [-o FILE] FILE
vigenere.py: error: the following arguments are required: FILE
```

When run with the `-h` or `--help` flag, it should print a longer usage:

```
$ ./vigenere.py -h
usage: vigenere.py [-h] [-k KEYWORD] [-d] [-o FILE] FILE

vigenere cipher

positional arguments:
  FILE                  Input file

optional arguments:
  -h, --help            show this help message and exit
  -k KEYWORD, --keyword KEYWORD
                        A keyword (default: CIPHER)
  -d, --decode          A boolean flag (default: False)
  -o FILE, --outfile FILE
                        Output file (default: std.out)
```

## Argument Validation

The program should use `argparse` to validate the file argument and generate errors for a file that cannot be opened.
For instance, _blargh_ in the following example represents a nonexistent file:

```
$ ./vigenere.py blargh
usage: vigenere.py [-h] [-n] [-d] FILE
vigenere.py: error: argument FILE: can't open 'blargh': 
[Errno 2] No such file or directory: 'blargh'
```
 
## Output

When run with a valid file, your program should print the lines of each file.
For instance, the _inputs/hello.txt_ file has one line:

```
$ ./vigenere.py ./inputs/hello.txt

```
