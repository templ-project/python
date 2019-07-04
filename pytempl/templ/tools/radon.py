from pytempl.templ.tools import Base


class Radon(Base):
    """
    :see: https://radon.readthedocs.io/en/latest/
    """

    TOKEN = 'radon'

    ORDER = 80

    def __init__(self, app=None):
        super().__init__(app)
        self._config.update({
            'hook': 'radon cc --min B --max E',
            'name': 'Radon (https://radon.readthedocs.io/en/latest/)',
            'packages': ['radon']
        })