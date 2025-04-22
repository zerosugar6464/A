import telebot
import yt_dlp
import os
from datetime import datetime

kedicik = print("token gir: ")
ramowlf = telebot.TeleBot(kedicik)

@ramowlf.message_handler(commands=['start'])
def ramazan(message):
    yarramiye = datetime.now().hour
    if 5 <= yarramiye < 12:
        sigma = "Günaydın 🥱"
    elif 12 <= yarramiye < 17:
        sigma = "İyi öğlenler 🫠"
    elif 17 <= yarramiye < 22:
        sigma = "İyi akşamlar 🤤"
    else:
        sigma = "İyi geceler 😴"

    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    button1 = telebot.types.InlineKeyboardButton("Sahibim ❤️‍🩹", url="https://t.me/ramowlf")
    button2 = telebot.types.InlineKeyboardButton("Komut 💋", callback_data="sikimKalkti")
    button3 = telebot.types.InlineKeyboardButton("Kanal 😍", url="https://t.me/TurkUserBotKanali")
    markup.add(button1, button2, button3)
    ramowlf.reply_to(message, f"{sigma} Ben müzik indirme botuyum, beni tercih ettiğiniz için teşekkür ederim.", reply_markup=markup)

@ramowlf.message_handler(commands=['indir'])
def TurkUserBotKanali(message):
    azginim = " ".join(message.text.split()[1:])
    if not azginim:
        ramowlf.send_message(message.chat.id, "örnek kullanım: /indir mert şenel şaraplar ve kadınlar")
        return

    ramowlf.send_message(message.chat.id, "🔍indiriliyor")

    try:
        ramazanozturk = {
            'format': '251',  
            'outtmpl': f'{azginim}.webm',
            'noplaylist': True,
            'quiet': True  
        }

        with yt_dlp.YoutubeDL(ramazanozturk) as ydl:
            tassak = ydl.extract_info(f"ytsearch:{azginim}", download=True)
            if 'entries' in tassak:
                tassak = tassak['entries'][0]
            yarragim = ydl.prepare_filename(tassak)

        with open(yarragim, 'rb') as audio:
            ramowlf.send_audio(message.chat.id, audio, caption=f"🎶 {tassak['title']}")

        os.remove(yarragim)  

    except:
        pass

@ramowlf.callback_query_handler(func=lambda call: True)
def Auuuuu(call):
    if call.data == "sikimKalkti":
        ramowlf.send_message(call.message.chat.id, "🍓 Komutlar;\n/start - Botu Başlatır 💓\n/indir - Müzik indirir 🥰\n\nAbi elimizde başka komut yok lütfen kızma")

ramowlf.polling(none_stop=True)