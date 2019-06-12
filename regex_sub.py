import re
from pathlib import Path
import json
import os

mycology_pattern = re.compile(r"(.*\n)(FAMILY) (.*\n)(LATIN NAME\(S\)) (.*\n)(ENGLISH NAME\(S\)) (.*\n)(NOTES)"
                              r" (?:(.*\n)(CHEMICAL REACTIONS|CAP|NEST|FRUITING BODY))(?: (.*\n)((?:OUTER|UPPER)"
                              r" SURFACE|FRUITING BODY|CAP))?(?: (.*\n)(INNER (?:LAYER|SURFACE)|FLESH))?"
                              r"(?: (.*\n)(SPORE MASS|INTERIOR|UNDERSIDE|PORES|TEETH|GILLS|EGGS))? (?:(.*\n)(STEM))?"
                              r"(?: (.*\n)(VEIL))?(?: (.*\n)(ODOR) (.*\n)(TASTE))?(?: (.*\n)(EDIBILITY))?(.*\n)"
                              r"(HABITAT)(?: (.*\n)(SPORE DEPOSIT))?(.*\n)(MICROSCOPIC) (.*\n)(NAME ORIGIN)"
                              r" (.*\n)(SIMILAR) (.*\n)(SOURCES)(.*\n)", re.MULTILINE )


current_dir = os.getcwd()

origin_dir = ("C:/webDev/pycharm/matchmaker/data/origin_data")
origin_dir_list = os.listdir(origin_dir)







#SNIP POINT






def make_json_from_regex(data_list_item):

    data_path = Path(data_list_item)
    data_filename = os.path.basename(data_path)
    data_file = open(data_path)
    data_contents = data_file.read()

    matches = re.findall(mycology_pattern, data_contents)

    mush_dict ={}
    count = 1
    for match in matches:

        keys = [
                    match[1],
                    match[3],
                    match[5],
                    match[7],
                    match[9],
                    match[11],
                    match[13],
                    match[15],
                    match[17],
                    match[19],
                    match[21],
                    match[23],
                    match[25],
                    match[27],
                    match[29],
                    match[31],
                    match[33],
                    match[35],
                    match[37]
                ]
        values = [
                    match[2],
                    match[4],
                    match[6],
                    match[8],
                    match[10],
                    match[12],
                    match[14],
                    match[16],
                    match[18],
                    match[20],
                    match[22],
                    match[24],
                    match[26],
                    match[28],
                    match[30],
                    match[32],
                    match[34],
                    match[36],
                    match[38]
                ]


        # keys =  list(range(1, 38, 2))
        # values = list(range(2,38, 2))
        single_mush_dict = dict(zip(keys, values))

        ###GENERATOR
        #keys = [[n, l] for n in match]

        mush_dict.update([count, single_mush_dict])
        count = count + 1

    output_folder = Path("c:/webDev/pycharm/matchmaker/data/json")
    output_file_path = os.path.join(output_folder,data_filename)

    with open(output_file_path, 'w') as outfile:
        json.dump(mush_dict, outfile)
    mush_dict ={}
    count = 1

print(origin_dir_list)


for data_list_item in origin_dir_list:
    item = os.path.join(origin_dir,data_list_item)
    make_json_from_regex(item)



#data_path = Path("C:/webDev/pycharm/matchmaker/data/vei_origin.txt")
#data_file = open(data_path)
#data_contents = data_file.read()
#matches = re.findall(mycology_pattern, data_contents)


#   for match in matches:
#     print('####')
#     #print(match[1])
#     keys = [
#         match[1],
#         match[3],
#         match[5],
#         match[7],
#         match[9],
#         match[11],
#         match[13],
#         match[15],
#         match[17],
#         match[19],
#         match[21],
#         match[23],
#         match[25],
#         match[27],
#         match[29],
#         match[31],
#         match[33],
#         match[35],
#         match[37]
#     ]
#     values = [
#         match[2],
#         match[4],
#         match[6],
#         match[8],
#         match[10],
#         match[12],
#         match[14],
#         match[16],
#         match[18],
#         match[20],
#         match[22],
#         match[24],
#         match[26],
#         match[28],
#         match[30],
#         match[32],
#         match[34],
#         match[36],
#         match[38]
#
#     ]
#     mush_dict = dict(zip(keys,values))
#     # for group in match:
#     #     print('<<<_______>>>')
#     #     print(group)
#     print(mush_dict.keys())
#
# mush_json = json.dumps(mush_dict)
#
# with open('data.txt', 'w') as outfile:
#     json.dump(mush_dict, outfile)