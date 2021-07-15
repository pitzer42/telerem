import asyncio

from rembot.event_bus import EventBus
from rembot.services import telegram
from rembot.features import reply_telegram_with_rem
from rembot.features import recurrent_telegram_message



async def main():

    events = EventBus()

    await telegram.attach(events)

    await reply_telegram_with_rem.attach(events)
    await recurrent_telegram_message.attach(events)

    print('running...')

    while True:
        await asyncio.sleep(1)

asyncio.run(main())
