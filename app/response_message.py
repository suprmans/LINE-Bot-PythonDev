from linebot.v3.messaging import TextMessage, Emoji

def reponse_message(event):
    request_message = event.message.text
    if request_message.lower() == "hello":
        emoji_data = [
            {
                "index": 0,
                "productId": "5ac1bfd5040ab15980c9b435",
                "emojiId": "002"
            },
            {
                "index": 37,
                "productId": "5ac21c46040ab15980c9b442",
                "emojiId": "002"
            },
        ]
        emojis = [Emoji(**emoji) for emoji in emoji_data]

        text_response = "$ Hello/สวัสดีครับ from PythonDevBot $"
        return TextMessage(text=text_response, emojis=emojis)
    

    if request_message.startswith("พยาการณ์อากาศ"):
        pass
    
    
    else: return None