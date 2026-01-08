🎄 New Year Countdown (Streamlit)

A responsive Streamlit countdown dashboard that shows exactly how much time is left until New Year (January 1) — with RU / EN language switch, Day / Night theme, falling snow, festive images, and a glowing Surprise button that plays a random holiday sound and launches lightweight confetti.

🌐 Live demo:
https://new-year-countdown.streamlit.app/

🚀 Features

⏳ Live countdown: days + hours + minutes + seconds

🌍 Language toggle: RU / EN

🇷🇺 Correct Russian pluralization
(день / дня / дней, час / часа / часов, etc.)

🌗 Day / Night mode

📱 Fully responsive UI (desktop & mobile)

🎄 Festive assets (Santa + ornaments)

❄️ Falling snow effect

🎁 Surprise button:

plays a random sound from assets/*.mp3

launches lightweight JS confetti (stable, no layout jumps)

glowing continuously

🧱 Project Structure
New-Year-Countdown/
│
├── app.py
├── requirements.txt
├── assets/
│   ├── santa_presents_3.png
│   ├── christmas_ornament_1.png
│   └── *.mp3
└── README.md

⚠️ Important (Streamlit Cloud)

⚠️ Streamlit Cloud runs on Linux — paths are case-sensitive.

Use exactly:

assets/


❌ ASSETS/
❌ Assets/

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

4️⃣ Run the app
streamlit run app.py

🧠 How It Works

The application calculates the time difference between:

the current local time (datetime.now())

the upcoming New Year (January 1, 00:00:00)

Then it renders:

🎅 Left image (Santa)

⏳ Center countdown (title, days, hours, minutes, seconds)

🎄 Right image (Christmas ornaments)

🎁 Surprise button (random sound + confetti)

☁️ Deployment (Streamlit Community Cloud)

Push the project to GitHub

Open: https://streamlit.io/cloud

Click New app

Select:

repository

branch

Main file path: app.py

Click Deploy ✅

Streamlit Cloud will automatically redeploy the app on every git push.

📦 Requirements

Create requirements.txt in the project root:

streamlit>=1.30


All other used modules (datetime, random, pathlib) are part of Python’s standard library.

🛠 Tech Stack

Python

Streamlit

JavaScript / CSS injection for:

glowing button

confetti overlay

Python standard library:

datetime

random

pathlib

🧩 Troubleshooting
Images or sounds not loading on Streamlit Cloud

Ensure assets/ folder is committed and pushed:

git add assets
git commit -m "Add assets"
git push


Check file names exactly (Linux is case-sensitive):

assets/santa_presents_3.png ✅
assets/Santa_Presents_3.png ❌

No audio plays

Ensure at least one .mp3 exists in assets/

Browser autoplay policies may block sound until user interaction
→ click the Surprise button again if needed

Confetti not visible

Confetti is rendered via a lightweight JS overlay

If you edited HTML/CSS, ensure the JS injection block is still present
