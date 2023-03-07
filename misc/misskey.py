import requests
import misc

def misskey_post(endpoint, data, i=misc.config["misskey"]["i"]):
    data["i"] = i
    r = requests.post(misc.config["misskey"]["host"] + '/api/' + endpoint,
                      json=data)
    try:
        value = r.json()
        return value
    except:
        return True