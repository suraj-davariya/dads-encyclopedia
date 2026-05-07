import json
import os
import glob

with open("index.html.backup", "r") as f:
    lines = f.readlines()

# Extract parts
header_html = "".join(lines[:702])

# Dynamic container
dynamic_container = """
<div id="week-display-container"></div>
"""

footer_html = "".join(lines[3962:])

# Read all batches and combine
all_weeks_data = {}
for file in sorted(glob.glob("data/batch_*.json")):
    with open(file, "r") as f:
        batch_data = json.load(f)
        all_weeks_data.update(batch_data)

# Convert combined dict back to a JSON string for JS
js_weeks_data = "const WEEKS_DATA = " + json.dumps(all_weeks_data, indent=2) + ";"

js_render_function = """
function renderWeek(key) {
  const data = WEEKS_DATA[key];
  if(!data) return;
  
  const container = document.getElementById('week-display-container');
  
  // Create symptom table rows safely
  const symptomRows = data.symptomTable && data.symptomTable.length > 0 
    ? data.symptomTable.map(s => `<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:var(--space-2);padding:var(--space-2) 0;border-bottom:1px solid var(--color-border);font-size:var(--text-sm)"><div><strong>${s.name}</strong></div><div>${s.why}</div><div>${s.help}</div></div>`).join('')
    : '<div style="font-size:var(--text-sm);color:var(--color-text-muted)">No major symptoms this week.</div>';

  // We recreate the layout structure with all data
  const html = `
<article id="week-${data.id}">
  <div class="week-header">
    <div class="container">
      <div class="week-eyebrow">
        <span class="week-badge">Week ${data.id === 'prep' || data.id === 'birth' ? '' : data.id + ' · '}${data.trimesterLabel}</span>
      </div>
      <h2 class="week-title">${data.emoji} ${data.title}</h2>
      <p class="week-subtitle">${data.subtitle}</p>
    </div>
  </div>

  <section class="section" style="padding-top:var(--space-8)">
    <div class="container">
      <div class="overview-grid fade-in">
        <div class="overview-card">
          <div class="ov-icon">🌱</div>
          <div class="ov-label">Baby Size</div>
          <div class="ov-value">${data.size}</div>
          <div class="ov-sub">${data.sizeDesc}</div>
        </div>
        <div class="overview-card">
          <div class="ov-icon">🫀</div>
          <div class="ov-label">Key Development</div>
          <div class="ov-value">${data.keyDev}</div>
          <div class="ov-sub">${data.keyDevDesc}</div>
        </div>
        <div class="overview-card">
          <div class="ov-icon">🦸‍♂️</div>
          <div class="ov-label">Dad's Priority</div>
          <div class="ov-value">${data.dadPriority}</div>
          <div class="ov-sub">${data.dadPriorityDesc}</div>
        </div>
        <div class="overview-card">
          <div class="ov-icon">🤰</div>
          <div class="ov-label">Partner's Symptoms</div>
          <div class="ov-value">${data.partnerSymptoms}</div>
          <div class="ov-sub">${data.partnerSymptomsDesc}</div>
        </div>
      </div>

      <div class="content-layout" style="margin-top:var(--space-10)">
        <div class="main-content">
          
          <div class="info-card fade-in">
            <div class="info-card-header">
              <div class="info-card-icon icon-baby">👶</div>
              <div>
                <div class="info-card-title">Baby's Development</div>
              </div>
            </div>
            <div class="list-items">
              ${data.babyDevBullets.map(b => `<div class="list-item"><span class="list-bullet"></span><span>${b}</span></div>`).join('')}
            </div>
          </div>
          
          <div class="info-card fade-in" style="margin-top:var(--space-6)">
            <div class="info-card-header">
              <div class="info-card-icon icon-partner">❤️</div>
              <div>
                <div class="info-card-title">Partner's Journey</div>
                <div class="info-card-desc">Symptom decoder and how to help</div>
              </div>
            </div>
            <div style="margin-top:var(--space-4)">
              <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:var(--space-2);padding-bottom:var(--space-2);border-bottom:2px solid var(--color-border);font-weight:700;font-size:var(--text-xs);text-transform:uppercase;letter-spacing:0.05em;color:var(--color-text-muted)">
                <div>Symptom</div><div>Why it's happening</div><div>How you can help</div>
              </div>
              ${symptomRows}
            </div>
          </div>

          <div class="info-card fade-in" style="margin-top:var(--space-6)">
            <div class="info-card-header">
              <div class="info-card-icon icon-mission">🚀</div>
              <div>
                <div class="info-card-title">Mission Control</div>
                <div class="info-card-desc">Your dad duties for this week</div>
              </div>
            </div>
            <div class="mission-tabs">
              <button class="mission-tab active" onclick="switchTab(this, 'tab-emotional')" aria-selected="true">Emotional</button>
              <button class="mission-tab" onclick="switchTab(this, 'tab-practical')" aria-selected="false">Practical</button>
              <button class="mission-tab" onclick="switchTab(this, 'tab-relationship')" aria-selected="false">Relationship</button>
            </div>
            <div class="mission-content">
              <div id="tab-emotional" class="mission-panel active">
                <ul style="padding-left:var(--space-4);margin:0;font-size:var(--text-sm)">
                  ${data.emotionalScripts.map(s => `<li style="margin-bottom:var(--space-2)">"${s}"</li>`).join('')}
                </ul>
              </div>
              <div id="tab-practical" class="mission-panel">
                <div class="checklist">
                  ${data.practicalTasks.map(t => `
                  <div class="check-item" onclick="toggleCheck(this)">
                    <div class="ci-box"></div>
                    <div class="ci-text">${t}</div>
                  </div>`).join('')}
                </div>
              </div>
              <div id="tab-relationship" class="mission-panel">
                <ul style="padding-left:var(--space-4);margin:0;font-size:var(--text-sm)">
                  ${data.relationshipIdeas.map(r => `<li style="margin-bottom:var(--space-2)">${r}</li>`).join('')}
                </ul>
              </div>
            </div>
          </div>

          <div class="info-card fade-in" style="margin-top:var(--space-6); background:var(--color-surface-2)">
            <div class="info-card-header">
              <div class="info-card-icon">🧠</div>
              <div>
                <div class="info-card-title">Takeaways</div>
              </div>
            </div>
            <div class="list-items" style="margin-top:var(--space-4)">
              ${data.takeaways.map(t => `<div class="list-item"><span class="list-bullet"></span><span style="font-weight:500">${t}</span></div>`).join('')}
            </div>
          </div>

        </div>
        
        <aside class="sidebar">
            <div class="sidebar-card">
                <div class="sidebar-title">
                  Progress Tracker
                </div>
                <p style="font-size:var(--text-sm);margin-bottom:var(--space-4)">Select a week below:</p>
                <div class="progress-weeks" style="gap: 5px;">
                  ${Object.keys(WEEKS_DATA).map(k => `
                    <div class="week-dot ${k===key ? 'current' : 'completed'}" 
                         onclick="renderWeek('${k}')" 
                         style="cursor:pointer"
                         title="${WEEKS_DATA[k].title}">
                      ${k === 'prep' ? 'P' : (k === 'birth' ? 'B' : k)}
                    </div>
                  `).join('')}
                </div>
            </div>

            <div class="sidebar-card" style="margin-top:var(--space-6)">
              <div class="sidebar-title">🛒 Dad's Shopping List</div>
              <div class="checklist" style="margin-top:var(--space-4)">
                <div style="font-weight:700;font-size:var(--text-xs);text-transform:uppercase;margin-bottom:var(--space-2)">Must Buy</div>
                ${data.mustBuy && data.mustBuy.length > 0 ? data.mustBuy.map(b => `<div class="check-item" onclick="toggleCheck(this)"><div class="ci-box"></div><div class="ci-text">${b}</div></div>`).join('') : '<div style="font-size:var(--text-sm);color:var(--color-text-muted)">None this week</div>'}
                <div style="font-weight:700;font-size:var(--text-xs);text-transform:uppercase;margin:var(--space-4) 0 var(--space-2) 0">Optional</div>
                ${data.optionalBuy && data.optionalBuy.length > 0 ? data.optionalBuy.map(b => `<div class="check-item" onclick="toggleCheck(this)"><div class="ci-box"></div><div class="ci-text">${b}</div></div>`).join('') : '<div style="font-size:var(--text-sm);color:var(--color-text-muted)">None this week</div>'}
              </div>
            </div>

            <div class="sidebar-card" style="margin-top:var(--space-6)">
              <div class="sidebar-title">🩺 Medical Roadmap</div>
              <ul style="padding-left:var(--space-4);font-size:var(--text-sm);margin-top:var(--space-4)">
                ${data.medicalRoadmap.map(m => `<li style="margin-bottom:var(--space-2)">${m}</li>`).join('')}
              </ul>
              ${data.questions && data.questions.length > 0 ? `
              <div style="font-weight:700;font-size:var(--text-xs);text-transform:uppercase;margin:var(--space-4) 0 var(--space-2) 0">Questions to Ask</div>
              <ul style="padding-left:var(--space-4);font-size:var(--text-sm);color:var(--color-text-muted)">
                ${data.questions.map(q => `<li>${q}</li>`).join('')}
              </ul>` : ''}
            </div>

        </aside>
      </div>
    </div>
  </section>
</article>
  `;
  container.innerHTML = html;
  
  // Update URL hash without jumping
  history.pushState(null, null, '#week-' + data.id);
  
  // Highlight trimester band
  document.querySelectorAll('.trimester-btn').forEach(btn => btn.classList.remove('active'));
  const trimBtn = document.querySelector(`.trimester-btn.${data.trimester}`);
  if(trimBtn) trimBtn.classList.add('active');
  
  // Scroll to top of week display smoothly
  document.getElementById('week-display-container').scrollIntoView({behavior: 'smooth', block: 'start'});
}

document.addEventListener('DOMContentLoaded', () => {
    // Check hash for initial load
    let initialKey = '4';
    if(window.location.hash) {
        const hash = window.location.hash.replace('#week-', '').replace('#', '');
        if(WEEKS_DATA[hash]) {
            initialKey = hash;
        } else if (hash === 'pre-conception') initialKey = 'prep';
        else if (hash === 'second-trimester') initialKey = '14';
        else if (hash === 'third-trimester') initialKey = '28';
        else if (hash === 'birth') initialKey = 'birth';
    }
    renderWeek(initialKey);
    
    // Override trimester buttons to use JS render instead of hash links
    document.querySelectorAll('.trimester-btn').forEach(btn => {
        btn.removeAttribute('onclick');
        btn.addEventListener('click', (e) => {
            if(btn.classList.contains('prep')) renderWeek('prep');
            else if(btn.classList.contains('t1')) renderWeek('1');
            else if(btn.classList.contains('t2')) renderWeek('14');
            else if(btn.classList.contains('t3')) renderWeek('28');
            else if(btn.classList.contains('birth')) renderWeek('birth');
        });
    });
});
"""

# Insert the script right before the closing body tag inside footer_html
footer_html = footer_html.replace("</body>", f"<script>\n{js_weeks_data}\n{js_render_function}\n</script>\n</body>")

final_html = header_html + dynamic_container + footer_html

with open("index.html", "w") as f:
    f.write(final_html)

print("Generated full dynamic index.html with all JSON batches successfully.")
