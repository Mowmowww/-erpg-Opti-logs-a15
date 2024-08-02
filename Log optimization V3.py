# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 21:29:14 2024

@author: Mowmowww
"""
def pourcents(level):
        pourcent1=(12.5 + (250 * (level - 100)) ** 0.2)/100
        if level>118:
            pourcent2=0.95
        elif level == 118:
            pourcent2=0.944
        elif level == 117:
            pourcent2=0.936
        elif level == 116:
            pourcent2=0.928
        elif level == 115:
            pourcent2=0.92
        elif level == 114:
            pourcent2=0.912
        elif level == 113:
            pourcent2=0.904
        elif level == 112:
            pourcent2=0.896
        elif level == 111:
            pourcent2=0.888
        elif level == 110:
            pourcent2=0.88
        elif level == 109:
            pourcent2=0.872
        elif level == 108:
            pourcent2=0.864
        elif level == 107:
            pourcent2=0.856
        elif level == 106:
            pourcent2=0.848
        elif level == 105:
            pourcent2=0.84
        elif level == 104:
            pourcent2=0.832
        elif level == 103:
            pourcent2=0.824
        elif level == 102:
            pourcent2=0.816
        elif level == 101:
            pourcent2=0.808
        return pourcent1,pourcent2




def opti(pourcent1, pourcent2):
    nombretesté = 26
    x1 = calc(pourcent1, pourcent2, nombretesté)
    x2 = calc(pourcent1, pourcent2, nombretesté+1)
    sum1 = x1-nombretesté
    sum2 = x2-nombretesté-1
    while sum2>sum1:
        nombretesté=nombretesté+1
        x1 = calc(pourcent1, pourcent2, nombretesté)
        x2 = calc(pourcent1, pourcent2, nombretesté+1)
        sum1 = x1-nombretesté
        sum2 = x2-nombretesté-1
    return nombretesté



def calc(pourcent1: float, pourcent2: float, nombretesté: int):
    formule(pourcent1, pourcent2)
    return calc7(pourcent1, pourcent2, nombretesté)



def formule(pourcent1, pourcent2):
    resformule=(0.8 + pourcent1) * pourcent2 + 0.8 * (1-pourcent2)
    return resformule



def calc1(pourcent1, pourcent2, nombretesté):
    rescalc1 = nombretesté
    if rescalc1 > 25 :
        if rescalc1 > 500 :
            rescalc1 = (rescalc1-500)*formule(pourcent1,pourcent2) + 500
        rescalc1 = 0.075*(rescalc1-25)*formule(pourcent1,pourcent2)+0.075*25
    return rescalc1



def calc2(pourcent1,pourcent2, nombretesté):
    rescalc2 = calc1(pourcent1, pourcent2, nombretesté)
    if rescalc2 > 25 :
        if rescalc2 > 300 :
            rescalc2 = (rescalc2-300)*formule(pourcent1,pourcent2) + 300
        rescalc2 = (rescalc2-25)*formule(pourcent1,pourcent2)+25
    return rescalc2



def calc3(pourcent1,pourcent2, nombretesté):
    rescalc3 = calc2(pourcent1, pourcent2, nombretesté)*2
    if rescalc3 > 100 :
        rescalc3 = (rescalc3-100)*formule(pourcent1,pourcent2)+100
    return rescalc3



def calc4(pourcent1,pourcent2, nombretesté):
    "en standby, useless probablement"
    rescalc4 = calc3(pourcent1, pourcent2, nombretesté)*3.75
    if rescalc4 > 25 :
        rescalc4 = (rescalc4-25)*formule(pourcent1,pourcent2)
        if rescalc4 > 500 :
            rescalc4 = (rescalc4-500)*formule(pourcent1,pourcent2) + 500
        rescalc4 = rescalc4 + 25
    return rescalc4



def calc5(pourcent1,pourcent2, nombretesté):
    rescalc5 = calc3(pourcent1, pourcent2, nombretesté)*3.75
    if rescalc5 > 300 :
        rescalc5 = (rescalc5-300)*formule(pourcent1,pourcent2)+300
    return rescalc5



def calc6(pourcent1,pourcent2, nombretesté):
    rescalc6 = calc5(pourcent1, pourcent2, nombretesté)*1.5
    if rescalc6 > 75:
        rescalc6 = (rescalc6-75)*formule(pourcent1,pourcent2)
        if rescalc6 > 300 :
            rescalc6 = (rescalc6-300)*formule(pourcent1,pourcent2) + 300
        rescalc6 = rescalc6 + 75
    return rescalc6



def calc7(pourcent1,pourcent2, nombretesté):
    rescalc7 = calc6(pourcent1, pourcent2, nombretesté)*1.5
    return rescalc7
































