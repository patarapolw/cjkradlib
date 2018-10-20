from importlib.resources import read_text
import re


def get_decomp():
    d = dict()
    exclusion = (set('⿰⿱⿸⿺⿳⿻⿵⿲⿹⿴⿷⿶')
                 | set(chr(i) for i in range(ord('①'), ord('⑳')+1)))
    for row in read_text('cjkradlib.data.cjkvi_ids', 'ids.txt').strip().split('\n'):
        if row[0] != '#':
            content = row.split('\t')
            assert len(content[1]) == 1
            d[content[1]] = [c for c in re.sub(r'(\[[^\]]+\]|&[^;]+;|[{}])'
                                               .format(re.escape(''.join(exclusion))),
                                               '',
                                               content[2])]

    return d


if __name__ == '__main__':
    print(get_decomp())
