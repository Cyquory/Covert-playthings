# Covert-playthings

Simple unconventional script for minecraft prison server.

It only require python installation and some python package

## Requirement
python 3.6+, `pynput`, `pydirectinput`

I get python for window using `pyenv for Windows`: https://github.com/pyenv-win/pyenv-win

Install `pynput` and `pydirectinput` with pip:
```
> pip install pynput
> pip install pydirectinput
```

Then you should run any script with by running the python code.
```
> python agent.py
```

## How to write my own script?
`pynput` detect mouse and keyboard inputs. `pydirectinput` simulate the keyboard input to the game.
I don't use pynput's keyboard input function. It use old interface that can't run with the game.

You may have heard of `pyautogui`. It may got the same problem as `pynput` and it can't do detection.

## Known issue
There're some problems regard to mouse movement between `pydirectinput` and minecraft. Some have already report it to Mojang but nothing can be done. https://bugs.mojang.com/browse/MC-230446

In my opinion, something is wrong along the pipline of mouse inputs but manybe only `pydirectinput` would care enough to tacle the issue. Anyhow, I got a temporary fix to my problem.

### The temporary fix
It may not work for everyone. proceed it with care.

In minecraft, open `Game menu` (press Esc in the game) > `Options..` > `Controls..` > `Mouse Settings..` and set `Raw Input` to OFF. Then the `pydirectinput.move()` should work as expected.

Under environment: Minecraft 1.17.1(vanilla), python 3.9.6, pydirectinput 1.0.4, Windows 10 Home 21H1