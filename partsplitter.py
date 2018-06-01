



def get_splitted_part_from_raw_input(input_file_path):
    f = open(input_file_path,"r")
    content = f.read()
    splitted_part = content.split("\n\n")
    for each_part in splitted_part:
        each_part.replace("\n"," ")
    return splitted_part


def split_element_in_part(part_as_string):
    sanitized_part = part_as_string.replace("\n"," ")
    splitted_group = sanitized_part.split(" ")
    return splitted_group


def identify(input_part):
    if input_part[0] == 'TTAA':
        #call a process
        pass
    if input_part[0] == 'TTBB':
        #call a process
        pass        
    if input_part[0] == 'TTCC':
        #call a process
        pass
    if input_part[0] == 'TTDD':
        #call a process
        pass

