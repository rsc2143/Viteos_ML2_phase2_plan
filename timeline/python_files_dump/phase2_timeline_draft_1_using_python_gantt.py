from datetime import datetime, date
import gantt

gantt.define_font_attributes(fill='black', stroke='black', stroke_width=0, font_family='Verdana')


# dates
ML2_Phase2_start_date = date(2021, 9, 13)

# Resources

## Workers

### EpowerX
Rohit = gantt.Resource("Rohit")
Pratik = gantt.Resource("Pratik")
Abhijeet = gantt.Resource("Abhijeet")
### ITG
Shitanshu = gantt.Resource("Shitanshu")
Ritesh = gantt.Resource("Ritesh")

# Technical managers
Rani = gantt.Resource("Rani")
Girish = gantt.Resource("Girish")

## Business Managers
Hari = gantt.Resource("Hari")
Tejas = gantt.Resource("Tejas")

# Colors
permission_access_color = '#FFFF00' # Yellow
code_design_color = '#00FF00' # Lime or light green
code_refactoring_color = '#FF00FF' # Magenta
ci_new_code_color = '#FF0000' # Red
api_color = '#800080' # Purple
docker_color = '#FFA500' # Orange
jenkins_color = '#7FFD4' #Aquamarine
kubernetes_cloud_color = '#0000FF' # Blue
deployment_color = '#FFC0CB' # Pink
testing_color = '#00FFFF' # Cyan
user_approval = '#008000' # Green

def custom_gantt_task(param_name = None,
                                    param_start = None,
                                    param_stop=None,
                                    param_duration=None,
                                    param_depends_of=None,
                                    param_resources=None,
                                    param_percent_done=None,
                                    param_color=None,
                                    param_fullname=None,
                                    param_display=True,
                                    param_state = '',
                                    param_project=None):
    """
    This function defines a new gantt task and adds the task to the gantt project

    :param <all_gantt_task_params>:   all parameters used to define a gantt.Task
    :param param_project:             gantt.project to which the newly defined task will be added to
    :return:                          newly defined gantt.Task

    """
    fun_task = gantt.Task(name=param_name, start=param_start, stop=param_stop, duration=param_duration, depends_of=param_depends_of, resources=param_resources, percent_done=param_percent_done, color=param_color, fullname=param_fullname, display=param_display, state=param_state)
    param_project.add_task(fun_task)
    fun_return_dict = {
                        "task":         fun_task,
                        "end_date":     fun_end_date,
                        "duration":     fun_duration}
    return fun_return_dict

# Permissions + Access
project_permission_access = gantt.Project(name='Permissions + Access', color=permission_access_color)

task_total_time_project_permission_access = custom_gantt_task(param_name='Total Time for Permissions and Accesses',
                                                                            param_start=ML2_Phase2_start_date,
                                                                            param_duration=14,
                                                                            param_resources=[Rohit, Rani],
                                                                            param_color=permission_access_color,
                                                                            param_project=project_permission_access)

task_total_time_project_permission_access = custom_gantt_task(param_name='Total Time for Permissions and Accesses',
                                                                            param_start=ML2_Phase2_start_date,
                                                                            param_duration=14,
                                                                            param_resources=[Rohit, Rani],
                                                                            param_color=permission_access_color,
                                                                            param_project=project_permission_access)

task_total_time_project_permission_access = custom_gantt_task(param_name='Total Time for Permissions and Accesses',
                                                                            param_start=ML2_Phase2_start_date,
                                                                            param_duration=14,
                                                                            param_resources=[Rohit, Rani],
                                                                            param_color=permission_access_color,
                                                                            param_project=project_permission_access)

# Code Design
task_total_time_code_design = gantt.Task(name='Total Time for Code Design', start=ML2_Phase2_start_date, duration=3, resources=[Rohit], color=code_design_color, depends_of = [total_time_project_permission_access])
project_code_design = gantt.Project(name='Code Design', color=code_design_color)
project_code_design.add_task(task_total_time_code_design)

# Code Refactoring
task_total_time_project_code_refactor = gantt.Task(name='Total Time for Code Refactoring', start=date(2021, 9, 23), duration=14, resources=[Rohit], color=code_refactoring_color)
project_code_refactor = gantt.Project(name='Code Refactoring', color=code_refactoring_color)
project_code_refactor.add_task(task_total_time_project_code_refactor)

# Continuous Intergration of new model code
task_total_time_project_CI_new_code = gantt.Task(name='Total Time for CI of New Models', start=date(2021, 9, 23), duration=90, resources=[Rohit, Pratik, Abhijeet], color=ci_new_code_color)
project_CI_new_code = gantt.Project(name='CI New Code', color=ci_new_code_color)
project_CI_new_code.add_task(task_total_time_project_CI_new_code)

# API
task_total_time_project_build_api = gantt.Task(name='Total Time for API', start=date(2021, 10, 7), duration=13, resources=[Rohit], color=api_color)
project_build_api = gantt.Project(name='Build model API', color=api_color)
project_build_api.add_task(task_total_time_project_build_api)

# Docker
task_total_time_project_docker = gantt.Task(name='Total Time for Docker', start=date(2021, 9, 27), duration=13, resources=[Rohit], color=docker_color)
project_docker = gantt.Project(name='Docker')
project_docker.add_task(task_total_time_project_docker)

# Jenkins
task_total_time_project_jenkins = gantt.Task(name='Total Time for Jenkins', start=date(2021, 9, 27), duration=13, resources=[Rohit], color="#FFFF40")
project_jenkins = gantt.Project(name='Jenkins')
project_jenkins.add_task(task_total_time_project_jenkins)

# Kubernetes +  Cloud
task_total_time_project_kubernetes_cloud = gantt.Task(name='Total Time for Kubernetes + Cloud', start=date(2021, 9, 27), duration=13, resources=[Rohit], color="#FFFF40")
project_kubernetes_cloud = gantt.Project(name='Kubernetes + Cloud')
project_kubernetes_cloud.add_task(task_total_time_project_kubernetes_cloud)

# Deployment
task_total_time_project_ = gantt.Task(name='Total Time for Deployment', start=date(2021, 9, 27), duration=13, resources=[Rohit, Ritesh, Tejas, Shitanshu], color="#FFFF40")
project_ = gantt.Project(name='')
project_.add_task(task_total_time_project_)

# Testing
task_total_time_project_ = gantt.Task(name='Total Time for Testing', start=date(2021, 9, 27), duration=13, resources=[Rohit, Ritesh, Tejas, Shitanshu], color="#FFFF40")
project_ = gantt.Project(name='')
project_.add_task(task_total_time_project_)

# User Approval
task_total_time_project_ = gantt.Task(name='Total Time for User Approval', start=date(2021, 9, 27), duration=13, resources=[Rohit, Ritesh, Tejas, Shitanshu], color="#FFFF40")
project_ = gantt.Project(name='')
project_.add_task(task_total_time_project_)

"""
#
task_total_time_project_jenkinstotal_time_project_ = gantt.Task(name='Total Time', start=date(2021, 9, 27), duration=13, resources=[Rohit, Ritesh, Tejas, Shitanshu], color="#FFFF40")
project_ = gantt.Project(name='')
project_.add_task(total_time_project_)

#
total_time_project_ = gantt.Task(name='Total Time', start=date(2021, 9, 27), duration=13, resources=[Rohit, Ritesh, Tejas, Shitanshu], color="#FFFF40")
project_ = gantt.Project(name='')
project_.add_task(total_time_project_)

#
total_time_project_ = gantt.Task(name='Total Time', start=date(2021, 9, 27), duration=13, resources=[Rohit, Ritesh, Tejas, Shitanshu], color="#FFFF40")
project_ = gantt.Project(name='')
project_.add_task(total_time_project_)
"""

# Create another project
p = gantt.Project(name='Full Gantt')
# wich contains the first two projects
# and a single task
full_task = gantt.Task(name='Full Project',
                       start=ML2_Phase2_start_date,
                       duration=150,
                       resources=[Rohit,Pratik,Abhijeet,Rani,Girish,Tejas,Ritesh,Shitanshu,Hari])


p.add_task(project_permission_access)
p.add_task(project_code_design)
p.add_task(project_code_refactor)
p.add_task(project_CI_new_code)
p.add_task(project_build_api)
p.add_task(full_task)

p.make_svg_for_tasks(filename='full_daily.svg',
                     today=ML2_Phase2_start_date,
                     scale=gantt.DRAW_WITH_DAILY_SCALE)

p.make_svg_for_resources(filename='full_daily_resources.svg',
                     today=ML2_Phase2_start_date,
                     scale=gantt.DRAW_WITH_DAILY_SCALE)
