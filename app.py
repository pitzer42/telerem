
from rembot import RemBot
from rembot.services import telegram
from rembot.features import reply_telegram_with_rem

app = RemBot()
telegram.attach(app)
reply_telegram_with_rem.attach(app)

#app.start()
print('running...')
