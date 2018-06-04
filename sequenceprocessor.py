import json


'''
    Part A - mandatory level below 100mb
    TTAA YYGGI IIiii 99PPP TTTDD dddff 00HHH TTTDD dddff
    92HHH TTTDD dddff 85HHH TTTDD dddff 70HHH TTTDD dddff 50HHH
    TTTDD dddff 40HHH TTTDD dddff 30HHH TTTDD dddff 25HHH TTTDD 
    dddff 20HHH TTTDD dddff 15HHH TTTDD dddff 10HHH TTTDD dddff
    88PPP TTTDD dddff 77PPP dddff...


'''



def process_seq_a1(seq_a1_as_a_list):
    '''
        a1 = TTAA YYGGI IIiii
    '''
    I = [100,200,300,400,500,700,850,1000]
    yyggi = process_yyggi(seq_a1_as_a_list[1])
    iiiii = process_iiiii(seq_a1_as_a_list[2])
    return ['TTAA',yyggi,iiiii]

'''
    Seq 1========================================================================
'''

def process_yyggi(input_yyggi):
    '''
        return pattern [day,hour,top level which wind data is include,wind_unit]
    '''
    yy =  int(input_yyggi[0:2])
    gg = int(input_yyggi[2:4])
    i = int(input_yyggi[4])
    wind_unit = "m/s"
    if yy > 50:        
        day = (yy + 50) % 100
        wind_unit = "knts" 

    i_as_dict = {1:100,2:200,3:300,4:400,5:500,6:600,7:700,8:850,0:1000}
    i = i_as_dict[i]
    return [day,gg,i,wind_unit]


def process_iiiii(input_iiiii):
    with open("wmo_number_as_dict.txt","r") as wmo_dict_file:
        wmo_dict_object = json.load(wmo_dict_file) 
        #json.load() to load a file, json.loads() to load string onlys        
    try:
        return str(wmo_dict_object[input_iiiii])
    except KeyError as e:
        print(e)
        return None

'''
    seq 2 ===========================================
'''

def process_tttdd(input_tttdd): 
    ttt = int(input_tttdd[0:3])
    dd = int(input_tttdd[3:])
    
    temperature = ttt/10
    if (ttt%10)%2 != 0:
        temperature = -temperature
    
    dewpoint = (dd+50)/10
    if dd <= 50:
        dewpoint = dd/10
    
    return [temperature,dewpoint]


def process_dddff(input_dddff):
    wind_direction = int(input_dddff[0:3])
    wind_speed = int(input_dddff[3:])

    if input_dddff[2] == '1' or input_dddff[2] == '6':
        wind_speed = wind_speed + 100
    if input_dddff[2] == '2' or input_dddff[2] == '7':
        wind_speed = wind_speed + 200
    else:
        if (wind_direction// 5 ) % 2 == 0:
            wind_speed = wind_speed + (wind_direction - (5 * (wind_direction//5)))*100

    return[wind_direction,wind_speed]        


def process_pphhh(input_pphhh):
    '''
        return pattern [pp,hhh]
    '''
    pp = int(input_pphhh[0:2])
    hhh = int(input_pphhh[2:])
    
    pp = pp * 10
    hhh_as_related_to_p_dict = {1000:hhh,920:hhh,850:hhh+1000,700:hhh+3000,500:hhh*10,
    400:hhh*10,300:hhh*10+10000,250:hhh*10+10000,200:hhh*10+10000,
    150:hhh*10+10000,100:hhh*10+10000,70:hhh*10+10000,50:hhh*10+20000,
    30:hhh*10+20000,20:hhh*10+20000,10:hhh*10+30000}

    hhh_code_check = {1000:500-hhh,700:hhh+200,300:hhh*10,250:hhh*10,
    50:hhh*10+10000,10:hhh*10+20000}
    
    if hhh >= 500:
        if pp in hhh_code_check.keys():
            hhh = hhh_code_check[pp]
        else:
            hhh = hhh_as_related_to_p_dict[pp]
    
    return [pp,hhh]


def process_99ppp(input_xxppp):
    ppp = int(input_xxppp[2:])
    if ppp < 100: 
        ppp = ppp + 1000
    return ppp


def process_seq_a2(input_seq_a2_as_list):
    xx_ppp = process_99ppp(input_seq_a2_as_list[0])
    
'''
    seq 3=============================================================
'''

def process_seq_a3(input_seq_a3_as_list):
    if len(input_seq_a3_as_list) == 1:
        return ['khong quan trac thay muc doi luu han']
    elif   len(input_seq_a3_as_list) == 3:
        ppp_88 = int(input_seq_a3_as_list[0])
        tttdd = int(input_seq_a3_as_list[1])
        ddfff = int(input_seq_a3_as_list[2])

        ppp_88 = ppp_88%1000
        if ppp_88 < 100:
            ppp_88 = ppp_88 + 1000
        tttdd = process_tttdd(tttdd)
        ddfff = process_dddff(ddfff)
        return [ppp_88,tttdd,ddfff]


'''
    seq a4 =============================================================
'''
def process_seq_a4(input_seq_a4_as_list):
    if '77999' in input_seq_a4_as_list:
        return ['khong quan trac thay muc doi luu han',input_seq_a4_as_list[1:]]
    else:
        print(input_seq_a4_as_list)


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