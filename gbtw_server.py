from pyfcm import FCMNotification

from pyfcm import FCMNotification

APIKEY = "AAAA2wElNj0:APA91bHEaiA0Sv_2fm"\
         "t0d7fW7P6fdXNr1yR9Tz0loDKF6TI45"\
         "nQUHrXLvMIyU08gOM2JXwQBogn0"\
         "KaQc0pTAbFw1-xZyLR7DWGcebHLi"\
         "--0Cv6G0ZAdxHaw5CpQLdqg_jqQ"\
         "bsdgM6nBR"
TOKEN = "Your Token"

# 파이어베이스 콘솔에서 얻어 온 서버 키를 넣어 줌
push_service = FCMNotification(APIKEY)


def sendMessage(body, title):
    # 메시지 (data 타입)
    data_message = {
        "body": body,
        "title": title
    }

    # 토큰값을 이용해 1명에게 푸시알림을 전송함
    result = push_service.single_device_data_message(registration_id=TOKEN, data_message=data_message)

    # 전송 결과 출력
    print(result)

sendMessage("배달의 민족", "치킨 8000원 쿠폰 도착!")

'''
APIKEY = "AAAA2wElNj0:APA91bHEaiA0Sv_2fm"\
         "t0d7fW7P6fdXNr1yR9Tz0loDKF6TI45"\
         "nQUHrXLvMIyU08gOM2JXwQBogn0"\
         "KaQc0pTAbFw1-xZyLR7DWGcebHLi"\
         "--0Cv6G0ZAdxHaw5CpQLdqg_jqQ"\
         "bsdgM6nBR"

push_service = FCMNotification(APIKEY)


def send_message(title, message):
    data_message = {
        "title": title,
        "body": message
    }

    result = push_service.notify_topic_subscribers(topic_name="GBTF", data_message=data_message)
    print('결과', result)


send_message("GBTF Reminder", "반갑습니다")
'''