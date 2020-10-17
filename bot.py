from telebot import *
from telebot.types import *

from bs4 import BeautifulSoup
import requests


def vaqt():
    URL = requests.get("https://islom.uz/lotin")
    SOUP = BeautifulSoup(URL.content,"html.parser")

    UZBDA = SOUP.find("div",class_="date_time")

    return UZBDA.text

def namoz_vaqtlari():
   URL = requests.get("https://islom.uz/lotin")
   SOUP = BeautifulSoup(URL.content,"html.parser")

   UZBDA = SOUP.find("div",class_="in_header_p")
   vaqt = UZBDA.text.split('\n')

   title = vaqt[1]
   vaqt_tong = "  :  ".join(vaqt[6:8])
   vaqt_quyosh = "  :  ".join(vaqt[14:16])
   vaqt_peshin = "  :  ".join(vaqt[21:23])
   vaqt_asr = "  :  ".join(vaqt[28:30])
   vaqt_shom = "  :  ".join(vaqt[35:37])
   vaqt_xufton = "  :  ".join(vaqt[42:44])
   
   xabar = "<b>{0}\n\n{1}\n{2}\n{3}\n{4}\n{5}\n{6}</b>".format(title,vaqt_tong,vaqt_quyosh,vaqt_peshin,vaqt_asr,vaqt_shom,vaqt_xufton)

   return xabar





bot = TeleBot("1320507646:AAFXBd8VNWEIHnVY8hOGaAl2ILUkvwDnT5I")



bosh_sahifa = InlineKeyboardMarkup()
bs_1 = InlineKeyboardButton("🗓 Namoz Vaqtlari",callback_data='namoz_vaqtlari')
bs_2 = InlineKeyboardButton("🕌 Juma Shukuhi",callback_data='juma_shukuhi')

bosh_sahifa.add(bs_1,bs_2)

ortga = InlineKeyboardMarkup()
ort = InlineKeyboardButton("◀️ Ortga",callback_data='ortga')

ortga.add(ort)

@bot.message_handler(commands=['start'])
def main(message):
    bot.delete_message(message.chat.id,message.message_id)
    bot.send_photo(
        chat_id=message.chat.id,
        photo='https://i1.sndcdn.com/artworks-000227818455-cfxhbu-t500x500.jpg',
        caption="<a href='https://github.com/000bakhtiyor'>Github</a> \n<b>Vaqt : {0}\n\n'Қуръонга боғланиб ажр-савобга эришинг' <i>\nManba : Islom.Uz</i></b>\n\nAssalomu Alaykum !\n<i>Tanlang :</i>".format(vaqt()),
        parse_mode='html',
        reply_markup=bosh_sahifa
        )

@bot.callback_query_handler(func=lambda call:True)
def callback_answer(call):
    if call.data == "namoz_vaqtlari":
        bot.delete_message(call.message.chat.id,call.message.message_id)
        bot.send_photo(
            call.message.chat.id,
            photo='http://ae01.alicdn.com/kf/Habdc4b6b0955453ca02a1344fb27b8f4B.jpg',
            caption=namoz_vaqtlari(),
            parse_mode='html',
            reply_markup=ortga
            )
    elif call.data == "juma_shukuhi":
        bot.delete_message(call.message.chat.id,call.message.message_id)
        bot.send_photo(
            call.message.chat.id,
            photo="https://mir-s3-cdn-cf.behance.net/project_modules/1400/51ef1438558223.5766a40bcf236.jpg",
            caption='<b>YouTube orqali tomosha qiling :</b> <a href="https://youtu.be/aLNqYOfRmWI">Juma shukuhi Video</a>',
            parse_mode='html',
            reply_markup=ortga
        )
    else:
        bot.delete_message(call.message.chat.id,call.message.message_id)
        bot.send_photo(
        chat_id=call.message.chat.id,
        photo='https://i1.sndcdn.com/artworks-000227818455-cfxhbu-t500x500.jpg',
        caption="<b>{0}\n\n'Қуръонга боғланиб ажр-савобга эришинг' <i>\nManba : Islom.Uz</i></b>\n\nAssalomu Alaykum !\n<i>Tanlang :</i>".format(vaqt()),
        parse_mode='html',
        reply_markup=bosh_sahifa
        )
        

bot.polling(none_stop=True)