# python has many built in libraries, to make of them, you just need to import them
# Importing a built in Library
import math                                             # for mathematical functions
import random                                           # for generating random numbers
import statistics                                       # for statistical functions
import datetime                                         # for working with dates and times


print(math.sqrt(16))                                  # Output: 4.0
print(math.pi)                                        # Output: 3.141592653589793

# Sometimes you don't need the whole library
# Importing part of a library
'''
from math

print('Square root of 36 is:', math.sqrt(36))         # Output: 6.0
print('Sine of 90 degrees is:', math.sin(math.radians(90)))  # Output: 1.0
print('Power of 2^3 is:', math.pow(2, 3))               # Output: 8.0
'''

# Generate random numbers
print('Random integer between 1 and 10 is:', random.randint(1, 10))
print('Random choice from a list is:', random.choice(['Bread', 'Cocoa', 'Yam', 'Beans', 'Banana']))
print('Random float between 0 and 1 is:', random.random())


# WWork with dates and times
today = datetime.date.today()
print('Today\'s date is:', today)

now = datetime.datetime.now()
print('Current time is:', now.strftime("%H:%M:%S"))
print('Current date is:', now.strftime("%Y-%m-%d"))


# Calculate the difference between two dates
birthday = datetime.date(2000, 1, 1)
age = today - birthday
print('Age is:', age.days // 365, 'years')

# INSTALLING PYTHON PACKAGES

# To install a Python package, you can use pip, which is the package installer for Python.
# You can install packages from the command line or terminal.

# For example, to install the requests library, you would run:
'''
pip install requests
'''
'''
Python has lots of built-in tools (standard library), but sometimes you'll need more.
That’s where third-party packages come in — extra tools made by the community.

pip

pip is Python’s tool for installing packages.

It stands for "Pip Installs Packages".

If you’re using Python 3.4 or newer, you already have pip3.

To install a package, just run: pip install package_name  



PyPI

PyPI (Python Package Index) is the place where all these third-party packages live.
pip automatically pulls packages from PyPI.

You can also visit pypi.org to search for packages manually.
Popular third-party libraries

PyPI has thousands of packages, it would be impossible to summarize them all.
But there are a handful of go-to packages that many people use for common tasks:

requests
scrapy
Twisted
Pillow
lxml
PyYAML
Django, Flask, Pyramid
SQLAlchemy
numpy, scipy, pandas
pytest, tox, coverage, mock
six
Jinija2
cryptography
pylint, flake8, pep8
pymongo, redis, MySQL-Python, psycopg2



Resources:

https://www.netsolutions.com/insights/top-10-python-frameworks-for-web-development-in-2019/
'''

# Standard Library

# The Python Standard Library is a collection of built-in modules that come with Python.
# These modules help you do common tasks like reading files, working with dates, or handling math — without installing anything extra.

# Popular Extra Python Libraries:

# TensorFlow – For machine learning and deep learning.

# Matplotlib – For creating charts and graphs.

# Pandas – For handling and analyzing data.

# NumPy – This is for working with numbers and large arrays.

# SciPy – For scientific and technical computing.

# Scrapy – For web scraping (getting data from websites).

# Scikit-learn – For machine learning (like predictions and classifications).

# PyGame – For building games with graphics and sound.

# PyTorch – For deep learning and neural networks.

# PyBrain – For beginners in machine learning and AI.

# There are many more libraries in Python. We can use a suitable library for our purposes.
# Hence, Python libraries play a very crucial role and are very helpful to the developers.