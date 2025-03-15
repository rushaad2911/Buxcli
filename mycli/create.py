import os
import subprocess
import platform
from rich.console import Console
from .check import *
console = Console()


class CreateProject:
    
    def __init__(self, project_name):
        self.project_name = project_name
        self.project_path = os.path.join(os.getcwd(),self.project_name)
        self.venv_name = os.path.join(self.project_path, "vir")  # Virtual environment folder name

    def run_command(self, command, cwd=None):
        """Runs a shell command and prints output."""
        process = subprocess.run(command, shell=True, text=True, cwd=cwd)
        if process.returncode != 0:
            console.print(f"[red]❌ Error executing: {command}[/red]")
            exit(1)

    def create_django_project(self):
        """Creates a Django project inside a virtual environment."""
        console.print(f"📦 Setting up your  Django project: [bold cyan]{self.project_name}[/bold cyan] in [yellow]{self.project_path}[/yellow]")

        # Ensure the directory exists
        os.makedirs(self.project_path, exist_ok=True)

        # Change to the selected directory
        # setting project path
        project_path = os.path.join(self.project_path,self.project_name)

        os.chdir(self.project_path)

        # Create virtual environment
        console.print("📦 Creating virtual environment...")
        self.run_command(f"python -m venv {self.venv_name}")

        # Determine OS and set paths correctly
        if platform.system() == "Windows":
            pip_path = os.path.join(self.venv_name, "Scripts", "pip")
            django_admin_path = os.path.join(self.venv_name, "Scripts", "django-admin")
        else:
            pip_path = os.path.join(self.venv_name, "bin", "pip")
            django_admin_path = os.path.join(self.venv_name, "bin", "django-admin")

        # Install Django
        console.print("📦 Installing Django...")
        self.run_command(f"{pip_path} install django")

        # Create Django project
        console.print(f"🦾 Creating Django project: [bold cyan]{self.project_name}[/bold cyan] in [yellow]{self.project_path}[/yellow]...")
        
        self.run_command(f"{django_admin_path} startproject {self.project_name} .", cwd=self.project_path)

        console.print("\n✅ [bold green]Django project setup complete![/bold green]")

    def create_flutter_project(self):
        result = is_flutter_installed()
        if result:
            console.print("Creating flutter app")
            self.run_command(f"flutter create {self.project_name}")
            console.print("Done creating Flutter Project")
    def create_reactnative_project(self):
        pass
    
    def create_react_project(self):
        pass 
    
    def create_flask_project(self):
        pass 
    
    def create_express_project(self):
        pass 
    
    def create_node_project(self):
        pass