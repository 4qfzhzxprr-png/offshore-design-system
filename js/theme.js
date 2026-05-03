// Offshore Design System — Light/Dark theme toggle.
//
// Loaded SYNCHRONOUSLY in <head> so the data-theme attribute is set before
// first paint (no flash). Reads explicit choice from localStorage; falls
// back to OS preference. Provides a toggle button injectable into any nav.
//
// Dark-mode CSS is injected at runtime — no edits needed to existing
// stylesheets, as long as they consume the design-system tokens (--navy,
// --bone, etc).
//
// Usage in a host project:
//   1. Include tokens/colors.css
//   2. Load this file synchronously in <head>:
//        <script src="path/to/theme.js"></script>
//   3. Theme is auto-resolved + applied. Toggle button auto-injected into
//      whichever nav container is found (configurable below in
//      injectToggleButton).
//   4. Use the public API at window.OffshoreTheme:
//        OffshoreTheme.get()       → 'light' | 'dark'
//        OffshoreTheme.set(theme)  → set explicitly
//        OffshoreTheme.toggle()    → flip
//
// The toggle button has class .ofs-theme-toggle and is icon-only by default;
// it shows a "Light" / "Dark" label at >= 720px. Restyle with:
//   .ofs-theme-toggle { ... }
(function () {
  'use strict';

  const STORAGE_KEY = 'offshore-theme';

  // ── 1. Resolve initial theme + set data-theme BEFORE paint ────────
  function systemPrefersDark() {
    return window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
  }
  function resolveInitialTheme() {
    let stored;
    try { stored = localStorage.getItem(STORAGE_KEY); } catch (_) {}
    if (stored === 'light' || stored === 'dark') return stored;
    return systemPrefersDark() ? 'dark' : 'light';
  }
  document.documentElement.setAttribute('data-theme', resolveInitialTheme());

  // ── 2. Inject the dark-mode CSS once ──────────────────────────────
  // This duplicates tokens/dark.css so the design system can drop in as
  // just-the-script-and-tokens-css, without needing the dark.css file to
  // be loaded separately. If you ARE loading dark.css, the duplicate
  // doesn't hurt (it's the same selectors with the same values).
  function injectDarkStyles() {
    if (document.getElementById('ofs-theme-dark-styles')) return;
    const css = `
      /* Token overrides — flip primary surfaces and ink, keep accent unchanged */
      html[data-theme="dark"] {
        --navy:        #F0EBD8;            /* primary ink → cream */
        --bone:        #0D1321;            /* primary bg → dark navy */
        --sand:        #15243A;            /* secondary bg */
        --paper:       #1D2D44;            /* lifted surfaces (cards/inputs) */
        --navy-rich:   #748CAB;            /* intermediate accent stays light blue */

        --ink:           var(--navy);
        --ink-soft:      rgba(240, 235, 216, 0.72);
        --ink-faint:     rgba(240, 235, 216, 0.48);
        --ink-quiet:     rgba(240, 235, 216, 0.28);
        --ink-hairline:  rgba(240, 235, 216, 0.10);
        --ink-whisper:   rgba(240, 235, 216, 0.05);

        --bone-soft:      rgba(13, 19, 33, 0.78);
        --bone-faint:     rgba(13, 19, 33, 0.55);
        --bone-hairline:  rgba(13, 19, 33, 0.14);

        --shadow-card:        0 1px 2px rgba(0,0,0,0.35), 0 8px 24px -8px rgba(0,0,0,0.55);
        --shadow-card-hover:  0 1px 2px rgba(0,0,0,0.45), 0 24px 48px -16px rgba(0,0,0,0.60);
        --shadow-float:       0 1px 1px rgba(0,0,0,0.30), 0 12px 32px -8px rgba(0,0,0,0.55);

        color-scheme: dark;
      }

      /* Image desaturation in dark mode — slight, so they don't scream */
      html[data-theme="dark"] img:not(.preserve-color):not([data-no-dim]) {
        filter: saturate(0.92) brightness(0.95);
      }

      /* The toggle button itself */
      .ofs-theme-toggle {
        background: transparent;
        border: 1px solid rgba(29, 45, 68, 0.14);
        border-radius: 999px;
        color: rgba(29, 45, 68, 0.72);
        cursor: pointer;
        padding: 6px 10px;
        display: inline-flex; align-items: center; justify-content: center;
        gap: 6px;
        font-family: 'Inter', system-ui, sans-serif;
        font-size: 11px; font-weight: 500;
        text-transform: uppercase; letter-spacing: 0.14em;
        transition: color 200ms cubic-bezier(0.23,1,0.32,1),
                    border-color 200ms cubic-bezier(0.23,1,0.32,1);
      }
      html[data-theme="dark"] .ofs-theme-toggle {
        border-color: rgba(240, 235, 216, 0.14);
        color: rgba(240, 235, 216, 0.72);
      }
      .ofs-theme-toggle:hover { color: var(--navy, #1D2D44); border-color: rgba(29,45,68,0.32); }
      html[data-theme="dark"] .ofs-theme-toggle:hover { color: #F0EBD8; border-color: rgba(240,235,216,0.32); }
      .ofs-theme-toggle svg { width: 14px; height: 14px; flex-shrink: 0; }
      .ofs-theme-toggle .label { display: none; }
      @media (min-width: 720px) {
        .ofs-theme-toggle .label { display: inline; }
      }
    `;
    const style = document.createElement('style');
    style.id = 'ofs-theme-dark-styles';
    style.textContent = css;
    (document.head || document.documentElement).appendChild(style);
  }
  injectDarkStyles();

  // ── 3. Toggle helpers ─────────────────────────────────────────────
  function currentTheme() {
    return document.documentElement.getAttribute('data-theme') || 'light';
  }
  function setTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    try { localStorage.setItem(STORAGE_KEY, theme); } catch (_) {}
    document.querySelectorAll('.ofs-theme-toggle').forEach(updateToggleVisual);
  }
  function toggleTheme() {
    setTheme(currentTheme() === 'dark' ? 'light' : 'dark');
  }
  window.OffshoreTheme = {
    get: currentTheme,
    set: setTheme,
    toggle: toggleTheme,
  };

  // React to system preference changes ONLY when user hasn't explicitly set one.
  if (window.matchMedia) {
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', e => {
      let stored;
      try { stored = localStorage.getItem(STORAGE_KEY); } catch (_) {}
      if (stored !== 'light' && stored !== 'dark') {
        document.documentElement.setAttribute('data-theme', e.matches ? 'dark' : 'light');
        document.querySelectorAll('.ofs-theme-toggle').forEach(updateToggleVisual);
      }
    });
  }

  // ── 4. Toggle button ──────────────────────────────────────────────
  const SUN_SVG = '<svg viewBox="0 0 16 16" fill="none" aria-hidden="true"><circle cx="8" cy="8" r="3" stroke="currentColor" stroke-width="1.4"/><path d="M8 1v2M8 13v2M1 8h2M13 8h2M3 3l1.4 1.4M11.6 11.6L13 13M3 13l1.4-1.4M11.6 4.4L13 3" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/></svg>';
  const MOON_SVG = '<svg viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M13 9.5A6 6 0 016.5 3a5 5 0 005 8.5A6 6 0 0113 9.5z" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round"/></svg>';

  function updateToggleVisual(btn) {
    const isDark = currentTheme() === 'dark';
    btn.innerHTML = (isDark ? SUN_SVG : MOON_SVG) + `<span class="label">${isDark ? 'Light' : 'Dark'}</span>`;
    btn.setAttribute('aria-label', isDark ? 'Switch to light mode' : 'Switch to dark mode');
    btn.setAttribute('title', isDark ? 'Switch to light mode' : 'Switch to dark mode');
  }

  function makeToggle() {
    const btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'ofs-theme-toggle';
    btn.addEventListener('click', toggleTheme);
    updateToggleVisual(btn);
    return btn;
  }

  // Inject into the first matched container; falls back to a fixed
  // floating button if no nav is found. Override by setting the
  // [data-theme-toggle-target] attribute on the desired container.
  function injectToggleButton() {
    if (document.querySelector('.ofs-theme-toggle')) return;

    const explicit = document.querySelector('[data-theme-toggle-target]');
    if (explicit) {
      explicit.appendChild(makeToggle());
      return;
    }

    const adminNav  = document.querySelector('.admin-nav');
    const navPill   = document.querySelector('.nav-pill');
    const navInner  = document.querySelector('.nav-inner');
    const navLinks  = document.querySelector('.nav-links');

    if (adminNav) {
      adminNav.appendChild(makeToggle());
      return;
    }
    if (navPill) {
      const btn = makeToggle();
      btn.style.marginLeft = '4px';
      navPill.appendChild(btn);
      return;
    }
    if (navInner) {
      navInner.appendChild(makeToggle());
      return;
    }
    if (navLinks) {
      navLinks.appendChild(makeToggle());
      return;
    }

    // No nav found — fall back to fixed floating button
    const btn = makeToggle();
    btn.style.cssText =
      'position:fixed;top:18px;right:18px;z-index:80;' +
      'background:var(--paper,#FAF7E8);box-shadow:0 1px 8px rgba(0,0,0,0.08);';
    document.body.appendChild(btn);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', injectToggleButton);
  } else {
    injectToggleButton();
  }
})();
