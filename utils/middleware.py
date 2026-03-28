from utils.auth import verify_token

def get_current_user(handler):
    auth = handler.request.headers.get("Authorization")

    if not auth:
        return None

    try:
        token = auth.split(" ")[1]
        return verify_token(token)
    except:
        return None