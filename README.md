# Covert-playthings

Simple unconventional script for minecraft prison server
It only require python installation and some python package

## Requirement
python 3.6+, pynput, pydirectinput

I get python for window using pyenv for Windows: https://github.com/pyenv-win/pyenv-win

Install pynput and pydirectinput with pip:
```
> pip install pynput
> pip install pydirectinput
```

Then you should run any script with by running the python code.
```
> python agent.py
```

## How to write my own script?
pynput detect mouse and keyboard inputs. pydirectinput simulate the keyboard input to the game.
I don't use pynput's keyboard input function. It use old interface that can't run with the game.

You may have heard of pyautogui. It may got the same problem as pynput and it can't do detection.