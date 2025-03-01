import os
import sys
import argparse
import subprocess
import platform
import inquirer
from mycli.create import CreateProject
from rich.console import Console




def main():
    parser = argparse.ArgumentParser(
        description="A simple CLI tool for project setup automation made to make me look cool."
    )

    parser.add_argument(
        "-c", "--create",
        action="store_true",
        help="Select a project to build."
    )

    # Check if any argument is provided
    if len(sys.argv) == 1:
        parser.print_help()
        exit()

    args = parser.parse_args()

    if args.create:
        # Define the project options
        project_choices = [
            "Django project",
        ]

        # Use inquirer to prompt the user for a selection
        questions = [
            inquirer.List(
                "project",
                message="⚒️  Select which project to create",
                choices=project_choices,
                carousel=True,
            ),
            inquirer.Text(
                "project_name",
                message="Enter Project name",
            ),
            inquirer.Text(
                "project_path",
                message="📂 Enter the directory where you want to create the project",
                default=os.getcwd()
            ),
            inquirer.Confirm(
                "confirm_path",
                message="Are you sure you want to create the project here?",
                default=True,
            ),
        ]

        answers = inquirer.prompt(questions)

        if not answers["confirm_path"]:
            console.print("[red]❌ Project creation canceled.[/red]")
            exit(0)

        if answers['project'] == 'Django project':
            CreateProject(
                project_name=answers['project_name'],
                project_path=answers['project_path']
            ).create_django_project()


if __name__ == "__main__":
    main()
