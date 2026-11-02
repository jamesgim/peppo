"""Build a portable deck ZIP from the current checked-out files."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import re

root = Path(__file__).resolve().parents[1]
deck = root / 'peppo_camp_deck'
page = (deck / 'index.html').read_text(encoding='utf-8')
missing = [name for name in set(re.findall(r'images/[^\s\"\'<>]+\.png', page)) if not (deck / name).is_file()]
if missing:
    raise SystemExit('Missing images: ' + ', '.join(sorted(missing)))
out = root / 'dist' / 'PEPPO_CAMP_latest.zip'
out.parent.mkdir(exist_ok=True)
with ZipFile(out, 'w', ZIP_DEFLATED) as archive:
    for path in sorted(deck.rglob('*')):
        if path.is_file() and '__pycache__' not in path.parts and path.suffix != '.pyc':
            archive.write(path, path.relative_to(root))
with ZipFile(out) as archive:
    assert archive.testzip() is None
print(out)
