from linebot.v3.messaging import TextMessage, Emoji

from dalert.dalert_disaster import disaster_alert

def reponse_message(event):
    # print(event)
    request_message = event.message.text

    if request_message.startswith("hello"):
        emoji_data = [
            {
                "index": 0,
                "productId": "5ac1bfd5040ab15980c9b435",
                "emojiId": "009"
            },
            {
                "index": 18,
                "productId": "5ac21c46040ab15980c9b442",
                "emojiId": "006"
            },
        ]
        emojis = [Emoji(**emoji) for emoji in emoji_data]
        message = "$ สวัสดี from Dev $"
        response = TextMessage(text=message, emojis=emojis)
        return response
    

    if request_message.startswith("เตือนภัย"):
        return disaster_alert(event)
    
    
    else: 
        return TextMessage(text="ไม่พบข้อความอัตโนมัติ กรุณาลองใหม่อีกครั้ง")