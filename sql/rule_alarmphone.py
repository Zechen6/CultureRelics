import numpy as np
import MySQLc
import datetime

def rule_alarmphone():
    dataSet = MySQLc.ExecSelect("SELECT area_id,state from equipment_data where equipment_type='{}'".format('报警电话'))
    data = np.array(dataSet)
    # print(data)
    for i in data:
       if i[1] == 1:
           MySQLc.ExecAddDelUpdate("UPDATE area_data SET area_alarmphone_rule=1,area_time='{}' WHERE area_id='{}'".format(datetime.datetime.now(),i[0]))
       else:
           MySQLc.ExecAddDelUpdate("UPDATE area_data SET area_alarmphone_rule=0,area_time='{}' WHERE area_id='{}'".format(datetime.datetime.now(),i[0]))

if __name__ == '__main__':
    rule_alarmphone()