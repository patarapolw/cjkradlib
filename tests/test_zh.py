import pytest

from cjkradlib import RadicalFinder

finder = RadicalFinder(lang='zh')


@pytest.mark.parametrize(
    ('character', 'compositions'),
    [
        ('频', ['步', '页']),
        ('从', ['人']),
        ('弱', ['60887'])
    ]
)
def test_compositions(character, compositions):
    assert finder.search(character).compositions == compositions


@pytest.mark.parametrize(
    ('character', 'supercompositions'),
    [
        ('它', ['蛇', '陀', '驼', '舵', '鸵', '沱', '佗', '砣']),
        ('店', ['惦', '掂', '踮']),
        ('諮', [])
    ]
)
def test_supercompositions(character, supercompositions):
    assert finder.search(character).supercompositions == supercompositions


@pytest.mark.parametrize(
    ('character', 'variants'),
    [
        ('隼', ['鶽', '鵻']),
        ('痴', ['癡']),
        ('怎', [])
    ]
)
def test_variants(character, variants):
    assert finder.search(character).variants == variants


if __name__ == '__main__':
    print(finder.search('麻'))
