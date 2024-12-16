from telethon import TelegramClient, events

api_id = 
api_hash = ''

client_tg = TelegramClient('session_name.session', api_id, api_hash)


@client_tg.on(events.NewMessage(from_users='r3s1l13n'))
async def normal_handler_1(event):
    # получаем сигнал
    # pprint(event.message)
    # mes = event.message.to_dict()# ['message']
    # print(mes)
    await client_tg.forward_messages(
        'me', event.message
    )
    # await client_tg.send_message(
    #     'me', mes
    # )

client_tg.start()

client_tg.run_until_disconnected()
