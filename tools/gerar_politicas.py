"""Gera as páginas de políticas (PT-BR) e o rodapé da página principal.

Preencha EMPRESA com os dados reais e rode:
    python tools/gerar_politicas.py
"""
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

EMPRESA = {
    "produto": "365 Receitas Sem Açúcar, Sem Glúten e Sem Lactose",
    "marca": "Chef Luana Queiroz",
    "email": "entregasdrive159@gmail.com",
    "plataforma": "Cakto",
    "atualizado": "17 de outubro de 2026",
}

PAGINAS = [
    ("politica-de-privacidade", "Política de Privacidade"),
    ("termos-de-uso", "Termos de Uso"),
    ("politica-de-reembolso", "Política de Reembolso"),
    ("aviso-legal", "Aviso Legal"),
    ("contato", "Contato"),
]

CONTEUDO = {
"politica-de-privacidade": """
<p>Esta Política de Privacidade explica como os responsáveis pelo produto <strong>{produto}</strong> (“nós”), coleta, usa e protege os dados pessoais de quem visita este site ou adquire o produto, em conformidade com a Lei Geral de Proteção de Dados (Lei nº 13.709/2018 – LGPD).</p>

<h2>1. Quais dados coletamos</h2>
<ul>
<li><strong>Dados fornecidos por você na compra:</strong> nome, e-mail, telefone e CPF, informados no checkout da plataforma de pagamento {plataforma}.</li>
<li><strong>Dados de navegação:</strong> endereço IP, tipo de navegador e dispositivo, páginas visitadas, origem do acesso e interações com a página, coletados por cookies e tecnologias semelhantes.</li>
<li><strong>Dados de contato:</strong> informações que você envia ao falar com o nosso suporte.</li>
</ul>
<p>Não coletamos dados de cartão de crédito. O pagamento é processado diretamente pela plataforma {plataforma}, que possui sua própria política de privacidade.</p>

<h2>2. Para que usamos os dados</h2>
<ul>
<li>Entregar o acesso ao produto adquirido e enviar comunicações sobre a compra;</li>
<li>Prestar suporte e responder às suas solicitações;</li>
<li>Processar pedidos de reembolso dentro do prazo de garantia;</li>
<li>Medir o desempenho do site e das campanhas de anúncios e melhorar a sua experiência;</li>
<li>Cumprir obrigações legais e fiscais.</li>
</ul>

<h2>3. Cookies e anúncios</h2>
<p>Este site utiliza cookies próprios e de terceiros, incluindo os do <strong>Google</strong> (Google Ads e Google Analytics), para medir visitas, entender quais anúncios trazem resultados e exibir anúncios relevantes em outros sites (remarketing).</p>
<p>O Google, como fornecedor terceirizado, usa cookies para veicular anúncios com base em visitas anteriores a este e a outros sites. Você pode desativar a publicidade personalizada nas <a href="https://adssettings.google.com" target="_blank" rel="noopener">Configurações de anúncios do Google</a> e saber mais em <a href="https://policies.google.com/technologies/ads?hl=pt-BR" target="_blank" rel="noopener">Como o Google usa cookies em publicidade</a>. Também é possível bloquear ou apagar cookies nas configurações do seu navegador.</p>

<h2>4. Compartilhamento de dados</h2>
<p>Não vendemos seus dados. Compartilhamos apenas o necessário com:</p>
<ul>
<li>a plataforma de pagamento {plataforma}, para processar a compra e a entrega;</li>
<li>ferramentas de análise e anúncios (como o Google), de forma agregada ou pseudonimizada;</li>
<li>autoridades públicas, quando exigido por lei.</li>
</ul>

<h2>5. Por quanto tempo guardamos</h2>
<p>Mantemos seus dados apenas pelo tempo necessário para as finalidades acima ou para cumprir obrigações legais. Depois disso, eles são excluídos ou anonimizados.</p>

<h2>6. Seus direitos</h2>
<p>Pela LGPD, você pode, a qualquer momento: confirmar se tratamos seus dados, acessá-los, corrigi-los, pedir a exclusão ou anonimização, revogar consentimentos e solicitar a portabilidade. Para isso, escreva para <a href="mailto:{email}">{email}</a>. Respondemos em até 15 dias.</p>

<h2>7. Segurança</h2>
<p>Adotamos medidas técnicas e administrativas razoáveis para proteger seus dados contra acessos não autorizados, perda ou alteração.</p>

<h2>8. Alterações</h2>
<p>Esta política pode ser atualizada. A data da última versão fica sempre indicada no topo desta página.</p>
""",

"termos-de-uso": """
<p>Ao acessar este site e adquirir o produto <strong>{produto}</strong>, você concorda com os termos abaixo. Leia com atenção.</p>

<h2>1. O produto</h2>
<p>O {produto} é um <strong>produto digital</strong> (e-book/material em PDF) com receitas culinárias. Não há envio de produto físico. O acesso é enviado para o e-mail informado na compra logo após a confirmação do pagamento.</p>

<h2>2. Compra e pagamento</h2>
<p>A compra é feita por meio da plataforma {plataforma}, que processa o pagamento e emite a confirmação. Os preços exibidos na página são os valores finais cobrados no checkout.</p>

<h2>3. Licença de uso</h2>
<p>Ao comprar, você recebe uma licença pessoal, intransferível e não exclusiva para usar o material. É proibido copiar, revender, distribuir, compartilhar publicamente ou disponibilizar o conteúdo, total ou parcialmente, sem autorização por escrito. Todo o conteúdo é protegido pela Lei de Direitos Autorais (Lei nº 9.610/1998).</p>

<h2>4. Natureza das informações</h2>
<p>As receitas têm caráter informativo e culinário. Elas <strong>não substituem</strong> orientação de médico, nutricionista ou outro profissional de saúde. Se você tem alergias, intolerâncias, diabetes ou qualquer condição de saúde, consulte um profissional antes de mudar sua alimentação e confira sempre os rótulos dos ingredientes.</p>

<h2>5. Garantia e reembolso</h2>
<p>Você tem 15 dias de garantia a partir da compra, conforme a nossa <a href="../politica-de-reembolso/">Política de Reembolso</a>.</p>

<h2>6. Limitação de responsabilidade</h2>
<p>Não nos responsabilizamos por resultados individuais, pelo uso inadequado das receitas ou por reações a ingredientes. Os resultados podem variar de pessoa para pessoa.</p>

<h2>7. Alterações</h2>
<p>Podemos atualizar estes termos a qualquer momento. A versão vigente é sempre a publicada nesta página.</p>

<h2>8. Foro</h2>
<p>Estes termos são regidos pelas leis brasileiras. Fica eleito o foro do domicílio do consumidor para resolver eventuais conflitos.</p>
""",

"politica-de-reembolso": """
<p>Queremos que você fique satisfeito(a) com o <strong>{produto}</strong>. Por isso, oferecemos uma <strong>garantia incondicional de 15 dias</strong>.</p>

<h2>1. Prazo</h2>
<p>Você pode pedir o reembolso em até <strong>15 dias corridos</strong> a partir da data da compra, sem precisar justificar o motivo. Esse prazo é maior que os 7 dias previstos no Art. 49 do Código de Defesa do Consumidor.</p>

<h2>2. Como pedir</h2>
<ul>
<li>Pela própria plataforma {plataforma}, usando o link de suporte que chega no e-mail de confirmação da compra; ou</li>
<li>Enviando um e-mail para <a href="mailto:{email}">{email}</a> com o nome e o e-mail usados na compra.</li>
</ul>

<h2>3. Como o valor é devolvido</h2>
<ul>
<li><strong>Pix ou boleto:</strong> devolvido na conta informada, em até 7 dias úteis após a aprovação;</li>
<li><strong>Cartão de crédito:</strong> estornado na fatura. Dependendo da data de fechamento, pode aparecer em até duas faturas seguintes, conforme as regras da operadora do cartão.</li>
</ul>

<h2>4. Depois do reembolso</h2>
<p>Com o reembolso, o acesso ao material é cancelado e a licença de uso deixa de valer.</p>
""",

"aviso-legal": """
<h2>Não substitui orientação profissional</h2>
<p>O conteúdo do {produto} é culinário e informativo. Ele não é um tratamento, dieta prescrita ou orientação médica e não substitui o acompanhamento de médico ou nutricionista. Pessoas com alergias, intolerâncias, doença celíaca, diabetes ou outras condições de saúde devem consultar um profissional e conferir os rótulos de todos os ingredientes.</p>

<h2>Resultados</h2>
<p>Os depoimentos exibidos refletem experiências individuais. Os resultados podem variar de pessoa para pessoa e não há garantia de resultados específicos.</p>

<h2>Marcas de terceiros</h2>
<p>Este site não faz parte do Google, YouTube, Facebook ou Instagram e não é endossado por essas empresas. Google e YouTube são marcas da Google LLC; Facebook e Instagram são marcas da Meta Platforms, Inc.</p>

<h2>Imagens</h2>
<p>As fotos de receitas são ilustrativas. A aparência do prato pode variar conforme os ingredientes e o preparo.</p>
""",

"contato": """
<p>Precisa de ajuda com a sua compra, acesso ou reembolso? Fale com a gente.</p>
<div class="caixa">
<p><strong>E-mail de suporte:</strong><br><a href="mailto:{email}">{email}</a></p>
<p><strong>Horário de atendimento:</strong><br>Segunda a sexta, das 9h às 18h (horário de Brasília). Respondemos em até 1 dia útil.</p>
</div>
<h2>Dúvidas comuns</h2>
<ul>
<li><strong>Não recebi o acesso:</strong> confira a caixa de spam e a aba Promoções do seu e-mail. Se não encontrar, escreva para nós com o e-mail usado na compra.</li>
<li><strong>Quero reembolso:</strong> veja a nossa <a href="../politica-de-reembolso/">Política de Reembolso</a>.</li>
</ul>
""",
}

ESTILO = """
:root{--verde:#064e3b;--verde-escuro:#043f31;--laranja:#ea580c;--texto:#292524;--suave:#57534e;--fundo:#fafaf9;--borda:#e7e5e4}
*{box-sizing:border-box}
body{margin:0;font-family:Poppins,system-ui,sans-serif;background:var(--fundo);color:var(--texto);line-height:1.7}
header{background:var(--verde);color:#fff;padding:18px 16px;text-align:center}
header a{color:#fff;text-decoration:none;font-weight:700;font-size:15px}
main{max-width:760px;margin:0 auto;padding:32px 16px 48px}
h1{color:var(--verde);font-size:28px;line-height:1.25;margin:0 0 4px;font-weight:800}
.data{color:var(--suave);font-size:13px;margin:0 0 24px}
h2{color:var(--verde);font-size:18px;margin:28px 0 8px;font-weight:700}
p,li{font-size:15px}
ul{padding-left:20px}
a{color:var(--laranja)}
.caixa{background:#fff;border:1px solid var(--borda);border-radius:16px;padding:8px 20px;margin:20px 0}
.voltar{display:inline-block;margin-top:32px;background:#16a34a;color:#fff;text-decoration:none;font-weight:700;padding:12px 22px;border-radius:12px}
"""


def rodape(prefixo):
    e = EMPRESA
    links = "".join(
        f'<a href="{prefixo}{slug}/" style="color:#fff;text-decoration:underline;text-underline-offset:3px">{titulo}</a>'
        for slug, titulo in PAGINAS
    )
    return f"""<footer style="background:#043f31;color:rgba(255,255,255,.8);padding:40px 16px;text-align:center;font-family:Poppins,system-ui,sans-serif">
<div style="max-width:760px;margin:0 auto">
<p style="font-weight:700;color:#fff;margin:0 0 6px">{e['produto']}</p>
<p style="font-size:13px;margin:0 0 20px">Suporte: <a href="mailto:{e['email']}" style="color:#fff">{e['email']}</a></p>
<nav aria-label="Links legais" style="display:flex;flex-wrap:wrap;justify-content:center;gap:10px 20px;font-size:14px;font-weight:600;margin-bottom:24px">{links}</nav>
<p style="font-size:12px;color:rgba(255,255,255,.65);line-height:1.6;margin:0 0 10px">Este produto não substitui o acompanhamento de médico ou nutricionista. Os resultados e depoimentos são individuais e podem variar de pessoa para pessoa. As imagens são ilustrativas.</p>
<p style="font-size:12px;color:rgba(255,255,255,.65);line-height:1.6;margin:0 0 16px">Este site não faz parte do Google, YouTube, Facebook ou Instagram e não é endossado por essas empresas.</p>
<p style="font-size:13px;margin:0">© 2026 {e['marca']}. Todos os direitos reservados.</p>
</div>
</footer>"""


AVISO_COOKIES = """<div id="aviso-cookies" role="dialog" aria-label="Aviso de cookies" style="display:none;position:fixed;left:12px;right:12px;bottom:12px;z-index:60;max-width:560px;margin:0 auto;background:#fff;color:#292524;border-radius:16px;box-shadow:0 10px 30px rgba(0,0,0,.25);padding:14px 16px;font-family:Poppins,system-ui,sans-serif;font-size:13px;line-height:1.5">
<p style="margin:0 0 10px">Usamos cookies para melhorar sua experiência e medir nossos anúncios. Saiba mais na nossa <a href="{prefixo}politica-de-privacidade/" style="color:#ea580c">Política de Privacidade</a>.</p>
<button type="button" id="aceitar-cookies" style="background:#16a34a;color:#fff;border:0;border-radius:10px;padding:9px 18px;font-weight:700;font-family:inherit;cursor:pointer">Entendi</button>
</div>
<script>(function(){var k="aviso-cookies-ok",a=document.getElementById("aviso-cookies");try{if(localStorage.getItem(k))return}catch(e){}a.style.display="block";document.getElementById("aceitar-cookies").onclick=function(){a.style.display="none";try{localStorage.setItem(k,"1")}catch(e){}}})();</script>"""


def pagina(slug, titulo):
    corpo = CONTEUDO[slug].format(**EMPRESA)
    data = "" if slug == "contato" else f'<p class="data">Última atualização: {EMPRESA["atualizado"]}</p>'
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titulo} | {EMPRESA['produto']}</title>
<meta name="description" content="{titulo} do produto {EMPRESA['produto']}.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800&display=swap">
<style>{ESTILO}</style>
</head>
<body>
<header><a href="../">← {EMPRESA['produto']}</a></header>
<main>
<h1>{titulo}</h1>
{data}
{corpo}
<a class="voltar" href="../">Voltar para a página</a>
</main>
{rodape('../')}
</body>
</html>
"""


def main():
    for slug, titulo in PAGINAS:
        os.makedirs(os.path.join(RAIZ, slug), exist_ok=True)
        with open(os.path.join(RAIZ, slug, "index.html"), "w", encoding="utf-8") as f:
            f.write(pagina(slug, titulo))

    caminho = os.path.join(RAIZ, "index.html")
    h = open(caminho, encoding="utf-8").read()
    h = re.sub(r"<footer.*?</footer>", lambda m: rodape(""), h, count=1, flags=re.S)
    h = re.sub(r'\n?<div id="aviso-cookies".*?</script>', "", h, flags=re.S)
    h = h.replace('<script src="assets/app.js"></script>',
                  AVISO_COOKIES.replace("{prefixo}", "") + '\n<script src="assets/app.js"></script>', 1)
    open(caminho, "w", encoding="utf-8").write(h)
    print("ok:", ", ".join(s for s, _ in PAGINAS))


if __name__ == "__main__":
    main()
