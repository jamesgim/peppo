"""Create a timestamped, versioned HTML snapshot and portable ZIP (KST)."""
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import argparse,zipfile,hashlib,json,shutil
p=argparse.ArgumentParser();p.add_argument('version');a=p.parse_args()
if not __import__('re').fullmatch(r'v\d+\.\d+\.\d+',a.version):raise SystemExit('Use vMAJOR.MINOR.PATCH')
r=Path(__file__).resolve().parents[1];deck=r/'peppo_camp_deck'
stamp=datetime.now(ZoneInfo('Asia/Seoul')).strftime('%Y%m%d_%H%M_KST')
name=f'{stamp}_{a.version}_PEPPO_WORLD'
html=deck/f'{name}.html';shutil.copy2(deck/'index.html',html)
out=r/'releases';out.mkdir(exist_ok=True);zpath=out/f'{name}.zip'
with zipfile.ZipFile(zpath,'w',zipfile.ZIP_DEFLATED) as z:
 for f in [deck/'index.html',html,deck/'README.txt',deck/'image_manifest.json',*sorted((deck/'images').glob('*'))]:
  if f.is_file():z.write(f,Path(name)/f.relative_to(deck))
with zipfile.ZipFile(zpath) as z:assert z.testzip() is None
meta={'version':a.version,'created_kst':stamp,'html':str(html.relative_to(r)),'zip':str(zpath.relative_to(r)),'sha256':hashlib.sha256(zpath.read_bytes()).hexdigest(),'bytes':zpath.stat().st_size}
(out/f'{name}.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2));print(json.dumps(meta,ensure_ascii=False))
