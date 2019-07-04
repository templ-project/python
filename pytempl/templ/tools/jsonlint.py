from pytempl.templ.tools import BaseReq


class Jsonlint(BaseReq):
    """
    :see: https://github.com/tangwz/jsonlint/
    :see: https://pypi.org/project/jsonlint/
    """

    TOKEN = 'jsonlint'

    ORDER = 80

    def __init__(self, app=None):
        super().__init__(app)
        self._config.update({
            'hook': 'pytempl jsonlint',
            'name': 'Jsonlint (https://github.com/tangwz/jsonlint)',
            'packages': ['jsonlint']
        })