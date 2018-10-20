# CJKradlib

[![Build Status](https://travis-ci.org/patarapolw/cjkradlib.svg?branch=master)](https://travis-ci.org/patarapolw/cjkradlib)
[![PyPI version shields.io](https://img.shields.io/pypi/v/cjkradlib.svg)](https://pypi.python.org/pypi/cjkradlib/)
[![PyPI license](https://img.shields.io/pypi/l/cjkradlib.svg)](https://pypi.python.org/pypi/cjkradlib/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/cjkradlib.svg)](https://pypi.python.org/pypi/cjkradlib/)

Generate compositions, supercompositions and variants for a given Hanzi / Kanji, based on [cjk-decomp](https://github.com/amake/cjk-decomp).

## Installation

```commandline
pip install cjkradlib
```

Also, IDS sequences use full range of CJK ideographs, so the fonts
that covers all encoded ideographs (such
as [HanaMin](http://fonts.jp/hanazono/)
or [Hanamin AFDKO](https://github.com/cjkvi/HanaMinAFDKO/releases) )
should be used.

## Usage

```python
from cjkradlib import RadicalFinder
finder = RadicalFinder(lang='zh')  # default is 'zh'
result = finder.search('麻')
print(result.compositions)  # ['广', '林']
print(result.supercompositions)  # ['摩', '魔', '磨', '嘛', '麽', '靡', '糜', '麾']
print(result.variants)  # ['菻']
```

Supercompositions are based on the character frequency in each language, so altering the language give slightly different results.

```python
from cjkradlib import RadicalFinder
finder = RadicalFinder(lang='jp')
result = finder.search('麻')
print(result.supercompositions)  # ['摩', '磨', '魔', '麿']
```

## Related projects

- [ChineseViewer](https://github.com/patarapolw/ChineseViewer)
- [HanziLevelUp](https://github.com/patarapolw/HanziLevelUp)
- [CJKrelate](https://github.com/patarapolw/CJKrelate)

## Plan

- Use https://github.com/cjkvi/cjkvi-ids as the source for CJK-decomposition.
