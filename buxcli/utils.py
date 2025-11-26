import click
import os
from email.mime.text import MIMEText
from dotenv import load_dotenv
from getpass import getpass
from .mail import *

ENV_FILE = os.path.join(os.path.expanduser("~"), ".buxcli.env")


def load_env():
    """Load email credentials from the environment file."""
    if not os.path.exists(ENV_FILE):
        setup_env()
    else:
        load_dotenv(ENV_FILE)
        return os.getenv("MAIL_ID"), os.getenv("EMAIL_API_KEY")


def setup_env():
    """Prompt for email credentials only if not already saved or invalid."""
    if not os.path.exists(ENV_FILE):
        click.echo(click.style("🔧 First-time setup: Configure your email notifications.", fg="yellow", bold=True))
        while True:
            mail_id = input("Enter your Gmail address: ").strip()
            password = getpass("Enter your App Password (input hidden): ").strip()

            if verify_email_credentials(mail_id, password):
                with open(ENV_FILE, "w") as f:
                    f.write(f"MAIL_ID={mail_id}\n")
                    f.write(f"EMAIL_API_KEY={password}\n")
                click.echo(click.style("✅ Credentials saved and verified!\n", fg="green", bold=True))
                return True  # ✅ verified
            else:
                click.echo(click.style("❌ Invalid credentials or failed to send test email.", fg="red", bold=True))
                click.echo(click.style("📺 Reference this video for Gmail App Password setup:", fg="yellow"))
                click.echo(click.style("🔗 https://youtu.be/lSURGX0JHbA?si=MOlQzCP2kGam1g-e\n", fg="cyan"))
                
                retry = input("Try again? (y/n): ").strip().lower()
                if retry == "n":
                    click.echo(click.style("❌ Setup aborted. Command execution cancelled.\n", fg="red", bold=True))
                    return False  # ❌ failed setup
                else:
                    setup_env()
    else:
        # Credentials exist, verify them once
        mail_id, password = load_env()
        if not verify_email_credentials(mail_id, password):
            click.echo(click.style("⚠️ Saved credentials are invalid. Please reconfigure.\n", fg="red", bold=True))
            os.remove(ENV_FILE)
            return setup_env()  # retry setup
        return True
