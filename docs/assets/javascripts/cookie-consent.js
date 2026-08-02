// Sitewide cookie-consent banner. No third-party trackers run on this site
// today -- this exists so we have a clear, compliant accept/reject record
// (and something proper to point to) as soon as any are added later.
(function () {
  var STORAGE_KEY = "lcCookieConsent";

  if (localStorage.getItem(STORAGE_KEY)) return;

  document.addEventListener("DOMContentLoaded", function () {
    var isLao = document.documentElement.lang === "lo";
    // Material computes __md_scope as the site root relative to the current
    // page (works correctly under both / and /lo/) -- reuse it so links
    // land on the right locale instead of hardcoding a relative path.
    var base = window.__md_scope || new URL(".", location);
    var cookiesUrl = new URL("cookies/", base).href;

    var banner = document.createElement("div");
    banner.className = "lc-cookie-banner";
    banner.setAttribute("role", "dialog");
    banner.setAttribute("aria-label", isLao ? "ການຍິນຍອມກ່ຽວກັບຄຸກກີ" : "Cookie consent");
    banner.innerHTML =
      '<img src="' + new URL("assets/img/cookie-icon.webp", base).href + '" alt="">' +
      '<div class="lc-cookie-banner-text">' +
      (isLao
        ? 'ພວກເຮົາໃຊ້ຄຸກກີ ແລະ ບ່ອນເກັບຂໍ້ມູນໃນເຄື່ອງເພື່ອຈື່ການຕັ້ງຄ່າຂອງທ່ານ (ເຊັ່ນ ໂໝດສະຫວ່າງ/ມືດ). ເບິ່ງ <a href="' + cookiesUrl + '">ນະໂຍບາຍຄຸກກີ</a> ຂອງພວກເຮົາ.'
        : 'We use cookies and similar local storage to remember your preferences (like light/dark mode). See our <a href="' + cookiesUrl + '">Cookie Policy</a>.') +
      "</div>" +
      '<div class="lc-cookie-banner-actions">' +
      '<button type="button" class="lc-cookie-accept">' + (isLao ? "ຍອມຮັບ" : "Accept") + "</button>" +
      '<button type="button" class="lc-cookie-reject">' + (isLao ? "ປະຕິເສດ" : "Reject") + "</button>" +
      "</div>";

    document.body.appendChild(banner);

    function dismiss(value) {
      localStorage.setItem(STORAGE_KEY, value);
      banner.setAttribute("hidden", "");
      setTimeout(function () {
        banner.remove();
      }, 400);
    }

    banner.querySelector(".lc-cookie-accept").addEventListener("click", function () {
      dismiss("accepted");
    });
    banner.querySelector(".lc-cookie-reject").addEventListener("click", function () {
      dismiss("rejected");
    });
  });
})();
