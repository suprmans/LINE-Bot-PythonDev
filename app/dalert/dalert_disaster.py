import json

from linebot.v3.messaging import FlexMessage, TextMessage
from linebot.v3.messaging.models import FlexContainer  # Don't import from `linebot.models` it was wrong version

def disaster_alert(event):

    # Load the JSON data from a file
    with open('./dalert/dalert_disaster.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Extract the required fields
    for entry in data:
        alert_date = entry['head'].get('alertDate')
        area_display = entry['head'].get('areaDisPlay')
        topic = entry['head'].get('topic')
        memo = entry['head'].get('memo')
        origin_file_path = entry['fileActive'].get('originFilePath')
        remark = entry['fileActive'].get('remark')

    # bubble_string = """ """
    
    # flex_alt_text = "diaster alert"
    # flex_contents = FlexContainer.from_json(bubble_string)
    
    # return FlexMessage(alt_text=flex_alt_text, contents=flex_contents)

    text_response = f"alert_date: {alert_date}\narea_display: {area_display}\ntopic: {topic}\nmemo: {memo}\norigin_file_path: {origin_file_path}\nremark: {remark}"
    # print(text_response)
    return TextMessage(text=text_response)