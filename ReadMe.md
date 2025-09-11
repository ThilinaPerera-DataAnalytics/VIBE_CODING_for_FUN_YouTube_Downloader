# 🎥 Project: YouTube Downloader

A Python-based tool to **download YouTube videos or audio**.
Originally developed as a *“vibe coding”* experiment, this project demonstrates **modular design**, **workflow automation**, and **practical use of third-party libraries** — all skills directly applicable to data science and software development.



## 📂 Project Structure

```
Project_YouTube_Downloader_Vibe_Coding/
├── .gitignore
├── README.md
├── requirements.txt
├── youtdwn.ipynb        # Jupyter Notebook interface
└── src/
    ├── __init__.py
    └── downloader.py    # Core download logic (modular, reusable)
```

## ⚙️ Setup & Installation

Clone the repository:

```bash
git clone https://github.com/ThilinaPerera-DataAnalytics/Vide_Coding_for_fun_YouTube_Downloader.git
cd Project_YouTube_Downloader_Vibe_Coding
```

Create and activate a virtual environment:

```bash
python -m venv venv
# macOS / Linux
source venv/bin/activate
# Windows
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

1. Open `youtdwn.ipynb` in Jupyter (VS Code, Jupyter Notebook, or JupyterLab).
2. Run the notebook step by step.
3. Input a YouTube URL → select **Video** or **Audio** → file downloads automatically.

---

## 🚀 Features

* Built with **Python + yt-dlp** for flexible, reliable downloads.
* **Notebook interface** for interactive exploration.
* **Modular codebase** (`downloader.py`) → functions can be reused in larger automation projects.
* Easily extendable: add new features (batch downloads, playlists, file format conversions).

---

## 📝 Notes

* Uses [`yt-dlp`](https://github.com/yt-dlp/yt-dlp), a modern fork of `youtube-dl`.
* Designed for experimentation, but follows **clean coding practices**: modular structure, virtual environment setup, and dependency management.

---

💡 **Recruiter Takeaway**: While simple in function, this project shows ability to:

* Structure Python projects with **reusable modules**.
* Work with **external APIs & libraries**.
* Document and package code for **team use or scaling up**.
* Use **Jupyter Notebooks** as a workflow/prototyping tool.