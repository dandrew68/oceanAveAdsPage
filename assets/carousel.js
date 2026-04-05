(() => {
  const AUTOPLAY_MS = 10000;
  const USER_PAUSE_MS = 60000;

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
    let autoplayTimer;
    let resumeTimer;

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

    const startAutoplay = () => {
      if (images.length < 2) {
        return;
      }
      clearInterval(autoplayTimer);
      autoplayTimer = window.setInterval(() => {
        show(index + 1);
      }, AUTOPLAY_MS);
    };

    const pauseAutoplayAfterManualControl = () => {
      clearInterval(autoplayTimer);
      clearTimeout(resumeTimer);
      resumeTimer = window.setTimeout(() => {
        startAutoplay();
      }, USER_PAUSE_MS);
    };

    prevBtn?.addEventListener("click", () => {
      show(index - 1);
      pauseAutoplayAfterManualControl();
    });
    nextBtn?.addEventListener("click", () => {
      show(index + 1);
      pauseAutoplayAfterManualControl();
    });
    dots.forEach((dot, dotIndex) => {
      dot.addEventListener("click", () => show(dotIndex));
    });

    startAutoplay();
  };

  const observeReady = () => {
    initCarousel();
    const observer = new MutationObserver(() => initCarousel());
    observer.observe(document.body, { childList: true, subtree: true });
  };

  document.addEventListener("DOMContentLoaded", observeReady);
  window.addEventListener("load", observeReady);
})();
