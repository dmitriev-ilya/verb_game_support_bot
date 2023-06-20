import os
from functools import partial

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from dotenv import load_dotenv
from dialogflow_bot import get_dialogflow_response_text


def start(update: Update, context: CallbackContext):
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Здравствуй, {user.mention_markdown_v2()}\!'
    )


def send_reply(update: Update, context: CallbackContext, project_id, session_id):
    update.message.reply_text(
        get_dialogflow_response_text(project_id, session_id, update.message.text, 'ru')
    )


if __name__ == '__main__':
    load_dotenv()
    telegram_bot_token = os.environ['SUPPORT_BOT_TELEGRAM_TOKEN']
    gcloud_project_id = os.environ['GCLOUD_PROJECT_ID']
    session_id = os.environ['TELEGRAM_USER_ID']

    updater = Updater(telegram_bot_token)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(
        MessageHandler(
            Filters.text & ~Filters.command,
            partial(send_reply, project_id=gcloud_project_id, session_id=session_id)
        )
    )

    updater.start_polling()
    updater.idle()
