from project import Project
from datetime import datetime

filename = "projects.txt"

def main():
    projects = load_project(filename)
    # for project in projects:
    #     print(project)
    # save_projects("projects_saved.txt", projects)
    # display_projects(projects)

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



main()