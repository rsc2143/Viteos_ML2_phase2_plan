from custom_gantt import ReadTimelineJson
import pprint
cs = ReadTimelineJson('timeline.json')
pprint.pprint(cs.return_new_timeline_dict_with_start_and_end_dates_2())
