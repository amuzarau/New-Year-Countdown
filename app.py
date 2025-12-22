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


# nonce to re-run confetti script each click (no key=)
if "confetti_nonce" not in st.session_state:
    st.session_state.confetti_nonce = 0


# -----------------------------
# Controls
# -----------------------------
c1, c2, c3 = st.columns([2, 3, 2])
with c2:
    lang = st.radio(
        "Language", ["RU", "EN"], horizontal=True, label_visibility="collapsed"
    )
with c3:
    night = st.toggle("🌙 Night", value=False)

bg = "#0b1220" if night else "#ffffff"
text = "#e8eefc" if night else "#111111"
sub = "#b7c4e6" if night else "#444444"


# -----------------------------
# CSS (glow ONLY on .ny-surprise-btn)
# -----------------------------
st.markdown(
    f"""
    <style>
      .stApp {{
        background: {bg};
        color: {text};
      }}

      .ny-center {{
        text-align: center;
        margin-top: 18px;
      }}

      .ny-title {{
        font-size: 38px;
        color: {sub};
      }}

      .ny-days {{
        font-size: 120px;
        font-weight: 800;
        line-height: 1;
        margin-top: 6px;
      }}

      .ny-time {{
        font-size: 36px;
        margin-top: 10px;
        color: {sub};
      }}

      @media (max-width: 768px) {{
        .ny-title {{ font-size: 26px; }}
        .ny-days  {{ font-size: 72px; }}
        .ny-time  {{ font-size: 26px; }}
      }}

      /* ✅ Only Surprise button gets this class via JS */
      .ny-surprise-btn {{
        font-size: 1.7rem !important;
        padding: 16px 56px !important;
        border-radius: 18px !important;
        background: #ffffff !important;
        color: #333 !important;
        border: 2px solid rgba(255, 235, 59, 0.9) !important;

        /* adaptive width */
        width: min(420px, 92vw) !important;
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
          font-size: 1.25rem !important;
          padding: 12px 18px !important;
          width: min(360px, 92vw) !important;
        }}
      }}

      @media (max-width: 380px) {{
        .ny-surprise-btn {{
          font-size: 1.1rem !important;
          padding: 10px 14px !important;
          width: 92vw !important;
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

      /* Confetti pieces (lightweight, no canvas loop) */
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

# Snow
st.snow()

# -----------------------------
# Side images
# -----------------------------
left, center, right = st.columns([2.5, 5, 3])
with left:
    st.image("assets/santa_presents_3.png", width="stretch")
with right:
    st.image("assets/christmas_ornament_1.png", width="stretch")


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
    btn_text = "🎁 Сюрприз"
else:
    title = "Time left until New Year"
    days_line = f"{days} day{'s' if days != 1 else ''}"
    time_line = (
        f"{hours} hour{'s' if hours != 1 else ''} "
        f"{minutes} minute{'s' if minutes != 1 else ''} "
        f"{secs} second{'s' if secs != 1 else ''}"
    )
    btn_text = "🎁 Surprise"


# -----------------------------
# Center block + button
# -----------------------------
clicked = False
with center:
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

    # Marker above the button (confetti origin)
    st.markdown("<div id='surprise-marker'></div>", unsafe_allow_html=True)

    # ✅ 2x larger gap before button
    st.markdown("<div style='height:80px;'></div>", unsafe_allow_html=True)

    b1, b2, b3 = st.columns([1, 2, 1])
    with b2:
        clicked = st.button(btn_text, key="surprise_button")


# -----------------------------
# Add class to the Surprise button (stable, prevents affecting other buttons)
# Run every time (cheap)
# -----------------------------
components.html(
    """
    <script>
    (function() {
      let doc = document;
      try { if (window.parent && window.parent.document) doc = window.parent.document; } catch(e) {}

      const texts = ["Surprise", "Сюрприз"];
      const buttons = Array.from(doc.querySelectorAll("button"));

      for (const b of buttons) {
        const t = (b.innerText || "").trim();
        if (texts.some(x => t.includes(x))) {
          b.classList.add("ny-surprise-btn");
        }
      }
    })();
    </script>
    """,
    height=1,
)

# -----------------------------
# Click: audio + simple stable confetti overlay (no layout jump)
# -----------------------------
if clicked:
    sounds = list(Path("assets").glob("*.mp3"))
    if sounds:
        st.audio(str(random.choice(sounds)), autoplay=True)

    st.session_state.confetti_nonce += 1
    nonce = st.session_state.confetti_nonce

    components.html(
        f"""
        <script>
        (function() {{
          let doc = document;
          let win = window;
          try {{
            if (window.parent && window.parent.document) {{
              doc = window.parent.document;
              win = window.parent;
            }}
          }} catch(e) {{}}

          // Remove previous layer
          const old = doc.getElementById("ny-confetti-layer");
          if (old) old.remove();

          // Origin: marker above button (fallback center)
          let x = win.innerWidth * 0.5;
          let y = win.innerHeight * 0.60;
          const marker = doc.getElementById("surprise-marker");
          if (marker) {{
            const r = marker.getBoundingClientRect();
            x = r.left + r.width / 2;
            y = Math.max(20, r.top - 6);
          }}

          // Create overlay layer
          const layer = doc.createElement("div");
          layer.id = "ny-confetti-layer";
          layer.className = "ny-confetti-layer";
          doc.body.appendChild(layer);

          const colors = ["#ff1744","#ffea00","#00e676","#2979ff","#ff9100","#e040fb"];
          const N = 70; // light + stable

          for (let i = 0; i < N; i++) {{
            const p = doc.createElement("div");
            p.className = "ny-confetti-piece";
            p.style.left = x + "px";
            p.style.top  = y + "px";
            p.style.background = colors[(Math.random() * colors.length) | 0];

            const dx = (Math.random() - 0.5) * 360;        // sideways
            const dy = -(120 + Math.random() * 220);       // up
            const rot = (Math.random() * 720 - 360) + "deg";
            const dur = (900 + Math.random() * 700) + "ms";

            p.style.setProperty("--dx", dx + "px");
            p.style.setProperty("--dy", dy + "px");
            p.style.setProperty("--rot", rot);
            p.style.setProperty("--dur", dur);

            layer.appendChild(p);
          }}

          // cleanup
          setTimeout(() => {{
            const lay = doc.getElementById("ny-confetti-layer");
            if (lay) lay.remove();
          }}, 1700);
        }})();
        </script>
        """,
        height=1,
    )
