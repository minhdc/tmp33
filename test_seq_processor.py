import unittest

from sequenceprocessor import *

def test_process_dddfff():
    assert process_dddff('21001') == [210,1]

def test_process_tttdd():
    assert process_tttdd('26816') == [26.8,1.6]

def test_process_iiiii():
    assert process_iiiii('46810') == "DONGSHA_(=597920)"

def test_process_yyggi():
    assert process_yyggi('74001') == [24,0,100,"knts"]

def test_process_pphhh():
    assert process_pphhh('50586') == [500,5860]

def test_process_seq_a1():
    assert process_seq_a1(['TTAA','74001','46810']) == ['TTAA',[24,0,100,"knts"],"DONGSHA_(=597920)"]

print(test_process_dddfff())
print(test_process_tttdd())
print(test_process_iiiii())
print(test_process_yyggi())
print(test_process_pphhh())
print(test_process_seq_a1())
print(process_pphhh('50586'))