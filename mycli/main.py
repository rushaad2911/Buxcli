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
        description="A simple CLI tool for project setup automation."
    )

    parser.add_argument(
        "-c", "--create",
        action="store_true",
        help="Select a project to build."
    )

    # Check if any argument is provided
    if len(sys.argv) == 1:
        args = parser.parse_args(['-c'])
    else:

        args = parser.parse_args()

    if args.create:
        # Define the project options
        project_choices = [
            "Django",
            "Flutter",
            "React Native"
            "React",
            "Flask",
            "Express.js",
            "Node.js",
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
                validate=lambda _, x: (bool(x.strip()) and x.strip() != "")
            ),
            inquirer.Text(
                "project_path",
                message="📂 Enter the directory where you want to create the project",
                default=os.getcwd()
            ),
            inquirer.Confirm(
                "confirm_path",
                message="Are you sure you want to create the project here? [default = Yes]",
                default=True,
            ),
        ]

        # getting question answers
        answers = inquirer.prompt(questions)
        
        
            
        if not answers["confirm_path"]:
            Console.print("[red]❌ Project creation canceled, path not found.[/red]")
            exit(0)

        # project name
        project = CreateProject(
                project_name=answers['project_name'],
            )
        
        # mapping project name with creation function
        create_project = {
            "Django":project.create_django_project,
            "Flutter":project.create_flutter_project,
            "React Native":None,
            "React":None,
            "Flask":None,
            "Express.js":None,
            "Node.js":None,
        }
        
        # creating project based on user input
        if answers['project'] == 'Django':
            project.create_django_project()
        elif answers['project']=='Flutter':
            project.create_flutter_project()
        
        

if __name__ == "__main__":
    main()
