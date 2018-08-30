"""
This class represent one word beloging to grammar class classified as 'Preposition'

What's a Preposition?
===
A word governing, and usually preceding, a noun or pronoun and expressing a relation
to another word or element in the clause.
Prepositions are often used to express spatial or temporal relations (in, under, towards, before)
"""

from .base import Word

# pylint: disable=too-few-public-methods,missing-docstring,no-self-use
class Preposition(Word):
    def __init__(self, content, context=None):
        Word.__init__(self, content, context)

    def has_plural(self):
        return False
