"""
This class represent one word beloging to grammar class classified as 'Numeral'

What's a Numeral?
===
In linguistics, a numeral is a member of a part of speech(word) characterized by the
designation of numbers;
"""
from .base import Word

# pylint: disable=too-few-public-methods,missing-docstring,no-self-use
class Numeral(Word):
    def __init__(self, content, context=None):
        Word.__init__(self, content, context)
