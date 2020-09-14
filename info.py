import requests,json,socket

#Obtener info de la red publica
def get_net_info():
    user_info = socket.gethostname()
    try:
        net_info = requests.get("https://ipinfo.io/json")
        net_info.raise_for_status()
        user_info = json.dumps(net_info.json())
    finally:
        return user_info

if __name__ == '__main__':
    print(get_net_info())
        