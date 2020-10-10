import vk_api
from vk_api.longpoll import VkLongPoll
from aiogram import Bot, Dispatcher, executor, types

token = ''
session = vk_api.VkApi(token=token)
vk = session.get_api()
longpoll = VkLongPoll(session)


bot = Bot('')
dp = Dispatcher(bot)


def vk_message_send(id, msg):
    vk.messages.send(user_id=id, message=msg, random_id=0)


@dp.message_handler(content_types=['text'])
async def echo(message: types.Message):
    split_text = message.text.split('\n')
    id = int(split_text[0])
    vk_message = ' '.join(split_text[1:])
    vk_message_send(id, vk_message)
    await message.answer('Сообщение отправлено')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
