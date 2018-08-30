# pylint: disable=missing-docstring
import re

from esperanto_analyzer.speech import Preposition
from .base import BaseMorphologicalAnalyzer # TODO: change to module name

class PrepositionMorphologicalAnalyzer(BaseMorphologicalAnalyzer):
    #  MATCHES: ["patro", "patroj", "patron", "patrojn"]
    MATCH_REGEXP = re.compile('^(.)$', re.IGNORECASE|re.UNICODE)

    def match(self, word):
        return self.MATCH_REGEXP.match(word)

    def word_class(self, word):
        return Preposition(word)
