(() => {
  const trackListingClick = (event) => {
    const link = event.currentTarget;
    const eventName = link.dataset.analyticsEvent;
    if (!eventName || typeof window.gtag !== "function") {
      return;
    }

    window.gtag("event", eventName, {
      destination_url: link.href,
      link_text: link.textContent.trim(),
    });
  };

  const initAnalyticsTracking = () => {
    document.querySelectorAll("[data-analytics-event]").forEach((link) => {
      if (link.dataset.analyticsReady === "true") {
        return;
      }
      link.dataset.analyticsReady = "true";
      link.addEventListener("click", trackListingClick);
    });
  };

  document.addEventListener("DOMContentLoaded", initAnalyticsTracking);
  window.addEventListener("load", initAnalyticsTracking);
})();
