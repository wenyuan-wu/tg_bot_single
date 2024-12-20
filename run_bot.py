import os
import telebot
from openai_res import get_response_openai, get_response_openai_test, get_settings
from dotenv import load_dotenv


def run_tg_bot(bot_token, settings):
    bot = telebot.TeleBot(bot_token)
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
        reply = get_response_openai(message.text, settings)
        max_length = 4096
        # Split the reply if it's too long
        for i in range(0, len(reply), max_length):
            bot.reply_to(message, reply[i:i + max_length], parse_mode="Markdown")

    bot.infinity_polling()


def main():
    load_dotenv()
    bot_token = os.environ.get('BOT_TOKEN')
    yaml_file = "./prompts.yaml"
    settings = get_settings(yaml_file)
    # print(os.getpid())
    run_tg_bot(bot_token, settings)


if __name__ == '__main__':
    main()
