(function () {
  var es = (document.documentElement.lang || "").indexOf("es") === 0;
  var L = es
    ? { locale: "es-MX", curtir: "Me gusta", placeholder: "Escribe un comentario...", enviar: "Enviar", voce: "Tú: " }
    : { locale: "pt-BR", curtir: "Curtir", placeholder: "Escreva um comentário...", enviar: "Enviar", voce: "Você: " };
  var hoje = new Date().toLocaleDateString(L.locale, { day: "2-digit", month: "2-digit", year: "numeric" });
  document.querySelectorAll("[data-hoje]").forEach(function (el) { el.textContent = hoje; });

  // Rolagem suave até a oferta
  function rolar(destino, duracao) {
    var inicio = window.pageYOffset, dist = destino - inicio;
    if (Math.abs(dist) < 2) return;
    var t0 = performance.now();
    var ease = function (c) { return c < .5 ? 4 * c * c * c : 1 - Math.pow(-2 * c + 2, 3) / 2; };
    (function passo(agora) {
      var p = Math.min((agora - t0) / duracao, 1);
      window.scrollTo(0, inicio + dist * ease(p));
      if (p < 1) requestAnimationFrame(passo);
    })(t0);
  }
  function irParaOferta() {
    var el = document.getElementById("offer");
    if (!el) return;
    var r = el.getBoundingClientRect(), topo = r.top + window.pageYOffset;
    var alvo = Math.min(topo + r.height - window.innerHeight + 20, topo - 12);
    rolar(Math.max(0, alvo), 1400);
  }
  document.querySelectorAll("button.animate-pulse-cta").forEach(function (b) { b.addEventListener("click", irParaOferta); });

  // Slideshow de receitas (troca a cada 1,5s)
  var dots = document.querySelectorAll('button[aria-label^="Slide "]');
  if (dots.length) {
    var fotos = dots[0].parentElement.previousElementSibling.querySelectorAll("img");
    var atual = 0;
    var mostrar = function (i) {
      atual = i;
      fotos.forEach(function (f, k) { f.classList.toggle("opacity-100", k === i); f.classList.toggle("opacity-0", k !== i); });
      dots.forEach(function (d, k) {
        d.classList.toggle("bg-[var(--brand-orange)]", k === i);
        d.classList.toggle("w-8", k === i);
        d.classList.toggle("bg-foreground/20", k !== i);
      });
    };
    dots.forEach(function (d, k) { d.addEventListener("click", function () { mostrar(k); }); });
    setInterval(function () { mostrar((atual + 1) % fotos.length); }, 1500);
  }

  // Carrossel de depoimentos (loop, autoplay 3s, arrastar)
  var regiao = document.querySelector('[aria-roledescription="carousel"]');
  if (regiao) {
    var janela = regiao.firstElementChild, trilho = janela.firstElementChild;
    var originais = Array.prototype.slice.call(trilho.children), total = originais.length;
    originais.forEach(function (s) { trilho.appendChild(s.cloneNode(true)); });
    originais.forEach(function (s) { trilho.insertBefore(s.cloneNode(true), trilho.firstChild); });
    var pos = total, pausado = false, arrastando = false, x0 = 0, dx = 0;
    var largura = function () { return trilho.children[0].getBoundingClientRect().width; };
    var aplicar = function (anim) {
      trilho.style.transition = anim ? "transform .5s ease" : "none";
      trilho.style.transform = "translate3d(" + (-pos * largura() + dx) + "px,0,0)";
    };
    var normalizar = function () {
      if (pos >= total * 2) { pos -= total; aplicar(false); }
      if (pos < total) { pos += total; aplicar(false); }
    };
    trilho.addEventListener("transitionend", normalizar);
    aplicar(false);
    window.addEventListener("resize", function () { aplicar(false); });
    window.addEventListener("load", function () { aplicar(false); });
    setInterval(function () { if (!pausado && !arrastando) { pos++; aplicar(true); } }, 3000);
    regiao.addEventListener("mouseenter", function () { pausado = true; });
    regiao.addEventListener("mouseleave", function () { pausado = false; });
    janela.style.touchAction = "pan-y";
    janela.style.cursor = "grab";
    janela.addEventListener("dragstart", function (e) { e.preventDefault(); });
    janela.addEventListener("pointerdown", function (e) {
      normalizar(); arrastando = true; x0 = e.clientX; dx = 0;
      janela.setPointerCapture(e.pointerId);
    });
    janela.addEventListener("pointermove", function (e) { if (arrastando) { dx = e.clientX - x0; aplicar(false); } });
    var soltar = function () {
      if (!arrastando) return;
      arrastando = false;
      var w = largura();
      if (Math.abs(dx) > w * 0.15) pos += dx < 0 ? Math.max(1, Math.round(-dx / w)) : -Math.max(1, Math.round(dx / w));
      dx = 0; aplicar(true);
    };
    janela.addEventListener("pointerup", soltar);
    janela.addEventListener("pointercancel", soltar);
  }

  // Curtir / Comentar nos depoimentos
  document.querySelectorAll("button").forEach(function (b) {
    if (!new RegExp(L.curtir + "\\s+\\d+").test(b.textContent)) return;
    var linha = b.parentElement, card = linha.parentElement, btnComentar = linha.children[1];
    var likes = parseInt(b.textContent.match(/\d+/)[0], 10), curtido = false;
    b.addEventListener("click", function () {
      curtido = !curtido; likes += curtido ? 1 : -1;
      b.innerHTML = "<span>" + (curtido ? "❤️" : "🤍") + "</span> " + L.curtir + " " + likes;
      ["bg-red-50", "border-red-200", "text-red-600"].forEach(function (c) { b.classList.toggle(c, curtido); });
      ["bg-white", "border-foreground/15", "text-foreground/70", "hover:bg-foreground/5"].forEach(function (c) { b.classList.toggle(c, !curtido); });
    });
    var lista = document.createElement("div");
    lista.className = "mt-3 space-y-1.5";
    lista.hidden = true;
    var form = document.createElement("div");
    form.className = "mt-3 flex gap-2";
    form.hidden = true;
    form.innerHTML = '<input placeholder="' + L.placeholder + '" class="flex-1 text-xs px-3 py-2 rounded-full border border-foreground/15 focus:outline-none focus:border-[var(--brand-orange)]"><button class="px-3 py-2 rounded-full bg-[var(--brand-orange)] text-white text-xs font-semibold hover:bg-[var(--brand-orange-hover)]">' + L.enviar + '</button>';
    card.appendChild(lista);
    card.appendChild(form);
    var campo = form.querySelector("input");
    var enviar = function () {
      var t = campo.value.trim();
      if (!t) return;
      var c = document.createElement("div");
      c.className = "text-xs bg-foreground/5 rounded-lg px-3 py-2 text-foreground/80";
      c.innerHTML = '<span class="font-semibold">' + L.voce + '</span>';
      c.appendChild(document.createTextNode(t));
      lista.appendChild(c); lista.hidden = false; campo.value = "";
    };
    form.querySelector("button").addEventListener("click", enviar);
    campo.addEventListener("keydown", function (e) { if (e.key === "Enter") enviar(); });
    btnComentar.addEventListener("click", function () {
      var abrir = form.hidden;
      document.querySelectorAll("[data-form-comentario]").forEach(function (f) { f.hidden = true; });
      form.hidden = !abrir;
      if (abrir) campo.focus();
    });
    form.setAttribute("data-form-comentario", "");
  });

  // FAQ (acordeão, um aberto por vez)
  var faqs = [];
  document.querySelectorAll("button").forEach(function (b) {
    var painel = b.nextElementSibling;
    if (painel && painel.classList.contains("grid-rows-[0fr]") || painel && painel.classList.contains("grid-rows-[1fr]")) faqs.push(b);
  });
  var setFaq = function (b, aberto) {
    var painel = b.nextElementSibling, titulo = b.children[0], seta = b.children[1];
    painel.classList.toggle("grid-rows-[1fr]", aberto); painel.classList.toggle("opacity-100", aberto);
    painel.classList.toggle("grid-rows-[0fr]", !aberto); painel.classList.toggle("opacity-0", !aberto);
    titulo.classList.toggle("text-[var(--brand-orange)]", aberto); titulo.classList.toggle("text-[var(--brand-green)]", !aberto);
    ["rotate-180", "bg-[var(--brand-orange)]", "text-white"].forEach(function (c) { seta.classList.toggle(c, aberto); });
    b.setAttribute("aria-expanded", aberto);
  };
  faqs.forEach(function (b) {
    b.setAttribute("aria-expanded", b.nextElementSibling.classList.contains("grid-rows-[1fr]"));
    b.addEventListener("click", function () {
      var abrir = b.getAttribute("aria-expanded") !== "true";
      faqs.forEach(function (o) { setFaq(o, false); });
      if (abrir) setFaq(b, true);
    });
  });
})();
