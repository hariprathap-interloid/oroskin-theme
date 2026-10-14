/**
 * <animate-on-scroll>: reveals its [data-animate] elements (including itself) as they scroll into view.
 *
 * The CSS in critical.css hides [data-animate] elements until they get the `is-visible` class.
 * This component adds that class once per element, then stops watching it.
 * When the theme editor re-renders a section, the browser runs connectedCallback again automatically.
 */
class AnimateOnScroll extends HTMLElement {
  connectedCallback() {
    const targets = [
      ...(this.matches('[data-animate]') ? [this] : []),
      ...this.querySelectorAll('[data-animate]'),
    ];
    if (!targets.length) return;

    // Reduced motion: the CSS already keeps everything visible; mark targets revealed and skip the observer
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      for (const target of targets) target.classList.add('is-visible');
      return;
    }

    this.observer = new IntersectionObserver(
      (entries) => {
        for (const entry of entries) {
          if (!entry.isIntersecting) continue;
          entry.target.classList.add('is-visible');
          this.observer.unobserve(entry.target); // animate once, then stop watching
        }
      },
      { rootMargin: '0px 0px -10% 0px', threshold: 0.1 }
    );

    for (const target of targets) this.observer.observe(target);
  }

  disconnectedCallback() {
    // The section was removed or re-rendered (theme editor): stop observing to avoid leaks
    this.observer?.disconnect();
  }
}

if (!customElements.get('animate-on-scroll')) {
  customElements.define('animate-on-scroll', AnimateOnScroll);
}
