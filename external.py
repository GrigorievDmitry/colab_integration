# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 17:11:21 2020

@author: HYPERPC
"""

def grader(week, answer):
    import requests
    resp = requests.get("https://colabconnectionhost.herokuapp.com/" + str(week),
                       params={"answer": answer})
    return resp.text
