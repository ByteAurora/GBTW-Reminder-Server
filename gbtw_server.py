from pyfcm import FCMNotification

APIKEY = "AAAAeMqKdfs:APA91bGdm7YD_RVcTX9_1oiJy_S4rZEgHmu66d" \
         "mbZZRaiRvpGD_kYL0kR7amy2o-I0XhEUxw_cOyoUDMvlncNhc0" \
         "X16Y-xGb3-B_Dq1LIr8fpEKk9DuvR-KhvKm4B1ymvpYDGnnoDj6i"
TOKEN = "d1VRBeqsSJiyR6djvMqrNH:APA91bHojG43VZL3M" \
        "9PTp6T_RLLWpcQocPBLB4_Rog_7cQuN1sF8-3t0j" \
        "TTsD-qI16PSu5HbILXFBg6eY7TFP5dCpYdS4Y4tW" \
        "ehcRYgN2z29-5NU64KuiNqtt99gBGAeuTkVwaOfMJ62"

push_service = FCMNotification(APIKEY)

print(APIKEY)
print(TOKEN)


def send_message(body, title):
    # 메시지 (data 타입)
    data_message = {
        "body": body,
        "title": title
    }

    # 데이터 형식으로 전달
    #result = push_service.single_device_data_message(registration_id=TOKEN, data_message=data_message)

    # 알림 형식으로 전달
    #result = push_service.notify_single_device(registration_id=TOKEN, message_title=title, message_body=body)

    # 그룹 전송
    result = push_service.notify_topic_subscribers(topic_name="GBTF", message_title=title, message_body=body)

    print("결과: ", result)


send_message("GBTW", "Test Message")

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
    print("결과: ", result)


send_message("GBTF Reminder", "반갑습니다")
'''
