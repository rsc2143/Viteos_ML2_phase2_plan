from datetime import datetime, date
import gantt
import json
class ReadTimelineJson:
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

    def read_timeline_projects(self):
        if('projects' in self.timeline_json_dict.keys()):
            print('Projects present in {self.path} file : '.format(self=self))
            list_timeline_projects = list(self.timeline_json_dict['projects'])
            for project in list_timeline_projects:
                print(project)
            return(list_timeline_projects)
        else:
            raise Exception(' No "projects" key in the {self.path} file'.format(self=self))

    def read_tasks_for_timeline_project(self, param_project = None):
        if(param_project is not None):
            if(str(param_project).strip() != ""):
                if(param_project in self.read_timeline_projects()):
                    if('tasks' in self.timeline_json_dict['projects'][param_project]):
                        print('Tasks present in {param_project} : '.format(param_project=param_project))
                        list_tasks_in_project = list(self.timeline_json_dict['projects'][param_project]['tasks'])
                        for task in list_tasks_in_project:
                            print(task)
                        return(list_tasks_in_project)
                    else:
                        raise Exception('No "tasks" key in the {param_project} project defined in {self.path} file'.format(self=self))
                else:
                    raise Exception('Project value passed in param_project argument is not present in projects defined in {self.path}'.format(self=self))
            else:
                raise Exception('Project value passed in param_project argument is empty string')
        else:
            raise Exception('Project is not passed and param_project type is the default, i.e., None')

    def check_key_present_for_project_key_combination(self, param_project = None, param_task = None,param_key = None):
        if(param_task is not None):
            if(str(param_task).strip() != ""):
                if(param_task in self.read_tasks_for_timeline_project(param_project)):
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

    def read_order_for_project_task_combination(self, param_project = None, param_task = None):
        key = check_key_present_for_project_key_combination(param_project, param_task, 'order')
        return self.timeline_json_dict['projects'][param_project]['tasks'][param_task][key]

    def get_total_order_values_in_project(self, param_project):
        order_values_list = []
        for task in self.read_tasks_for_timeline_project(param_project):
            if(task != "Total Time"):
                self.timeline_json_dict['projects'][param_project]['tasks'][task]['order']

    def read_max_duration_for_same_order_in_project_task_combination(self, param_project = None, param_task = None, )

class custom_gantt:
    def __init__():
        pass
    def read_duration(param_duration):
        pass
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
        if(param_name) != "Total Time":
            fun_task = gantt.Task(name=param_name, start=param_start, stop=param_stop, duration=param_duration, depends_of=param_depends_of, resources=param_resources, percent_done=param_percent_done, color=param_color, fullname=param_fullname, display=param_display, state=param_state)
            param_project.add_task(fun_task)
            fun_return_dict = {
                                "task":         fun_task,
                                "end_date":     fun_end_date,
                                "duration":     fun_duration}
            return fun_return_dict
