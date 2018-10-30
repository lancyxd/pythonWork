#! /usr/bin/python
# -*- coding: utf-8 -*-


bonus=0
profits = float(input("请输入当月利润，单位为万元："))

bonus1=10*0.1
bonus2=bonus1+10*0.075
bonus4=bonus2+20*0.05
bonus6=bonus4+20*0.03
bonus10=bonus6+40*0.015

def bonus_count(profits):
    if profits <= 10:
        bonus = profits * 0.1
    elif profits >= 10 and profits <= 20:
        bonus = bonus1 + (profits - 10) * 0.075
    elif profits >= 20 and profits <= 40:
        bonus = bonus2 + (profits - 20) * 0.05
    elif profits >= 40 and profits <= 60:
        bonus = bonus4 + (profits - 40) * 0.03
    elif profits >= 60 and profits <= 100:
        bonus = bonus6 + (profits - 60) * 0.015
    else:
        bonus = bonus10 + (profits - 100) * 0.01
    return bonus


bonus=bonus_count(profits)

print("奖金为(单位为万元)：",bonus)











