// Muestra debajo de cada precio en dólares el valor aproximado en la moneda local del visitante (según su IP).
(function () {
  var campos = document.querySelectorAll("[data-precio-local]");
  if (!campos.length || !window.fetch) return;

  var MONEDAS = {
    AR: "ARS", BO: "BOB", BR: "BRL", CL: "CLP", CO: "COP", CR: "CRC", CU: "CUP", DO: "DOP",
    EC: "USD", SV: "USD", GT: "GTQ", HN: "HNL", MX: "MXN", NI: "NIO", PA: "USD", PY: "PYG",
    PE: "PEN", PR: "USD", UY: "UYU", VE: "VES", ES: "EUR", US: "USD"
  };
  var CLAVE = "precio-local-v1";

  function leerCache() {
    try { return JSON.parse(sessionStorage.getItem(CLAVE) || "null"); } catch (e) { return null; }
  }
  function guardarCache(d) {
    try { sessionStorage.setItem(CLAVE, JSON.stringify(d)); } catch (e) {}
  }
  function json(url) {
    return fetch(url).then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); });
  }

  // País del visitante: intenta ipapi.co y, si falla, ipwho.is
  function obtenerPais() {
    return json("https://ipapi.co/json/")
      .then(function (d) {
        if (!d.country_code) throw new Error("sin país");
        return { pais: d.country_code, moneda: d.currency };
      })
      .catch(function () {
        return json("https://ipwho.is/").then(function (d) {
          if (!d.success) throw new Error("sin país");
          return { pais: d.country_code, moneda: d.currency && d.currency.code };
        });
      });
  }

  function mostrar(d) {
    if (!d || !d.moneda || d.moneda === "USD" || !d.tasa) return;
    var nombre = d.moneda;
    try {
      nombre = new Intl.DisplayNames(["es"], { type: "currency" }).of(d.moneda);
      nombre = nombre.charAt(0).toUpperCase() + nombre.slice(1);
    } catch (e) {}
    campos.forEach(function (el) {
      var valor = parseFloat(el.getAttribute("data-precio-local")) * d.tasa;
      var decimales = valor >= 1000 ? 0 : 2;
      var numero;
      try {
        numero = new Intl.NumberFormat("es-" + d.pais, {
          style: "currency", currency: d.moneda, currencyDisplay: "narrowSymbol",
          minimumFractionDigits: decimales, maximumFractionDigits: decimales
        }).format(valor);
      } catch (e) {
        numero = valor.toFixed(decimales);
      }
      el.textContent = "≈ " + numero + " " + d.moneda + " · " + nombre;
      el.style.display = "block";
    });
  }

  var cache = leerCache();
  if (cache) return mostrar(cache);

  obtenerPais()
    .then(function (p) {
      var moneda = MONEDAS[p.pais] || p.moneda;
      if (!moneda || moneda === "USD") return null;
      return json("https://open.er-api.com/v6/latest/USD").then(function (r) {
        var tasa = r && r.rates && r.rates[moneda];
        return tasa ? { pais: p.pais, moneda: moneda, tasa: tasa } : null;
      });
    })
    .then(function (d) { if (d) { guardarCache(d); mostrar(d); } })
    .catch(function () {});
})();
