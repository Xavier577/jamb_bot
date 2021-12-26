# Overview

This is a bot that helps check admission status and output the result to the terminal.
This project usings the power of selenium (check out the unofficial <a href="https://selenium-python.readthedocs.io/">doc</a>) and chromedrivers to run. Jamb (Joint Admissions and Matriculation Board) by the way is body that happens admission into universities in my country.

# Requirements to run this bot

To run this bot, first you need

<ul>
<li> python (version >= 3.6) </li>
<li> pipenv </li>
<li> chromedriver (for windows or linux or windows at version 92.0.4515.107) </li>
<li> selenium </li>
</ul>

# To use this bot

> With python install (if you don't have pipenv)

```
pip install pipenv
```

> In the root directory of the project (This will Activate a virtual environment)

```
pipenv shell

```

> To install all packages from pipfile

```
pipenv install

```

> Assuming you have chrome_driver and you on either mac, windows or linux

```
python main.py

```

and if done correctly it should ask you for your utme registration number, your username/email and your password in the terminal/command_prompt

# Issues with chrome driver

please do make sure your chrome driver is the same version as your chrome. If you not then download the correct chrome driver for your corresponding operation system and play in the chrome_driver at the folders representing your corresponding operating system.
