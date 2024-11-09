import requests
import os
from datetime import datetime

from dotenv import load_dotenv

from linebot.v3.messaging import FlexMessage, TextMessage
from linebot.v3.messaging.models import FlexContainer  # Don't import from `linebot.models` it was wrong version

load_dotenv(override=True)

def daily_forecast(event):
    request_message = event.message.text

    UID = os.getenv('TMD_UID')
    UKEY = os.getenv('TMD_UKEY')
    url = f"https://data.tmd.go.th/api/DailyForecast/v2/?uid={UID}&ukey={UKEY}&format=json"

    try:
        response = requests.get(url, timeout=5)
        response.encoding = 'utf-8'
        if response.status_code == 200:
            data = response.json()

            forecast_datetime = data["header"]["lastBuildDate"]
            dt = datetime.strptime(forecast_datetime, "%Y-%m-%d %H:%M:%S")
            thai_year = dt.year + 543
            thai_months = [
                "มกราคม", "กุมภาพันธ์", "มีนาคม", "เมษายน", "พฤษภาคม", "มิถุนายน",
                "กรกฎาคม", "สิงหาคม", "กันยายน", "ตุลาคม", "พฤศจิกายน", "ธันวาคม"
            ]
            thai_date_str = f"วันที่ {dt.day} {thai_months[dt.month - 1]} {thai_year} เวลา {dt.strftime('%H:%M')}"

            if ("กรุงเทพ" in request_message) or ("bangkok" in request_message.lower()):
                bagkok_forecast = data["DailyForecast"]["RegionForecast"][6]["DescriptionThai"]
                text_response = f"กรุงเทพมหานครและปริมณฑล\n{thai_date_str}\n\n{bagkok_forecast}"
            else:
                overall_forecast = data["DailyForecast"]["OverallDescriptionThai"]
                text_response = f"{thai_date_str}\n\n{overall_forecast}"
        else:
            print(response)
            text_response = "เกิดข้อผิดพลาด"

    except requests.exceptions.Timeout:
        text_response = "การเชื่อมต่อล้มเหลว โปรดลองอีกครั้ง (Connection timed out, please try again)"
    except requests.exceptions.RequestException as e:
        text_response = "เกิดข้อผิดพลาด กรุณาลองใหม่อีกครั้ง (An error occurred, please try again)"

    return TextMessage(text=text_response)