import os
import random

import vk_api as vk
from vk_api.longpoll import VkLongPoll, VkEventType
from dotenv import load_dotenv

from dialogflow_bot import get_dialogflow_response


def send_reply(event, vk_api, gcloud_project_id, session_id):
    dialogflaw_response = get_dialogflow_response(
        gcloud_project_id,
        session_id,
        event.text
    )
    if not dialogflaw_response.query_result.intent.is_fallback:
        reply_message = dialogflaw_response.query_result.fulfillment_text
        vk_api.messages.send(
            user_id=event.user_id,
            message=reply_message,
            random_id=random.randint(1,1000)
        )


if __name__ == '__main__':
    load_dotenv()
    vk_group_api_token = os.environ['VK_GROUP_API_TOKEN']
    gcloud_project_id = os.environ['GCLOUD_PROJECT_ID']
    session_id = os.environ['TELEGRAM_USER_ID']

    vk_session = vk.VkApi(token=vk_group_api_token)

    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            send_reply(event, vk_api, gcloud_project_id, session_id)
