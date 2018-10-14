import pytest

from cjkradlib import RadicalFinder

finder = RadicalFinder(lang='jp')


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
        ('它', ['蛇', '陀', '舵']),
        ('刃', ['忍', '籾', '靭']),
        ('店', [])
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
    from cjkradlib.frequency import JpFrequency
    jp = JpFrequency()

    for _ in range(50):
        print(finder.search(jp.random()))
