import os
from functools import partial
import logging

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from dotenv import load_dotenv

from dialogflow_bot import get_dialogflow_response
from logger import SupportBotLogsHandler


logger = logging.getLogger(__file__)


def start(update: Update, context: CallbackContext):
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Здравствуй, {user.mention_markdown_v2()}\!'
    )


def send_reply(update: Update, context: CallbackContext, project_id):
    session_id = f'tg-{update.message.from_user["id"]}'

    dialogflow_response = get_dialogflow_response(
        project_id,
        session_id,
        update.message.text
    )
    update.message.reply_text(
        dialogflow_response.query_result.fulfillment_text
    )


if __name__ == '__main__':
    load_dotenv()
    telegram_bot_token = os.environ['SUPPORT_BOT_TELEGRAM_TOKEN']
    gcloud_project_id = os.environ['GCLOUD_PROJECT_ID']
    telegram_chat_id = os.environ['TELEGRAM_USER_ID']

    logger.setLevel(logging.INFO)
    logger.addHandler(SupportBotLogsHandler(telegram_bot_token, telegram_chat_id))

    try:
        updater = Updater(telegram_bot_token)

        dispatcher = updater.dispatcher
        dispatcher.add_handler(CommandHandler("start", start))
        dispatcher.add_handler(
            MessageHandler(
                Filters.text & ~Filters.command,
                partial(send_reply, project_id=gcloud_project_id)
            )
        )

        updater.start_polling()
        logger.info('Telegram-бот запущен')
    except Exception as err:
        logger.error('Telegram-бот упал с ошибкой:')
        logger.error(err, exc_info=True)

    updater.idle()
