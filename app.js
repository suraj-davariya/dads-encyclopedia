// ============================================================
// FIRST-TIME DAD'S PREGNANCY ENCYCLOPEDIA — app.js
// Milestone 1: Core interactions
// ============================================================

document.addEventListener('DOMContentLoaded', () => {
  initThemeToggle();
  initChecklist();
  initExpandables();
  initTabPanels();
  initProgressBar();
  initNavHighlight();
});

// ─── 1. THEME TOGGLE ────────────────────────────────────────
function initThemeToggle() {
  const btn = document.getElementById('theme-toggle');
  if (!btn) return;

  const saved = localStorage.getItem('theme') || 'light';
  document.documentElement.setAttribute('data-theme', saved);
  btn.setAttribute('aria-label', saved === 'dark' ? 'Switch to light mode' : 'Switch to dark mode');

  btn.addEventListener('click', () => {
    const current = document.documentElement.getAttribute('data-theme');
    const next = current === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', next);
    localStorage.setItem('theme', next);
    btn.setAttribute('aria-label', next === 'dark' ? 'Switch to light mode' : 'Switch to dark mode');
    btn.querySelector('.theme-icon').textContent = next === 'dark' ? '☀️' : '🌙';
  });

  // Set initial icon
  const icon = btn.querySelector('.theme-icon');
  if (icon) icon.textContent = saved === 'dark' ? '☀️' : '🌙';
}

// ─── 2. CHECKLIST TRACKER ───────────────────────────────────
function initChecklist() {
  const checklists = document.querySelectorAll('.checklist');
  checklists.forEach(list => {
    const key = 'checklist-' + (list.dataset.id || list.closest('[id]')?.id || 'default');
    const saved = JSON.parse(localStorage.getItem(key) || '{}');

    const items = list.querySelectorAll('.checklist-item input[type="checkbox"]');
    items.forEach((cb, i) => {
      if (saved[i]) cb.checked = true;
      cb.addEventListener('change', () => {
        saved[i] = cb.checked;
        localStorage.setItem(key, JSON.stringify(saved));
        updateChecklistProgress(list);
        if (cb.checked) celebrateCheck(cb);
      });
    });
    updateChecklistProgress(list);
  });
}

function updateChecklistProgress(list) {
  const items = list.querySelectorAll('input[type="checkbox"]');
  const done = list.querySelectorAll('input[type="checkbox"]:checked').length;
  const total = items.length;
  const bar = list.querySelector('.checklist-progress-fill');
  const label = list.querySelector('.checklist-progress-label');
  if (bar) bar.style.width = total ? ((done / total) * 100) + '%' : '0%';
  if (label) label.textContent = `${done} / ${total} complete`;
}

function celebrateCheck(el) {
  const span = document.createElement('span');
  span.className = 'check-celebrate';
  span.textContent = '✅';
  el.parentElement.appendChild(span);
  setTimeout(() => span.remove(), 800);
}

// ─── 3. EXPANDABLE SECTIONS ─────────────────────────────────
function initExpandables() {
  document.querySelectorAll('.expandable-toggle').forEach(btn => {
    const target = document.getElementById(btn.getAttribute('aria-controls'));
    if (!target) return;

    const isOpen = btn.getAttribute('aria-expanded') === 'true';
    target.hidden = !isOpen;

    btn.addEventListener('click', () => {
      const open = btn.getAttribute('aria-expanded') === 'true';
      btn.setAttribute('aria-expanded', String(!open));
      target.hidden = open;
      const icon = btn.querySelector('.expand-icon');
      if (icon) icon.textContent = open ? '▶' : '▼';
    });
  });
}

// ─── 4. TAB PANELS ──────────────────────────────────────────
function initTabPanels() {
  document.querySelectorAll('.tabs').forEach(tabGroup => {
    const tabs = tabGroup.querySelectorAll('[role="tab"]');
    const panels = tabGroup.querySelectorAll('[role="tabpanel"]');

    tabs.forEach((tab, i) => {
      tab.addEventListener('click', () => {
        tabs.forEach(t => { t.setAttribute('aria-selected', 'false'); t.classList.remove('active'); });
        panels.forEach(p => { p.hidden = true; });
        tab.setAttribute('aria-selected', 'true');
        tab.classList.add('active');
        const target = document.getElementById(tab.getAttribute('aria-controls'));
        if (target) target.hidden = false;
      });
    });

    // Keyboard nav
    tabGroup.addEventListener('keydown', e => {
      const active = tabGroup.querySelector('[role="tab"][aria-selected="true"]');
      const idx = [...tabs].indexOf(active);
      if (e.key === 'ArrowRight') tabs[(idx + 1) % tabs.length]?.click();
      if (e.key === 'ArrowLeft') tabs[(idx - 1 + tabs.length) % tabs.length]?.click();
    });
  });
}

// ─── 5. SCROLL PROGRESS BAR ─────────────────────────────────
function initProgressBar() {
  const bar = document.getElementById('scroll-progress');
  if (!bar) return;
  window.addEventListener('scroll', () => {
    const total = document.body.scrollHeight - window.innerHeight;
    bar.style.width = total > 0 ? (window.scrollY / total * 100) + '%' : '0%';
  }, { passive: true });
}

// ─── 6. ACTIVE NAV HIGHLIGHT ────────────────────────────────
function initNavHighlight() {
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.week-nav a[href^="#"]');
  if (!sections.length || !navLinks.length) return;

  const obs = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        navLinks.forEach(a => a.classList.remove('active'));
        const link = document.querySelector(`.week-nav a[href="#${entry.target.id}"]`);
        if (link) link.classList.add('active');
      }
    });
  }, { rootMargin: '-20% 0px -60% 0px' });

  sections.forEach(s => obs.observe(s));
}

// ─── UTILITIES ───────────────────────────────────────────────
function smoothScroll(targetId) {
  const el = document.getElementById(targetId);
  if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
}
