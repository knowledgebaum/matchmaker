import re
# file_path = 'testing_text.txt'
#
# def get_variables(file_path):
#     regex = r"([A-Z]{3,}|[A-Z]{3,} [A-Z]{3,}\(?S?\)?)(  .*$)"
#
#     mushroom_file = open(file_path, mode='r')
#     test_str = mushroom_file.read()
#
#     matches = re.finditer(regex, test_str, re.MULTILINE)
#
#
#     mushroom_regex = re.compile()
#


##2
#FORM: Term, Definition
mycology_pattern = re.compile(r"(^[A-Z]{3,} [A-Z]{3,}\(?S?\)?|^[A-Z]{3,})(.*$)?", re.MULTILINE)

#FORM: Definition
#mycology_pattern = re.compile(r"(  .*$)", re.MULTILINE)

data_file = open('testing_text.txt')
data_contents = data_file.read()
matches = re.findall(mycology_pattern, data_contents)
#mo = re.finditer(mycology_pattern, data_contents)
#mycology_data.findall(data_contents)

#print(matches)
i = 1
for match in matches:
    print(str(i) + '#####'+str(match))
    i = i + 1

inner_count = 0
myco_id_count = 1
out_count = 0
myco_dict = {}
prop_count = 0

for


for i in range(0, len(matches), 18):
    myco_dict.update({'myco_ID': myco_id_count })
    outer_count = outer_count + 1
    myco_id_count = myco_id_count + 1
    #prop_count = prop_count + 18

    ##MO1 the name
    for j in range(outer_count, outer_count+18):
        # or myco_dict.update({
        myco_dict['myco_props'].update({
        family:
        latin_name
        english_name
        notes
        chemical_reaction
        cap
        flesh
        underside
        stem
        odor
        taste
        edibility
        habitat
        spore_deposit
        microscopic
        name_origin
        similar
        sources

        } )

