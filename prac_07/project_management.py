from project import Project

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