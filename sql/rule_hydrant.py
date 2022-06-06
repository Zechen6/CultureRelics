from math import radians, cos, sin, asin, sqrt
import numpy as np
import MySQLc
import datetime

def get_distance(lon1, lat1, lon2, lat2):
    # 将十进制度数转化为弧度
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine公式
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # 地球平均半径，单位为公里
    # print(c * r * 1000)
    return c * r * 1000

def rule_hydrant():
    dataSet = MySQLc.ExecSelect("SELECT area_id,area_lon,area_lat from area_data")
    data_1 = np.array(dataSet)
    # print(data_1)

    dataSet = MySQLc.ExecSelect("SELECT equipment_id,hydrant_lon,hydrant_lat from equipment_data where state='{}' and equipment_type='{}' ".format(1,'水泵'))
    data_2 = np.array(dataSet)
    # print(data_2)

    for i in data_1:
        distance=0.06
        for j in data_2:
            # distance_test = get_distance(i[1], i[2], j[1], j[2])
            # if distance_test < distance:
            #     distance = distance_test
           if i[1]:
               distance_test = get_distance(i[1], i[2], j[1], j[2])
               if distance_test < distance:
                    distance=distance_test
        print(distance)
        if distance <= 0.05:
            MySQLc.ExecAddDelUpdate("UPDATE area_data SET area_hydrant_rule=1,area_time='{}' WHERE area_id='{}'".format(datetime.datetime.now(),i[0]))
        else:
            MySQLc.ExecAddDelUpdate("UPDATE area_data SET area_hydrant_rule=0,area_time='{}' WHERE area_id='{}'".format(datetime.datetime.now(),i[0]))





if __name__ == '__main__':
    rule_hydrant()