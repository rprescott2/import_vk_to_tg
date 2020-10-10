import asyncio
import vk_api
from vk_api.longpoll import VkEventType, VkLongPoll
from aiogram import Bot, Dispatcher, types

token = ''
session = vk_api.VkApi(token=token)
vk = session.get_api()
longpoll = VkLongPoll(session)


bot = Bot('')
dp = Dispatcher(bot)


async def send_to_telegram(text):
    await bot.send_message(461218321, text)


def get_photo(event):
    for attach in event.attachments:
        if 'photo' in event.attachments.get(attach):
            return "Пользователь прислал фотографию"
    return ""


def get_voice_message(event):
    attach = event.attachments.get('attachments')
    if attach:
        for att in attach.split(','):
            if 'link_mp3' in att:
                a = att.split('"')
                return str(a[3])
    return ""


async def get_messages():
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.from_user:
            user = vk.users.get(user_id=event.user_id)[0]
            get_voice_message(event)
            tmp_text = ["{} {}".format(user.get('first_name'), user.get('last_name')), str(event.user_id), event.text,
                        get_voice_message(event), get_photo(event)]
            text = []
            for i in tmp_text:
                if i:
                    text.append(i)
            await send_to_telegram("\n".join(text))


if __name__ == '__main__':
    asyncio.run(get_messages())
