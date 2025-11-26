import click
import os
from email.mime.text import MIMEText
from dotenv import load_dotenv
from getpass import getpass
from .mail import *

ENV_FILE = os.path.join(os.path.expanduser("~"), ".buxcli.env")


def load_env():
    if not os.path.exists(ENV_FILE):
        return None, None

    load_dotenv(ENV_FILE)
    return os.getenv("MAIL_ID"), os.getenv("EMAIL_API_KEY")
def setup_env():
    """Run email setup ONLY if env file does NOT exist."""
    if not os.path.exists(ENV_FILE):
        click.echo(click.style("🔧 First-time setup: Configure your email notifications.", fg="yellow", bold=True))

        while True:
            mail_id = input("Enter your Gmail address: ").strip()
            password = getpass("Enter your App Password (input hidden): ").strip()

            # 🔥 Verify ONLY in first-time setup
            if verify_email_credentials(mail_id, password):
                with open(ENV_FILE, "w") as f:
                    f.write(f"MAIL_ID={mail_id}\n")
                    f.write(f"EMAIL_API_KEY={password}\n")
                click.echo(click.style("✅ Credentials saved and verified!\n", fg="green", bold=True))
                return True
            else:
                click.echo(click.style("❌ Invalid credentials.", fg="red"))
                retry = input("Try again? (y/n): ").strip().lower()
                if retry == "n":
                    return False
    else:
        # 🔥 Do NOT verify again
        return True
