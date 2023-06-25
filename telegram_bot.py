import os
from functools import partial
import logging
from time import sleep

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from dotenv import load_dotenv
import telegram

from dialogflow_bot import get_dialogflow_response
from logger import SupportBotLogsHandler


logger = logging.getLogger(__file__)


def start(update: Update, context: CallbackContext):
    try:
        user = update.effective_user
        update.message.reply_markdown_v2(
            fr'Здравствуй, {user.mention_markdown_v2()}\!'
        )
    except Exception as err:
        logger.error('Telegram-бот упал с ошибкой:')
        logger.error(err, exc_info=True)


def send_reply(update: Update, context: CallbackContext, project_id, session_id):
    try:
        dialogflow_response = get_dialogflow_response(
            project_id,
            session_id,
            update.message.text
        )
        update.message.reply_text(
            dialogflow_response.query_result.fulfillment_text
        )
    except Exception as err:
        logger.error('Telegram-бот упал с ошибкой:')
        logger.error(err, exc_info=True)


if __name__ == '__main__':
    load_dotenv()
    telegram_bot_token = os.environ['SUPPORT_BOT_TELEGRAM_TOKEN']
    gcloud_project_id = os.environ['GCLOUD_PROJECT_ID']
    session_id = os.environ['TELEGRAM_USER_ID']

    tg_bot = telegram.Bot(token=telegram_bot_token)

    logger.setLevel(logging.INFO)
    logger.addHandler(SupportBotLogsHandler(tg_bot, session_id))

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
    logger.info('Telegram-бот запущен')

    updater.idle()
