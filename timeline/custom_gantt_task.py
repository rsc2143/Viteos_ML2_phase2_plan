
# Import Statements
import gantt
from datetime import date


# Creating Resources
Rani = gantt.Resource("Rani")
Rohit = gantt.Resource("Rohit")
Abhijeet = gantt.Resource("Abhijeet")
IT = gantt.Resource("IT")
Pratik = gantt.Resource("Pratik")
Ritesh = gantt.Resource("Ritesh")


# Creating tasks for project : permission_access
tasks_for_project_permission_access = []

task_Jenkins_project_permission_access = gantt.Task(name="Jenkins", start=date(2021,9,13), duration=3, resources=[Rani, IT, Rohit], color="#FFFF00")
tasks_for_project_permission_access.append(task_Jenkins_project_permission_access)

task_Docker_project_permission_access = gantt.Task(name="Docker", start=date(2021,9,13), duration=7, resources=[Rani], color="#FFFF00")
tasks_for_project_permission_access.append(task_Docker_project_permission_access)

task_Super_User_Creation_project_permission_access = gantt.Task(name="Super_User_Creation", start=date(2021,9,13), duration=3, resources=[Rani, IT, Rohit], color="#FFFF00")
tasks_for_project_permission_access.append(task_Super_User_Creation_project_permission_access)

task_Firewall_access_for_package_installations_project_permission_access = gantt.Task(name="Firewall_access_for_package_installations", start=date(2021,9,20), duration=3, resources=[Rani, IT, Rohit, Pratik, Abhijeet], color="#FFFF00")
tasks_for_project_permission_access.append(task_Firewall_access_for_package_installations_project_permission_access)

task_test_task_order_2_project_permission_access = gantt.Task(name="test_task_order_2", start=date(2021,9,20), duration=5, resources=[Rani, IT, Rohit], color="#FFFF00")
tasks_for_project_permission_access.append(task_test_task_order_2_project_permission_access)

task_test_task_order_2_second_project_permission_access = gantt.Task(name="test_task_order_2_second", start=date(2021,9,20), duration=2, resources=[Rani, IT, Rohit], color="#FFFF00")
tasks_for_project_permission_access.append(task_test_task_order_2_second_project_permission_access)

task_test_task_order_2_third_project_permission_access = gantt.Task(name="test_task_order_2_third", start=date(2021,9,20), duration=2, resources=[Rani, IT, Rohit], color="#FFFF00")
tasks_for_project_permission_access.append(task_test_task_order_2_third_project_permission_access)

task_test_task_order_3_project_permission_access = gantt.Task(name="test_task_order_3", start=date(2021,9,25), duration=3, resources=[Rani, IT, Rohit], color="#FFFF00")
tasks_for_project_permission_access.append(task_test_task_order_3_project_permission_access)

task_test_task_order_3_second_project_permission_access = gantt.Task(name="test_task_order_3_second", start=date(2021,9,25), duration=5, resources=[Rani, IT, Rohit], color="#FFFF00")
tasks_for_project_permission_access.append(task_test_task_order_3_second_project_permission_access)

task_test_task_order_4_project_permission_access = gantt.Task(name="test_task_order_4", start=date(2021,9,30), duration=3, resources=[Rani, IT, Rohit], color="#FFFF00")
tasks_for_project_permission_access.append(task_test_task_order_4_project_permission_access)

task_test_task_order_4_second_project_permission_access = gantt.Task(name="test_task_order_4_second", start=date(2021,9,30), duration=3, resources=[Rani, IT, Rohit], color="#FFFF00")
tasks_for_project_permission_access.append(task_test_task_order_4_second_project_permission_access)

# Creating project : permission_access
project_permission_access = gantt.Project(name='permission_access')
for task in tasks_for_project_permission_access:
   project_permission_access.add_task(task)

# Creating tasks for project : code_design
tasks_for_project_code_design = []

task_test_task_order_1_project_code_design = gantt.Task(name="test_task_order_1", start=date(2021,10,3), duration=3, resources=[Rani, IT, Rohit], color="#00FF00")
tasks_for_project_code_design.append(task_test_task_order_1_project_code_design)

task_Jenkins_project_code_design = gantt.Task(name="Jenkins", start=date(2021,10,3), duration=3, resources=[Rani, IT, Rohit, Ritesh], color="#00FF00")
tasks_for_project_code_design.append(task_Jenkins_project_code_design)

task_Docker_project_code_design = gantt.Task(name="Docker", start=date(2021,10,3), duration=7, resources=[Rani], color="#00FF00")
tasks_for_project_code_design.append(task_Docker_project_code_design)

task_Super_User_Creation_project_code_design = gantt.Task(name="Super_User_Creation", start=date(2021,10,3), duration=3, resources=[Rani, IT, Rohit], color="#00FF00")
tasks_for_project_code_design.append(task_Super_User_Creation_project_code_design)

task_test_task_order_2_project_code_design = gantt.Task(name="test_task_order_2", start=date(2021,10,10), duration=3, resources=[Rani], color="#00FF00")
tasks_for_project_code_design.append(task_test_task_order_2_project_code_design)

# Creating project : code_design
project_code_design = gantt.Project(name='code_design')
for task in tasks_for_project_code_design:
   project_code_design.add_task(task)

all_projects = gantt.Project(name='All Projects')

all_projects.add_task(project_permission_access)
all_projects.add_task(project_code_design)
all_projects.make_svg_for_resources(filename="all_projects_timeline_daily_scale.svg",
                                    today=date(2021,9,19),
                                    start=date(2021,9,13),
                                    end=date(2021,10,13),
                                    scale=gantt.DRAW_WITH_DAILY_SCALE)