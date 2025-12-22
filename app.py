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


# -----------------------------
# TOP image slot
# -----------------------------
hero_slot = st.empty()

# -----------------------------
# Controls
# -----------------------------
c1, c2, c3 = st.columns([2, 3, 2])
with c2:
    lang = st.radio("Language", ["RU", "EN"], horizontal=True, label_visibility="collapsed")
with c3:
    night = st.toggle("🌙 Day / Night", value=False)

bg = "#0b1220" if night else "#ffffff"
text = "#e8eefc" if night else "#111111"
sub = "#b7c4e6" if night else "#444444"

# -----------------------------
# CSS
# -----------------------------
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
        margin-top: 16px;
      }}

      .ny-title {{ font-size: 34px; color: {sub}; }}
      .ny-days  {{ font-size: 112px; font-weight: 800; line-height: 1; margin-top: 6px; }}
      .ny-time  {{ font-size: 34px; margin-top: 10px; color: {sub}; }}

      @media (max-width: 768px) {{
        .ny-title {{ font-size: 24px; }}
        .ny-days  {{ font-size: 68px; }}
        .ny-time  {{ font-size: 24px; }}
      }}

      /* Button wrapper centering (covers different Streamlit DOMs) */
      div[data-testid="stButton"],
      div[data-testid="stButton"] > div,
      .stButton,
      .stButton > div,
      div.stButton {{
        width: 100% !important;
        display: flex !important;
        justify-content: center !important;
      }}

      /* Only Surprise button */
      .ny-surprise-btn {{
        font-size: 1.7rem !important;
        padding: 16px 56px !important;
        border-radius: 18px !important;
        background: #ffffff !important;
        color: #333 !important;
        border: 2px solid rgba(255, 235, 59, 0.9) !important;

        width: 380px !important;
        max-width: 92vw !important;

        display: block !important;
        margin-left: auto !important;
        margin-right: auto !important;

        box-shadow:
          0 0 18px rgba(255, 235, 59, 1),
          0 0 38px rgba(255, 193, 7, 0.95),
          0 0 72px rgba(255, 152, 0, 0.9);

        animation: glow 1.4s infinite alternate;
      }}

      @media (max-width: 600px) {{
        .ny-surprise-btn {{
          font-size: 1.25rem !important;
          padding: 12px 18px !important;
          width: min(360px, 92vw) !important;
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

      /* Confetti */
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
        transform: translate(0,0) rotate(0deg);
      }}

      @keyframes nyConfetti {{
        from {{
          transform: translate(0px, 0px) rotate(0deg);
          opacity: 1;
        }}
        to {{
          transform: translate(var(--dx), var(--dy)) rotate(var(--rot));
          opacity: 0;
        }}
      }}
    </style>
    """,
    unsafe_allow_html=True,
)

st.snow()

# -----------------------------
# HERO IMAGE (Cloud-safe)
# Only repo paths: assets/
# Never crash if missing
# -----------------------------
hero_candidates = [
    Path("assets/christmas-tree-presents.png"),
    Path("assets/christmas-tree-presents.webp"),
    Path("assets/christmas-tree-presents.jpg"),
]
hero_path = next((p for p in hero_candidates if p.exists()), None)

with hero_slot:
    if hero_path:
        try:
            st.image(str(hero_path), width="stretch")
        except Exception:
            st.warning("Hero image cannot be opened. Check that it exists in the repo under assets/ and is not corrupted.")
            st.markdown("<div class='ny-center' style='font-size:48px;'>🎄🎁</div>", unsafe_allow_html=True)
    else:
        st.warning("Hero image not found. Put it in assets/ as christmas-tree-presents.png (or .jpg/.webp).")
        st.markdown("<div class='ny-center' style='font-size:48px;'>🎄🎁</div>", unsafe_allow_html=True)

st.markdown("<div style='height:20px;'></div>", unsafe_allow_html=True)

# -----------------------------
# Countdown
# -----------------------------
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

btn_text = "🎁 Surprise"

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

# marker for confetti origin
st.markdown("<div id='surprise-marker'></div>", unsafe_allow_html=True)
st.markdown("<div style='height:70px;'></div>", unsafe_allow_html=True)

clicked = st.button(btn_text, key="surprise_button")

# Glow + centering enforcement (short polling helps Streamlit rerenders)
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

        const btn = Array.from(doc.querySelectorAll("button"))
          .find(b => ((b.innerText || "").trim()).includes("Surprise"));
        if (!btn) return;

        btn.classList.add("ny-surprise-btn");
        btn.style.display = "block";
        btn.style.marginLeft = "auto";
        btn.style.marginRight = "auto";

        const wrap =
          btn.closest('div[data-testid="stButton"]') ||
          btn.closest('.stButton') ||
          btn.closest('div.stButton');

        if (wrap) {
          wrap.style.width = "100%";
          wrap.style.display = "flex";
          wrap.style.justifyContent = "center";
        }

        clearInterval(timer);
      }, 60);
    })();
    </script>
    """,
    height=1,
)

# Click: audio + confetti upwards
if clicked:
    sounds = list(Path("assets").glob("*.mp3"))
    if sounds:
        st.audio(str(random.choice(sounds)), autoplay=True)

    st.session_state.confetti_nonce += 1

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
          let y = win.innerHeight * 0.65;
          const marker = doc.getElementById("surprise-marker");
          if (marker) {
            const r = marker.getBoundingClientRect();
            x = r.left + r.width / 2;
            y = Math.max(20, r.top - 6);
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
