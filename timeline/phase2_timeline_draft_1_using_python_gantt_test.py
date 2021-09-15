from datetime import date
import gantt

# Change font default
gantt.define_font_attributes(fill='black', stroke='black', stroke_width=0, font_family="Verdana")

# Create 2 employees
Ben = gantt.Resource("Ben")
Alex = gantt.Resource("Alex")

task1_project1 = gantt.Task(name='task1', start=date(2021, 1, 27), duration=13, resources=[Ben], color="#a3ddcb")
task2_project1 = gantt.Task(name='task2', start=date(2021, 2, 10), duration=8, resources=[Alex], color="#a3ddcb")
task3_project1 = gantt.Task(name='task3', start=date(2021, 2, 19), duration=10, resources=[Ben], color="#a3ddcb")
task4_project1 = gantt.Task(name='task4', start=date(2021, 3, 1), duration=12, resources=[Ben, Alex], color="#a3ddcb")

# Createa a project
project_1 = gantt.Project(name='Project 1')

# Add tasks to that project
for task in [task1_project1, task2_project1, task3_project1, task4_project1]:
    project_1.add_task(task)

gantt.add_vacations(start_date=date(2021, 3, 15), end_date= date(2021,3,20))

project_1.make_svg_for_tasks(
                      filename='Project_1.svg',
                      today=date(2021, 1, 27),
                      start=date(2021,1, 20),
                      end=date(2021, 4, 1)
                     )

# Create tasks for project 2
task1_project2 = gantt.Task(name='task1', start=date(2021, 3, 13), duration=10, resources=[Alex], color="#ffe3de")
task2_project2 = gantt.Task(name='task2', start=date(2021, 3, 23), duration=8, resources=[Ben], color="#ffe3de")
task3_project2 = gantt.Task(name='task3', start=date(2021, 3, 24), duration=10, resources=[Ben], color="#ffe3de")
task4_project2 = gantt.Task(name='task4', start=date(2021, 4, 5), duration=5, resources=[Ben, Alex], color="#ffe3de")

# Add milestones
ms1 = gantt.Milestone(name='Milestone 1', depends_of=[task1_project2, task3_project2])
ms2 = gantt.Milestone(name='Milestone 2', depends_of=[task1_project2, task4_project2])

# Create project 2
project_2 = gantt.Project(name='Project 2')

# Add tasks and milestones to the project
for task in [task1_project2, task2_project2, task3_project2, task4_project2]:
    project_2.add_task(task)

for milestone in [ms1, ms2]:
    project_2.add_task(milestone)

# Create project that contains 2 projects
all_projects = gantt.Project(name='All Projects')

for project in [project_1, project_2]:
    all_projects.add_task(project)

all_projects.make_svg_for_tasks(
                      filename='multiple_projects.svg',
                      today=date(2021, 1, 27),
                      start=date(2021,1, 20),
                      end=date(2021, 4, 30)
                     )
