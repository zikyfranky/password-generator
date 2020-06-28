# Random password Generator

##### A simple and custom random password generator.

- Generate a simple password of default length 10.

## Usage

- Generate the password (Default length of password 10 unless specified via argument).

#### Generate a secure password with length 10.

```bash
python passwordGenerator
```

## Watch Video

[![Tutorial](https://img.youtube.com/vi/wTON4XIEpcc/maxresdefault.jpg "Watch Video")](https://youtu.be/wTON4XIEpcc "Watch Video")

#### Specify the length of the password using the `l` or `--length` argument.

```bash
python passwordGenerator -l 20
```

#### You can also import and use this function in your project.

```bash
from passwordGenerator import generate
password = generate()
```