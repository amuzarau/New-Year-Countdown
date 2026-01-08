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
⚠️ Streamlit Cloud runs on Linux: paths are case-sensitive.
Use assets/ exactly (not ASSETS/).

⚙️ How to Run Locally
1️⃣ Clone repository
bash
Копировать код
git clone https://github.com/amuzarau/new-year-countdown.git
cd new-year-countdown
2️⃣ Create virtual environment
bash
Копировать код
python -m venv .venv
source .venv/bin/activate   # Linux / macOS
.venv\Scripts\Activate.ps1  # Windows PowerShell
3️⃣ Install dependencies
bash
Копировать код
pip install -r requirements.txt
4️⃣ Run the app
bash
Копировать код
streamlit run app.py
🧠 How it works
The app calculates the time difference between the current local time (datetime.now()) and the upcoming New Year (Jan 1, 00:00:00). It then renders:

Left image (Santa)

Center countdown (title, days, time)

Right image (ornaments)

Surprise button (random sound + confetti)

📊 App Logic Flow (Mermaid)
mermaid
Копировать код
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
🎁 Surprise Button Logic (Sequence Diagram)
mermaid
Копировать код
sequenceDiagram
    participant User
    participant Streamlit
    participant Assets
    participant Browser

    User->>Streamlit: Click "Surprise"
    Streamlit->>Assets: Pick random *.mp3
    Streamlit->>Browser: Play audio (st.audio)
    Streamlit->>Browser: Inject confetti overlay (JS/CSS)
☁️ Deployment (Streamlit Community Cloud)
Push the project to GitHub

Go to https://streamlit.io/cloud

Click New app

Select repository + branch

Set Main file path: app.py

Click Deploy ✅

Streamlit Cloud will automatically redeploy the app on every git push.

📦 Requirements
Create requirements.txt in the repository root:

txt
Копировать код
streamlit>=1.30
Note: Everything else used in the project (datetime, random, pathlib) is part of Python’s standard library.

🛠 Tech Stack
Python

Streamlit

Lightweight JS/CSS injection for:

constant glowing button style

confetti overlay

Standard library: datetime, random, pathlib

🧩 Troubleshooting
Images or sounds not loading on Streamlit Cloud
Ensure assets/ folder exists in GitHub and is pushed:

bash
Копировать код
git add assets
git commit -m "Add assets"
git push
Check file names exactly (Linux is case-sensitive):

assets/santa_presents_3.png ✅

assets/Santa_Presents_3.png ❌

No audio plays
Confirm you have at least one .mp3 in assets/

Browser autoplay policies may block sound until user interaction — click the button again if needed

Confetti not visible
Confetti uses a lightweight overlay. If you changed HTML/CSS, ensure the JS injection block is still present.
