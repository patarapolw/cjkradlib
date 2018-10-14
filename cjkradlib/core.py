from .decompose import Decompose
from .frequency import ZhFrequency, JpFrequency
from .variant import Variant


class _RadicalObject:
    def __init__(self, character, params):
        self.character = character
        self.params = params

    @property
    def compositions(self):
        return self.params['decompose'].get_sub(self.character)

    @property
    def supercompositions(self):
        return self.params['sorter'].sort_char(self.params['decompose'].get_super(self.character))

    @property
    def variants(self):
        return self.params['variant'].get(self.character)

    def __repr__(self):
        return repr({
            'character': self.character,
            'compositions': self.compositions,
            'supercompositions': self.supercompositions,
            'variants': self.variants
        })


class RadicalFinder:
    def __init__(self, lang='zh'):
        self.params = {
            'decompose': Decompose(),
            'variant': Variant(),
            'sorter': None
        }

        if lang == 'zh':
            self.params['sorter'] = ZhFrequency()
        elif lang == 'jp':
            self.params['sorter'] = JpFrequency()
        else:
            raise NotImplementedError('Please choose either zh or jp')

    def search(self, character):
        return _RadicalObject(character, self.params)
