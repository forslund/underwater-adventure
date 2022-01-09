
from contextlib import contextmanager
from pathlib import Path

BASE_PATH = Path(Path(__file__).parent, 'locale')


@contextmanager
def open_locale_file(lang, path):
    file_path = Path(BASE_PATH, lang, path)
    with open(file_path) as f:
        yield f
