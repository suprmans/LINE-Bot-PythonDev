from linebot.v3.messaging import TextMessage, Emoji

def reponse_message(event):
    # print(event)
    request_message = event.message.text

    if request_message.startswith("hello"):
        emoji_data = [
            {
                "index": 0,
                "productId": "5ac1bfd5040ab15980c9b435",
                "emojiId": "024"
            },
            {
                "index": 18,
                "productId": "5ac1bfd5040ab15980c9b435",
                "emojiId": "062"
            },
        ]
        emojis = [Emoji(**emoji) for emoji in emoji_data]
        message = "$ สวัสดี from Dev $"
        response = TextMessage(text=message, emojis=emojis)
        return response
    
    else: 
        return TextMessage(text="ไม่พบข้อความอัตโนมัติ กรุณาลองใหม่อีกครั้ง")