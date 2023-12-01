from fastapi import Header, Request, Depends
import logging,json,base64


LOGGER = logging.getLogger(__file__)

def get_refresh_token(request: Request):
    session_cookie = request.cookies.get("session-1")
    if not session_cookie:
        LOGGER.error(f"session-1 token is missing for request")
        # raise MpApiError(AuthErrorEnum.AUTH_006)
    return session_cookie

def verify_token_return_userid(token: str = Header(...)):
    # even when i remove e, it still works
    jwt_token = token

    # Split the JWT into its parts
    header, payload, signature = jwt_token.split(".")

    # Decode the base64-encoded payload
    decoded_payload = base64.urlsafe_b64decode(payload + "===").decode("utf-8")

    # Parse the JSON content of the payload
    payload_data = json.loads(decoded_payload)
    # Access the user ID
    user_id = payload_data.get("user_uid")

    return user_id