import numpy as np
import MySQLc
import math
import datetime

def rule_annihilator():
    dataSet = MySQLc.ExecSelect("SELECT area_id, area_measure,area_type from area_data")
    data = np.array(dataSet)
    # print(data)
    for i in data:
        count = MySQLc.ExecSelect("SELECT count(*) from equipment_data where area_id='{}' and equipment_type='{}'".format(i[0], '灭火瓶'))[0][0]
        if i[1] is None :
            if count >= 2:
                MySQLc.ExecAddDelUpdate("UPDATE area_data SET area_annihilator_rule=1,area_time='{}' WHERE area_id='{}'".format(datetime.datetime.now(),i[0]))
            else:
                MySQLc.ExecAddDelUpdate("UPDATE area_data SET area_annihilator_rule=0,area_time='{}' WHERE area_id='{}'".format(datetime.datetime.now(),i[0]))
            continue
        else:
            measure = math.ceil(i[1]/(10*i[2]))            # print(measure)
            if count >= measure*2:
                MySQLc.ExecAddDelUpdate("UPDATE area_data SET area_annihilator_rule=1,area_time='{}' WHERE area_id='{}'".format(datetime.datetime.now(),i[0]))
            else:
                MySQLc.ExecAddDelUpdate("UPDATE area_data SET area_annihilator_rule=0,area_time='{}' WHERE area_id='{}'".format(datetime.datetime.now(),i[0]))
            continue

if __name__ == '__main__':
    rule_annihilator()