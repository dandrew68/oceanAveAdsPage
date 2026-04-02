(() => {
  const initCarousel = () => {
    const carousel = document.querySelector("[data-carousel]");
    if (!carousel || carousel.dataset.ready === "true") {
      return;
    }
    carousel.dataset.ready = "true";
    const images = Array.from(carousel.querySelectorAll(".carousel-image"));
    const dots = Array.from(carousel.querySelectorAll(".dot"));
    const prevBtn = carousel.querySelector("[data-action='prev']");
    const nextBtn = carousel.querySelector("[data-action='next']");
    if (!images.length) {
      return;
    }
    let index = 0;

    const show = (nextIndex) => {
      images[index].classList.remove("is-active");
      if (dots[index]) {
        dots[index].classList.remove("is-active");
      }
      index = (nextIndex + images.length) % images.length;
      images[index].classList.add("is-active");
      if (dots[index]) {
        dots[index].classList.add("is-active");
      }
    };

    prevBtn?.addEventListener("click", () => show(index - 1));
    nextBtn?.addEventListener("click", () => show(index + 1));
    dots.forEach((dot, dotIndex) => {
      dot.addEventListener("click", () => show(dotIndex));
    });
  };

  const observeReady = () => {
    initCarousel();
    const observer = new MutationObserver(() => initCarousel());
    observer.observe(document.body, { childList: true, subtree: true });
  };

  document.addEventListener("DOMContentLoaded", observeReady);
  window.addEventListener("load", observeReady);
})();
