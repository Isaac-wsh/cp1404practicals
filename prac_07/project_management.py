from project import Project
from datetime import datetime

filename = "projects.txt"

def main():
    """The main function to run the project management program."""
    projects = load_project(filename)
    # for project in projects:
    #     print(project)
    # save_projects("projects_saved.txt", projects)
    # display_projects(projects)
    print("Welcome to Pythonic Project Management")
    print(f"Loaded {len(projects)} projects from projects.txt")
    user_choice = ""
    while user_choice != "q":
        display_menu()
        user_choice = input(">>> ").strip().lower()
        if user_choice == "l":
            projects = load_project(filename)
            print(f"{len(projects)} projects loaded from projects.txt")
        elif user_choice == "s":
            save_projects(filename, projects)
            print(f"{len(projects)} projects saved to projects.txt")
        elif user_choice == "d":
            display_projects(projects)
        elif user_choice == "f":
            input_date = input("Show projects that start after date (dd/mm/yy): ")
            filter_by_date(projects, input_date)
        elif user_choice == "a":
            print("Let's add a new project")
            new_project = add_new_project()
            projects.append(new_project)
        elif user_choice == "u":
            update_project(projects)
        elif user_choice == "q":
            save_input = input("Would you like to save to projects.txt? ").strip().lower()
            if save_input in ["y", "yes"]:
                save_projects(filename, projects)
            else:
                print("no, I think not.")
            print("Thank you for using custom-built project management software.")

def display_menu():
    """Show menu to users"""
    print("- (L)oad projects")
    print("- (S)ave projects")
    print("- (D)isplay projects")
    print("- (F)ilter projects by date")
    print("- (A)dd new project")
    print("- (U)pdate project")
    print("- (Q)uit")

def load_project(filename):
    """Load project data from the file"""
    projects = []
    in_file = open(filename, "r")
    in_file.readline()
    for line in in_file:
        parts = line.strip().split("\t")
        name = parts[0]
        start_time = parts[1]
        priority = parts[2]
        estimate = parts[3]
        completion = parts[4]
        project = Project(name, start_time, priority, estimate, completion)
        projects.append(project)
    in_file.close()
    return projects

def save_projects(filename, projects):
    """Save a list of data to a file"""
    out_file = open(filename, "w")
    print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
    for project in projects:
        line = f"{project.name}\t{project.start_time.strftime('%d/%m/%Y')}\t" \
               f"{project.priority}\t{project.estimate:.2f}\t{project.completion}"
        print(line, file = out_file)
    out_file.close()

def display_projects(projects):
    """Display incomplete and complete projects and sorted by priority."""
    incomplete = []
    complete = []
    for project in projects:
        if project.is_complete():
            complete.append(project)
        else:
            incomplete.append(project)
    incomplete.sort()
    complete.sort()
    print("Incomplete projects:")
    for project in incomplete:
        print(f"{   project}")
    print("Completed projects:")
    for project in complete:
        print(f"{   project}")

def get_start_time(project):
    """Return the start_time of a Project object"""
    return project.start_time

def filter_by_date(projects, date_str):
    """Display start or after the given date and sort by start_time"""
    try:
        filter_date = datetime.strptime(date_str, "%d/%m/%Y").date()
    except ValueError:
        print("Invalid date format. Please use dd/mm/yy.")
        return None
    filtered_projects = []
    for project in projects:
        if project.start_time >= filter_date:
            filtered_projects.append(project)
    filtered_projects.sort(key=get_start_time)
    for project in filtered_projects:
        print(project)

def add_new_project():
    """Prompt the user to input details for a new project and return a Project"""
    name = input("Name: ")
    start_time = input("Start date (dd/mm/yy): ")
    date_valid = False
    while not date_valid:
        try:
            datetime.strptime(start_time, "%d/%m/%Y")
            date_valid = True
        except ValueError:
            print("Invalid date format. Please use dd/mm/yy.")
            start_time = input("Start date (dd/mm/yy): ")
    priority = int(input("Priority: "))
    estimate = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))
    return Project(name, start_time, priority, estimate, completion)

def update_project(projects):
    """Let the user update the project"""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    try:
        choice = int(input("Project choice: "))
        project = projects[choice]
    except ValueError:
        print("Invalid choice")
        return None
    print(project)
    completion_input = input("New Percent: ")
    priority_input = input("New Priority: ")
    if completion_input != "":
        try:
            project.completion = int(completion_input)
        except ValueError:
            print("Invalid value")
    if priority_input != "":
        try:
            project.priority = int(priority_input)
        except ValueError:
            print("Invalid value")


main()