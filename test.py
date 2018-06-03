import json

from partsplitter import *
from partprocessor import *
from seqprocessor import *

'''
splitted_part = get_splitted_part_from_raw_input("input.txt")
for each_part in splitted_part:
    splitted_element_in_each_part = split_element_in_part(each_part)
    if splitted_element_in_each_part[0] == 'TTAA':
        print()
        print(process_seq_a1(get_sub_sequence_in_a(splitted_element_in_each_part)[0]))
    if splitted_element_in_each_part[0] == 'TTBB':
        print("this is B")
    if splitted_element_in_each_part[0] == 'TTCC':
        print("this is C")    '''

with open("wmo_number_as_dict.txt","r") as wmo_file:
    wmo_dict = json.loads(wmo_file.read())

print(wmo_dict['46811'])