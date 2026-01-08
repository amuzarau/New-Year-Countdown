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
- 🎁 **Surprise** button:
  - plays a random `assets/*.mp3`
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

⚠️ Streamlit Cloud runs on Linux: paths are case-sensitive.
Use assets/ exactly (not ASSETS/).

⚙️ How to Run Locally
1️⃣ Clone repository
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>

2️⃣ Create virtual environment
python -m venv .venv
source .venv/bin/activate   # Linux / macOS
.venv\Scripts\Activate.ps1  # Windows PowerShell

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run Streamlit app
streamlit run app.py

📊 App Logic Flow (Mermaid)
flowchart TD
    A[App start] --> B[UI controls<br/>RU/EN + Day/Night]
    B --> C[Compute time to Jan 1]
    C --> D[Render layout<br/>Images + Countdown]
    D --> E{Surprise clicked?}
    E -- No --> D
    E -- Yes --> F[Pick random MP3 from assets/]
    F --> G[Play audio]
    G --> H[Show confetti overlay]
    H --> D

☁️ Deployment (Streamlit Community Cloud)

Push the project to GitHub

Go to https://streamlit.io/cloud

Click New app

Select repository + branch

Set Main file path: app.py

Deploy ✅
Streamlit Cloud auto-redeploys on every push.

📦 Requirements

requirements.txt

streamlit>=1.30

🛠 Tech Stack

Python

Streamlit

Lightweight JS/CSS injection (confetti + glow)

Standard library: datetime, random, pathlib
