import base64
#must pass in as a stirng
def base64ToString(s):
    return base64.b64decode(s).decode('utf-8')
