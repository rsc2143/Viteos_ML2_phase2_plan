from custom_gantt import ReadTimelineJson, CustomGantt
import pprint
cs = ReadTimelineJson('timeline.json')
pprint.pprint(cs.return_new_timeline_dict_with_start_and_end_dates())

custom_gantt_obj = CustomGantt('timeline.json')
pprint.pprint(custom_gantt_obj.test_super_obj)
