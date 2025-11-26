import click
import subprocess
from email.mime.text import MIMEText
from .utils import *
from .intro import *
from .mail import *
import sys
import os
import logging
from .version import __version__

# --- Force Windows console to UTF-8 ---
if os.name == "nt":
    os.system("chcp 65001 > nul")

# --- Force stdout/stderr to UTF-8 ---
sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

# --- Force all logging StreamHandlers to use UTF-8 ---
logging.basicConfig(
    level=logging.INFO,
    handlers=[logging.StreamHandler(sys.stdout)],
    force=True
)

def run_command(command_list):
    try:
        # Change Windows terminal code page to UTF-8 (does nothing on Linux/macOS)
        if os.name == "nt":
            os.system("chcp 65001 > nul")

        # Reconfigure Python output streams to UTF-8
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

    mail_id, password = load_env()
    command = " ".join(command_list)
    click.echo(click.style(f"🚀 Running: {command}\n", fg="blue", bold=True))

    process = subprocess.Popen(
        command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True
    )

    server_started = False
    keywords = [
        "starting development server at",
        "running on http://",
        "listening on",
        "application started",
        "server started"
    ]

    try:
        for line in iter(process.stdout.readline, ""):
            click.echo(line, nl=False)

            if any(keyword in line.lower() for keyword in keywords) and not server_started:
                server_started = True
                send_email(mail_id, password, "🚀 Server Started",
                           f"{command} started successfully!")

        process.wait()

        if process.returncode == 0 and not server_started:
            send_email(mail_id, password, "✅ Success", f"Command succeeded: {command}")
        elif process.returncode != 0:
            send_email(mail_id, password, "❌ Failure", f"Command failed: {command}")

    except KeyboardInterrupt:
        click.echo(click.style("\n🛑 Keyboard interrupt received — stopping command...", fg="red", bold=True))

        try:
            process.terminate()   # Try graceful termination
            process.wait(timeout=3)
        except Exception:
            process.kill()        # Force kill if terminate doesn't work

        click.echo(click.style("✔ Command stopped.", fg="yellow"))
        return


@click.group(cls=BuxCLI, invoke_without_command=True)
@click.argument("cmd", nargs=-1)
@click.option("--version", is_flag=True, help="Show current BuxCLI version")
@click.option("--reconfig",is_flag=True, help="Reconfigure email Credentials")
@click.pass_context
def cli(ctx, cmd, reconfig,version):


    # Show version and exit
    if version:
        click.echo(click.style(f"BuxCLI Version: {__version__}", fg="green", bold=True))
        return


    # If user wants reconfig — delete file and setup again
    if reconfig:
        if os.path.exists(ENV_FILE):
            os.remove(ENV_FILE)
        setup_env()

    # First-time setup (only if env file missing)
    if not os.path.exists(ENV_FILE):
        ok = setup_env()
        if not ok:
            click.echo(click.style("❌ Email setup failed. Aborting command.\n", fg="red"))
            return

    if ctx.invoked_subcommand is None and not cmd:
        return

    if cmd:
        run_command(cmd)



@cli.command()
@click.argument("cmd", nargs=-1)
def run(cmd):
    """Run any shell command with email notifications"""
    run_command(cmd)

if __name__ == "__main__":
    cli()
