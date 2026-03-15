/**
 * copyElement(el) -- put an element's contents on the clipboard as
 * both HTML (so pasting into an email keeps its layout) and plain text
 * (for anywhere that only takes text). Returns a Promise.
 *
 * elementText(el) -- that plain text: the element as rendered, with a
 * table row's "Label<tab>value" turned into "Label: value".
 *
 * mailtoWithBody(link, el) -- set a mailto: link's body to
 * elementText(el) just before it's followed, so the email starts with
 * exactly what's shown on the page. Leaves any other query parameters
 * (e.g. the subject) as they were.
 *
 * Falls back to selecting the element and the older execCommand("copy")
 * where the async Clipboard API isn't available -- e.g. a page served
 * over plain http from anywhere but localhost.
 */
(function () {
  function copyBySelection(el) {
    const selection = window.getSelection();
    const range = document.createRange();
    range.selectNodeContents(el);
    selection.removeAllRanges();
    selection.addRange(range);
    document.execCommand("copy");
    selection.removeAllRanges();
    return Promise.resolve();
  }

  window.elementText = function (el) {
    return el.innerText.replace(/\t+/g, ": ").trim();
  };

  window.mailtoWithBody = function (link, el) {
    const [address, query = ""] = link.getAttribute("href").split("?");
    const params = new URLSearchParams(query);
    params.set("body", window.elementText(el));
    // URLSearchParams encodes spaces as "+", which mail clients show
    // literally -- mailto: wants %20 (RFC 6068).
    link.setAttribute("href", address + "?" + params.toString().replace(/\+/g, "%20"));
  };

  window.copyElement = function (el) {
    if (navigator.clipboard && window.isSecureContext && window.ClipboardItem) {
      const item = new ClipboardItem({
        "text/html": new Blob([el.innerHTML], { type: "text/html" }),
        "text/plain": new Blob([window.elementText(el)], { type: "text/plain" }),
      });
      return navigator.clipboard.write([item]).catch(function () {
        return copyBySelection(el);
      });
    }
    return copyBySelection(el);
  };
})();
