import json 
wmo_input = open("wmo_number.txt","r")

wmo_number_as_dict = {}
for line in wmo_input:
    splitted_element = (' '.join(line.split())).split(" ")
    key = splitted_element[0]
    value = splitted_element[7]
    wmo_number_as_dict [key] = value

with open('wmo_number_as_dict.txt',"w+") as wmo_number_as_file:
    wmo_number_as_file.write(json.dumps(wmo_number_as_dict))

