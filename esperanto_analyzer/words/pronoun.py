"""
This class represent one word beloging to grammar class classified as 'Pronoun'

What's a Pronoun?
===
In linguistics and grammar, a pronoun is a word that substitutes for a noun
or noun phrase.
Pronouns are often used to refer to a noun that has already been mentioned.
"""

from .base import Word

# pylint: disable=too-few-public-methods,missing-docstring,no-self-use
class Pronoun(Word):
    def __init__(self, content, context=None):
        Word.__init__(self, content, context)

    def has_gender(self):
        return True
