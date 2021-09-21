
# Import Statements
import gantt
from datetime import date


# Creating Resources
Pratik = gantt.Resource("Pratik")
IT = gantt.Resource("IT")
Abhijeet = gantt.Resource("Abhijeet")
Girish = gantt.Resource("Girish")
Rani = gantt.Resource("Rani")
Rohit = gantt.Resource("Rohit")
Tejas_and_team = gantt.Resource("Tejas_and_team")
Hari = gantt.Resource("Hari")


# Creating tasks for project : Planning
tasks_for_project_Planning = []

task_Jenkins_project_Planning = gantt.Task(name="Jenkins", start=date(2021,9,20), duration=3, resources=[Rani, IT, Rohit], color="#FFFF00")
tasks_for_project_Planning.append(task_Jenkins_project_Planning)

task_Docker_project_Planning = gantt.Task(name="Docker", start=date(2021,9,20), duration=7, resources=[Rani], color="#FFFF00")
tasks_for_project_Planning.append(task_Docker_project_Planning)

task_Super_User_Creation_project_Planning = gantt.Task(name="Super_User_Creation", start=date(2021,9,20), duration=3, resources=[Rani, IT, Rohit], color="#FFFF00")
tasks_for_project_Planning.append(task_Super_User_Creation_project_Planning)

task_Version_control_access_plus_creation_of_package_repo_project_Planning = gantt.Task(name="Version_control_access_plus_creation_of_package_repo", start=date(2021,9,20), duration=5, resources=[Rohit, Tejas_and_team, Rani, IT], color="#FFFF00")
tasks_for_project_Planning.append(task_Version_control_access_plus_creation_of_package_repo_project_Planning)

task_Project_management_project_Planning = gantt.Task(name="Project_management", start=date(2021,9,20), duration=3, resources=[Rohit, Rani, IT, Pratik, Abhijeet], color="#FFFF00")
tasks_for_project_Planning.append(task_Project_management_project_Planning)

task_New_client_requirement_gathering_project_Planning = gantt.Task(name="New_client_requirement_gathering", start=date(2021,9,20), duration=3, resources=[Rani, Hari, Rohit, Pratik, Abhijeet, Girish], color="#FFFF00")
tasks_for_project_Planning.append(task_New_client_requirement_gathering_project_Planning)

task_Decide_issue_logging_mechanism_like_Git_issues_project_Planning = gantt.Task(name="Decide_issue_logging_mechanism_like_Git_issues", start=date(2021,9,27), duration=3, resources=[Rani, Tejas_and_team, Girish], color="#FFFF00")
tasks_for_project_Planning.append(task_Decide_issue_logging_mechanism_like_Git_issues_project_Planning)

task_New_client_data_gathering_project_Planning = gantt.Task(name="New_client_data_gathering", start=date(2021,9,27), duration=3, resources=[Rani, Tejas_and_team, Girish], color="#FFFF00")
tasks_for_project_Planning.append(task_New_client_data_gathering_project_Planning)

task_Firewall_access_for_package_installations_project_Planning = gantt.Task(name="Firewall_access_for_package_installations", start=date(2021,9,27), duration=3, resources=[Rani, IT, Rohit], color="#FFFF00")
tasks_for_project_Planning.append(task_Firewall_access_for_package_installations_project_Planning)

task_Decide_on_Cloud_infrastructure_project_Planning = gantt.Task(name="Decide_on_Cloud_infrastructure", start=date(2021,9,27), duration=3, resources=[Rani, IT, Rohit, Hari], color="#FFFF00")
tasks_for_project_Planning.append(task_Decide_on_Cloud_infrastructure_project_Planning)

task_Which_IDE_to_use_project_Planning = gantt.Task(name="Which_IDE_to_use", start=date(2021,9,27), duration=3, resources=[Rani, IT, Rohit, Pratik, Abhijeet], color="#FFFF00")
tasks_for_project_Planning.append(task_Which_IDE_to_use_project_Planning)

task_New_client_initial_data_analysis_project_Planning = gantt.Task(name="New_client_initial_data_analysis", start=date(2021,9,30), duration=5, resources=[Rani, Girish, Pratik, Abhijeet], color="#FFFF00")
tasks_for_project_Planning.append(task_New_client_initial_data_analysis_project_Planning)

task_Complete_unfinished_work_project_Planning = gantt.Task(name="Complete_unfinished_work", start=date(2021,9,30), duration=5, resources=[Rani, Rohit, Pratik, Abhijeet, Hari], color="#FFFF00")
tasks_for_project_Planning.append(task_Complete_unfinished_work_project_Planning)

task_Decide_Tejas_team_work_involvement_bandwidth_project_Planning = gantt.Task(name="Decide_Tejas_team_work_involvement_bandwidth", start=date(2021,9,30), duration=3, resources=[Rani, Tejas_and_team, Hari], color="#FFFF00")
tasks_for_project_Planning.append(task_Decide_Tejas_team_work_involvement_bandwidth_project_Planning)

task_Decide_Girish_team_work_involvement_bandwidth_project_Planning = gantt.Task(name="Decide_Girish_team_work_involvement_bandwidth", start=date(2021,9,30), duration=3, resources=[Rani, Girish, Hari], color="#FFFF00")
tasks_for_project_Planning.append(task_Decide_Girish_team_work_involvement_bandwidth_project_Planning)

task_Decide_documentation_style_project_Planning = gantt.Task(name="Decide_documentation_style", start=date(2021,9,30), duration=2, resources=[Rani, Rohit], color="#FFFF00")
tasks_for_project_Planning.append(task_Decide_documentation_style_project_Planning)

task_Milestone_plus_documentation_project_Planning = gantt.Task(name="Milestone_plus_documentation", start=date(2021,10,5), duration=3, resources=[Rani, Rohit, Pratik, Abhijeet, Hari], color="#FFFF00")
tasks_for_project_Planning.append(task_Milestone_plus_documentation_project_Planning)

task_Decide_project_stakeholders_project_Planning = gantt.Task(name="Decide_project_stakeholders", start=date(2021,10,5), duration=3, resources=[Rani, Rohit, Pratik, Abhijeet, Hari], color="#FFFF00")
tasks_for_project_Planning.append(task_Decide_project_stakeholders_project_Planning)

task_Decide_change_management_policy_project_Planning = gantt.Task(name="Decide_change_management_policy", start=date(2021,10,5), duration=3, resources=[Rani, Rohit, Pratik, Abhijeet, Hari], color="#FFFF00")
tasks_for_project_Planning.append(task_Decide_change_management_policy_project_Planning)

task_Decide_and_evaluate_other_team_involvement_project_Planning = gantt.Task(name="Decide_and_evaluate_other_team_involvement", start=date(2021,10,5), duration=3, resources=[Rani, Rohit, Pratik, Abhijeet, Hari], color="#FFFF00")
tasks_for_project_Planning.append(task_Decide_and_evaluate_other_team_involvement_project_Planning)

task_New_clients_approval_project_Planning = gantt.Task(name="New_clients_approval", start=date(2021,10,5), duration=3, resources=[Rani, Rohit, Pratik, Abhijeet, Hari, Girish], color="#FFFF00")
tasks_for_project_Planning.append(task_New_clients_approval_project_Planning)

task_Setup_Calls_with_Business_for_new_perspective_of_Existing_clients_project_Planning = gantt.Task(name="Setup_Calls_with_Business_for_new_perspective_of_Existing_clients", start=date(2021,10,5), duration=4, resources=[Rani, Hari, Girish], color="#FFFF00")
tasks_for_project_Planning.append(task_Setup_Calls_with_Business_for_new_perspective_of_Existing_clients_project_Planning)

task_Evaluate_and_add_new_tasks_if_any_project_Planning = gantt.Task(name="Evaluate_and_add_new_tasks_if_any", start=date(2021,10,9), duration=4, resources=[Rani, Rohit, Pratik, Abhijeet], color="#FFFF00")
tasks_for_project_Planning.append(task_Evaluate_and_add_new_tasks_if_any_project_Planning)

task_Research_version_control_best_practices_project_Planning = gantt.Task(name="Research_version_control_best_practices", start=date(2021,10,9), duration=4, resources=[Rani, Rohit, Pratik, Abhijeet], color="#FFFF00")
tasks_for_project_Planning.append(task_Research_version_control_best_practices_project_Planning)

# Creating project : Planning
project_Planning = gantt.Project(name='Planning')
for task in tasks_for_project_Planning:
   project_Planning.add_task(task)

# Creating tasks for project : CodeDesign
tasks_for_project_CodeDesign = []

task_Research_design_pattern_most_suitable_for_pythonic_classes_project_CodeDesign = gantt.Task(name="Research_design_pattern_most_suitable_for_pythonic_classes", start=date(2021,10,13), duration=4, resources=[Rohit], color="#00FF00")
tasks_for_project_CodeDesign.append(task_Research_design_pattern_most_suitable_for_pythonic_classes_project_CodeDesign)

task_New_clients_Decide_business_POCs_project_CodeDesign = gantt.Task(name="New_clients_Decide_business_POCs", start=date(2021,10,13), duration=3, resources=[Rani, Girish], color="#00FF00")
tasks_for_project_CodeDesign.append(task_New_clients_Decide_business_POCs_project_CodeDesign)

task_Document_POCs_and_share_with_EpowerX_project_CodeDesign = gantt.Task(name="Document_POCs_and_share_with_EpowerX", start=date(2021,10,13), duration=1, resources=[Rani, Girish], color="#00FF00")
tasks_for_project_CodeDesign.append(task_Document_POCs_and_share_with_EpowerX_project_CodeDesign)

task_Decide_on_virtualenv_or_conda_to_use_as_package_or_environment_manager_project_CodeDesign = gantt.Task(name="Decide_on_virtualenv_or_conda_to_use_as_package_or_environment_manager", start=date(2021,10,13), duration=1, resources=[Rohit], color="#00FF00")
tasks_for_project_CodeDesign.append(task_Decide_on_virtualenv_or_conda_to_use_as_package_or_environment_manager_project_CodeDesign)

task_Python_Wheels_project_CodeDesign = gantt.Task(name="Python_Wheels", start=date(2021,10,13), duration=2, resources=[Rohit], color="#00FF00")
tasks_for_project_CodeDesign.append(task_Python_Wheels_project_CodeDesign)

task_Revamp_Architecture_for_break_resolution_project_CodeDesign = gantt.Task(name="Revamp_Architecture_for_break_resolution", start=date(2021,10,13), duration=4, resources=[Pratik], color="#00FF00")
tasks_for_project_CodeDesign.append(task_Revamp_Architecture_for_break_resolution_project_CodeDesign)

task_Revamp_Architecture_for_comment_resolution_project_CodeDesign = gantt.Task(name="Revamp_Architecture_for_comment_resolution", start=date(2021,10,13), duration=4, resources=[Abhijeet], color="#00FF00")
tasks_for_project_CodeDesign.append(task_Revamp_Architecture_for_comment_resolution_project_CodeDesign)

task_Research_API_design_from_coding_perspective_project_CodeDesign = gantt.Task(name="Research_API_design_from_coding_perspective", start=date(2021,10,13), duration=4, resources=[Rohit], color="#00FF00")
tasks_for_project_CodeDesign.append(task_Research_API_design_from_coding_perspective_project_CodeDesign)

task_Research_API_design_from_user_perspective_project_CodeDesign = gantt.Task(name="Research_API_design_from_user_perspective", start=date(2021,10,13), duration=4, resources=[Rohit, Rani, Girish], color="#00FF00")
tasks_for_project_CodeDesign.append(task_Research_API_design_from_user_perspective_project_CodeDesign)

task_Get_New_client_Business_POCs_time_of_availability_and_bandwidth_project_CodeDesign = gantt.Task(name="Get_New_client_Business_POCs_time_of_availability_and_bandwidth", start=date(2021,10,13), duration=3, resources=[Rani, Girish], color="#00FF00")
tasks_for_project_CodeDesign.append(task_Get_New_client_Business_POCs_time_of_availability_and_bandwidth_project_CodeDesign)

task_Break_resolution_architecture_design_project_CodeDesign = gantt.Task(name="Break_resolution_architecture_design", start=date(2021,10,17), duration=2, resources=[Rohit, Pratik, Abhijeet], color="#00FF00")
tasks_for_project_CodeDesign.append(task_Break_resolution_architecture_design_project_CodeDesign)

task_Existing_clients_Prepare_task_document_with_business_leaders_for_any_new_ask_project_CodeDesign = gantt.Task(name="Existing_clients_Prepare_task_document_with_business_leaders_for_any_new_ask", start=date(2021,10,17), duration=3, resources=[Rani, Girish, Hari], color="#00FF00")
tasks_for_project_CodeDesign.append(task_Existing_clients_Prepare_task_document_with_business_leaders_for_any_new_ask_project_CodeDesign)

task_Comment_resolution_architecture_design_project_CodeDesign = gantt.Task(name="Comment_resolution_architecture_design", start=date(2021,10,17), duration=3, resources=[Rohit, Pratik, Abhijeet], color="#00FF00")
tasks_for_project_CodeDesign.append(task_Comment_resolution_architecture_design_project_CodeDesign)

task_Complete_unfinished_work_project_CodeDesign = gantt.Task(name="Complete_unfinished_work", start=date(2021,10,20), duration=5, resources=[Rani, Rohit, Pratik, Abhijeet], color="#00FF00")
tasks_for_project_CodeDesign.append(task_Complete_unfinished_work_project_CodeDesign)

task_Check_and_merge_all_code_into_version_control_1_project_CodeDesign = gantt.Task(name="Check_and_merge_all_code_into_version_control_1", start=date(2021,10,20), duration=5, resources=[Rani, Rohit, Pratik, Abhijeet], color="#00FF00")
tasks_for_project_CodeDesign.append(task_Check_and_merge_all_code_into_version_control_1_project_CodeDesign)

task_Configure_logging_module_database_project_CodeDesign = gantt.Task(name="Configure_logging_module_database", start=date(2021,10,25), duration=2, resources=[Rohit, Tejas_and_team], color="#00FF00")
tasks_for_project_CodeDesign.append(task_Configure_logging_module_database_project_CodeDesign)

task_Build_logging_module_project_CodeDesign = gantt.Task(name="Build_logging_module", start=date(2021,10,25), duration=6, resources=[Rohit], color="#00FF00")
tasks_for_project_CodeDesign.append(task_Build_logging_module_project_CodeDesign)

task_New_clients_Discuss_first_level_of_break_resolution_procedure_for_new_client_1_and_2_all_setups_project_CodeDesign = gantt.Task(name="New_clients_Discuss_first_level_of_break_resolution_procedure_for_new_client_1_and_2_all_setups", start=date(2021,10,25), duration=6, resources=[Pratik, Rani], color="#00FF00")
tasks_for_project_CodeDesign.append(task_New_clients_Discuss_first_level_of_break_resolution_procedure_for_new_client_1_and_2_all_setups_project_CodeDesign)

task_New_clients_Discuss_first_level_of_comment_resolution_procedure_for_new_client_1_and_2_all_setups_project_CodeDesign = gantt.Task(name="New_clients_Discuss_first_level_of_comment_resolution_procedure_for_new_client_1_and_2_all_setups", start=date(2021,10,25), duration=6, resources=[Abhijeet, Rani], color="#00FF00")
tasks_for_project_CodeDesign.append(task_New_clients_Discuss_first_level_of_comment_resolution_procedure_for_new_client_1_and_2_all_setups_project_CodeDesign)

task_Research_integration_of_logging_module_look_and_usage_in_proposed_API_project_CodeDesign = gantt.Task(name="Research_integration_of_logging_module_look_and_usage_in_proposed_API", start=date(2021,10,31), duration=6, resources=[Rohit], color="#00FF00")
tasks_for_project_CodeDesign.append(task_Research_integration_of_logging_module_look_and_usage_in_proposed_API_project_CodeDesign)

task_New_clients_write_rough_code_for_break_resolution_procedure_for_new_client_1_and_2_all_setups_project_CodeDesign = gantt.Task(name="New_clients_write_rough_code_for_break_resolution_procedure_for_new_client_1_and_2_all_setups", start=date(2021,10,31), duration=6, resources=[Pratik, Rani], color="#00FF00")
tasks_for_project_CodeDesign.append(task_New_clients_write_rough_code_for_break_resolution_procedure_for_new_client_1_and_2_all_setups_project_CodeDesign)

task_New_clients_write_rough_code_for_comment_resolution_procedure_for_new_client_1_and_2_all_setups_project_CodeDesign = gantt.Task(name="New_clients_write_rough_code_for_comment_resolution_procedure_for_new_client_1_and_2_all_setups", start=date(2021,10,31), duration=6, resources=[Abhijeet, Rani], color="#00FF00")
tasks_for_project_CodeDesign.append(task_New_clients_write_rough_code_for_comment_resolution_procedure_for_new_client_1_and_2_all_setups_project_CodeDesign)

task_Milestone_plus_documentation_project_CodeDesign = gantt.Task(name="Milestone_plus_documentation", start=date(2021,11,6), duration=3, resources=[Rani, Rohit, Pratik, Abhijeet], color="#00FF00")
tasks_for_project_CodeDesign.append(task_Milestone_plus_documentation_project_CodeDesign)

task_Check_and_merge_all_code_into_version_control_2_project_CodeDesign = gantt.Task(name="Check_and_merge_all_code_into_version_control_2", start=date(2021,11,6), duration=3, resources=[Rani, Rohit, Pratik, Abhijeet], color="#00FF00")
tasks_for_project_CodeDesign.append(task_Check_and_merge_all_code_into_version_control_2_project_CodeDesign)

# Creating project : CodeDesign
project_CodeDesign = gantt.Project(name='CodeDesign')
for task in tasks_for_project_CodeDesign:
   project_CodeDesign.add_task(task)

# Creating tasks for project : CodeRefactoringTesting
tasks_for_project_CodeRefactoringTesting = []

task_Existing_clients_Get_approval_from_EpowerX_team_for_new_accuracy_plus_new_ask_project_CodeRefactoringTesting = gantt.Task(name="Existing_clients_Get_approval_from_EpowerX_team_for_new_accuracy_plus_new_ask", start=date(2021,11,9), duration=4, resources=[Rohit, Pratik, Abhijeet, Rani, Hari, Girish], color="#FFA07A")
tasks_for_project_CodeRefactoringTesting.append(task_Existing_clients_Get_approval_from_EpowerX_team_for_new_accuracy_plus_new_ask_project_CodeRefactoringTesting)

task_Build_super_class_for_Data_Read_Standardization_project_CodeRefactoringTesting = gantt.Task(name="Build_super_class_for_Data_Read_Standardization", start=date(2021,11,9), duration=4, resources=[Rohit], color="#FFA07A")
tasks_for_project_CodeRefactoringTesting.append(task_Build_super_class_for_Data_Read_Standardization_project_CodeRefactoringTesting)

task_Build_super_class_for_db_project_CodeRefactoringTesting = gantt.Task(name="Build_super_class_for_db", start=date(2021,11,9), duration=4, resources=[Rohit], color="#FFA07A")
tasks_for_project_CodeRefactoringTesting.append(task_Build_super_class_for_db_project_CodeRefactoringTesting)

task_Build_super_class_for_closed_architecture_project_CodeRefactoringTesting = gantt.Task(name="Build_super_class_for_closed_architecture", start=date(2021,11,9), duration=5, resources=[Rohit, Abhijeet], color="#FFA07A")
tasks_for_project_CodeRefactoringTesting.append(task_Build_super_class_for_closed_architecture_project_CodeRefactoringTesting)

task_Build_super_class_for_break_resolution_architecture_project_CodeRefactoringTesting = gantt.Task(name="Build_super_class_for_break_resolution_architecture", start=date(2021,11,9), duration=7, resources=[Rohit, Pratik], color="#FFA07A")
tasks_for_project_CodeRefactoringTesting.append(task_Build_super_class_for_break_resolution_architecture_project_CodeRefactoringTesting)

task_Build_super_class_for_comment_resolution_architecture_project_CodeRefactoringTesting = gantt.Task(name="Build_super_class_for_comment_resolution_architecture", start=date(2021,11,9), duration=7, resources=[Rohit, Abhijeet], color="#FFA07A")
tasks_for_project_CodeRefactoringTesting.append(task_Build_super_class_for_comment_resolution_architecture_project_CodeRefactoringTesting)

task_Existing_clients_Revert_with_business_about_EpowerX_comments_project_CodeRefactoringTesting = gantt.Task(name="Existing_clients_Revert_with_business_about_EpowerX_comments", start=date(2021,11,16), duration=3, resources=[Hari, Rani, Girish], color="#FFA07A")
tasks_for_project_CodeRefactoringTesting.append(task_Existing_clients_Revert_with_business_about_EpowerX_comments_project_CodeRefactoringTesting)

task_Build_inherited_Read_class_from_Data_Read_Standardization_and_db_class_project_CodeRefactoringTesting = gantt.Task(name="Build_inherited_Read_class_from_Data_Read_Standardization_and_db_class", start=date(2021,11,16), duration=3, resources=[Rohit], color="#FFA07A")
tasks_for_project_CodeRefactoringTesting.append(task_Build_inherited_Read_class_from_Data_Read_Standardization_and_db_class_project_CodeRefactoringTesting)

task_Build_super_class_for_interacting_trans_type_closed_project_CodeRefactoringTesting = gantt.Task(name="Build_super_class_for_interacting_trans_type_closed", start=date(2021,11,16), duration=5, resources=[Rohit], color="#FFA07A")
tasks_for_project_CodeRefactoringTesting.append(task_Build_super_class_for_interacting_trans_type_closed_project_CodeRefactoringTesting)

task_Build_super_class_for_non_interacting_trans_type_closed_project_CodeRefactoringTesting = gantt.Task(name="Build_super_class_for_non_interacting_trans_type_closed", start=date(2021,11,16), duration=5, resources=[Rohit], color="#FFA07A")
tasks_for_project_CodeRefactoringTesting.append(task_Build_super_class_for_non_interacting_trans_type_closed_project_CodeRefactoringTesting)

task_Build_super_class_for_UMR_OTO_Class_project_CodeRefactoringTesting = gantt.Task(name="Build_super_class_for_UMR_OTO_Class", start=date(2021,11,16), duration=7, resources=[Pratik], color="#FFA07A")
tasks_for_project_CodeRefactoringTesting.append(task_Build_super_class_for_UMR_OTO_Class_project_CodeRefactoringTesting)

task_Build_super_class_for_UMR_MTO_OTM_Class_project_CodeRefactoringTesting = gantt.Task(name="Build_super_class_for_UMR_MTO_OTM_Class", start=date(2021,11,16), duration=7, resources=[Pratik], color="#FFA07A")
tasks_for_project_CodeRefactoringTesting.append(task_Build_super_class_for_UMR_MTO_OTM_Class_project_CodeRefactoringTesting)

task_Build_super_class_for_UMR_MTM_Class_project_CodeRefactoringTesting = gantt.Task(name="Build_super_class_for_UMR_MTM_Class", start=date(2021,11,16), duration=7, resources=[Pratik], color="#FFA07A")
tasks_for_project_CodeRefactoringTesting.append(task_Build_super_class_for_UMR_MTM_Class_project_CodeRefactoringTesting)

task_Build_super_class_for_Description_Regex_Class_project_CodeRefactoringTesting = gantt.Task(name="Build_super_class_for_Description_Regex_Class", start=date(2021,11,16), duration=3, resources=[Abhijeet], color="#FFA07A")
tasks_for_project_CodeRefactoringTesting.append(task_Build_super_class_for_Description_Regex_Class_project_CodeRefactoringTesting)

task_Placeholder_for_other_comment_work_project_CodeRefactoringTesting = gantt.Task(name="Placeholder_for_other_comment_work", start=date(2021,11,16), duration=3, resources=[Abhijeet], color="#FFA07A")
tasks_for_project_CodeRefactoringTesting.append(task_Placeholder_for_other_comment_work_project_CodeRefactoringTesting)

task_Existing_clients_Get_Tejas_team_consensus_for_existing_client_accuracies_and_asks_project_CodeRefactoringTesting = gantt.Task(name="Existing_clients_Get_Tejas_team_consensus_for_existing_client_accuracies_and_asks", start=date(2021,11,23), duration=3, resources=[Tejas_and_team, Rani, Girish], color="#FFA07A")
tasks_for_project_CodeRefactoringTesting.append(task_Existing_clients_Get_Tejas_team_consensus_for_existing_client_accuracies_and_asks_project_CodeRefactoringTesting)

task_Consolidate_Work_done_till_above_project_CodeRefactoringTesting = gantt.Task(name="Consolidate_Work_done_till_above", start=date(2021,11,23), duration=3, resources=[Rohit, Pratik, Abhijeet, Rani], color="#FFA07A")
tasks_for_project_CodeRefactoringTesting.append(task_Consolidate_Work_done_till_above_project_CodeRefactoringTesting)

task_Get_EpowerX_consensus_for_Tejas_suggestions_project_CodeRefactoringTesting = gantt.Task(name="Get_EpowerX_consensus_for_Tejas_suggestions", start=date(2021,11,23), duration=3, resources=[Rohit, Pratik, Abhijeet, Rani, Girish], color="#FFA07A")
tasks_for_project_CodeRefactoringTesting.append(task_Get_EpowerX_consensus_for_Tejas_suggestions_project_CodeRefactoringTesting)

task_New_clients_Discuss_first_level_of_break_resolution_procedure_for_new_client_3_and_4_all_setups_project_CodeRefactoringTesting = gantt.Task(name="New_clients_Discuss_first_level_of_break_resolution_procedure_for_new_client_3_and_4_all_setups", start=date(2021,11,23), duration=6, resources=[Pratik, Rani], color="#FFA07A")
tasks_for_project_CodeRefactoringTesting.append(task_New_clients_Discuss_first_level_of_break_resolution_procedure_for_new_client_3_and_4_all_setups_project_CodeRefactoringTesting)

task_New_clients_Discuss_first_level_of_comment_resolution_procedure_for_new_client_3_and_4_all_setups_project_CodeRefactoringTesting = gantt.Task(name="New_clients_Discuss_first_level_of_comment_resolution_procedure_for_new_client_3_and_4_all_setups", start=date(2021,11,23), duration=6, resources=[Abhijeet, Rani], color="#FFA07A")
tasks_for_project_CodeRefactoringTesting.append(task_New_clients_Discuss_first_level_of_comment_resolution_procedure_for_new_client_3_and_4_all_setups_project_CodeRefactoringTesting)

task_Get_overall_consensus_for_existing_client_approval_and_document_finally_project_CodeRefactoringTesting = gantt.Task(name="Get_overall_consensus_for_existing_client_approval_and_document_finally", start=date(2021,11,29), duration=3, resources=[Rohit, Pratik, Abhijeet, Rani, Girish, Hari, Tejas_and_team], color="#FFA07A")
tasks_for_project_CodeRefactoringTesting.append(task_Get_overall_consensus_for_existing_client_approval_and_document_finally_project_CodeRefactoringTesting)

task_Build_super_class_for_UMB_OTO_Class_project_CodeRefactoringTesting = gantt.Task(name="Build_super_class_for_UMB_OTO_Class", start=date(2021,11,29), duration=7, resources=[Pratik], color="#FFA07A")
tasks_for_project_CodeRefactoringTesting.append(task_Build_super_class_for_UMB_OTO_Class_project_CodeRefactoringTesting)

task_Build_super_class_for_UMB_MTO_OTM_Class_project_CodeRefactoringTesting = gantt.Task(name="Build_super_class_for_UMB_MTO_OTM_Class", start=date(2021,11,29), duration=7, resources=[Pratik], color="#FFA07A")
tasks_for_project_CodeRefactoringTesting.append(task_Build_super_class_for_UMB_MTO_OTM_Class_project_CodeRefactoringTesting)

task_Build_super_class_for_UMB_MTM_Class_project_CodeRefactoringTesting = gantt.Task(name="Build_super_class_for_UMB_MTM_Class", start=date(2021,11,29), duration=7, resources=[Pratik], color="#FFA07A")
tasks_for_project_CodeRefactoringTesting.append(task_Build_super_class_for_UMB_MTM_Class_project_CodeRefactoringTesting)

task_Write_tests_for_each_class_written_upto_now_project_CodeRefactoringTesting = gantt.Task(name="Write_tests_for_each_class_written_upto_now", start=date(2021,11,29), duration=7, resources=[Rohit], color="#FFA07A")
tasks_for_project_CodeRefactoringTesting.append(task_Write_tests_for_each_class_written_upto_now_project_CodeRefactoringTesting)

task_Build_inherited_Model_Architecture_Class_project_CodeRefactoringTesting = gantt.Task(name="Build_inherited_Model_Architecture_Class", start=date(2021,11,29), duration=7, resources=[Rohit], color="#FFA07A")
tasks_for_project_CodeRefactoringTesting.append(task_Build_inherited_Model_Architecture_Class_project_CodeRefactoringTesting)

task_Build_inherited_Comment_Resolution_Logic_Class_project_CodeRefactoringTesting = gantt.Task(name="Build_inherited_Comment_Resolution_Logic_Class", start=date(2021,12,6), duration=7, resources=[Abhijeet, Rohit], color="#FFA07A")
tasks_for_project_CodeRefactoringTesting.append(task_Build_inherited_Comment_Resolution_Logic_Class_project_CodeRefactoringTesting)

task_New_clients_write_rough_code_for_break_resolution_procedure_for_new_client_3_and_4_all_setups_project_CodeRefactoringTesting = gantt.Task(name="New_clients_write_rough_code_for_break_resolution_procedure_for_new_client_3_and_4_all_setups", start=date(2021,12,6), duration=7, resources=[Pratik, Rani], color="#FFA07A")
tasks_for_project_CodeRefactoringTesting.append(task_New_clients_write_rough_code_for_break_resolution_procedure_for_new_client_3_and_4_all_setups_project_CodeRefactoringTesting)

task_New_clients_write_rough_code_for_comment_resolution_procedure_for_new_client_3_and_4_all_setups_project_CodeRefactoringTesting = gantt.Task(name="New_clients_write_rough_code_for_comment_resolution_procedure_for_new_client_3_and_4_all_setups", start=date(2021,12,13), duration=7, resources=[Abhijeet, Rani], color="#FFA07A")
tasks_for_project_CodeRefactoringTesting.append(task_New_clients_write_rough_code_for_comment_resolution_procedure_for_new_client_3_and_4_all_setups_project_CodeRefactoringTesting)

task_Milestone_plus_documentation_project_CodeRefactoringTesting = gantt.Task(name="Milestone_plus_documentation", start=date(2021,12,13), duration=3, resources=[Rani, Rohit, Pratik, Abhijeet], color="#FFA07A")
tasks_for_project_CodeRefactoringTesting.append(task_Milestone_plus_documentation_project_CodeRefactoringTesting)

task_New_clients_Discuss_first_level_of_break_resolution_procedure_for_new_client_5_and_6_all_setups_project_CodeRefactoringTesting = gantt.Task(name="New_clients_Discuss_first_level_of_break_resolution_procedure_for_new_client_5_and_6_all_setups", start=date(2021,12,20), duration=6, resources=[Pratik, Rani], color="#FFA07A")
tasks_for_project_CodeRefactoringTesting.append(task_New_clients_Discuss_first_level_of_break_resolution_procedure_for_new_client_5_and_6_all_setups_project_CodeRefactoringTesting)

task_New_clients_Discuss_first_level_of_comment_resolution_procedure_for_new_client_5_and_6_all_setups_project_CodeRefactoringTesting = gantt.Task(name="New_clients_Discuss_first_level_of_comment_resolution_procedure_for_new_client_5_and_6_all_setups", start=date(2021,12,20), duration=6, resources=[Abhijeet, Rani], color="#FFA07A")
tasks_for_project_CodeRefactoringTesting.append(task_New_clients_Discuss_first_level_of_comment_resolution_procedure_for_new_client_5_and_6_all_setups_project_CodeRefactoringTesting)

task_New_clients_write_rough_code_for_break_resolution_procedure_for_new_client_5_and_6_all_setups_project_CodeRefactoringTesting = gantt.Task(name="New_clients_write_rough_code_for_break_resolution_procedure_for_new_client_5_and_6_all_setups", start=date(2021,12,26), duration=7, resources=[Pratik, Rani], color="#FFA07A")
tasks_for_project_CodeRefactoringTesting.append(task_New_clients_write_rough_code_for_break_resolution_procedure_for_new_client_5_and_6_all_setups_project_CodeRefactoringTesting)

task_New_clients_write_rough_code_for_comment_resolution_procedure_for_new_client_5_and_6_all_setups_project_CodeRefactoringTesting = gantt.Task(name="New_clients_write_rough_code_for_comment_resolution_procedure_for_new_client_5_and_6_all_setups", start=date(2021,12,26), duration=7, resources=[Abhijeet, Rani], color="#FFA07A")
tasks_for_project_CodeRefactoringTesting.append(task_New_clients_write_rough_code_for_comment_resolution_procedure_for_new_client_5_and_6_all_setups_project_CodeRefactoringTesting)

task_Build_inherited_Break_Resolution_Logic_Class_project_CodeRefactoringTesting = gantt.Task(name="Build_inherited_Break_Resolution_Logic_Class", start=date(2022,1,2), duration=3, resources=[Rohit, Pratik, Abhijeet], color="#FFA07A")
tasks_for_project_CodeRefactoringTesting.append(task_Build_inherited_Break_Resolution_Logic_Class_project_CodeRefactoringTesting)

task_Decide_best_Python_API_tool_project_CodeRefactoringTesting = gantt.Task(name="Decide_best_Python_API_tool", start=date(2022,1,2), duration=3, resources=[Rani, Rohit, Pratik, Abhijeet], color="#FFA07A")
tasks_for_project_CodeRefactoringTesting.append(task_Decide_best_Python_API_tool_project_CodeRefactoringTesting)

task_Write_tests_for_each_class_written_upto_now_2_project_CodeRefactoringTesting = gantt.Task(name="Write_tests_for_each_class_written_upto_now_2", start=date(2022,1,2), duration=7, resources=[Rohit], color="#FFA07A")
tasks_for_project_CodeRefactoringTesting.append(task_Write_tests_for_each_class_written_upto_now_2_project_CodeRefactoringTesting)

task_Complete_unfinished_work_project_CodeRefactoringTesting = gantt.Task(name="Complete_unfinished_work", start=date(2022,1,9), duration=5, resources=[Rohit], color="#FFA07A")
tasks_for_project_CodeRefactoringTesting.append(task_Complete_unfinished_work_project_CodeRefactoringTesting)

task_Existing_clients_Setup_Calls_with_Business_POCs_to_understand_how_accuracies_and_asks_can_be_coded_in_project_CodeRefactoringTesting = gantt.Task(name="Existing_clients_Setup_Calls_with_Business_POCs_to_understand_how_accuracies_and_asks_can_be_coded_in", start=date(2022,1,9), duration=4, resources=[Rani, Hari, Girish], color="#FFA07A")
tasks_for_project_CodeRefactoringTesting.append(task_Existing_clients_Setup_Calls_with_Business_POCs_to_understand_how_accuracies_and_asks_can_be_coded_in_project_CodeRefactoringTesting)

task_Build_inherited_Model_Class_project_CodeRefactoringTesting = gantt.Task(name="Build_inherited_Model_Class", start=date(2022,1,14), duration=4, resources=[Rohit], color="#FFA07A")
tasks_for_project_CodeRefactoringTesting.append(task_Build_inherited_Model_Class_project_CodeRefactoringTesting)

task_Existing_clients_Data_scientist_hold_talks_with_business_POCs_to_understand_new_ask_and_accuracy_improvement_project_CodeRefactoringTesting = gantt.Task(name="Existing_clients_Data_scientist_hold_talks_with_business_POCs_to_understand_new_ask_and_accuracy_improvement", start=date(2022,1,14), duration=10, resources=[Pratik, Abhijeet], color="#FFA07A")
tasks_for_project_CodeRefactoringTesting.append(task_Existing_clients_Data_scientist_hold_talks_with_business_POCs_to_understand_new_ask_and_accuracy_improvement_project_CodeRefactoringTesting)

task_Asynchronous_Message_RabbitMQ_Class_project_CodeRefactoringTesting = gantt.Task(name="Asynchronous_Message_RabbitMQ_Class", start=date(2022,1,14), duration=4, resources=[Rohit], color="#FFA07A")
tasks_for_project_CodeRefactoringTesting.append(task_Asynchronous_Message_RabbitMQ_Class_project_CodeRefactoringTesting)

task_Milestone_plus_documentation_2_project_CodeRefactoringTesting = gantt.Task(name="Milestone_plus_documentation_2", start=date(2022,1,24), duration=4, resources=[Rani, Rohit, Pratik, Abhijeet], color="#FFA07A")
tasks_for_project_CodeRefactoringTesting.append(task_Milestone_plus_documentation_2_project_CodeRefactoringTesting)

task_Synchronous_Message_RabbitMQ_Class_project_CodeRefactoringTesting = gantt.Task(name="Synchronous_Message_RabbitMQ_Class", start=date(2022,1,24), duration=4, resources=[Rohit], color="#FFA07A")
tasks_for_project_CodeRefactoringTesting.append(task_Synchronous_Message_RabbitMQ_Class_project_CodeRefactoringTesting)

task_Existing_clients_Prepare_roadmap_for_new_code_changes_project_CodeRefactoringTesting = gantt.Task(name="Existing_clients_Prepare_roadmap_for_new_code_changes", start=date(2022,1,24), duration=4, resources=[Pratik, Abhijeet], color="#FFA07A")
tasks_for_project_CodeRefactoringTesting.append(task_Existing_clients_Prepare_roadmap_for_new_code_changes_project_CodeRefactoringTesting)

task_Existing_client_Code_changes_part_1_project_CodeRefactoringTesting = gantt.Task(name="Existing_client_Code_changes_part_1", start=date(2022,1,24), duration=5, resources=[Pratik, Abhijeet], color="#FFA07A")
tasks_for_project_CodeRefactoringTesting.append(task_Existing_client_Code_changes_part_1_project_CodeRefactoringTesting)

task_Gather_data_type_requirement_for_writing_data_from_ml_into_db_project_CodeRefactoringTesting = gantt.Task(name="Gather_data_type_requirement_for_writing_data_from_ml_into_db", start=date(2022,1,29), duration=3, resources=[Rohit, Tejas_and_team], color="#FFA07A")
tasks_for_project_CodeRefactoringTesting.append(task_Gather_data_type_requirement_for_writing_data_from_ml_into_db_project_CodeRefactoringTesting)

task_Existing_client_Code_changes_part_2_project_CodeRefactoringTesting = gantt.Task(name="Existing_client_Code_changes_part_2", start=date(2022,1,29), duration=5, resources=[Pratik, Abhijeet], color="#FFA07A")
tasks_for_project_CodeRefactoringTesting.append(task_Existing_client_Code_changes_part_2_project_CodeRefactoringTesting)

task_Write_class_coding_project_CodeRefactoringTesting = gantt.Task(name="Write_class_coding", start=date(2022,2,3), duration=4, resources=[Rohit], color="#FFA07A")
tasks_for_project_CodeRefactoringTesting.append(task_Write_class_coding_project_CodeRefactoringTesting)

task_Existing_client_Code_changes_part_3_project_CodeRefactoringTesting = gantt.Task(name="Existing_client_Code_changes_part_3", start=date(2022,2,3), duration=5, resources=[Pratik, Abhijeet], color="#FFA07A")
tasks_for_project_CodeRefactoringTesting.append(task_Existing_client_Code_changes_part_3_project_CodeRefactoringTesting)

task_Write_tests_for_write_class_project_CodeRefactoringTesting = gantt.Task(name="Write_tests_for_write_class", start=date(2022,2,8), duration=5, resources=[Rohit], color="#FFA07A")
tasks_for_project_CodeRefactoringTesting.append(task_Write_tests_for_write_class_project_CodeRefactoringTesting)

task_Existing_client_Code_changes_part_4_project_CodeRefactoringTesting = gantt.Task(name="Existing_client_Code_changes_part_4", start=date(2022,2,8), duration=5, resources=[Pratik, Abhijeet], color="#FFA07A")
tasks_for_project_CodeRefactoringTesting.append(task_Existing_client_Code_changes_part_4_project_CodeRefactoringTesting)

task_Complete_unfinished_work_and_scope_for_break_project_CodeRefactoringTesting = gantt.Task(name="Complete_unfinished_work_and_scope_for_break", start=date(2022,2,13), duration=5, resources=[Rohit, Pratik, Abhijeet, Rani], color="#FFA07A")
tasks_for_project_CodeRefactoringTesting.append(task_Complete_unfinished_work_and_scope_for_break_project_CodeRefactoringTesting)

task_ML2_Phase2_Project_Checkpoint_project_CodeRefactoringTesting = gantt.Task(name="ML2_Phase2_Project_Checkpoint", start=date(2022,2,18), duration=5, resources=[Rohit, Pratik, Abhijeet, Rani, Hari, Girish, Tejas_and_team], color="#FFA07A")
tasks_for_project_CodeRefactoringTesting.append(task_ML2_Phase2_Project_Checkpoint_project_CodeRefactoringTesting)

task_Documentation_Review_project_CodeRefactoringTesting = gantt.Task(name="Documentation_Review", start=date(2022,2,18), duration=5, resources=[Rohit, Pratik, Abhijeet, Rani, Hari, Girish, Tejas_and_team], color="#FFA07A")
tasks_for_project_CodeRefactoringTesting.append(task_Documentation_Review_project_CodeRefactoringTesting)

task_Code_Review_project_CodeRefactoringTesting = gantt.Task(name="Code_Review", start=date(2022,2,18), duration=5, resources=[Rohit, Pratik, Abhijeet, Rani, Hari, Girish, Tejas_and_team], color="#FFA07A")
tasks_for_project_CodeRefactoringTesting.append(task_Code_Review_project_CodeRefactoringTesting)

task_Testing_Review_project_CodeRefactoringTesting = gantt.Task(name="Testing_Review", start=date(2022,2,18), duration=5, resources=[Rohit, Pratik, Abhijeet, Rani, Hari, Girish, Tejas_and_team], color="#FFA07A")
tasks_for_project_CodeRefactoringTesting.append(task_Testing_Review_project_CodeRefactoringTesting)

task_Test_code_with_real_data_project_CodeRefactoringTesting = gantt.Task(name="Test_code_with_real_data", start=date(2022,2,23), duration=5, resources=[Rohit, Pratik, Abhijeet, Rani, Hari, Girish, Tejas_and_team], color="#FFA07A")
tasks_for_project_CodeRefactoringTesting.append(task_Test_code_with_real_data_project_CodeRefactoringTesting)

# Creating project : CodeRefactoringTesting
project_CodeRefactoringTesting = gantt.Project(name='CodeRefactoringTesting')
for task in tasks_for_project_CodeRefactoringTesting:
   project_CodeRefactoringTesting.add_task(task)

# Creating tasks for project : ApiPlusNewClients
tasks_for_project_ApiPlusNewClients = []

task_Choose_API_client_like_Postman_or_Python_Connexion_Swagget_combo_project_ApiPlusNewClients = gantt.Task(name="Choose_API_client_like_Postman_or_Python_Connexion_Swagget_combo", start=date(2022,2,28), duration=2, resources=[Rohit], color="#FF00FF")
tasks_for_project_ApiPlusNewClients.append(task_Choose_API_client_like_Postman_or_Python_Connexion_Swagget_combo_project_ApiPlusNewClients)

task_Make_rough_framework_of_API_endpoints_project_ApiPlusNewClients = gantt.Task(name="Make_rough_framework_of_API_endpoints", start=date(2022,2,28), duration=4, resources=[Rohit], color="#FF00FF")
tasks_for_project_ApiPlusNewClients.append(task_Make_rough_framework_of_API_endpoints_project_ApiPlusNewClients)

task_Configure_API_internal_database_project_ApiPlusNewClients = gantt.Task(name="Configure_API_internal_database", start=date(2022,3,4), duration=4, resources=[Rohit], color="#FF00FF")
tasks_for_project_ApiPlusNewClients.append(task_Configure_API_internal_database_project_ApiPlusNewClients)

# Creating project : ApiPlusNewClients
project_ApiPlusNewClients = gantt.Project(name='ApiPlusNewClients')
for task in tasks_for_project_ApiPlusNewClients:
   project_ApiPlusNewClients.add_task(task)

# Creating tasks for project : ExistingClientsNewCodeIntegration
tasks_for_project_ExistingClientsNewCodeIntegration = []

task_Existing_client_Plan_integration_with_existing_Viteos_stack_project_ExistingClientsNewCodeIntegration = gantt.Task(name="Existing_client_Plan_integration_with_existing_Viteos_stack", start=date(2022,3,8), duration=4, resources=[Rohit, Pratik, Abhijeet, Rani, Hari, Girish], color="#D2691E")
tasks_for_project_ExistingClientsNewCodeIntegration.append(task_Existing_client_Plan_integration_with_existing_Viteos_stack_project_ExistingClientsNewCodeIntegration)

# Creating project : ExistingClientsNewCodeIntegration
project_ExistingClientsNewCodeIntegration = gantt.Project(name='ExistingClientsNewCodeIntegration')
for task in tasks_for_project_ExistingClientsNewCodeIntegration:
   project_ExistingClientsNewCodeIntegration.add_task(task)

all_projects = gantt.Project(name='All Projects')

all_projects.add_task(project_Planning)
all_projects.add_task(project_CodeDesign)
all_projects.add_task(project_CodeRefactoringTesting)
all_projects.add_task(project_ApiPlusNewClients)
all_projects.add_task(project_ExistingClientsNewCodeIntegration)
all_projects.make_svg_for_resources(filename="all_projects_timeline_final_resources_daily_scale.svg",
                                    today=date(2021,9,21),
                                    start=date(2021,9,20),
                                    end=date(2022,3,22),
                                    scale=gantt.DRAW_WITH_DAILY_SCALE)
all_projects.make_svg_for_tasks(filename="all_projects_timeline_final_tasks_daily_scale.svg",
                                    today=date(2021,9,21),
                                    start=date(2021,9,20),
                                    end=date(2022,3,22),
                                    scale=gantt.DRAW_WITH_DAILY_SCALE)
all_projects.make_svg_for_resources(filename="all_projects_timeline_final_resources_weekly_scale.svg",
                                    today=date(2021,9,21),
                                    start=date(2021,9,20),
                                    end=date(2022,6,22),
                                    scale=gantt.DRAW_WITH_WEEKLY_SCALE)
all_projects.make_svg_for_tasks(filename="all_projects_timeline_final_tasks_weekly_scale.svg",
                                    today=date(2021,9,21),
                                    start=date(2021,9,20),
                                    end=date(2022,6,22),
                                    scale=gantt.DRAW_WITH_WEEKLY_SCALE)