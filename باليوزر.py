import telebot

bot = telebot.TeleBot("6922859569:AAEXdrJuHt4KAQr92zTFtIOImVbagIEACvo")

@bot.message_handler(commands=["start"])
def start(message):
		bot.reply_to(message,"""
اهلا بك ✨
قم برفع البوت في مجموعتك مع اعطاء صلاحية حذف الرسائل ، لكي يقوم بحذف رسائل المنع 〽️
📌المطور : @altaee_z
""")
		
@bot.message_handler(func=lambda message: message.text in ['كسمك','كسعمتك','كسختك','عيري','اير','عير','زب','زوب','كسي','طيز','امك','خالتك','مص','كسك','مصلي','موطه','موطة','موطلي','انيج امك','كسختك','عير باختك','عير بامك','عير بيك','بلاع','نيج','نيجني','انيجك','امك الكحبه','اختك الكحبه','تيل بيك','تيل','اه','سكسي','سكس','sex','+18','نيجه','مصه','كحبه','كحبه','امك تنيج','اختك تنيج','خالتك الشكرا','خالتك الشكره','خالتك الشكرة','وردي','ما اتحمل','كله لو بس الراس','مصيلي','ااه','اهه','🍑'])
def echo_message(message):
    # Send the username of the user who sent the message.
    bot.send_message(message.chat.id, f"""هذه الرسالة ممنوعة ⚠️ .
لا تصير جاهل يـ @{message.from_user.username} 
اذا رسلتها مره ثانية تنحظر 😉 !""")
    
    # Delete the message.
    bot.delete_message(message.chat.id, message.message_id)



print("""تم تفعيل البوت 
ارفع البوت مشرف في مجموعتك مع صلاحية حذف الرسائل ومبروك
لا تنسى حسابي تلي : @dudrd""")



bot.polling()