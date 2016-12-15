#!/usr/bin/env python
import pymysql
import config
import http_utils
import datetime
from pprint import pprint
import curio

def prober ():
    conn= pymysql.connect(host=config.HOST,user=config.USER,passwd=config.PASS,db=config.DB,charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
    cursor=conn.cursor()

    sql="SELECT node_id, node_ip, probing_frequency, last_probed FROM dashboard_node WHERE active = '1'"
    cursor.execute(sql)
    results=cursor.fetchall()
    node_list = []
    curr_time = datetime.datetime.now()

    for row in results:
        node = {}
        node_id = row["node_id"]
        node_ip = row["node_ip"]
        ProbingFrequency = row["probing_frequency"]
        last_probed_at = row["last_probed"]

        if last_probed_at:
            time_diff = curr_time - last_probed_at

            if time_diff.seconds < ProbingFrequency :
                continue

        node["node_id"] = node_id
        node["node_url"] = node_ip
        node["node_port"] = "8000"
        node["get_path"] = "/"
        node["timeout"] = "20"
        node["node_counter_data_endpoint"] = node_ip
        node_list.append(node)
    try:
        
        if len(node_list) > 0:
            node_res = curio.run(http_utils.fetch_data(node_list))
            value = ""
            first_value = True
            for node_id in node_res:
                node = node_res[node_id]
                node_status = node["status"]
                node_error = ""
                last_error = "0000-00-00 00:00:00"

                if node_status != -1:
                    node_data = node["data"]

                    for data in node_data:
                        if first_value:
                            value += "(" + str(node_id) + ",'" + str(data) +"', '" + str(node_data[data]) +"', '" + str(curr_time) + "')"
                        else:
                            value += ",(" + str(node_id) + ",'" + str(data) +"', '" + str(node_data[data]) +"', '" + str(curr_time) + "')"
                        first_value = False
                else:
                    node_error = node["error"]
                    last_error = ""
                

                sqlTwo = "UPDATE dashboard_node SET last_probed = \'" + str(curr_time) + "\', last_status = '" + str(node_status) + "', last_failure = \'" + str(curr_time) + "\', error_msg = \'" + node_error + "\' WHERE node_id = " + str(node_id)
                try:
                    # Execute the SQL command
                    cursor.execute(sqlTwo)
                    # Commit your changes in the database
                    conn.commit()
                except:
                    # Rollback in case there is any error
                    conn.rollback()

            if first_value == False:
                sql = 'INSERT INTO dashboard_counter (node_id, tag, value, timestamp) VALUES ' + value
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
