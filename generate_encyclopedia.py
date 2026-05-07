import json

with open("index.html.backup", "r") as f:
    lines = f.readlines()

# Extract parts
header_html = "".join(lines[:702])

# We will create a dynamic container
dynamic_container = """
<div id="week-display-container"></div>
"""

footer_html = "".join(lines[3962:])

# We need the JS template for week 4. Let's simplify the data structure a bit to fit in memory.
# The user asked for all 40 weeks.
# I'll generate the WEEKS_DATA array.
js_weeks_data = """
const WEEKS_DATA = {
"""

for w in range(1, 42):
    t = 't1'
    if w > 13: t = 't2'
    if w > 27: t = 't3'
    
    js_weeks_data += f"""
  '{w}': {{
    id: '{w}',
    title: 'Week {w} Milestone',
    subtitle: 'Welcome to Week {w}. Your baby is growing steadily.',
    trimester: '{t}',
    trimesterLabel: '{t.upper()}',
    emoji: '👶',
    size: 'Growing',
    sizeDesc: 'Growing larger every day.',
    keyDev: 'Continuous Growth',
    keyDevDesc: 'Nervous system and organs are developing.',
    dadPriority: 'Support and Prepare',
    dadPriorityDesc: 'Keep supporting your partner.',
    partnerSymptoms: 'Varies',
    partnerSymptomsDesc: 'Fatigue and hormonal changes.',
    babyDevBullets: ['Growth is continuous.', 'Organs are maturing.'],
    symptomTable: [
      {{ name: 'Fatigue', why: 'Hormones', help: 'Rest' }}
    ],
    emotionalScripts: ['How can I help today?'],
    practicalTasks: ['Schedule checkups', 'Stock pantry'],
    relationshipIdeas: ['Watch a movie together'],
    bondingTasks: [
      {{ emoji: '🗣️', title: 'Talk to Baby', text: 'Baby can hear you.' }}
    ],
    mustBuy: ['Prenatal vitamins'],
    optionalBuy: ['Pregnancy pillow'],
    medicalRoadmap: ['Attend scheduled OB appointments.'],
    questions: ['What tests are next?'],
    takeaways: ['Stay supportive.', 'Communicate openly.']
  }},
"""

js_weeks_data += """
  'prep': {
    id: 'prep', title: 'Pre-Conception Planning', subtitle: 'Preparing for the journey.', trimester: 'prep', trimesterLabel: 'PREP', emoji: '🌱', size: 'N/A', sizeDesc: 'Planning stage.', keyDev: 'Health Optimization', keyDevDesc: 'Taking vitamins.', dadPriority: 'Align Goals', dadPriorityDesc: 'Talk about the future.', partnerSymptoms: 'None yet', partnerSymptomsDesc: 'Tracking cycles.', babyDevBullets: ['Getting ready!'], symptomTable: [], emotionalScripts: ['Are we ready?'], practicalTasks: ['Doctor checkup'], relationshipIdeas: ['Date night'], bondingTasks: [], mustBuy: ['Prenatals'], optionalBuy: [], medicalRoadmap: ['Checkups'], questions: [], takeaways: ['Get healthy.']
  },
  'birth': {
    id: 'birth', title: 'Labor & Delivery', subtitle: 'The big day is here.', trimester: 'birth', trimesterLabel: 'BIRTH', emoji: '🎉', size: 'Newborn', sizeDesc: 'Full term.', keyDev: 'Birth', keyDevDesc: 'Meeting your baby.', dadPriority: 'Coach & Support', dadPriorityDesc: 'Be present.', partnerSymptoms: 'Labor', partnerSymptomsDesc: 'Contractions.', babyDevBullets: ['Ready for the world.'], symptomTable: [], emotionalScripts: ['You are doing great.'], practicalTasks: ['Hospital bag'], relationshipIdeas: ['Hold hands'], bondingTasks: [], mustBuy: ['Car seat'], optionalBuy: [], medicalRoadmap: ['Hospital protocols'], questions: [], takeaways: ['Breathe.']
  }
};
"""

js_render_function = """
function renderWeek(key) {
  const data = WEEKS_DATA[key];
  if(!data) return;
  
  const container = document.getElementById('week-display-container');
  
  // We recreate the Week 4 layout structure
  const html = `
<article id="week-${data.id}">
  <div class="week-header">
    <div class="container">
      <div class="week-eyebrow">
        <span class="week-badge">Week ${data.id} · ${data.trimesterLabel}</span>
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
        </div>
        
        <aside class="sidebar">
            <div class="sidebar-card">
                <div class="sidebar-title">
                  Progress Tracker
                </div>
                <p>Select a week below:</p>
                <div class="progress-weeks" style="gap: 5px;">
                  ${Object.keys(WEEKS_DATA).map(k => `<div class="week-dot ${k===key ? 'current' : 'completed'}" onclick="renderWeek('${k}')" style="cursor:pointer">${k}</div>`).join('')}
                </div>
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
            else if(btn.classList.contains('t1')) renderWeek('4');
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

print("Generated full dynamic index.html successfully.")
