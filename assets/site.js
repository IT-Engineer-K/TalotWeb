/* ひとやすみタロット — 月齢の月と数秘術の計算（アプリと同じ計算） */
(function () {
  "use strict";
  var SYNODIC = 29.530588853;                      // 平均の朔望月（日）
  var REF_NEW_MOON = Date.UTC(2000, 0, 6, 18, 14); // 基準の新月 2000-01-06 18:14 UTC
  var NAMES = ["新月", "三日月", "上弦の月", "満ちていく月", "満月", "欠けていく月", "下弦の月", "有明の月"];

  function moonAge(date) {
    var days = (date.getTime() - REF_NEW_MOON) / 86400000;
    var age = days % SYNODIC;
    if (age < 0) age += SYNODIC;
    return age;
  }
  function phaseIndex(age) { return Math.round((age / SYNODIC) * 8) % 8; }
  function isFullDay(age) { return Math.abs(age - SYNODIC / 2) < 0.75; }

  // 光っている部分：縁の半円＋境目の半分の楕円（日本の見え方：満ちるときは右が光る）
  function litPath(cx, cy, r, p) {
    var side = p < 0.5 ? 1 : -1;
    var e = r * Math.cos(2 * Math.PI * p);
    var pts = [], i, t;
    for (i = 0; i <= 48; i++) { t = Math.PI * i / 48; pts.push([cx + side * r * Math.sin(t), cy - r * Math.cos(t)]); }
    for (i = 48; i >= 0; i--) { t = Math.PI * i / 48; pts.push([cx + side * e * Math.sin(t), cy - r * Math.cos(t)]); }
    return "M" + pts.map(function (q) { return q[0].toFixed(2) + "," + q[1].toFixed(2); }).join(" L") + " Z";
  }
  var uid = 0;
  function moonSvg(p, gold) {
    var id = "mg" + (uid++);
    var c1 = gold ? "#FFF1C4" : "#FFF7E0", c2 = gold ? "#D4B26A" : "#E6D3A3";
    return '<svg viewBox="0 0 100 100" aria-hidden="true">' +
      '<defs><radialGradient id="' + id + '" cx="38%" cy="35%" r="70%"><stop offset="0" stop-color="' + c1 + '"/><stop offset="1" stop-color="' + c2 + '"/></radialGradient></defs>' +
      '<circle cx="50" cy="50" r="46" fill="#2E3566" stroke="#E6D3A3" stroke-opacity=".35" stroke-width="1"/>' +
      '<path d="' + litPath(50, 50, 46, p) + '" fill="url(#' + id + ')"/></svg>';
  }
  window.HitoyasumiMoon = { svg: moonSvg, names: NAMES };

  var now = new Date();
  var age = moonAge(now);
  var p = age / SYNODIC;
  var idx = phaseIndex(age);
  var full = isFullDay(age);

  // 今の月を描く
  document.querySelectorAll("[data-moon-now]").forEach(function (el) { el.innerHTML = moonSvg(p, full); });
  // 決まった形の月を描く（data-moon-phase="0〜7"）
  document.querySelectorAll("[data-moon-phase]").forEach(function (el) {
    var k = parseInt(el.getAttribute("data-moon-phase"), 10);
    el.innerHTML = moonSvg(k / 8 + (k === 0 ? 0.001 : 0), false);
  });
  // 名前・月齢・一言
  document.querySelectorAll("[data-moon-name]").forEach(function (el) { el.textContent = NAMES[idx]; });
  document.querySelectorAll("[data-moon-age]").forEach(function (el) { el.textContent = age.toFixed(1); });
  var moonText = document.getElementById("moon-texts");
  if (moonText) {
    try {
      var texts = JSON.parse(moonText.textContent);
      document.querySelectorAll("[data-moon-text]").forEach(function (el) { el.textContent = texts[String(idx)] || ""; });
    } catch (e) { /* 何もしない */ }
  }
  document.querySelectorAll("[data-moon-card]").forEach(function (el) {
    el.classList.toggle("is-current", parseInt(el.getAttribute("data-moon-card"), 10) === idx);
  });

  // 数秘術：ライフパスナンバー（11・22・33 はそのまま）とパーソナルデイ
  function digits(n) { return String(n).split("").reduce(function (s, d) { return s + Number(d); }, 0); }
  function reduce(n, keepMaster) {
    while (n > 9 && !(keepMaster && (n === 11 || n === 22 || n === 33))) n = digits(n);
    return n;
  }
  var form = document.getElementById("np-form");
  var numData = document.getElementById("np-texts");
  if (form && numData) {
    var data = JSON.parse(numData.textContent);
    form.addEventListener("submit", function (ev) {
      ev.preventDefault();
      var y = parseInt(form.y.value, 10), m = parseInt(form.m.value, 10), d = parseInt(form.d.value, 10);
      var out = document.getElementById("np-result");
      var test = new Date(y, m - 1, d);
      if (!y || !m || !d || test.getMonth() !== m - 1 || y < 1900 || y > now.getFullYear()) {
        out.classList.add("show");
        out.innerHTML = '<p class="muted">生年月日をもう一度ご確認ください。</p>';
        return;
      }
      var lp = reduce(digits(y) + digits(m) + digits(d), true);
      var today = digits(now.getFullYear()) + digits(now.getMonth() + 1) + digits(now.getDate());
      var pd = reduce(digits(m) + digits(d) + today, false);
      var master = (lp > 9) ? "（マスターナンバー）" : "";
      out.innerHTML =
        '<p class="muted small" style="margin:0">あなたのライフパスナンバー</p>' +
        '<div class="big-num">' + lp + '<span style="font-size:20px">' + master + '</span></div>' +
        '<p>' + (data.lifePath[String(lp)] || "") + '</p>' +
        '<p class="muted small" style="margin:18px 0 0">今日のパーソナルデイ</p>' +
        '<div class="big-num" style="font-size:40px">' + pd + '</div>' +
        '<p>' + (data.day[String(pd)] || "") + '</p>';
      out.classList.add("show");
    });
  }
})();
