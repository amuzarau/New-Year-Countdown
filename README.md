# 🎄 New Year Countdown (Streamlit)

A responsive Streamlit web app that counts down the time left until New Year, supports **RU/EN** language toggle, **Day/Night** theme, falling snow, a glowing **Surprise** button with random holiday sounds, and lightweight confetti effects.

**Live demo:** https://new-year-countdown.streamlit.app/

---

## ✨ Features

- ✅ Countdown to New Year (days + hours + minutes + seconds)
- ✅ **RU / EN** language switch
- ✅ Correct Russian plural forms (день/дня/дней, час/часа/часов, …)
- ✅ **Day / Night** mode
- ✅ Responsive layout for desktop & mobile
- ✅ Festive visuals (Santa + ornaments)
- ✅ **Surprise** button:
  - plays a random sound (`assets/*.mp3`)
  - triggers lightweight confetti animation (no layout jumps)

---

## 🧠 How it works (Mermaid)

```mermaid
flowchart TD
    A[User opens app] --> B[Load UI settings<br/>Language + Theme]
    B --> C[Compute time to Jan 1 (New Year)]
    C --> D[Render layout<br/>Images + Countdown + Button]
    D --> E{User clicks "Surprise"?}
    E -- No --> D
    E -- Yes --> F[Pick random MP3 from assets/]
    F --> G[Play audio in Streamlit]
    G --> H[Inject lightweight confetti overlay (JS/CSS)]
    H --> D

🗂 Project structure
Happy-New-Year-Countdown/
├── app.py
├── requirements.txt
└── assets/
    ├── santa_presents_3.png
    ├── christmas_ornament_1.png
    └── *.mp3


⚠️ Streamlit Cloud runs on Linux, so paths are case-sensitive.
Use assets/ exactly (not ASSETS/).

🚀 Run locally
Create & activate venv (recommended)

Windows (PowerShell)

python -m venv .venv
.venv\Scripts\Activate.ps1


macOS / Linux

python -m venv .venv
source .venv/bin/activate

Install dependencies
pip install -r requirements.txt

Run the app
streamlit run app.py

☁️ Deploy to Streamlit Community Cloud

Push the project to GitHub

Go to Streamlit Cloud → New app

Select your repository + branch

Set Main file path: app.py

Deploy ✅

⚙️ Requirements

requirements.txt

streamlit>=1.30

🧰 Tech stack

Python

Streamlit

Lightweight JS/CSS injection for confetti/glow behavior

Standard library: datetime, random, pathlib
