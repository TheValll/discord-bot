import os
import json

PATH = os.path.join(os.path.dirname(__file__), "../bdd.json")
with open(PATH, "r") as file:
    data = json.load(file)
    servers = data["servers"]


def get_channel_id_from_member(server_id):
    for server in servers:
        if server["id_server"] == server_id:
            return server["channel_id"]
        else:
            continue