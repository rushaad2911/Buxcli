import click
import subprocess
from email.mime.text import MIMEText
from .utils import *
from .intro import *
from .mail import *





def run_command(command_list):
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
        for line in process.stdout:
            click.echo(line, nl=False)
            if any(keyword in line.lower() for keyword in keywords) and not server_started:
                server_started = True
                send_email(mail_id, password, "🚀 Server Started", f"{command} started successfully!")

        process.wait()

        if process.returncode == 0 and not server_started:
            send_email(mail_id, password, "✅ Success", f"Command succeeded: {command}")
        elif process.returncode != 0:
            send_email(mail_id, password, "❌ Failure", f"Command failed: {command}")

    except KeyboardInterrupt:
        click.echo(click.style("\n🛑 Command interrupted by user.", fg="red", bold=True))
        process.terminate()
        send_email(mail_id, password, "🛑 Interrupted", f"Command interrupted: {command}")



@click.group(cls=BuxCLI, invoke_without_command=True)
@click.argument("cmd", nargs=-1)
@click.pass_context
def cli(ctx, cmd):
    """buxcli - Run commands with automatic email notifications"""
    setup_env()
    if ctx.invoked_subcommand is None and not cmd:
        # Only intro
        return
    elif cmd:
        run_command(cmd)

@cli.command()
@click.argument("cmd", nargs=-1)
def run(cmd):
    """Run any shell command with email notifications"""
    run_command(cmd)

if __name__ == "__main__":
    cli()
