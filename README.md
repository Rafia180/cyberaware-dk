# CyberAware DK

**A Social Engineering Awareness Website for International Students in Denmark**

CyberAware DK is a small educational website. It helps international students in Denmark recognise common scams (such as fake MitID messages, fake landlords and fake job offers) and tells them what to do if something has already gone wrong.

It was built as a BSc Computer Science final year project.

> **Important:** every example message on this website is **invented for learning**. None of them is a real message. The website does **not** check or analyse real messages, and it never asks for any personal information.

---

## Contents

1. [What is on the website](#1-what-is-on-the-website)
2. [What you need before you start](#2-what-you-need-before-you-start)
3. [Get the project files](#3-get-the-project-files)
4. [Run the website with Docker (recommended)](#4-run-the-website-with-docker-recommended)
5. [Run the website without Docker](#5-run-the-website-without-docker)
6. [How the project is organised](#6-how-the-project-is-organised)
7. [How to change the content](#7-how-to-change-the-content)
8. [Common problems and how to fix them](#8-common-problems-and-how-to-fix-them)
9. [Tools used](#9-tools-used)
10. [About this project](#10-about-this-project)

---

## 1. What is on the website

The website has **nine pages**:

| Page | What it shows |
|---|---|
| **Home** | Who the site is for, and three steps that work for every scam: **Stop, Check, Ask** |
| **Learn** | Five main kinds of scam, plus eight simple rules to remember |
| **5 topic pages** | For each kind of scam: what it is, invented examples, warning signs, what to do, what not to do, who can help, and official sources |
| **Get Help** | Seven steps to follow if you think you have been scammed, and the official Danish organisations to contact |
| **About** | What the project is for and what it does not do |

The five scam topics are:

1. Fake messages, calls and impersonation
2. Danish services and identity (MitID, CPR, SKAT, SIRI, Digital Post, police)
3. Money, banking and online buying
4. Housing and job scams
5. Relationship and trust scams

---

## 2. What you need before you start

You only need **one** of these two options.

**Option A: Docker (easiest, recommended)**
- Download and install [Docker Desktop](https://www.docker.com/products/docker-desktop/). Keep the default options.
- On Windows, the installer may ask you to turn on **WSL 2** (a small Linux system Docker needs). Accept, and restart your computer if it asks.
- Open Docker Desktop once and accept the terms. You can skip signing in.
- You do **not** need to install Python.

**Option B: Python**
- [Python](https://www.python.org/downloads/) 3.12 or newer.
- On Windows, tick **Add Python to PATH** on the first screen of the installer.
- Use this if you cannot install Docker.

You also need an internet connection the first time, so the packages can be downloaded.

> **What is Docker?** Docker packs the website together with everything it needs (Python and the packages) into one box called a **container**. Because everything is inside the box, the website runs the same way on every computer, and you do not have to install anything else.

---

## 3. Get the project files

**Easiest way (no tools needed):**

1. On this GitHub page, click the green **Code** button.
2. Click **Download ZIP**.
3. Unzip (extract) the folder somewhere easy to find, for example your Desktop. On Windows: right-click the ZIP file and choose **Extract All**.

> The unzipped folder is called **`cyberaware-dk-main`** (GitHub adds `-main` to the name). Windows sometimes puts a second folder with the same name inside it. The right folder is the one that contains `Dockerfile` and `requirements.txt`. Use that folder in all the steps below.

**If you use Git:**

```bash
git clone https://github.com/YOUR-USERNAME/cyberaware-dk.git
cd cyberaware-dk
```

---

## 4. Run the website with Docker (recommended)

### Step 1: Open Docker Desktop
Start Docker Desktop and wait until it says **Engine running** (bottom left of the window). Keep it open the whole time. Docker commands do not work while it is closed.

### Step 2: Open a terminal in the project folder
Choose **one** of these ways:

- **Windows:** open the project folder in File Explorer, click the address bar at the top, type `powershell` and press Enter.
- **Mac:** right-click the folder and choose **New Terminal at Folder**.
- **Any computer:** open a terminal and move into the folder with `cd`, for example:
  - Windows: `cd C:\Users\YourName\Desktop\cyberaware-dk-main`
  - Mac: `cd ~/Desktop/cyberaware-dk-main`
  - If you used `git clone`, the folder is called `cyberaware-dk` instead.

To check you are in the right place, type `dir` (Windows) or `ls` (Mac). You should see `Dockerfile` in the list.

### Step 3: Build the website
Type this and press Enter (do not forget the full stop at the end):

```bash
docker build -t cyberaware-dk .
```

What this means:
- `-t cyberaware-dk` gives the image the name `cyberaware-dk`.
- `.` means "use the `Dockerfile` in this folder".

Docker follows the instructions in the `Dockerfile` and makes an **image**: a ready-to-run copy of the website. The first time it downloads Python, so it can take a few minutes. The build is finished when the terminal is ready for typing again and shows no red `ERROR` lines.

### Step 4: Start the website

```bash
docker run -p 8000:8000 --name cyberaware cyberaware-dk
```

What this means:
- `-p 8000:8000` connects port 8000 on your computer to port 8000 inside the container, so your browser can reach the website.
- `--name cyberaware` gives the running container a simple name.
- `cyberaware-dk` is the image you built in Step 3.

When you see `Uvicorn running on http://0.0.0.0:8000`, the website is running. **Leave this terminal window open.** Closing it stops the website.

> **Prefer clicking?** After Step 3, open Docker Desktop, go to **Images**, and press ▶ (Run) next to `cyberaware-dk`. Open **Optional settings**, type `cyberaware` as the container name and `8000` as the **Host port**, then click **Run**. Do not skip the host port, or your browser cannot reach the website.

### Step 5: Open the website
Open your web browser and go to:

**http://localhost:8000**

> Do **not** type `0.0.0.0:8000` into your browser. That address only works inside the container.

### Stop and start again

| I want to... | Do this |
|---|---|
| Stop the website | Press `Ctrl + C` in the terminal |
| Start it again later | `docker start -a cyberaware` (or press ▶ next to `cyberaware` in Docker Desktop) |
| Remove it completely | `docker rm -f cyberaware` |

> **Do not run Step 4 a second time** to start the website again. The container already exists, so Docker will show a "name already in use" error. Use `docker start -a cyberaware` instead.

> **Changed a file?** The container keeps the old version. Run these three commands from the project folder:
>
> ```bash
> docker build -t cyberaware-dk .
> docker rm -f cyberaware
> docker run -p 8000:8000 --name cyberaware cyberaware-dk
> ```

---

## 5. Run the website without Docker

Use this if you cannot use Docker. Type each command below in a terminal and press Enter after each one.

**Step 0: Go into the project folder**

Every command below must run from inside the project folder. Open a terminal and move into it with `cd` (short for "change directory"):

```bash
cd cyberaware-dk
```

This works if the terminal is already in the folder that *contains* `cyberaware-dk` (for example, straight after `git clone`). If not, give the full path instead. If you downloaded the ZIP, the folder is called `cyberaware-dk-main`, for example:

- Windows: `cd C:\Users\YourName\Desktop\cyberaware-dk-main`
- Mac: `cd ~/Desktop/cyberaware-dk-main`

To check you are in the right place, type `dir` (Windows) or `ls` (Mac). You should see `requirements.txt` and the `app` folder in the list.

**Step 1: Create a virtual environment** (a private space for this project's packages):

```bash
python -m venv venv
```

On a Mac, type `python3` instead of `python` if `python` is not found.

This creates a folder called `venv`. You only need to do this step once.

**Step 2: Turn it on:**

- Windows: `venv\Scripts\activate`
- Mac or Linux: `source venv/bin/activate`

You will see `(venv)` at the start of the line. You need to turn it on **every time** you open a new terminal.

> **Windows error "running scripts is disabled on this system"?** Run this once, then try Step 2 again:
> `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` (type `Y` if it asks to confirm).

**Step 3: Install the packages the website needs:**

```bash
pip install -r requirements.txt
```

**Step 4: Start the website:**

```bash
uvicorn app.main:app --reload
```

When you see `Uvicorn running on http://127.0.0.1:8000`, the website is running. Leave this terminal open.

**Step 5:** open **http://127.0.0.1:8000** in your browser.

`--reload` means the website updates by itself when you save a change. Press `Ctrl + C` to stop it.

**Next time**, you only need Step 0, Step 2 and Step 4.

> Do not run the Docker version and this version at the same time. Both use port 8000.

---

## 6. How the project is organised

```
cyberaware-dk/
├── app/
│   ├── __init__.py        Tells Python this folder is a package (empty file)
│   ├── main.py            The server: decides which page to show for each web address
│   └── content.py         ALL the words on the website: topics, rules, steps, contacts
├── templates/             The HTML layout of each page
│   ├── base.html          The shared frame: header, menu and footer on every page
│   ├── index.html         Home page
│   ├── learn.html         Learn page
│   ├── topic_detail.html  One layout used by all five topic pages
│   ├── get_help.html      Get Help page
│   └── about.html         About page
├── static/
│   ├── css/style.css      The design: colours, spacing, layout for phone and computer
│   └── js/main.js         The "Menu" button on phones (the only JavaScript)
├── Dockerfile             Instructions Docker follows to build the website's container
├── .dockerignore          Files Docker should not copy into the container
├── .gitignore             Files Git should not upload to GitHub (such as venv)
├── requirements.txt       The Python packages the website needs, with exact versions
└── README.md              This file
```

**How a page is made, in four steps:**

1. You visit an address, for example `/learn`.
2. `main.py` finds the matching function.
3. That function takes the content from `content.py` and puts it into a template from `templates/`.
4. The finished page is sent to your browser, which uses `style.css` to make it look right.

There is **no database**. The website only shows fixed content, and nothing is saved, so all the content lives in one Python file.

---

## 7. How to change the content

All text is in **`app/content.py`**. You do not need to touch the HTML to change words.

- **Change a warning sign or a tip:** find the topic in `TOPICS` and edit the line inside the quotation marks.
- **Change a phone number or contact:** edit `HELP_CHANNELS`.
- **Change the Get Help steps:** edit `EMERGENCY_STEPS`.
- **Change the eight rules:** edit `CORE_RULES`.

Then, to see the change:

- **Without Docker:** save the file. With `--reload` the website restarts by itself. Refresh the browser.
- **With Docker:** rebuild and restart the container (see **Changed a file?** in section 4).

> Keep the quotation marks `" "` and commas `,` exactly as they are. A missing comma is the most common reason the website stops starting.

---

## 8. Common problems and how to fix them

| What you see | What it means | How to fix it |
|---|---|---|
| `error during connect` or `cannot connect to the Docker daemon` | Docker Desktop is not open | Open Docker Desktop and wait for **Engine running** |
| `failed to read dockerfile` | You are in the wrong folder | Open the terminal in the folder that contains `Dockerfile` |
| `port is already allocated` | Something else is already using port 8000 | Stop the other program, or use `-p 8080:8000` and open `http://localhost:8080` |
| `container name "/cyberaware" is already in use` | The container already exists | Use `docker start -a cyberaware`, or remove it with `docker rm -f cyberaware` |
| `ERR_ADDRESS_INVALID` in the browser | You typed `0.0.0.0:8000` | Use `http://localhost:8000` |
| The page loads but your change is not there | The old version is still running | Rebuild (Docker) or restart (Python), then press `Ctrl + F5` in the browser |
| `'python' is not recognized` | Python is not installed, or not on your PATH | Reinstall Python and tick **Add Python to PATH** |
| `'uvicorn' is not recognized` or `No module named fastapi` | The virtual environment is not turned on, or the packages are not installed | Turn it on (section 5, Step 2) and run `pip install -r requirements.txt` |
| `running scripts is disabled on this system` | Windows blocks the activate script | Run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`, then try again |
| `Could not open requirements file` | You are in the wrong folder | `cd` into the folder that contains `requirements.txt` |
| Virtualization or WSL error when Docker Desktop starts | Windows is missing a feature Docker needs | Run `wsl --update` in PowerShell, restart, and check that virtualization is turned on in your computer's BIOS settings |

---

## 9. Tools used

| Tool | What it does in this project |
|---|---|
| **Python** | The programming language |
| **FastAPI** | Turns Python functions into web pages |
| **Uvicorn** | The web server that runs FastAPI |
| **Jinja2** | Fills the HTML templates with the content |
| **HTML and CSS** | The structure and design of the pages |
| **JavaScript** | Only the phone menu button |
| **Docker** | Packs everything into a container that runs the same everywhere |

**Safety choices in the code:**
- The container runs as a normal user, not as the all-powerful "root" user.
- Package versions are fixed in `requirements.txt`, so the website behaves the same on every computer.
- External links open safely in a new tab (`rel="noopener"`).
- The website has no logins, no forms and no database, so there is nothing for it to store or leak.

---

## 10. About this project

- **Type:** BSc Computer Science final year project
- **Audience:** international students in Denmark
- **Language:** English only
- **Content:** based on official Danish guidance (borger.dk, sikkerdigital.dk, MitID, the Danish Police, SIRI and others). Each topic page links to its sources.
- **Contact details checked:** October 2026. Phone numbers and opening hours can change, so always check the official website.

This website is **not** connected to MitID, SKAT, SIRI, the police or any bank. All example messages are fictional.

**Author:** Rafia Tasnim