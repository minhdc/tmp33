import json


def process_seq_a1(seq_a1_as_a_list):
    I = [100,200,300,400,500,700,850,1000]
    print("Ngay phat bao :",seq_a1_as_a_list[1][0:2])
    print("Gio phat bao (GMT) ",seq_a1_as_a_list[1][2:4])
    print("ap suat be mat: ")


def process_yygg(input_yyggi):
    yy = input_yyggi[0:2]
    gg = input_yyggi[2:4]
    if yy > 50:
        print("winds are in knts")
        day = (yy + 50) % 10
        print("...Ngay %r"%(day))
    

def process_iiiii(input_iiiii):
    with open("wmo_number_as_dict.txt","r") as wmo_dict_file:
        wmo_dict_object = json.loads(wmo_dict_file)
    try:
        return wmo_dict_object[input_iiiii]
    except KeyError as e:
        print(e)
        return None


def process_tttdd(input_tttdd): 
    ttt = int(input_tttdd[0:2])
    dd = int(input_tttdd[2:])
    
    temperature = ttt/10
    if (ttt/100)%2 != 0:
        temperature = -temperature
    
    dewpoint = (dd+50)/10
    if dd <= 50:
        dewpoint = dd/10
    
    return [temperature,dewpoint]


def process_dddff(input_dddff):
    pass


def check_missing(input_text,length):
    if length == 1:
        if input_text == '/':
            return ".. missing .."
    if length == 2:
        if input_text == '//':
            return ".. missing .."
    if length == 3:
        if input_text == '///':
            return ".. missing .."            
    return False