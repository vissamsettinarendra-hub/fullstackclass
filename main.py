'''
create one package utilities
      calculator
      greetings

main.py
import from utilities and use them
'''
from utilities.calculator import add
print(add(10,20))

from utilities.greetings import greet
print(greet("megha"))

import math
print(math.__name__)
print(math.__doc__)

import math
import sys
print(sys.path)

print(dir(math))

#pip--python package manager

#1-sys
#python virtual environment 

#commands
#1.python -m venv env
#2.env\Scripts\Activate.ps1
#3.Set-ExecutionPolicy RemoteSigned -Scope CurrentUser