import os

from dotenv import load_dotenv
from linebot.v3 import messaging  # type: ignore

load_dotenv(override=True)


def main():
    user_id = os.getenv("LINE_USER_ID")
    access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")

    configuration = messaging.Configuration(access_token=access_token)
    message_dict = {
        "to": user_id,
        "messages": [
            {"type": "text", "text": "text"},
        ],
    }

    with messaging.ApiClient(configuration=configuration) as client:
        messaging_api = messaging.MessagingApi(client)
        push_message_request = messaging.PushMessageRequest.from_dict(obj=message_dict)
        try:
            resp = messaging_api.push_message(push_message_request)  # noqa
            print(resp)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
