import telegram

token = 'token'
id = "id"

bot = telegram.Bot(token)
bot.sendMessage(chat_id=id, text="send simple message")