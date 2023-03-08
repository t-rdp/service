import requests
import misc

def api_req(endpoint, data, i=misc.config["misskey"]["i"]):
    data["i"] = i
    r = requests.post(misc.config["misskey"]["host"] + '/api/' + endpoint,
                      json=data)
    try:
        value = r.json()
        return value
    except:
        return True

def create_public_note(content, i):
    data = {"localOnly": False, "poll": None, "visibility": "public", "text": content}
    return api_req("notes/create", data, i)