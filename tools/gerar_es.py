"""Gera es/index.html a partir de index.html.

Uso: python tools/gerar_es.py index.html tools/es.json es/index.html
"""
import sys,re,json
src,dic,out=sys.argv[1:4]
h=open(src,encoding='utf-8').read()
# o /es mantém o rodapé próprio e não tem o aviso de cookies em PT
h=re.sub(r'<footer.*?</footer>',lambda m:'@@RODAPE_ES@@',h,count=1,flags=re.S)
h=re.sub(r'\n?<div id="aviso-cookies".*?</script>','',h,flags=re.S)
h=re.sub(r'<!-- Google tag \(gtag.js\) -->.*?<!-- /Google tag -->\n','',h,flags=re.S)  # tag do Google só no PT
T=json.load(open(dic,encoding='utf-8'))
miss=[]
def tr(s):
    t=s.strip()
    if not t or not re.search('[A-Za-zÀ-ú]',t): return s
    if t in T: return s.replace(t,T[t])
    miss.append(t); return s
# text nodes (skip inside <script>)
parts=re.split(r'(<script.*?</script>)',h,flags=re.S)
for i,p in enumerate(parts):
    if p.startswith('<script'): continue
    p=re.sub(r'>([^<>]+)<',lambda m:'>'+tr(m.group(1))+'<',p)
    p=re.sub(r'\b(alt|placeholder|aria-label|content)="([^"]*)"',lambda m:m.group(1)+'="'+(T.get(m.group(2),m.group(2)))+'"',p)
    parts[i]=p
h=''.join(parts)
h=h.replace('</head>','<!-- UTMify -->\n<script src="https://cdn.utmify.com.br/scripts/utms/latest.js" data-utmify-prevent-xcod-sck data-utmify-prevent-subids async defer></script>\n<script>window.pixelId = "6a0cd702e8bb6229c5902383";\n  var a = document.createElement("script");\n  a.setAttribute("async", ""); a.setAttribute("defer", "");\n  a.setAttribute("src", "https://cdn.utmify.com.br/scripts/pixel/pixel.js");\n  document.head.appendChild(a);\n</script>\n'+'</head>',1)
h=h.replace('<html lang="pt-BR">','<html lang="es">')
h=h.replace('href="assets/','href="../assets/').replace('src="assets/','src="../assets/')
open(out,'w',encoding='utf-8').write(h)
print('faltando:',[m for m in miss if m not in('AM','JS','CF','PR','RB','LC','Ana M.','Juliana S.','Camila F.','Patricia R.','Renata B.','Larissa C.')])

# --- precios en dólares + precio local por IP ---
h=open(out,encoding='utf-8').read()
local='<p data-precio-local="%s" class="font-semibold" style="display:none;font-size:13px;line-height:1.3;color:#57534e;margin-top:4px"></p>'
P=[('leading-none">R$ 10</p>','leading-none" style="white-space:nowrap"><span style="font-size:.5em;vertical-align:.45em;margin-right:.08em">US$</span>6</p>'+local%'6'),
   ('leading-none">R$ 18</p>','leading-none" style="white-space:nowrap"><span style="font-size:.5em;vertical-align:.45em;margin-right:.08em">US$</span>9,90</p>'+local%'9.90'),
   ('De R$ 97,00 por solo','De US$ 57,00 por solo'),
   ('De R$ 197,00 por solo','De US$ 117,00 por solo'),
   ('>R$ 29,90<','>US$ 17,90<'),('>R$ 39,90<','>US$ 23,90<'),('>R$ 24,90<','>US$ 14,90<')]
for a,b in P:
    assert a in h,a; h=h.replace(a,b)
h=h.replace('<script src="../assets/app.js"></script>','<script src="../assets/app.js"></script>\n<script src="../assets/precio-local.js"></script>')
assert 'R$' not in h
h=h.replace('https://pay.cakto.com.br/jat9wer_1210800','https://pay.wiapy.com/Ci6of1B5M1ll').replace('https://pay.cakto.com.br/3e626fx_1210811','https://pay.wiapy.com/3IdUSNfye7KS')
open(out,'w',encoding='utf-8').write(h)
h=open(out,encoding='utf-8').read().replace('@@RODAPE_ES@@','<footer class="bg-[var(--brand-green-deep)] text-white/80 py-10 px-4 text-center"><p class="font-bold text-white mb-2">365 Recetas Sin Azúcar, Sin Gluten y Sin Lactosa</p><p class="text-sm">© 2026 Todos los derechos reservados.</p><p class="text-xs mt-3 text-white/60">El checkout se configurará más adelante.</p></footer>')
open(out,'w',encoding='utf-8').write(h)
