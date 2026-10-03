import os, random, telebot
TOKEN=os.getenv("BOT_TOKEN")
bot=telebot.TeleBot(TOKEN)
left=5
@bot.message_handler(commands=['start'])
def s(m):
 bot.send_message(m.chat.id,"You Are Scanning With NKW7.FX\nNKW7.FX GOLD|NASDAQ|US30\nTap /scan")
@bot.message_handler(commands=['scan'])
def sc(m):
 global left
 if left<=0:
  bot.send_message(m.chat.id,"❌ 0 left - Pay R250 for 100 scans")
  return
 left-=1
 p=random.choice(["GOLD 🥇","NASDAQ 📈","US30 🇺🇸"])
 bot.send_message(m.chat.id,f"🔍 NKW7.FX SCAN\n{p}\nSMC BUY ZONE\nBUY NOW\nSL 30 TP 60\nLeft:{left}")
bot.infinity_polling()
