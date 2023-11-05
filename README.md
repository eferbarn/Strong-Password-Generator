# 🎲🔐 Strong Password Generator
Using this‌ CLI tool, create strong and secure passwords in a **STANDALONE** manner and use them where needed.

## Usage (Try `$ passgen -h` to see this instruction):

```plain
usage: passgen [-h] [-n] [-s] [length]

This script generates a secure and random string. You can use this string as your password or wherever you need a
random string.

positional arguments:
  length         Length of the random string

options:
  -h, --help     show this help message and exit
  -n, --number   Exclude numbers in the random string
  -s, --special  Exclude special characters in the random string
```

## Examples:

Here you can find some examples of the CLI tool.
---
1. `passgen` Generates a random 18-character (the default length when you don't provide a specific length) string with alphabets, numbers, and specials.
```
$ passgen
YJDnFU!PAlN$FMOzWx
```
---
2. `passgen i` Generates a random i-character string with alphabets, numbers, and specials.
```
$ passgen 22
500Q3DgKHL$qEoRt1L$v5q
```
---
3. `passgen i -n` Generates a random i-character string excluding numbers (-n).
```
$ passgen 12 -n
&OERuhY&IEi(
```
---
4. `passgen i -n -s` Generates a random i-character string excluding numbers (-n) and special characters (-s).
```
$ passgen 12 -n -s
TwGsRtIXTLWp
```
---
5. `passgen -h` Shows the usage and instruction.
```
$ passgen -h
usage: passgen [-h] [-n] [-s] [length]

This script generates a secure and random string. You can use this string as your password or wherever you need a
random string.
.
.
.
  -s, --special  Exclude special characters in the random string
```