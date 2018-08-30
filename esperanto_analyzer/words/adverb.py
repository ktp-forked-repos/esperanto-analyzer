"""
This class represent one word beloging to grammar class classified as 'Adverb'

What's an Adverb?
===
A word or phrase that modifies or qualifies an adjective, verb, or other adverb or
a word group, expressing a relation of place, time, circumstance, manner, cause, degree, etc.
(e.g., now, yesterday, today, gently, quite, then, there).
"""

from .base import Word

# pylint: disable=too-few-public-methods,missing-docstring
class Adverb(Word):
    def __init__(self, content, context=None):
        Word.__init__(self, content, context)

    def has_plural(self):
        """
         Adverbs are invariable
        """
        return False
