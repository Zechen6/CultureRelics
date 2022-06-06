import datetime

import numpy as np
import MySQLc

def insertState():
    dataSet=MySQLc.ExecSelect("SELECT equipment_id, equipment_type, use_Double, quality_guarantee_period, block, hydraulic_pressure,ntime from equipment_state_data order by event_id DESC limit 1")
    data= np.array(dataSet)
    print(data)
    for i in data:
        if i[2] == 0 :
            MySQLc.ExecAddDelUpdate(
                "insert into equipment_data (equipment_id, equipment_type, state) values(%d,'%s',%d) ON DUPLICATE KEY UPDATE state=0" % (
                    i[0], i[1], 0))

        else:
            if i[1] == '灭火瓶':
               if i[3] > datetime.datetime.now() :
                   MySQLc.ExecAddDelUpdate("UPDATE equipment_data SET state=1,other=0 WHERE equipment_id={}".format(i[0]))
                   continue
               else:
                   MySQLc.ExecAddDelUpdate("UPDATE equipment_data SET state=0,other='过期了' WHERE equipment_id={}".format(i[0]))
                   continue



            if i[1] == '消防通道':
               if i[4] == 0 :
                   MySQLc.ExecAddDelUpdate(
                       "insert into equipment_data (equipment_id, equipment_type, state) values(%d,'%s',%d) ON DUPLICATE KEY UPDATE state=1" % (
                           i[0], i[1], 1))
                   continue
               else:
                   MySQLc.ExecAddDelUpdate("UPDATE equipment_data SET state=0,other='堵塞' WHERE equipment_id={}".format(i[0]))
                   continue


            if i[1] == '水泵':
               if i[5] >10 :
                   MySQLc.ExecAddDelUpdate(
                       "insert into equipment_data (equipment_id, equipment_type, state) values(%d,'%s',%d) ON DUPLICATE KEY UPDATE state=1" % (
                           i[0], i[1], 1))
                   continue
               else:
                   MySQLc.ExecAddDelUpdate(
                       "UPDATE equipment_data SET state=0,other='水压过低' WHERE equipment_id={}".format(i[0]))
                   continue

            if i[1] == '报警电话':
                MySQLc.ExecAddDelUpdate(
                    "insert into equipment_data (equipment_id, equipment_type, state) values(%d,'%s',%d) ON DUPLICATE KEY UPDATE state=1" % (
                        i[0], i[1], 1))


if __name__ == '__main__':
    insertState()