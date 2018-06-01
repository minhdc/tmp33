

def get_sub_sequence_in_a(input_a_part_as_list):
    seq_a1 = input_a_part_as_list[:3]
    index_of_begin_of_a3 = 0
    try:
        index_of_begin_of_a3 = input_a_part_as_list.index(88999)
    except ValueError:
        for each_element in input_a_part_as_list:
            if "88" in each_element:
                index_of_begin_of_a3 = input_a_part_as_list.index(each_element)
                break
    seq_a2 = input_a_part_as_list[3:index_of_begin_of_a3]

    index_of_begin_of_a4 = 0
    try:
        index_of_begin_of_a4 = input_a_part_as_list.index(77999)
    except ValueError:
        for each_element in input_a_part_as_list:
            if "77" in each_element:
                index_of_begin_of_a4 = input_a_part_as_list.index(each_element)
                break

    seq_a3 = input_a_part_as_list[index_of_begin_of_a3:index_of_begin_of_a4]
    seq_a4 = input_a_part_as_list[index_of_begin_of_a4:]

    list_of_sub_seq = []
    list_of_sub_seq.append(seq_a1)
    list_of_sub_seq.append(seq_a2)
    list_of_sub_seq.append(seq_a3)
    list_of_sub_seq.append(seq_a4)

    return list_of_sub_seq

