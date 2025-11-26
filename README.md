# ⚡ BuxCLI 🚀  
Run any command + get instant email notifications

BuxCLI is a lightweight command-line tool that runs shell commands and sends instant **email alerts** when your command:

1️⃣ **Succeeds**  
2️⃣ **Fails**  
3️⃣ **Server starts** (auto-detects “server ready” messages)

Perfect for developers, sysadmins, and DevOps engineers who don’t want to stare at terminals.

---

# 📑 Table of Contents

- [Features](#-features)  
- [Installation](#-installation)  
- [Usage Examples](#-usage-examples)  
  - [Long Running Commands](#1-long-running-commands)  
  - [Server Startup Detection](#2-server-starting-commands)  
- [Contributing](#-contributing)  
- [Contact](#-contact)  
- [License](#-license)

---

## ✨ Features

- 🔔 Email alerts for **success**, **failure**, or **server startup**
- 🔐 Secure Gmail App Password setup
- 💬 Test email option during initial setup
- 🔄 Automatic retry if credentials are invalid
- 🎨 Colorful CLI output with ASCII banner
- 🧪 Works with all commands (Python, Django, Docker, Node, Bash, etc.)

---

## 💻 Installation

Install using pip:

```bash
pip install buxcli
```
Check Instalation
```bash
buxcli --help
```

Output:
```bash

██████  ██    ██ ██   ██  ██████ ██      ██ 
██   ██ ██    ██  ██ ██  ██      ██      ██ 
██████  ██    ██   ███   ██      ██      ██ 
██   ██ ██    ██  ██ ██  ██      ██      ██ 
██████   ██████  ██   ██  ██████ ███████ ██ 

Run commands with automatic email notifications when they succeed, fail, or a server starts.

Examples:
  buxcli run "python manage.py runserver"
  buxcli docker pull ollama
Usage: buxcli [OPTIONS] [CMD]... COMMAND [ARGS]...

  buxcli - Run commands with automatic email notifications

Options:
  --reconfig  Reconfigure email Credentials
  --help  Show this message and exit.

Commands example:
  buxcli docker pull nginx

```
---

## 🔗 Example
### 1) Long Running Commands

```bash
- buxcli docker pull nginx

- buxcli flutter build apk

# send mail on sucess or failure
```
### 2) Server Starting commands

```bash
- buxcli python manage.py runserver

# send mail on server starting
```
---

## 🤝 Contributing

```bash

# 1. Fork the repository

# 2. Create a feature branch
git checkout -b feature/my-feature

# 3. Commit your changes
git commit -m "Add new feature"

# 4. Push to GitHub
git push origin feature/my-feature

# 5. Open a Pull Request

```
---
## 📡 Contact 
```bash
Mohd. Rushaad Buxy
Email: m.rushaadq@gmail.com
GitHub: https://github.com/rushaad2911/Buxcli

buxcli – Never miss a command status again! 🚀
```
---
## 📝 License
```bash
This project is licensed under the MIT License. See the LICENSE file for details.
```

