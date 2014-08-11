'''
Created on 7/8/2014

@author: Jean Carlos
'''
# content of test_sample.py
def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5
    print(func(3))