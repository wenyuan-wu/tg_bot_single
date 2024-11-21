import os
import telebot
from openai_res import get_response_openai, get_response_openai_test, get_settings
from dotenv import load_dotenv


def run_tg_bot(bot_token, yaml_file):
    bot = telebot.TeleBot(bot_token)
    settings = get_settings(yaml_file)
    welcome_msg = settings["welcome_message"]
    help_msg = settings["help_message"]

    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.reply_to(message, welcome_msg)

    @bot.message_handler(commands=['help'])
    def send_welcome(message):
        bot.reply_to(message, help_msg)

    @bot.message_handler(func=lambda message: True)
    def echo_all(message):
        reply = get_response_openai(message.text)
        bot.reply_to(message, reply, parse_mode="Markdown")

    bot.infinity_polling()


def main():
    load_dotenv()
    bot_token = os.environ.get('BOT_TOKEN')
    run_tg_bot(bot_token)


if __name__ == '__main__':
    main()
