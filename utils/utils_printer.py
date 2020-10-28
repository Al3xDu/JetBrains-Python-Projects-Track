import os


def print_hi_to_this_project():
    project_name = os.getcwd()
    project_name = project_name.split("\\")
    print(f"Hello you are now inside: {project_name[len(project_name) - 1]}")
