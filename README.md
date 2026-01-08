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
.
├── app.py
├── requirements.txt
└── assets/
    ├── santa_presents_3.png
    ├── christmas_ornament_1.png
    └── *.mp3


⚠️ Important: Streamlit Cloud runs on Linux, so paths are case-sensitive.
Use assets/ exactly (not ASSETS/).

🚀 Run locally
1) Create and activate a virtual environment (recommended)

Windows (PowerShell)

python -m venv .venv
.venv\Scripts\Activate.ps1


macOS / Linux

python -m venv .venv
source .venv/bin/activate

2) Install dependencies
pip install -r requirements.txt

3) Start the app
streamlit run app.py

☁️ Deploy to Streamlit Community Cloud

Push the project to GitHub

Go to Streamlit Cloud → New app

Select your repository + branch

Set Main file path: app.py

Deploy ✅

⚙️ Configuration
Assets

Place your images and sounds in the assets/ folder:

Images used by the UI:

assets/santa_presents_3.png

assets/christmas_ornament_1.png

Sounds:

any *.mp3 file in assets/ will be used by the Surprise button

Customization ideas

Replace images in assets/ to rebrand the app

Add more sounds (assets/*.mp3) to expand the Surprise variety

Adjust spacing / font sizes in the embedded CSS for your design

🧰 Tech stack

Python

Streamlit

Lightweight JS/CSS injection for confetti/glow behavior

Standard library only: datetime, random, pathlib

📄 License

This project is released under the MIT License (you can add a LICENSE file if you want).

🙌 Credits

Built with Streamlit and festive assets/sounds provided by the project author.
