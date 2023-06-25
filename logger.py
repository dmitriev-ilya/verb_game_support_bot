import logging
import telegram


class SupportBotLogsHandler(logging.Handler):

    def __init__(self, telegram_bot_token, chat_id):
        super().__init__()
        self.chat_id = chat_id
        self.tg_bot = telegram.Bot(token=telegram_bot_token)

    def emit(self, record):
        log_entry = self.format(record)
        self.tg_bot.send_message(chat_id=self.chat_id, text=log_entry)
