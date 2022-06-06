import pymysql
import pandas as pd
import sys

def connect_mysql():
    db_config = {
        "host":"10.255.51.168",
        "user":"root",
        "passwd":"159357",
        "db":"test",
        "charset":"utf8"
    }
    try:
        cnx = pymysql.connect(**db_config)
    except Exception as e:
        raise e
    return cnx

#更新一条记录
def ExecAddDelUpdate(sqlstring):
    ren_int=0
    conn = connect_mysql()
    cursor = conn.cursor()
    try:
        ren_int =cursor.execute(sqlstring)  # 执行mysql连接和语句
        cursor.close()  # 关闭游标对象
        conn.commit()  # 提交事务,否则执行的语句会回滚，从而不生效
    except  Exception as e:  # 如报错，则抛出，并将操作回滚
        raise e
        conn.rollback()
    finally:
        conn.close()  # 关闭连接
    return ren_int

#更新多条记录
def ExecAddDelUpdateS(get_sqluptylist):
    ren_int=len(get_sqluptylist)
    conn = connect_mysql()
    cursor = conn.cursor()
    try:
        for onesql in get_sqluptylist:
            cursor.execute(onesql)  # 执行mysql连接和语句
        cursor.close()  # 关闭游标对象
        conn.commit()  # 提交事务,否则执行的语句会回滚，从而不生效
    except  Exception as e:  # 如报错，则抛出，并将操作回滚
        raise e
        conn.rollback()
    finally:
        conn.close()  # 关闭连接
    return ren_int

def ExecSelect(sqlstring):
    conn = connect_mysql()
    try:
        cursor = conn.cursor()
        cursor.execute(sqlstring)
        result = cursor.fetchall()
        cursor.close()
        conn.commit()
    except  Exception as e:  # 如报错，则抛出，并将操作回滚
        raise e
        conn.rollback()
        result=e
    finally:
        conn.close()  # 关闭连接
    return result

def PDExecSelect(sqlstring):
    conn = connect_mysql()
    try:
        result = pd.read_sql(sqlstring, conn)
    except  Exception as e:  # 如报错，则抛出，并将操作回滚
        raise e
        result=e
    finally:
        conn.close()  # 关闭连接
    return result


#import MySQLc
if __name__ == '__main__':
    sql="SELECT * from rdc"
    jg=ExecSelect(sql)
    #jg=MySQLc.ExecSelect(sql)
    print(jg)





