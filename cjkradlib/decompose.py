import re

try:
    from importlib.resources import read_text
except ImportError:
    from importlib_resources import read_text


class Decompose:
    EXCLUSION = (
            set('⿰⿱⿸⿺⿳⿻⿵⿲⿹⿴⿷⿶')
            # | set(chr(i) for i in range(ord('①'), ord('⑳') + 1))
    )

    def __init__(self):
        self.sub = dict()
        self.super = dict()

        for row in read_text('cjkradlib.data.cjkvi_ids', 'ids.txt').strip().split('\n'):
            if row[0] != '#':
                content = row.split('\t')
                assert len(content[1]) == 1
                self.sub[content[1]] = set(c for c in re.sub(r'(\[[^\]]+\]|&[^;]+;|[{}])'
                                                             .format(re.escape(''.join(self.EXCLUSION))),
                                                             '',
                                                             content[2]))

        for k, v in self.sub.items():
            for c in v:
                self.super.setdefault(c, set()).add(k)

    def get_sub(self, char):
        return sorted(self.sub.get(char, set()))

    def get_super(self, char):
        return sorted(self.super.get(char, set()))
