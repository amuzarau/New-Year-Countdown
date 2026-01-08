🎄 New Year Countdown (Streamlit)
A responsive Streamlit web app that counts down the time left until New Year.
Supports RU/EN language toggle, Day/Night theme, falling snow, festive images, and a glowing Surprise button that plays a random sound and launches lightweight confetti.

Live demo: https://new-year-countdown.streamlit.app/

✨ Features
Countdown to New Year (days + hours + minutes + seconds)

RU / EN language switch

Correct Russian plural forms (день/дня/дней, час/часа/часов, …)

Day / Night mode

Responsive layout for desktop & mobile

Festive UI assets (Santa + ornaments)

Surprise button:

plays a random audio file from assets/*.mp3

triggers lightweight confetti (stable, no layout jumps)

🧠 How it works
mermaid
flowchart TD
    A[App start] --> B[Read UI settings<br/>Language + Theme]
    B --> C[Compute delta to Jan 1<br/>days/hours/minutes/seconds]
    C --> D[Render UI<br/>Images + Countdown + Surprise button]
    D --> E{Click Surprise?}
    E -- No --> D
    E -- Yes --> F[Pick random sound from assets/*.mp3]
    F --> G[Play audio via st.audio]
    G --> H[Render confetti overlay (JS/CSS)]
    H --> D
📁 Project structure
Код
Happy-New-Year-Countdown/
├── app.py
├── requirements.txt
└── assets/
    ├── santa_presents_3.png
    ├── christmas_ornament_1.png
    └── *.mp3
⚠️ Streamlit Community Cloud runs on Linux, so paths are case‑sensitive.
Use assets/ exactly (not ASSETS/).

🚀 Run locally
1) Create and activate a virtual environment (recommended)
Windows (PowerShell)

bash
python -m venv .venv
.venv\Scripts\Activate.ps1
macOS / Linux

bash
python -m venv .venv
source .venv/bin/activate
2) Install dependencies
bash
pip install -r requirements.txt
3) Run the app
bash
streamlit run app.py
☁️ Deploy to Streamlit Community Cloud
Push the project to GitHub

Open Streamlit Cloud → New app

Select your repository and branch

Set Main file path to app.py

Click Deploy

⚙️ Requirements
requirements.txt:

Код
streamlit>=1.30
🛠 Tech stack
Python

Streamlit

Lightweight JS/CSS injection (confetti + button glow)

Standard library: datetime, random, pathlib
