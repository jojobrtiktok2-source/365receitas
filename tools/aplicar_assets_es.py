from pathlib import Path
import json
root=Path(__file__).resolve().parent.parent
manifest=root/'es/assets/inventario.json'
items=json.loads(manifest.read_text(encoding='utf-8'))
p=root/'es/index.html';h=p.read_text(encoding='utf-8')
for item in items:h=h.replace(item['src'],item['localized'])
p.write_text(h,encoding='utf-8')
print('Localized image references applied:',len(items))
