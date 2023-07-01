#    Copyright (c) 2021 Ayush
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
#    License can be found in < https://github.com/Ayush7445/telegram-auto_forwarder/blob/main/License > .

import logging
from os import environ

from telethon import TelegramClient, events
from telethon.sessions import StringSession


logging.basicConfig(format='%(message)s', level=logging.INFO)
logging.getLogger('telethon').setLevel(logging.WARN)
log = logging.getLogger(__name__)


async def message_handler(event):
    for chat in TO:
        try:
            await client.send_message(
                chat,
                event.message
            )
        except Exception as e:
            print(e)


if __name__ == '__main__':
    FROM = [int(i) for i in environ["FROM_CHANNEL"].split()]
    TO = [int(i) for i in environ["TO_CHANNEL"].split()]

    with TelegramClient(
        StringSession(environ["SESSION"]),
        environ["API_ID"],
        environ["API_HASH"]
    ) as client:
        client.add_event_handler(message_handler, events.NewMessage(incoming=True, chats=FROM))
        client.run_until_disconnected()
