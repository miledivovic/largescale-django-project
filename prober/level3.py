import curio
import curio_http
# from pprint import pprint

async def fetch_one(node_id, url):
    async with curio_http.ClientSession() as session:
        status = ""
        error = ""
        content = ""
        try:
            response = await session.get(url)
            status = response.status_code
            content = await response.json()
        except Exception as e:
            status = -1
            error = e
        return  node_id, status, content, error


async def fetch_data (node_list):
    tasks = []

    node_res = {}

    for node in node_list:
        url = "http://" + node["node_url"] + ":" + node["node_port"] + node["get_path"] + "monitoring/counters/"
        # print(url)
        task = await curio.spawn(fetch_one( node["node_id"], url ))
        tasks.append(task)

    for task in tasks:
        node_id, status, content, error = await task.join()
        res = {}
        res["status"] = status
        if status != -1:
            res["data"] = content
        else:
            res["error"] = content

        node_res[node_id] = res

    return node_res
