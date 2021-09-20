
# Import Statements
import gantt
from datetime import date


# Creating Resources
Tejas_and_team = gantt.Resource("Tejas_and_team")
Pratik = gantt.Resource("Pratik")
IT = gantt.Resource("IT")
Rani = gantt.Resource("Rani")
Abhijeet = gantt.Resource("Abhijeet")
Hari = gantt.Resource("Hari")
Rohit = gantt.Resource("Rohit")
Girish = gantt.Resource("Girish")


# Creating tasks for project : permission_access
tasks_for_project_permission_access = []

task_Jenkins_project_permission_access = gantt.Task(name="Jenkins", start=date(2021,9,20), duration=3, resources=[Rani, IT, Rohit], color="#FFFF00")
tasks_for_project_permission_access.append(task_Jenkins_project_permission_access)

task_Docker_project_permission_access = gantt.Task(name="Docker", start=date(2021,9,20), duration=7, resources=[Rani], color="#FFFF00")
tasks_for_project_permission_access.append(task_Docker_project_permission_access)

task_Super_User_Creation_project_permission_access = gantt.Task(name="Super_User_Creation", start=date(2021,9,20), duration=3, resources=[Rani, IT, Rohit], color="#FFFF00")
tasks_for_project_permission_access.append(task_Super_User_Creation_project_permission_access)

task_Version_control_access_plus_creation_of_package_repo_project_permission_access = gantt.Task(name="Version_control_access_plus_creation_of_package_repo", start=date(2021,9,20), duration=5, resources=[Rohit, Tejas_and_team, Rani, IT], color="#FFFF00")
tasks_for_project_permission_access.append(task_Version_control_access_plus_creation_of_package_repo_project_permission_access)

task_Project_management_project_permission_access = gantt.Task(name="Project_management", start=date(2021,9,20), duration=3, resources=[Rohit, Rani, IT, Pratik, Abhijeet], color="#FFFF00")
tasks_for_project_permission_access.append(task_Project_management_project_permission_access)

task_New_client_requirement_gathering_project_permission_access = gantt.Task(name="New_client_requirement_gathering", start=date(2021,9,20), duration=3, resources=[Rani, Hari, Rohit, Pratik, Abhijeet, Girish], color="#FFFF00")
tasks_for_project_permission_access.append(task_New_client_requirement_gathering_project_permission_access)

task_New_client_data_gathering_project_permission_access = gantt.Task(name="New_client_data_gathering", start=date(2021,9,27), duration=3, resources=[Rani, Tejas_and_team, Girish], color="#FFFF00")
tasks_for_project_permission_access.append(task_New_client_data_gathering_project_permission_access)

task_Firewall_access_for_package_installations_project_permission_access = gantt.Task(name="Firewall_access_for_package_installations", start=date(2021,9,27), duration=3, resources=[Rani, IT, Rohit], color="#FFFF00")
tasks_for_project_permission_access.append(task_Firewall_access_for_package_installations_project_permission_access)

task_Decide_on_Cloud_infrastructure_project_permission_access = gantt.Task(name="Decide_on_Cloud_infrastructure", start=date(2021,9,27), duration=3, resources=[Rani, IT, Rohit, Hari], color="#FFFF00")
tasks_for_project_permission_access.append(task_Decide_on_Cloud_infrastructure_project_permission_access)

task_Which_IDE_to_use_project_permission_access = gantt.Task(name="Which_IDE_to_use", start=date(2021,9,27), duration=3, resources=[Rani, IT, Rohit, Pratik, Abhijeet], color="#FFFF00")
tasks_for_project_permission_access.append(task_Which_IDE_to_use_project_permission_access)

task_New_client_initial_data_analysis_project_permission_access = gantt.Task(name="New_client_initial_data_analysis", start=date(2021,9,30), duration=5, resources=[Rani, Girish, Pratik, Abhijeet], color="#FFFF00")
tasks_for_project_permission_access.append(task_New_client_initial_data_analysis_project_permission_access)

task_Complete_unfinished_work_project_permission_access = gantt.Task(name="Complete_unfinished_work", start=date(2021,9,30), duration=3, resources=[Rani, Rohit, Pratik, Abhijeet, Hari], color="#FFFF00")
tasks_for_project_permission_access.append(task_Complete_unfinished_work_project_permission_access)

task_Decide_Tejas_team_work_involvement_bandwidth_project_permission_access = gantt.Task(name="Decide_Tejas_team_work_involvement_bandwidth", start=date(2021,9,30), duration=3, resources=[Rani, Tejas_and_team, Hari], color="#FFFF00")
tasks_for_project_permission_access.append(task_Decide_Tejas_team_work_involvement_bandwidth_project_permission_access)

task_Decide_Girish_team_work_involvement_bandwidth_project_permission_access = gantt.Task(name="Decide_Girish_team_work_involvement_bandwidth", start=date(2021,9,30), duration=3, resources=[Rani, Girish, Hari], color="#FFFF00")
tasks_for_project_permission_access.append(task_Decide_Girish_team_work_involvement_bandwidth_project_permission_access)

task_Decide_documentation_style_project_permission_access = gantt.Task(name="Decide_documentation_style", start=date(2021,9,30), duration=2, resources=[Rani, Rohit], color="#FFFF00")
tasks_for_project_permission_access.append(task_Decide_documentation_style_project_permission_access)

task_Milestone_plus_documentation_project_permission_access = gantt.Task(name="Milestone_plus_documentation", start=date(2021,10,5), duration=3, resources=[Rani, Rohit, Pratik, Abhijeet, Hari], color="#FFFF00")
tasks_for_project_permission_access.append(task_Milestone_plus_documentation_project_permission_access)

task_Decide_project_stakeholders_project_permission_access = gantt.Task(name="Decide_project_stakeholders", start=date(2021,10,5), duration=3, resources=[Rani, Rohit, Pratik, Abhijeet, Hari], color="#FFFF00")
tasks_for_project_permission_access.append(task_Decide_project_stakeholders_project_permission_access)

task_Decide_change_management_policy_project_permission_access = gantt.Task(name="Decide_change_management_policy", start=date(2021,10,5), duration=3, resources=[Rani, Rohit, Pratik, Abhijeet, Hari], color="#FFFF00")
tasks_for_project_permission_access.append(task_Decide_change_management_policy_project_permission_access)

task_Decide_and_evaluate_other_team_involvement_project_permission_access = gantt.Task(name="Decide_and_evaluate_other_team_involvement", start=date(2021,10,5), duration=3, resources=[Rani, Rohit, Pratik, Abhijeet, Hari], color="#FFFF00")
tasks_for_project_permission_access.append(task_Decide_and_evaluate_other_team_involvement_project_permission_access)

task_Approve_new_clients_project_permission_access = gantt.Task(name="Approve_new_clients", start=date(2021,10,5), duration=3, resources=[Rani, Rohit, Pratik, Abhijeet, Hari, Girish], color="#FFFF00")
tasks_for_project_permission_access.append(task_Approve_new_clients_project_permission_access)

# Creating project : permission_access
project_permission_access = gantt.Project(name='permission_access')
for task in tasks_for_project_permission_access:
   project_permission_access.add_task(task)

# Creating tasks for project : code_design
tasks_for_project_code_design = []

task_Research_design_pattern_most_suitable_for_pythonic_classes_project_code_design = gantt.Task(name="Research_design_pattern_most_suitable_for_pythonic_classes", start=date(2021,10,8), duration=4, resources=[Rohit], color="#00FF00")
tasks_for_project_code_design.append(task_Research_design_pattern_most_suitable_for_pythonic_classes_project_code_design)

task_Decide_on_virtualenv_or_conda_to_use_as_package_or_environment_manager_project_code_design = gantt.Task(name="Decide_on_virtualenv_or_conda_to_use_as_package_or_environment_manager", start=date(2021,10,8), duration=1, resources=[Rohit], color="#00FF00")
tasks_for_project_code_design.append(task_Decide_on_virtualenv_or_conda_to_use_as_package_or_environment_manager_project_code_design)

task_Python_Wheels_project_code_design = gantt.Task(name="Python_Wheels", start=date(2021,10,8), duration=2, resources=[Rohit], color="#00FF00")
tasks_for_project_code_design.append(task_Python_Wheels_project_code_design)

task_Revamp_Architecture_for_break_resolution_project_code_design = gantt.Task(name="Revamp_Architecture_for_break_resolution", start=date(2021,10,8), duration=4, resources=[Pratik], color="#00FF00")
tasks_for_project_code_design.append(task_Revamp_Architecture_for_break_resolution_project_code_design)

task_Revamp_Architecture_for_comment_resolution_project_code_design = gantt.Task(name="Revamp_Architecture_for_comment_resolution", start=date(2021,10,8), duration=4, resources=[Abhijeet], color="#00FF00")
tasks_for_project_code_design.append(task_Revamp_Architecture_for_comment_resolution_project_code_design)

task_Research_API_design_from_coding_perspective_project_code_design = gantt.Task(name="Research_API_design_from_coding_perspective", start=date(2021,10,8), duration=4, resources=[Rohit], color="#00FF00")
tasks_for_project_code_design.append(task_Research_API_design_from_coding_perspective_project_code_design)

task_Research_API_design_from_user_perspective_project_code_design = gantt.Task(name="Research_API_design_from_user_perspective", start=date(2021,10,8), duration=4, resources=[Rohit, Rani, Girish], color="#00FF00")
tasks_for_project_code_design.append(task_Research_API_design_from_user_perspective_project_code_design)

task_Break_resolution_architecture_design_project_code_design = gantt.Task(name="Break_resolution_architecture_design", start=date(2021,10,12), duration=2, resources=[Rohit, Pratik, Abhijeet], color="#00FF00")
tasks_for_project_code_design.append(task_Break_resolution_architecture_design_project_code_design)

task_Comment_resolution_architecture_design_project_code_design = gantt.Task(name="Comment_resolution_architecture_design", start=date(2021,10,12), duration=3, resources=[Rohit, Pratik, Abhijeet], color="#00FF00")
tasks_for_project_code_design.append(task_Comment_resolution_architecture_design_project_code_design)

task_Complete_unfinished_work_project_code_design = gantt.Task(name="Complete_unfinished_work", start=date(2021,10,15), duration=3, resources=[Rani, Rohit, Pratik, Abhijeet], color="#00FF00")
tasks_for_project_code_design.append(task_Complete_unfinished_work_project_code_design)

task_Milestone_plus_documentation_project_code_design = gantt.Task(name="Milestone_plus_documentation", start=date(2021,10,18), duration=3, resources=[Rani, Rohit, Pratik, Abhijeet], color="#00FF00")
tasks_for_project_code_design.append(task_Milestone_plus_documentation_project_code_design)

# Creating project : code_design
project_code_design = gantt.Project(name='code_design')
for task in tasks_for_project_code_design:
   project_code_design.add_task(task)

# Creating tasks for project : code_refactoring_plus_testing
tasks_for_project_code_refactoring_plus_testing = []

task_Build_super_class_for_Data_Read_Standardization_project_code_refactoring_plus_testing = gantt.Task(name="Build_super_class_for_Data_Read_Standardization", start=date(2021,10,21), duration=4, resources=[Rohit], color="#FF0000")
tasks_for_project_code_refactoring_plus_testing.append(task_Build_super_class_for_Data_Read_Standardization_project_code_refactoring_plus_testing)

task_Build_super_class_for_db_project_code_refactoring_plus_testing = gantt.Task(name="Build_super_class_for_db", start=date(2021,10,21), duration=4, resources=[Rohit], color="#FF0000")
tasks_for_project_code_refactoring_plus_testing.append(task_Build_super_class_for_db_project_code_refactoring_plus_testing)

task_Build_super_class_for_closed_architecture_project_code_refactoring_plus_testing = gantt.Task(name="Build_super_class_for_closed_architecture", start=date(2021,10,21), duration=5, resources=[Rohit, Abhijeet], color="#FF0000")
tasks_for_project_code_refactoring_plus_testing.append(task_Build_super_class_for_closed_architecture_project_code_refactoring_plus_testing)

task_Build_super_class_for_break_resolution_architecture_project_code_refactoring_plus_testing = gantt.Task(name="Build_super_class_for_break_resolution_architecture", start=date(2021,10,21), duration=7, resources=[Rohit, Pratik], color="#FF0000")
tasks_for_project_code_refactoring_plus_testing.append(task_Build_super_class_for_break_resolution_architecture_project_code_refactoring_plus_testing)

task_Build_super_class_for_comment_resolution_architecture_project_code_refactoring_plus_testing = gantt.Task(name="Build_super_class_for_comment_resolution_architecture", start=date(2021,10,21), duration=7, resources=[Rohit, Abhijeet], color="#FF0000")
tasks_for_project_code_refactoring_plus_testing.append(task_Build_super_class_for_comment_resolution_architecture_project_code_refactoring_plus_testing)

task_Build_inherited_Read_class_from_Data_Read_Standardization_and_db_class_project_code_refactoring_plus_testing = gantt.Task(name="Build_inherited_Read_class_from_Data_Read_Standardization_and_db_class", start=date(2021,10,28), duration=3, resources=[Rohit], color="#FF0000")
tasks_for_project_code_refactoring_plus_testing.append(task_Build_inherited_Read_class_from_Data_Read_Standardization_and_db_class_project_code_refactoring_plus_testing)

task_Build_super_class_for_interacting_trans_type_closed_project_code_refactoring_plus_testing = gantt.Task(name="Build_super_class_for_interacting_trans_type_closed", start=date(2021,10,28), duration=5, resources=[Rohit], color="#FF0000")
tasks_for_project_code_refactoring_plus_testing.append(task_Build_super_class_for_interacting_trans_type_closed_project_code_refactoring_plus_testing)

task_Build_super_class_for_non_interacting_trans_type_closed_project_code_refactoring_plus_testing = gantt.Task(name="Build_super_class_for_non_interacting_trans_type_closed", start=date(2021,10,28), duration=5, resources=[Rohit], color="#FF0000")
tasks_for_project_code_refactoring_plus_testing.append(task_Build_super_class_for_non_interacting_trans_type_closed_project_code_refactoring_plus_testing)

task_Build_super_class_for_UMR_OTO_Class_project_code_refactoring_plus_testing = gantt.Task(name="Build_super_class_for_UMR_OTO_Class", start=date(2021,10,28), duration=7, resources=[Pratik], color="#FF0000")
tasks_for_project_code_refactoring_plus_testing.append(task_Build_super_class_for_UMR_OTO_Class_project_code_refactoring_plus_testing)

task_Build_super_class_for_UMR_MTO_OTM_Class_project_code_refactoring_plus_testing = gantt.Task(name="Build_super_class_for_UMR_MTO_OTM_Class", start=date(2021,10,28), duration=7, resources=[Pratik], color="#FF0000")
tasks_for_project_code_refactoring_plus_testing.append(task_Build_super_class_for_UMR_MTO_OTM_Class_project_code_refactoring_plus_testing)

task_Build_super_class_for_UMR_MTM_Class_project_code_refactoring_plus_testing = gantt.Task(name="Build_super_class_for_UMR_MTM_Class", start=date(2021,10,28), duration=7, resources=[Pratik], color="#FF0000")
tasks_for_project_code_refactoring_plus_testing.append(task_Build_super_class_for_UMR_MTM_Class_project_code_refactoring_plus_testing)

task_Build_super_class_for_Description_Regex_Class_project_code_refactoring_plus_testing = gantt.Task(name="Build_super_class_for_Description_Regex_Class", start=date(2021,10,28), duration=3, resources=[Abhijeet], color="#FF0000")
tasks_for_project_code_refactoring_plus_testing.append(task_Build_super_class_for_Description_Regex_Class_project_code_refactoring_plus_testing)

task_Placeholder_for_other_comment_work_project_code_refactoring_plus_testing = gantt.Task(name="Placeholder_for_other_comment_work", start=date(2021,10,28), duration=3, resources=[Abhijeet], color="#FF0000")
tasks_for_project_code_refactoring_plus_testing.append(task_Placeholder_for_other_comment_work_project_code_refactoring_plus_testing)

task_Consolidate_Work_done_till_above_project_code_refactoring_plus_testing = gantt.Task(name="Consolidate_Work_done_till_above", start=date(2021,11,4), duration=3, resources=[Rohit, Pratik, Abhijeet, Rani], color="#FF0000")
tasks_for_project_code_refactoring_plus_testing.append(task_Consolidate_Work_done_till_above_project_code_refactoring_plus_testing)

task_Build_super_class_for_UMB_OTO_Class_project_code_refactoring_plus_testing = gantt.Task(name="Build_super_class_for_UMB_OTO_Class", start=date(2021,11,7), duration=7, resources=[Pratik], color="#FF0000")
tasks_for_project_code_refactoring_plus_testing.append(task_Build_super_class_for_UMB_OTO_Class_project_code_refactoring_plus_testing)

task_Build_super_class_for_UMB_MTO_OTM_Class_project_code_refactoring_plus_testing = gantt.Task(name="Build_super_class_for_UMB_MTO_OTM_Class", start=date(2021,11,7), duration=7, resources=[Pratik], color="#FF0000")
tasks_for_project_code_refactoring_plus_testing.append(task_Build_super_class_for_UMB_MTO_OTM_Class_project_code_refactoring_plus_testing)

task_Build_super_class_for_UMB_MTM_Class_project_code_refactoring_plus_testing = gantt.Task(name="Build_super_class_for_UMB_MTM_Class", start=date(2021,11,7), duration=7, resources=[Pratik], color="#FF0000")
tasks_for_project_code_refactoring_plus_testing.append(task_Build_super_class_for_UMB_MTM_Class_project_code_refactoring_plus_testing)

task_Write_tests_for_each_class_written_upto_now_project_code_refactoring_plus_testing = gantt.Task(name="Write_tests_for_each_class_written_upto_now", start=date(2021,11,7), duration=7, resources=[Rohit], color="#FF0000")
tasks_for_project_code_refactoring_plus_testing.append(task_Write_tests_for_each_class_written_upto_now_project_code_refactoring_plus_testing)

task_Build_inherited_Model_Architecture_Class_project_code_refactoring_plus_testing = gantt.Task(name="Build_inherited_Model_Architecture_Class", start=date(2021,11,7), duration=7, resources=[Rohit], color="#FF0000")
tasks_for_project_code_refactoring_plus_testing.append(task_Build_inherited_Model_Architecture_Class_project_code_refactoring_plus_testing)

task_Build_inherited_Comment_Resolution_Logic_Class_project_code_refactoring_plus_testing = gantt.Task(name="Build_inherited_Comment_Resolution_Logic_Class", start=date(2021,11,14), duration=7, resources=[Abhijeet, Rohit], color="#FF0000")
tasks_for_project_code_refactoring_plus_testing.append(task_Build_inherited_Comment_Resolution_Logic_Class_project_code_refactoring_plus_testing)

task_Milestone_plus_documentation_project_code_refactoring_plus_testing = gantt.Task(name="Milestone_plus_documentation", start=date(2021,11,21), duration=3, resources=[Rani, Rohit, Pratik, Abhijeet], color="#FF0000")
tasks_for_project_code_refactoring_plus_testing.append(task_Milestone_plus_documentation_project_code_refactoring_plus_testing)

task_Build_inherited_Break_Resolution_Logic_Class_project_code_refactoring_plus_testing = gantt.Task(name="Build_inherited_Break_Resolution_Logic_Class", start=date(2021,11,24), duration=3, resources=[Rohit, Pratik, Abhijeet], color="#FF0000")
tasks_for_project_code_refactoring_plus_testing.append(task_Build_inherited_Break_Resolution_Logic_Class_project_code_refactoring_plus_testing)

task_Decide_best_Python_API_tool_project_code_refactoring_plus_testing = gantt.Task(name="Decide_best_Python_API_tool", start=date(2021,11,24), duration=3, resources=[Rani, Rohit, Pratik, Abhijeet], color="#FF0000")
tasks_for_project_code_refactoring_plus_testing.append(task_Decide_best_Python_API_tool_project_code_refactoring_plus_testing)

task_Write_tests_for_each_class_written_upto_now_2_project_code_refactoring_plus_testing = gantt.Task(name="Write_tests_for_each_class_written_upto_now_2", start=date(2021,11,24), duration=3, resources=[Rohit], color="#FF0000")
tasks_for_project_code_refactoring_plus_testing.append(task_Write_tests_for_each_class_written_upto_now_2_project_code_refactoring_plus_testing)

task_Complete_unfinished_work_project_code_refactoring_plus_testing = gantt.Task(name="Complete_unfinished_work", start=date(2021,11,27), duration=4, resources=[Rohit], color="#FF0000")
tasks_for_project_code_refactoring_plus_testing.append(task_Complete_unfinished_work_project_code_refactoring_plus_testing)

task_Milestone_plus_documentation_2_project_code_refactoring_plus_testing = gantt.Task(name="Milestone_plus_documentation_2", start=date(2021,11,27), duration=4, resources=[Rani, Rohit, Pratik, Abhijeet], color="#FF0000")
tasks_for_project_code_refactoring_plus_testing.append(task_Milestone_plus_documentation_2_project_code_refactoring_plus_testing)

# Creating project : code_refactoring_plus_testing
project_code_refactoring_plus_testing = gantt.Project(name='code_refactoring_plus_testing')
for task in tasks_for_project_code_refactoring_plus_testing:
   project_code_refactoring_plus_testing.add_task(task)

all_projects = gantt.Project(name='All Projects')

all_projects.add_task(project_permission_access)
all_projects.add_task(project_code_design)
all_projects.add_task(project_code_refactoring_plus_testing)
all_projects.make_svg_for_resources(filename="all_projects_timeline_final_daily_scale.svg",
                                    today=date(2021,9,20),
                                    start=date(2021,9,20),
                                    end=date(2021,12,11),
                                    scale=gantt.DRAW_WITH_DAILY_SCALE)