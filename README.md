# 🎄 New Year Countdown (Streamlit)

A responsive **Streamlit countdown dashboard** that shows exactly how much time is left until **New Year (Jan 1)** — with **RU/EN** language switch, **Day/Night** theme, falling snow, festive images, and a glowing **Surprise** button that plays a random holiday sound and launches lightweight confetti.

**Live demo:** https://new-year-countdown.streamlit.app/

---

## 🚀 Features

- ⏳ Live countdown: **days + hours + minutes + seconds**
- 🌍 Language toggle: **RU / EN**
- 🇷🇺 Correct Russian pluralization (день/дня/дней, час/часа/часов, …)
- 🌗 **Day / Night** mode
- 📱 Fully responsive UI (desktop + mobile)
- 🎄 Festive assets (Santa + ornaments)
- ❄️ Falling snow effect
- 🎁 **Surprise** button:
  - plays a random sound from `assets/*.mp3`
  - launches lightweight confetti (stable, no layout jumps)

---

## 🧱 Project Structure

```text
New-Year-Countdown/
│
├── app.py
├── requirements.txt
├── assets/
│   ├── santa_presents_3.png
│   ├── christmas_ornament_1.png
│   └── *.mp3
└── README.md
