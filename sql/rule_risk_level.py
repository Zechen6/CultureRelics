import numpy as np
import MySQLc
import datetime

def rule_risk_level():
    dataSet = MySQLc.ExecSelect("SELECT area_id,area_annihilator_rule,area_alarmphone_rule,area_hydrant_rule from area_data")
    data = np.array(dataSet)
    print(data)
    for i in data:
        area_risk_level=5
        if i[1] == 1:
            area_risk_level = area_risk_level-1
        if i[2] == 1:
            area_risk_level = area_risk_level-1
        if i[3] == 1:
            area_risk_level = area_risk_level-1
        MySQLc.ExecAddDelUpdate("UPDATE area_data SET area_risk_level='{}',area_time='{}' WHERE area_id='{}'".format(area_risk_level,datetime.datetime.now(),i[0]))

if __name__ == '__main__':
    rule_risk_level()