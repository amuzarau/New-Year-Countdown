import streamlit as st
from datetime import datetime
import random
from pathlib import Path
import streamlit.components.v1 as components

st.set_page_config(page_title="🎄 New Year Countdown", layout="wide")


def plural_ru(n: int, one: str, two: str, five: str) -> str:
    if 11 <= n % 100 <= 14:
        return five
    if n % 10 == 1:
        return one
    if 2 <= n % 10 <= 4:
        return two
    return five


if "confetti_nonce" not in st.session_state:
    st.session_state.confetti_nonce = 0


def find_hero_image() -> Path | None:
    candidates = [
        Path("assets/christmas-tree-presents.png"),
        Path("assets/christmas-tree-presents.webp"),
        Path("assets/christmas-tree-presents.jpg"),
        Path("/mnt/data/christmas-tree-presents.png"),
        Path("/mnt/data/christmas-tree-presents.webp"),
        Path("/mnt/data/christmas-tree-presents.jpg"),
    ]
    for p in candidates:
        if p.exists():
            return p
    return None


# =========================================================
# 1) HERO IMAGE — TOP OF APP
# =========================================================
hero_path = find_hero_image()

top_l, top_c, top_r = st.columns([1, 6, 1])
with top_c:
    if hero_path:
        st.image(str(hero_path), width="stretch")
    else:
        st.warning("Hero image not found. Put it in assets/ as christmas-tree-presents.png")
        st.markdown("<div style='text-align:center;font-size:48px;'>🎄🎁</div>", unsafe_allow_html=True)

st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)

# =========================================================
# 2) CONTROLS
# =========================================================
c1, c2, c3 = st.columns([2, 3, 2])
with c2:
    lang = st.radio("Language", ["RU", "EN"], horizontal=True, label_visibility="collapsed")
with c3:
    night = st.toggle("🌙 Day / Night", value=False)

bg = "#0b1220" if night else "#ffffff"
text = "#e8eefc" if night else "#111111"
sub = "#b7c4e6" if night else "#444444"

btn_text = "🎁 Сюрприз" if lang == "RU" else "🎁 Surprise"

# =========================================================
# CSS
# =========================================================
st.markdown(
    f"""
    <style>
      .stApp {{
        background: {bg};
        color: {text};
      }}

      /* Controls text dark */
      div[data-testid="stRadio"] * {{ color: #111 !important; }}
      div[data-testid="stToggle"] * {{ color: #111 !important; }}

      /* Light chip behind controls */
      div[data-testid="stRadio"] > div {{
        background: rgba(255,255,255,0.92);
        padding: 8px 12px;
        border-radius: 14px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.08);
      }}
      div[data-testid="stToggle"] {{
        background: rgba(255,255,255,0.92);
        padding: 8px 12px;
        border-radius: 14px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.08);
      }}

      .ny-center {{
        text-align: center;
        margin-top: 14px;
      }}

      .ny-title {{ font-size: 34px; color: {sub}; }}
      .ny-days  {{ font-size: 112px; font-weight: 800; line-height: 1; margin-top: 6px; }}

      /* ✅ keep bottom margin at 0 so button can be glued */
      .ny-time {{
        font-size: 34px;
        margin-top: 10px;
        margin-bottom: 0 !important;
        padding-bottom: 0 !important;
        color: {sub};
      }}

      @media (max-width: 768px) {{
        .ny-title {{ font-size: 24px; }}
        .ny-days  {{ font-size: 68px; }}
        .ny-time  {{ font-size: 24px; }}
      }}

      /* ✅ Ultra-tight button block: remove ALL vertical spacing */
      div[data-testid="stButton"],
      div[data-testid="stButton"] > div,
      .stButton,
      .stButton > div,
      div.stButton {{
        width: 100% !important;
        display: flex !important;
        justify-content: center !important;

        margin-top: 0 !important;
        margin-bottom: 0 !important;
        padding-top: 0 !important;
        padding-bottom: 0 !important;
        gap: 0 !important;
      }}

      /* Some Streamlit versions add extra margin on markdown wrappers */
      .element-container {{
        margin-top: 0 !important;
        margin-bottom: 0 !important;
      }}

      /* Glow button */
      .ny-surprise-btn {{
        font-size: 1.45rem !important;
        padding: 14px 48px !important;
        border-radius: 18px !important;
        background: #ffffff !important;
        color: #333 !important;
        border: 2px solid rgba(255, 235, 59, 0.9) !important;

        width: 360px !important;
        max-width: 92vw !important;

        display: inline-flex !important;
        justify-content: center !important;

        box-shadow:
          0 0 18px rgba(255, 235, 59, 1),
          0 0 38px rgba(255, 193, 7, 0.95),
          0 0 72px rgba(255, 152, 0, 0.9);

        animation: glow 1.4s infinite alternate;
      }}

      @media (max-width: 600px) {{
        .ny-surprise-btn {{
          font-size: 1.18rem !important;
          padding: 12px 18px !important;
          width: min(340px, 92vw) !important;
        }}
      }}

      @keyframes glow {{
        from {{
          box-shadow:
            0 0 14px rgba(255, 235, 59, 0.85),
            0 0 30px rgba(255, 193, 7, 0.75),
            0 0 56px rgba(255, 152, 0, 0.7);
        }}
        to {{
          box-shadow:
            0 0 28px rgba(255, 235, 59, 1),
            0 0 64px rgba(255, 193, 7, 0.98),
            0 0 110px rgba(255, 152, 0, 0.95);
        }}
      }}

      /* Confetti overlay */
      .ny-confetti-layer {{
        position: fixed;
        inset: 0;
        pointer-events: none;
        z-index: 999999;
      }}
      .ny-confetti-piece {{
        position: fixed;
        width: 8px;
        height: 6px;
        border-radius: 2px;
        opacity: 1;
        will-change: transform, opacity;
        animation: nyConfetti var(--dur) ease-out forwards;
      }}
      @keyframes nyConfetti {{
        from {{ transform: translate(0px, 0px) rotate(0deg); opacity: 1; }}
        to   {{ transform: translate(var(--dx), var(--dy)) rotate(var(--rot)); opacity: 0; }}
      }}
    </style>
    """,
    unsafe_allow_html=True,
)

st.snow()

# =========================================================
# 3) COUNTDOWN
# =========================================================
now = datetime.now()
new_year = datetime(now.year + 1, 1, 1, 0, 0, 0)
delta = new_year - now

days = delta.days
seconds = delta.seconds
hours = seconds // 3600
minutes = (seconds % 3600) // 60
secs = seconds % 60

if lang == "RU":
    title = "До Нового года осталось"
    days_line = f"{days} {plural_ru(days, 'день', 'дня', 'дней')}"
    time_line = (
        f"{hours} {plural_ru(hours, 'час', 'часа', 'часов')} "
        f"{minutes} {plural_ru(minutes, 'минута', 'минуты', 'минут')} "
        f"{secs} {plural_ru(secs, 'секунда', 'секунды', 'секунд')}"
    )
else:
    title = "Time left until New Year"
    days_line = f"{days} day{'s' if days != 1 else ''}"
    time_line = (
        f"{hours} hour{'s' if hours != 1 else ''} "
        f"{minutes} minute{'s' if minutes != 1 else ''} "
        f"{secs} second{'s' if secs != 1 else ''}"
    )

mid_l, mid_c, mid_r = st.columns([1, 6, 1])
with mid_c:
    st.markdown(
        f"""
        <div class="ny-center">
          <div class="ny-title">{title}</div>
          <div class="ny-days">{days_line}</div>
          <div class="ny-time">{time_line}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ✅ ZERO GAP (closer than 2px)
st.markdown("<div style='height:0px;'></div>", unsafe_allow_html=True)

# marker for confetti origin
st.markdown("<div id='surprise-marker'></div>", unsafe_allow_html=True)

# =========================================================
# 4) BUTTON
# =========================================================
b1, b2, b3 = st.columns([1, 2, 1])
with b2:
    clicked = st.button(btn_text, key="surprise_button")

# Add glow class for RU/EN
components.html(
    """
    <script>
    (function() {
      let doc = document;
      try { if (window.parent && window.parent.document) doc = window.parent.document; } catch(e) {}

      const start = Date.now();
      const maxMs = 2500;

      const timer = setInterval(() => {
        if (Date.now() - start > maxMs) { clearInterval(timer); return; }

        const texts = ["Surprise", "Сюрприз"];
        const btn = Array.from(doc.querySelectorAll("button"))
          .find(b => texts.some(t => ((b.innerText || "").trim()).includes(t)));
        if (!btn) return;

        btn.classList.add("ny-surprise-btn");
        clearInterval(timer);
      }, 60);
    })();
    </script>
    """,
    height=1,
)

# =========================================================
# 5) CLICK: AUDIO + CONFETTI
# =========================================================
if clicked:
    sounds = list(Path("assets").glob("*.mp3"))
    if sounds:
        st.audio(str(random.choice(sounds)), autoplay=True)

    components.html(
        """
        <script>
        (function() {
          let doc = document;
          let win = window;
          try {
            if (window.parent && window.parent.document) {
              doc = window.parent.document;
              win = window.parent;
            }
          } catch(e) {}

          const old = doc.getElementById("ny-confetti-layer");
          if (old) old.remove();

          let x = win.innerWidth * 0.5;
          let y = win.innerHeight * 0.55;
          const marker = doc.getElementById("surprise-marker");
          if (marker) {
            const r = marker.getBoundingClientRect();
            x = r.left + r.width / 2;
            y = Math.max(20, r.top + 10);
          }

          const layer = doc.createElement("div");
          layer.id = "ny-confetti-layer";
          layer.className = "ny-confetti-layer";
          doc.body.appendChild(layer);

          const colors = ["#ff1744","#ffea00","#00e676","#2979ff","#ff9100","#e040fb"];
          const N = 90;

          for (let i = 0; i < N; i++) {
            const p = doc.createElement("div");
            p.className = "ny-confetti-piece";
            p.style.left = x + "px";
            p.style.top  = y + "px";
            p.style.background = colors[(Math.random() * colors.length) | 0];

            const dx = (Math.random() - 0.5) * 420;
            const dy = -(180 + Math.random() * 320);
            const rot = (Math.random() * 720 - 360) + "deg";
            const dur = (900 + Math.random() * 800) + "ms";

            p.style.setProperty("--dx", dx + "px");
            p.style.setProperty("--dy", dy + "px");
            p.style.setProperty("--rot", rot);
            p.style.setProperty("--dur", dur);

            layer.appendChild(p);
          }

          setTimeout(() => {
            const lay = doc.getElementById("ny-confetti-layer");
            if (lay) lay.remove();
          }, 1900);
        })();
        </script>
        """,
        height=1,
    )
