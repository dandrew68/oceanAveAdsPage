(() => {
  document.addEventListener("click", (event) => {
    const link = event.target.closest("[data-analytics-event]");
    if (!link || typeof window.gtag !== "function") {
      return;
    }

    window.gtag("event", link.dataset.analyticsEvent, {
      destination_url: link.href,
      link_text: link.textContent.trim(),
      transport_type: "beacon",
    });
  });
})();
