from project import Project

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


main()