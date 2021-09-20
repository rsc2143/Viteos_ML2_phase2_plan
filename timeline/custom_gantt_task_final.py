
# Import Statements
import gantt
from datetime import date


# Creating Resources
Pratik = gantt.Resource("Pratik")
Ritesh = gantt.Resource("Ritesh")
IT = gantt.Resource("IT")
Abhijeet = gantt.Resource("Abhijeet")
Rohit = gantt.Resource("Rohit")
Hari = gantt.Resource("Hari")
Rani = gantt.Resource("Rani")


# Creating tasks for project : permission_access
tasks_for_project_permission_access = []

task_Jenkins_project_permission_access = gantt.Task(name="Jenkins", start=date(2021,9,13), duration=3, resources=[Rani, IT, Rohit], color="#FFFF00")
tasks_for_project_permission_access.append(task_Jenkins_project_permission_access)

task_Docker_project_permission_access = gantt.Task(name="Docker", start=date(2021,9,13), duration=7, resources=[Rani], color="#FFFF00")
tasks_for_project_permission_access.append(task_Docker_project_permission_access)

task_Super_User_Creation_project_permission_access = gantt.Task(name="Super_User_Creation", start=date(2021,9,13), duration=3, resources=[Rani, IT, Rohit], color="#FFFF00")
tasks_for_project_permission_access.append(task_Super_User_Creation_project_permission_access)

task_Version_control_access_plus_creation_of_package_repo_project_permission_access = gantt.Task(name="Version_control_access_plus_creation_of_package_repo", start=date(2021,9,13), duration=5, resources=[Rohit, Ritesh, Rani, IT], color="#FFFF00")
tasks_for_project_permission_access.append(task_Version_control_access_plus_creation_of_package_repo_project_permission_access)

task_Project_management_project_permission_access = gantt.Task(name="Project_management", start=date(2021,9,13), duration=3, resources=[Rohit, Rani, IT, Pratik, Abhijeet], color="#FFFF00")
tasks_for_project_permission_access.append(task_Project_management_project_permission_access)

task_Firewall_access_for_package_installations_project_permission_access = gantt.Task(name="Firewall_access_for_package_installations", start=date(2021,9,20), duration=3, resources=[Rani, IT, Rohit], color="#FFFF00")
tasks_for_project_permission_access.append(task_Firewall_access_for_package_installations_project_permission_access)

task_Decide_on_Cloud_infrastructure_project_permission_access = gantt.Task(name="Decide_on_Cloud_infrastructure", start=date(2021,9,20), duration=3, resources=[Rani, IT, Rohit, Hari], color="#FFFF00")
tasks_for_project_permission_access.append(task_Decide_on_Cloud_infrastructure_project_permission_access)

task_Which_IDE_to_use_project_permission_access = gantt.Task(name="Which_IDE_to_use", start=date(2021,9,20), duration=3, resources=[Rani, IT, Rohit, Pratik, Abhijeet], color="#FFFF00")
tasks_for_project_permission_access.append(task_Which_IDE_to_use_project_permission_access)

task_Milestone_plus_documentation_project_permission_access = gantt.Task(name="Milestone_plus_documentation", start=date(2021,9,23), duration=3, resources=[Rani, Rohit, Pratik, Abhijeet], color="#FFFF00")
tasks_for_project_permission_access.append(task_Milestone_plus_documentation_project_permission_access)

# Creating project : permission_access
project_permission_access = gantt.Project(name='permission_access')
for task in tasks_for_project_permission_access:
   project_permission_access.add_task(task)

# Creating tasks for project : code_design
tasks_for_project_code_design = []

task_Research_design_pattern_most_suitable_for_pythonic_classes_project_code_design = gantt.Task(name="Research_design_pattern_most_suitable_for_pythonic_classes", start=date(2021,9,26), duration=4, resources=[Rohit], color="#00FF00")
tasks_for_project_code_design.append(task_Research_design_pattern_most_suitable_for_pythonic_classes_project_code_design)

task_Decide_on_virtualenv_or_conda_to_use_as_package_or_environment_manager_project_code_design = gantt.Task(name="Decide_on_virtualenv_or_conda_to_use_as_package_or_environment_manager", start=date(2021,9,26), duration=1, resources=[Rohit], color="#00FF00")
tasks_for_project_code_design.append(task_Decide_on_virtualenv_or_conda_to_use_as_package_or_environment_manager_project_code_design)

task_Python_Wheels_project_code_design = gantt.Task(name="Python_Wheels", start=date(2021,9,26), duration=2, resources=[Rohit], color="#00FF00")
tasks_for_project_code_design.append(task_Python_Wheels_project_code_design)

task_Revamp_Architecture_for_break_resolution_project_code_design = gantt.Task(name="Revamp_Architecture_for_break_resolution", start=date(2021,9,26), duration=4, resources=[Pratik], color="#00FF00")
tasks_for_project_code_design.append(task_Revamp_Architecture_for_break_resolution_project_code_design)

task_Revamp_Architecture_for_comment_resolution_project_code_design = gantt.Task(name="Revamp_Architecture_for_comment_resolution", start=date(2021,9,26), duration=4, resources=[Abhijeet], color="#00FF00")
tasks_for_project_code_design.append(task_Revamp_Architecture_for_comment_resolution_project_code_design)

task_Break_resolution_architecture_design_project_code_design = gantt.Task(name="Break_resolution_architecture_design", start=date(2021,9,30), duration=2, resources=[Rohit, Pratik, Abhijeet], color="#00FF00")
tasks_for_project_code_design.append(task_Break_resolution_architecture_design_project_code_design)

task_Comment_resolution_architecture_design_project_code_design = gantt.Task(name="Comment_resolution_architecture_design", start=date(2021,9,30), duration=3, resources=[Rohit, Pratik, Abhijeet], color="#00FF00")
tasks_for_project_code_design.append(task_Comment_resolution_architecture_design_project_code_design)

task_Build_class_for_reading_data_project_code_design = gantt.Task(name="Build_class_for_reading_data", start=date(2021,10,3), duration=3, resources=[Rohit], color="#00FF00")
tasks_for_project_code_design.append(task_Build_class_for_reading_data_project_code_design)

task_Milestone_plus_documentation_project_code_design = gantt.Task(name="Milestone_plus_documentation", start=date(2021,10,6), duration=3, resources=[Rani, Rohit, Pratik, Abhijeet], color="#00FF00")
tasks_for_project_code_design.append(task_Milestone_plus_documentation_project_code_design)

# Creating project : code_design
project_code_design = gantt.Project(name='code_design')
for task in tasks_for_project_code_design:
   project_code_design.add_task(task)

all_projects = gantt.Project(name='All Projects')

all_projects.add_task(project_permission_access)
all_projects.add_task(project_code_design)
all_projects.make_svg_for_resources(filename="all_projects_timeline_final_daily_scale.svg",
                                    today=date(2021,9,20),
                                    start=date(2021,9,13),
                                    end=date(2021,10,19),
                                    scale=gantt.DRAW_WITH_DAILY_SCALE)