import math
import json
import random

try:
    from importlib.resources import read_text
except ImportError:
    from importlib_resources import read_text


class ZhFrequency:
    def __init__(self):
        self.sequence = []
        for row in read_text('cjkradlib.data.zh', 'junda.tsv').strip().split('\n'):
            contents = row.split('\t')
            self.sequence.append(contents[1])

    def sort_char(self, hanzi_list, limit=5000):
        return sorted([hanzi for hanzi in hanzi_list if self.freq_char(hanzi) <= limit], key=self.freq_char)

    def freq_char(self, hanzi):
        try:
            return self.sequence.index(hanzi)
        except ValueError:
            return math.inf

    def random(self):
        return random.choice(self.sequence)


class JpFrequency:
    def __init__(self):
        self.entries = json.loads(read_text('cjkradlib.data.jp', 'grade.json'))

    def sort_char(self, kanji_list):
        return sorted([kanji for kanji in kanji_list if self.freq_char(kanji) is not None],
                      key=lambda x: self.freq_char(x))

    def freq_char(self, kanji):
        for k, v in self.entries.items():
            if kanji in v:
                return k, v.index(kanji)

        return None

    def random(self):
        return random.choice(''.join(x for x in self.entries.values()))
