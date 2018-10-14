# CJKradlib

Generate compositions, supercompositions and variants for a given Hanzi / Kanji.

## Installation

```commandline
pip install cjkradlib
```

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

- [HanziLevelUp](https://github.com/patarapolw/HanziLevelUp)
- [ChineseViewer](https://github.com/patarapolw/ChineseViewer)
- [CJKrelate](https://github.com/patarapolw/CJKrelate)
