import re

try:
    from importlib.resources import read_text
except ImportError:
    from importlib_resources import read_text


class Variant:
    def __init__(self):
        self.entries = dict(self._load())

    @staticmethod
    def _load():
        for row in read_text('cjkradlib.data', 'Unihan_Variants.txt').strip().split('\n'):
            _ = re.match(r'U\+([0-9A-F]{4,})\t(\w+)\t(.+)', row)
            if _ is not None:
                char, variant_type, variants = _.groups()
                yield chr(int(char, 16)), [chr(int(item.group(1), 16))
                                           for item in re.finditer(r'U\+([0-9A-F]{4,})', variants)]
            else:
                # print(row)
                pass

    def get(self, character):
        return self.entries.get(character, [])
