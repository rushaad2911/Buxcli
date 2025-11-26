# Buxcli 🚀

BuxCLI is a lightweight command-line utility that runs any shell command and instantly sends email notifications on:

### 1) ✅ Success
### 2) ❌ Failure
### 3) 🚀 Server started (auto-detects “server ready” messages)

Perfect for developers and DevOps engineers who want real-time alerts without monitoring their terminal.

---

## ✨ Features

🔔 Email Alerts for success, failure, or server startup

🔐 Secure Gmail App Password Setup

💬 Test Email during first-time configuration

🔄 Auto Retry if email credentials are incorrect

🎨 Beautiful CLI Output with colors + ASCII banner

🧪 Works with all commands (e.g., Python, Django, Docker, Node, Bash)  

---

## 💻 Installation

Install via pip:

```bash
pip install buxcli
```

Check Installation:

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

