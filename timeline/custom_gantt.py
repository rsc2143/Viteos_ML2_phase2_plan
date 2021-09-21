from datetime import datetime, date, timedelta
import gantt
import json
import os
class ReadTimelineJson:
    time_continued_values_list = ["False, take from ML2_Phase2_start_date",
                                  "First task encountered in task order",
                                  "True, take from lastest task in previous order",
                                  "True, take from lastest project"]

    def __init__(self, param_json_filepath = None):
        self.path = param_json_filepath
        if(self.path is not None):
            if(str(self.path.strip()) != ""):
                try:
                    with open(self.path, 'r') as timeline_json_open_obj:
                        timeline_json_data = timeline_json_open_obj.read()
                    self.timeline_json_dict = json.loads(timeline_json_data)
                except:
                    raise Exception('Cannot read json file given in param_json_filepath')
            else:
                raise Exception('param_json_filepath is empty string')
        else:
            raise Exception('param_json_filepath is None')

    def return_all_timeline_projects(self):
        if('projects' in self.timeline_json_dict.keys()):
            # print('Projects present in {self.path} file : '.format(self=self))
            list_timeline_projects = list(self.timeline_json_dict['projects'])
            # for project in list_timeline_projects:
                # print(project)
            return(list_timeline_projects)
        else:
            raise Exception(' No "projects" key in the {self.path} file'.format(self=self))

    def return_all_tasks_for_single_project(self, param_project = None):
        if(param_project is not None):
            if(str(param_project).strip() != ""):
                if(param_project in self.return_all_timeline_projects()):
                    if('tasks' in self.timeline_json_dict['projects'][param_project]):
                        # print('Tasks present in {param_project} : '.format(param_project=param_project))
                        list_tasks_in_project = list(self.timeline_json_dict['projects'][param_project]['tasks'])
                        # for task in list_tasks_in_project:
                            # print(task)
                        return(list_tasks_in_project)
                    else:
                        raise Exception('No "tasks" key in the {param_project} project defined in {self.path} file'.format(self=self))
                else:
                    raise Exception('Project value passed in param_project argument is not present in projects defined in {self.path}'.format(self=self))
            else:
                raise Exception('Project value passed in param_project argument is empty string')
        else:
            raise Exception('Project is not passed and param_project type is the default, i.e., None')

    def return_tasks_only_for_single_task_order_inside_project(self, param_project, param_task_order):
        if(param_project is not None):
            if(str(param_project).strip() != ""):
                if(param_project in self.return_all_timeline_projects()):
                    if('tasks' in self.timeline_json_dict['projects'][param_project]):
                        task_list_to_return = []
                        for task in self.timeline_json_dict['projects'][param_project]['tasks']:
                            if(self.timeline_json_dict['projects'][param_project]['tasks'][task]['order'] == param_task_order):
                                task_list_to_return.append(task)
                            else:
                                continue
                        return(task_list_to_return)
                    else:
                        raise Exception('No "tasks" key in the {param_project} project defined in {self.path} file'.format(self=self))

                else:
                    raise Exception('Project value passed in param_project argument is not present in projects defined in {self.path}'.format(self=self))
            else:
                raise Exception('Project value passed in param_project argument is empty string')
        else:
            raise Exception('Project is not passed and param_project type is the default, i.e., None')

    def return_all_resources(self):
        resources_list = []
        for project in self.return_all_timeline_projects():
            for task in self.return_all_tasks_for_single_project(project):
                single_task_resources_list = self.timeline_json_dict['projects'][project]['tasks'][task]['resources']
                resources_list.append(single_task_resources_list)
        resources_set = set()
        for resource_list in resources_list:
            for resource in resource_list:
                resources_set.add(resource)
        return list(resources_set)

    def check_key_present_for_project_task_key_combination(self, param_project = None, param_task = None,param_key = None):
        if(param_task is not None):
            if(str(param_task).strip() != ""):
                if(param_task in self.return_all_tasks_for_single_project(param_project)):
                    if(param_key is not None):
                        if(str(param_key).strip() != ""):
                            if(param_key in self.timeline_json_dict['projects'][param_project]['tasks'][param_task]):
                                return param_key
                            else:
                                raise Exception('Key passed in param_key is not present in keys for the {param_project}{param_task} combination'.format(param_project=param_project, param_task=param_task))
                        else:
                            raise Exception('Key passed in param_key argument is empty string')
                    else:
                        raise Exception('Key is not passed and param_key type is the default, i.e., None')
                else:
                    raise Exception('Task value passed in param_task is not present in tasks for the {param_project} project'.format(param_project=param_project))
            else:
                raise Exception('Task value passed in param_task argument is empty string')
        else:
            raise Exception('Task is not passed and param_task type is the default, i.e., None')

    def check_key_present_for_project_key_combination(self, param_project = None,param_key = None):
        if(param_project is not None):
            if(str(param_project).strip() != ""):
                if(param_project in self.return_all_timeline_projects()):
                    if(param_key is not None):
                        if(str(param_key).strip() != ""):
                            if(param_key in self.timeline_json_dict['projects'][param_project]):
                                return param_key
                                return param_key
                            else:
                                raise Exception('Key passed in param_key is not present in keys for the {param_project}{param_task} combination'.format(param_project=param_project, param_task=param_task))
                        else:
                            raise Exception('Key passed in param_key argument is empty string')
                    else:
                        raise Exception('Key is not passed and param_key type is the default, i.e., None')
                else:
                    raise Exception('Task value passed in param_task is not present in tasks for the {param_project} project'.format(param_project=param_project))
            else:
                raise Exception('Project value passed in param_project argument is empty string')
        else:
            raise Exception('Project is not passed and param_project type is the default, i.e., None')

    def read_order_for_project_task_combination(self, param_project = None, param_task = None):
        key = check_key_present_for_project_task_key_combination(param_project, param_task, 'order')
        return self.timeline_json_dict['projects'][param_project]['tasks'][param_task][key]

    def read_order_for_project(self, param_project = None):
        key = check_key_present_for_project_key_combination(param_project, 'order')
        return self.timeline_json_dict['projects'][param_project][key]

    def get_total_order_values_in_project(self, param_project):
        order_values_list = []
        for task in self.return_all_tasks_for_single_project(param_project):
            order_values_list.append(self.timeline_json_dict['projects'][param_project]['tasks'][task]['order'])
        return(order_values_list)

    def read_max_duration_for_same_order_in_project_task_combination(self, param_project = None, param_order = None):
        # unique_order_values_list = list(set(self.get_total_order_values_in_project(param_project)))
        duration = {0}
        if(param_order is not None):
            for task in self.return_all_tasks_for_single_project(param_project):
                if('order' in self.timeline_json_dict['projects'][param_project]['tasks'][task]):
                    if(param_order == self.timeline_json_dict['projects'][param_project]['tasks'][task]['order']):
                        duration.add(self.timeline_json_dict['projects'][param_project]['tasks'][task]['duration'])
                else:
                    print('Key names "order" not present in Task = {task} for Project = {param_project}. Skipping {task} task'.format(task=task, param_project=param_project))
            if(duration != {0}):
                return max(duration)
            else:
                raise Exception('Either no duration found for {param_project, param_object} combination, or duration variable is explicitely kept equal to 0. Exiting code dur to logical error')
        else:
            raise Exception('Order value is not passed and param_order type is the default, i.e., None')

    def return_datetime_value_for_str_date(self, param_date_in_str = None, param_date_in_str_format = "%d-%m-%Y"):
        if(param_date_in_str is not None):
            if(str(param_date_in_str).strip() != ""):
                return datetime.date(datetime.strptime(param_date_in_str, param_date_in_str_format))
            else:
                raise Exception('Date value passed in param_date_in_str argument is empty string')
        else:
            raise Exception('Date is not passed and param_date_in_str type is the default, i.e., None')

    def return_datetime_value_for_startdate_enddate_based_on_timecontinued_and_duration(self, param_time_continued = None, param_duration_to_add_to_get_end_date = None, param_duration_to_add_to_get_start_date = None, param_date_to_start_from_in_datetime_format = None):
        if(param_time_continued is not None):
            if(str(param_time_continued).strip() != ""):
                if(param_time_continued == "False, take from ML2_Phase2_start_date" or param_time_continued == "False"):
                    start_date = self.return_datetime_value_for_str_date(self.timeline_json_dict["ML2_Phase2_start_date"])
                    end_date = start_date + timedelta(days=param_duration_to_add_to_get_end_date)
                # elif(param_time_continued == "First task encountered in task order" or param_time_continued == "True, take from lastest task in previous order" or param_time_continued == "True, take from lastest project" or param_time_continued == "True"):
                else:
                    if(param_date_to_start_from_in_datetime_format is not None):
                        if(isinstance(param_date_to_start_from_in_datetime_format,datetime) == True or isinstance(param_date_to_start_from_in_datetime_format,date) == True):
                            start_date =  param_date_to_start_from_in_datetime_format + timedelta(days=param_duration_to_add_to_get_start_date)
                            end_date = start_date + timedelta(days=param_duration_to_add_to_get_end_date)
                        else:
                            print(type(param_date_to_start_from_in_datetime_format))
                            raise Exception('End Date to start from value passed in param_date_to_start_from_in_datetime_format argument is supposed to be datetime, but format of variable passed is not datetime')
                    else:
                        raise Exception('End Date to start from value is not passed and param_date_to_start_from_in_datetime_format type is the default, i.e., None')
            else:
                raise Exception('Time Continued value passed in param_time_continued argument is empty string')
        else:
            raise Exception('Time Continued value is not passed and param_time_continued type is the default, i.e., None')
        return(start_date, end_date)

    def return_all_project_orders(self):
        all_project_order_set = set()
        for project in self.return_all_timeline_projects():
            all_project_order_set.add(self.timeline_json_dict['projects'][project][self.check_key_present_for_project_key_combination(param_project = project, param_key = 'order')])
        return list(all_project_order_set)

    def return_all_task_orders_in_single_project(self, param_project):
        all_task_order_set = set()
        for task in self.return_all_tasks_for_single_project(param_project):
            all_task_order_set.add(self.timeline_json_dict['projects'][param_project][self.check_key_present_for_project_key_combination(param_project = param_project, param_key = 'tasks')][task][self.check_key_present_for_project_task_key_combination(param_project = param_project, param_task = task, param_key = 'order')])
        return list(all_task_order_set)



    def return_new_timeline_dict_with_start_and_end_dates(self):
        new_timeline_dict = self.timeline_json_dict
        project_start_date = None
        for project_order in sorted(self.return_all_project_orders()):
            for project in self.timeline_json_dict['projects']:
                if(project_order == self.timeline_json_dict['projects'][project][self.check_key_present_for_project_key_combination(param_project = project, param_key = 'order')]):
                    for task_order in self.return_all_task_orders_in_single_project(project):
                        timecontinued_for_same_task_order = "First task encountered in task order"

                        for task in self.return_tasks_only_for_single_task_order_inside_project(param_project = project, param_task_order = task_order):

                            if(task_order == self.timeline_json_dict['projects'][project]['tasks'][task][self.check_key_present_for_project_task_key_combination(param_project=project, param_task=task, param_key='order')]):
                                if((project_order == 1) & (task_order == 1)):
                                    if((timecontinued_for_same_task_order == "First task encountered in task order") & (self.timeline_json_dict['projects'][project]['tasks'][task][self.check_key_present_for_project_task_key_combination(param_project=project, param_task=task, param_key='time_continued')] == "False, take from ML2_Phase2_start_date")):
                                        task_order_start_date_list = []
                                        task_order_end_date_list = []
                                        temp_start_date, temp_end_date = self.return_datetime_value_for_startdate_enddate_based_on_timecontinued_and_duration(param_time_continued = self.timeline_json_dict['projects'][project]['tasks'][task][self.check_key_present_for_project_task_key_combination(param_project=project, param_task=task, param_key='time_continued')],
                                                                                                                                                              param_duration_to_add_to_get_end_date = self.timeline_json_dict['projects'][project]['tasks'][task][self.check_key_present_for_project_task_key_combination(param_project=project, param_task=task, param_key='duration')])
                                        new_timeline_dict['projects'][project]['tasks'][task]['start_date'] = temp_start_date
                                        new_timeline_dict['projects'][project]['tasks'][task]['end_date'] = temp_end_date
                                        task_order_start_date_list.append(temp_start_date)
                                        task_order_end_date_list.append(temp_end_date)
                                        timecontinued_for_same_task_order = self.timeline_json_dict['projects'][project]['tasks'][task][self.check_key_present_for_project_task_key_combination(param_project=project, param_task=task, param_key='time_continued')]
                                    elif(timecontinued_for_same_task_order == self.timeline_json_dict['projects'][project]['tasks'][task][self.check_key_present_for_project_task_key_combination(param_project=project, param_task=task, param_key='time_continued')]):
                                        temp_start_date, temp_end_date = self.return_datetime_value_for_startdate_enddate_based_on_timecontinued_and_duration(param_time_continued = self.timeline_json_dict['projects'][project]['tasks'][task][self.check_key_present_for_project_task_key_combination(param_project=project, param_task=task, param_key='time_continued')],
                                                                                                                                                              param_duration_to_add_to_get_end_date = self.timeline_json_dict['projects'][project]['tasks'][task][self.check_key_present_for_project_task_key_combination(param_project=project, param_task=task, param_key='duration')])
                                        new_timeline_dict['projects'][project]['tasks'][task]['start_date'] = temp_start_date
                                        new_timeline_dict['projects'][project]['tasks'][task]['end_date'] = temp_end_date
                                        task_order_start_date_list.append(temp_start_date)
                                        task_order_end_date_list.append(temp_end_date)
                                        timecontinued_for_same_task_order = self.timeline_json_dict['projects'][project]['tasks'][task][self.check_key_present_for_project_task_key_combination(param_project=project, param_task=task, param_key='time_continued')]

                                    else:
                                        raise Exception("project = {project} and task = {task} can only have time_continued = 'False, take from ML2_Phase2_start_date' since project order == 1 and task order == 1 can only start from ML2_Phase2_start_date".format(project=project, task=task))
                                    task_order_end_date_to_pass_on = max(task_order_end_date_list)
                                elif((project_order != 1) & (task_order == 1)):
                                    if((timecontinued_for_same_task_order == "First task encountered in task order") & (self.timeline_json_dict['projects'][project]['tasks'][task][self.check_key_present_for_project_task_key_combination(param_project=project, param_task=task, param_key='time_continued')] == "True, take from lastest project")):
                                        task_order_start_date_list = []
                                        task_order_end_date_list = [project_order_end_date_to_pass_on]
                                        temp_start_date, temp_end_date = self.return_datetime_value_for_startdate_enddate_based_on_timecontinued_and_duration(param_time_continued = self.timeline_json_dict['projects'][project]['tasks'][task][self.check_key_present_for_project_task_key_combination(param_project=project, param_task=task, param_key='time_continued')],
                                                                                                                                                              param_duration_to_add_to_get_end_date = self.timeline_json_dict['projects'][project]['tasks'][task][self.check_key_present_for_project_task_key_combination(param_project=project, param_task=task, param_key='duration')],
                                                                                                                                                              # param_duration_to_add_to_get_start_date = self.read_max_duration_for_same_order_in_project_task_combination(param_project = project, param_order = task_order),
                                                                                                                                                              param_duration_to_add_to_get_start_date = 0,
                                                                                                                                                              param_date_to_start_from_in_datetime_format = max(task_order_end_date_list))
                                        new_timeline_dict['projects'][project]['tasks'][task]['start_date'] = temp_start_date
                                        new_timeline_dict['projects'][project]['tasks'][task]['end_date'] = temp_end_date
                                        task_order_start_date_list.append(temp_start_date)
                                        task_order_end_date_list.append(temp_end_date)
                                        timecontinued_for_same_task_order = self.timeline_json_dict['projects'][project]['tasks'][task][self.check_key_present_for_project_task_key_combination(param_project=project, param_task=task, param_key='time_continued')]
                                    elif(timecontinued_for_same_task_order == self.timeline_json_dict['projects'][project]['tasks'][task][self.check_key_present_for_project_task_key_combination(param_project=project, param_task=task, param_key='time_continued')]):
                                        temp_start_date, temp_end_date = self.return_datetime_value_for_startdate_enddate_based_on_timecontinued_and_duration(param_time_continued = self.timeline_json_dict['projects'][project]['tasks'][task][self.check_key_present_for_project_task_key_combination(param_project=project, param_task=task, param_key='time_continued')],
                                                                                                                                                              param_duration_to_add_to_get_end_date = self.timeline_json_dict['projects'][project]['tasks'][task][self.check_key_present_for_project_task_key_combination(param_project=project, param_task=task, param_key='duration')],
                                                                                                                                                              # param_duration_to_add_to_get_start_date = self.read_max_duration_for_same_order_in_project_task_combination(param_project = project, param_order = task_order),
                                                                                                                                                              param_duration_to_add_to_get_start_date = 0,
                                                                                                                                                              param_date_to_start_from_in_datetime_format = min(task_order_start_date_list))
                                        new_timeline_dict['projects'][project]['tasks'][task]['start_date'] = temp_start_date
                                        new_timeline_dict['projects'][project]['tasks'][task]['end_date'] = temp_end_date
                                        task_order_start_date_list.append(temp_start_date)
                                        task_order_end_date_list.append(temp_end_date)
                                        timecontinued_for_same_task_order = self.timeline_json_dict['projects'][project]['tasks'][task][self.check_key_present_for_project_task_key_combination(param_project=project, param_task=task, param_key='time_continued')]

                                    else:
                                        raise Exception("project = {project} and task = {task} can only have time_continued = 'True, take from lastest project' since project order == 1 and task order == 1 can only start from ML2_Phase2_start_date".format(project=project, task=task))
                                    task_order_end_date_to_pass_on = max(task_order_end_date_list)
                                else:
                                    if(timecontinued_for_same_task_order == "First task encountered in task order"):
                                        task_order_start_date_list = []
                                        task_order_end_date_list = [task_order_end_date_to_pass_on]
                                        temp_start_date, temp_end_date = self.return_datetime_value_for_startdate_enddate_based_on_timecontinued_and_duration(param_time_continued = self.timeline_json_dict['projects'][project]['tasks'][task][self.check_key_present_for_project_task_key_combination(param_project=project, param_task=task, param_key='time_continued')],
                                                                                                                                                              param_duration_to_add_to_get_end_date = self.timeline_json_dict['projects'][project]['tasks'][task][self.check_key_present_for_project_task_key_combination(param_project=project, param_task=task, param_key='duration')],
                                                                                                                                                              # param_duration_to_add_to_get_start_date = self.read_max_duration_for_same_order_in_project_task_combination(param_project = project, param_order = task_order),
                                                                                                                                                              param_duration_to_add_to_get_start_date = 0,
                                                                                                                                                              param_date_to_start_from_in_datetime_format = max(task_order_end_date_list))
                                        new_timeline_dict['projects'][project]['tasks'][task]['start_date'] = temp_start_date
                                        new_timeline_dict['projects'][project]['tasks'][task]['end_date'] = temp_end_date
                                        task_order_start_date_list.append(temp_start_date)
                                        task_order_end_date_list.append(temp_end_date)
                                    elif(timecontinued_for_same_task_order == self.timeline_json_dict['projects'][project]['tasks'][task][self.check_key_present_for_project_task_key_combination(param_project=project, param_task=task, param_key='time_continued')]):
                                        temp_start_date, temp_end_date = self.return_datetime_value_for_startdate_enddate_based_on_timecontinued_and_duration(param_time_continued = self.timeline_json_dict['projects'][project]['tasks'][task][self.check_key_present_for_project_task_key_combination(param_project=project, param_task=task, param_key='time_continued')],
                                                                                                                                                              param_duration_to_add_to_get_end_date = self.timeline_json_dict['projects'][project]['tasks'][task][self.check_key_present_for_project_task_key_combination(param_project=project, param_task=task, param_key='duration')],
                                                                                                                                                              # param_duration_to_add_to_get_start_date = self.read_max_duration_for_same_order_in_project_task_combination(param_project = project, param_order = task_order),
                                                                                                                                                              param_duration_to_add_to_get_start_date = 0,
                                                                                                                                                              param_date_to_start_from_in_datetime_format = min(task_order_start_date_list))
                                        new_timeline_dict['projects'][project]['tasks'][task]['start_date'] = temp_start_date
                                        new_timeline_dict['projects'][project]['tasks'][task]['end_date'] = temp_end_date
                                        task_order_start_date_list.append(temp_start_date)
                                        task_order_end_date_list.append(temp_end_date)


                                    timecontinued_for_same_task_order = self.timeline_json_dict['projects'][project]['tasks'][task][self.check_key_present_for_project_task_key_combination(param_project=project, param_task=task, param_key='time_continued')]
                                    task_order_end_date_to_pass_on = max(task_order_end_date_list)

                project_order_end_date_to_pass_on = max(task_order_end_date_list)

        return new_timeline_dict, project_order_end_date_to_pass_on

# pseudocode to get start and end date for each task within a project
# 1. go inside task with a loop for each task based on order
# 2. if project order == 1,
#     check that time_continued cannot be anything except "False, take from ML2_Phase2_start_date" or "True, take from lastest task"
#     if task order == 1,
#         i. start date = ML2_Phase2_start_date
#         ii. end date = start_date + max duration for that task order
#         iii. store end date in temp date variable which will become start date for next task order
#         iv. Check that time_continued cannot be anything except "False, take from ML2_Phase2_start_date"
#     3. 1 < task order < max task order within project, then
#         i. if time_continued == "False, take from ML2_Phase2_start_date"
#             a. start date = ML2_Phase2_start_date
#             b. end date = max duration for that task order
#             c. store end date in temp date variable which will become start date for next task order
#         i. start date = last task order end date
#         ii. end date = start date + max duration for that task order
#     4. if project order == 1, task order == max task order within project, then
#         i. repeat 3.i and 3.ii
#         ii. store end date in temp date variable which will become start date for next project order
#
#     5. if project order > 1, task order == 1,
#         i. start date = last project and task order end date
#         ii. end date = start date + max duration for that task order
#     6. if project order > 1 and task order > 1
#         i. 3i and 3ii


class CustomGantt(ReadTimelineJson):
    def __init__(self, param_json_filepath, param_python_file_filepath_to_append_to, param_all_projects_svg_filepath):
        super().__init__(param_json_filepath)
        if(param_python_file_filepath_to_append_to is not None):
            if(param_python_file_filepath_to_append_to.strip() != ""):

                self.filepath_to_append_to = param_python_file_filepath_to_append_to
                if os.path.isfile(self.filepath_to_append_to) or os.path.islink(self.filepath_to_append_to):
                    os.remove(self.filepath_to_append_to)  # remove the file
            else:
                raise Exception("param_python_file_filepath_to_append_to is empty string. Please give a value")
        else:
            raise Exception("param_python_file_filepath_to_append_to is left empty. Please give a string value as param_python_file_filepath_to_append_to cannot be left empty")
        if(param_all_projects_svg_filepath is not None):
            if(param_all_projects_svg_filepath.strip() != ""):
                self.all_projects_svg_filepath = param_all_projects_svg_filepath
            else:
                raise Exception("param_all_projects_svg_filepath is empty string. Please give a value")
        else:
            raise Exception("param_all_projects_svg_filepath is left empty. Please give a string value as param_all_projects_svg_filepath cannot be left empty")
        self.new_timeline_dict_from_super, self.all_projects_end_date = super().return_new_timeline_dict_with_start_and_end_dates()
        self.all_projects_start_date = self.return_datetime_value_for_str_date(self.new_timeline_dict_from_super["ML2_Phase2_start_date"])
        self.all_projects_today_date = date.today()

        self.all_projects_end_date = self.all_projects_end_date + timedelta(days=10)

        self.all_projects_end_date_year, self.all_projects_end_date_month, self.all_projects_end_date_day, = self.all_projects_end_date.year, self.all_projects_end_date.month, self.all_projects_end_date.day
        self.all_projects_start_date_year, self.all_projects_start_date_month, self.all_projects_start_date_day, = self.all_projects_start_date.year, self.all_projects_start_date.month, self.all_projects_start_date.day
        self.all_projects_today_date_year, self.all_projects_today_date_month, self.all_projects_today_date_day, = self.all_projects_today_date.year, self.all_projects_today_date.month, self.all_projects_today_date.day

    def write_string_text_for_import_statements(self, param_import_statement_list):
        file_to_write = open(self.filepath_to_append_to,"a")
        file_to_write.write("\n")
        file_to_write.write("# Import Statements")
        file_to_write.write("\n")
        for import_statement in param_import_statement_list:
            file_to_write.write(import_statement)
            file_to_write.write("\n")
        file_to_write.write("\n")

    def write_string_text_for_resources(self):
        file_to_write = open(self.filepath_to_append_to,"a")
        file_to_write.write("\n")
        file_to_write.write("# Creating Resources")
        file_to_write.write("\n")
        for resource_name in self.return_all_resources():
            file_to_write.write("{resource_name} = gantt.Resource(\"{resource_name}\")\n".format(resource_name=resource_name))
        file_to_write.write("\n")

    def create_tasks_for_project(self, param_project_name):
        file_to_write = open(self.filepath_to_append_to,"a")
        file_to_write.write("\n")
        file_to_write.write("# Creating tasks for project : {param_project_name}".format(param_project_name=param_project_name))
        file_to_write.write("\n")
        file_to_write.write("tasks_for_project_{format_param_project_name} = []".format(format_param_project_name=param_project_name))
        file_to_write.write("\n")

        project_color = self.new_timeline_dict_from_super['projects'][param_project_name]['color']
        for task in self.return_all_tasks_for_single_project(param_project_name):
            task_name = task
            task_dict = self.new_timeline_dict_from_super['projects'][param_project_name]['tasks'][task]
            task_start_date = task_dict['start_date']
            task_start_date_year = task_start_date.year
            task_start_date_month = task_start_date.month
            task_start_date_day = task_start_date.day

            task_end_date = task_dict['end_date']
            task_duration = task_dict['duration']
            task_resources = task_dict['resources']
            file_to_write.write("\n")
            file_to_write.write("task_{format_task_name}_project_{format_param_project_name} = gantt.Task(name=\"{format_task_name}\", start=date({format_task_start_date_year},{format_task_start_date_month},{format_task_start_date_day}), duration={format_task_duration}, resources={format_task_resources}, color=\"{format_project_color}\")".format(format_task_name=task_name,
                                                                                                                                                                                                                                                             format_param_project_name=param_project_name,
                                                                                                                                                                                                                                                             format_task_start_date_year=task_start_date_year,
                                                                                                                                                                                                                                                             format_task_start_date_month=task_start_date_month,
                                                                                                                                                                                                                                                             format_task_start_date_day=task_start_date_day,
                                                                                                                                                                                                                                                             format_task_duration=task_duration,
                                                                                                                                                                                                                                                             format_task_resources=task_resources,
                                                                                                                                                                                                                                                             format_project_color=project_color).replace("'",""))

            file_to_write.write("\n")
            file_to_write.write("tasks_for_project_{format_param_project_name}.append(task_{format_task_name}_project_{format_param_project_name})".format(format_param_project_name=param_project_name,
                                                                                                                                                           format_task_name=task_name))
            file_to_write.write("\n")

        file_to_write.write("\n")
        file_to_write.write("# Creating project : {format_param_project_name}".format(format_param_project_name=param_project_name))
        file_to_write.write("\n")
        file_to_write.write("project_{format_param_project_name} = gantt.Project(name='{format_param_project_name}')".format(format_param_project_name=param_project_name))
        file_to_write.write("\n")
        file_to_write.write("for task in tasks_for_project_{format_param_project_name}:".format(format_param_project_name=param_project_name))
        file_to_write.write("\n")
        file_to_write.write("   project_{format_param_project_name}.add_task(task)".format(format_param_project_name=param_project_name))
        file_to_write.write("\n")

    def create_all_projects(self):
        file_to_write = open(self.filepath_to_append_to,"a")
        file_to_write.write("\n")
        file_to_write.write("all_projects = gantt.Project(name='All Projects')")
        file_to_write.write("\n")

        for project in self.return_all_timeline_projects():
            self.create_tasks_for_project(project)
            file_to_write.write("\n")
            file_to_write.write("all_projects.add_task(project_{format_project_name})".format(format_project_name=project))

        file_to_write.write("\n")
        file_to_write.write("all_projects.make_svg_for_resources(filename=\"{format_all_projects_svg_filepath}_resources_daily_scale.svg\",\n".format(format_all_projects_svg_filepath=self.all_projects_svg_filepath))
        file_to_write.write("                                    today=date({format_all_projects_today_date_year},{format_all_projects_today_date_month},{format_all_projects_today_date_day}),\n".format(format_all_projects_today_date_year=self.all_projects_today_date_year,
                                                                                                                                                                         format_all_projects_today_date_month=self.all_projects_today_date_month,
                                                                                                                                                                         format_all_projects_today_date_day=self.all_projects_today_date_day))
        file_to_write.write("                                    start=date({format_all_projects_start_date_year},{format_all_projects_start_date_month},{format_all_projects_start_date_day}),\n".format(format_all_projects_start_date_year=self.all_projects_start_date_year,
                                                                                                                                                                         format_all_projects_start_date_month=self.all_projects_start_date_month,
                                                                                                                                                                         format_all_projects_start_date_day=self.all_projects_start_date_day))
        file_to_write.write("                                    end=date({format_all_projects_end_date_year},{format_all_projects_end_date_month},{format_all_projects_end_date_day}),\n".format(format_all_projects_end_date_year=self.all_projects_end_date_year,
                                                                                                                                                                         format_all_projects_end_date_month=self.all_projects_end_date_month,
                                                                                                                                                                         format_all_projects_end_date_day=self.all_projects_end_date_day))
        file_to_write.write("                                    scale=gantt.DRAW_WITH_DAILY_SCALE)")

        file_to_write.write("\n")
        file_to_write.write("all_projects.make_svg_for_tasks(filename=\"{format_all_projects_svg_filepath}_tasks_daily_scale.svg\",\n".format(format_all_projects_svg_filepath=self.all_projects_svg_filepath))
        file_to_write.write("                                    today=date({format_all_projects_today_date_year},{format_all_projects_today_date_month},{format_all_projects_today_date_day}),\n".format(format_all_projects_today_date_year=self.all_projects_today_date_year,
                                                                                                                                                                         format_all_projects_today_date_month=self.all_projects_today_date_month,
                                                                                                                                                                         format_all_projects_today_date_day=self.all_projects_today_date_day))
        file_to_write.write("                                    start=date({format_all_projects_start_date_year},{format_all_projects_start_date_month},{format_all_projects_start_date_day}),\n".format(format_all_projects_start_date_year=self.all_projects_start_date_year,
                                                                                                                                                                         format_all_projects_start_date_month=self.all_projects_start_date_month,
                                                                                                                                                                         format_all_projects_start_date_day=self.all_projects_start_date_day))
        file_to_write.write("                                    end=date({format_all_projects_end_date_year},{format_all_projects_end_date_month},{format_all_projects_end_date_day}),\n".format(format_all_projects_end_date_year=self.all_projects_end_date_year,
                                                                                                                                                                         format_all_projects_end_date_month=self.all_projects_end_date_month,
                                                                                                                                                                         format_all_projects_end_date_day=self.all_projects_end_date_day))
        file_to_write.write("                                    scale=gantt.DRAW_WITH_DAILY_SCALE)")
        file_to_write.write("\n")
        file_to_write.write("all_projects.make_svg_for_resources(filename=\"{format_all_projects_svg_filepath}_resources_weekly_scale.svg\",\n".format(format_all_projects_svg_filepath=self.all_projects_svg_filepath))
        file_to_write.write("                                    today=date({format_all_projects_today_date_year},{format_all_projects_today_date_month},{format_all_projects_today_date_day}),\n".format(format_all_projects_today_date_year=self.all_projects_today_date_year,
                                                                                                                                                                         format_all_projects_today_date_month=self.all_projects_today_date_month,
                                                                                                                                                                         format_all_projects_today_date_day=self.all_projects_today_date_day))
        file_to_write.write("                                    start=date({format_all_projects_start_date_year},{format_all_projects_start_date_month},{format_all_projects_start_date_day}),\n".format(format_all_projects_start_date_year=self.all_projects_start_date_year,
                                                                                                                                                                         format_all_projects_start_date_month=self.all_projects_start_date_month,
                                                                                                                                                                         format_all_projects_start_date_day=self.all_projects_start_date_day))
        file_to_write.write("                                    end=date({format_all_projects_end_date_year},{format_all_projects_end_date_month},{format_all_projects_end_date_day}),\n".format(format_all_projects_end_date_year=self.all_projects_end_date_year,
                                                                                                                                                                         format_all_projects_end_date_month=self.all_projects_end_date_month+3,
                                                                                                                                                                         format_all_projects_end_date_day=self.all_projects_end_date_day))
        file_to_write.write("                                    scale=gantt.DRAW_WITH_WEEKLY_SCALE)")
        file_to_write.write("\n")
        file_to_write.write("all_projects.make_svg_for_tasks(filename=\"{format_all_projects_svg_filepath}_tasks_weekly_scale.svg\",\n".format(format_all_projects_svg_filepath=self.all_projects_svg_filepath))
        file_to_write.write("                                    today=date({format_all_projects_today_date_year},{format_all_projects_today_date_month},{format_all_projects_today_date_day}),\n".format(format_all_projects_today_date_year=self.all_projects_today_date_year,
                                                                                                                                                                         format_all_projects_today_date_month=self.all_projects_today_date_month,
                                                                                                                                                                         format_all_projects_today_date_day=self.all_projects_today_date_day))
        file_to_write.write("                                    start=date({format_all_projects_start_date_year},{format_all_projects_start_date_month},{format_all_projects_start_date_day}),\n".format(format_all_projects_start_date_year=self.all_projects_start_date_year,
                                                                                                                                                                         format_all_projects_start_date_month=self.all_projects_start_date_month,
                                                                                                                                                                         format_all_projects_start_date_day=self.all_projects_start_date_day))
        file_to_write.write("                                    end=date({format_all_projects_end_date_year},{format_all_projects_end_date_month},{format_all_projects_end_date_day}),\n".format(format_all_projects_end_date_year=self.all_projects_end_date_year,
                                                                                                                                                                         format_all_projects_end_date_month=self.all_projects_end_date_month+3,
                                                                                                                                                                         format_all_projects_end_date_day=self.all_projects_end_date_day))
        file_to_write.write("                                    scale=gantt.DRAW_WITH_WEEKLY_SCALE)")

# End of class CustomGantt
if __name__ == '__main__':
    from custom_gantt import ReadTimelineJson, CustomGantt
    import pprint

    custom_gantt_obj = CustomGantt('timeline_final.json', 'custom_gantt_task_final.py', 'all_projects_timeline_final')
    import_statement_list = ["import gantt","from datetime import date"]
    py_file_to_execute_name = 'custom_gantt_py_file.py'
    custom_gantt_obj.write_string_text_for_import_statements(import_statement_list)
    custom_gantt_obj.write_string_text_for_resources()
    # custom_gantt_obj.create_tasks_for_project("permission_access")
    custom_gantt_obj.create_all_projects()
