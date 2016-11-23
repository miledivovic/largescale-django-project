#!/usr/bin/env python
import pymysql
# import pymysql.cursor
import config
import level3
# from time import datetime
import datetime
from pprint import pprint
import curio

def prober ():

    conn= pymysql.connect(host=config.HOST,user=config.USER,passwd=config.PASS,db='monitoring',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
    cursor=conn.cursor()

    sql='SELECT id, node_ip, ProbingFrequency, last_probed_at FROM node_master'
    cursor.execute(sql)
    results=cursor.fetchall()
    node_list = []
    curr_time = datetime.datetime.now()


    for row in results:
        # print(row)
        node = {}
        node_id = row["id"]
        node_ip = row["node_ip"]
        ProbingFrequency = row["ProbingFrequency"]
        last_probed_at = row["last_probed_at"]


        if last_probed_at:
            time_diff = curr_time - last_probed_at

            if time_diff.seconds < ProbingFrequency :
                continue

        node["node_id"] = node_id
        node["node_url"] = node_ip
        node["node_port"] = "8000"
        node["get_path"] = "/"
        node["timeout"] = "20"

        node_list.append(node)


    try:
        
        if len(node_list) > 0:
            # pprint(node_list)
            node_res = curio.run(level3.fetch_data(node_list))
            # pprint(node_res)

            value = ""
            first_value = True


            for node_id in node_res:
                node = node_res[node_id]
                node_status = node["status"]
                node_error = ""
                
                if node_status != -1:
                    node_data = node["data"]

                    for data in node_data:
                        if first_value:
                            value += "(" + str(node_id) + ",'" + str(data) +"', " + str(node_data[data]) + ")"
                        else:
                            value += ",(" + str(node_id) + ",'" + str(data) +"', " + str(node_data[data]) + ")"
                        first_value = False
                else:
                    node_error = node["error"]
                

                sqlTwo = "UPDATE node_master SET last_probed_at = \'" + str(curr_time) + "\', last_status = " + str(node_status) + ", last_error = \'" + node_error + "\' WHERE id = " + str(node_id)

                print (sqlTwo)
                try:
                    # Execute the SQL command
                    cursor.execute(sqlTwo)
                    # Commit your changes in the database
                    conn.commit()
                except:
                    # Rollback in case there is any error
                    conn.rollback()

            if first_value == False:
                sql = "INSERT INTO data_table (node_id, CounterName, Value) VALUES " + value
                print (sql)
                try:
                  # Execute the SQL command
                  cursor.execute(sql)
                  # Commit your changes in the database
                  conn.commit()
                except:
                  # Rollback in case there is any error
                  conn.rollback()


    except Exception as e:
        print(e)
