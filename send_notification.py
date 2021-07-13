from pyfcm import FCMNotification

APIKEY = "AAAAeMqKdfs:APA91bGdm7YD_RVcTX9_1oiJy_S4rZEgHmu66d" \
         "mbZZRaiRvpGD_kYL0kR7amy2o-I0XhEUxw_cOyoUDMvlncNhc0" \
         "X16Y-xGb3-B_Dq1LIr8fpEKk9DuvR-KhvKm4B1ymvpYDGnnoDj6i"

push_service = FCMNotification(APIKEY)


# 공지 전송 - 그룹
def send_notify_to_all(title, message):
    return push_service.notify_topic_subscribers(topic_name="GBTF", message_title=title, message_body=message)


# 공지 전송 - 개인
def send_notify_to_target(token, title, message):
    return push_service.notify_single_device(registration_id=token, message_title=title, message_body=message)


# 데이터 전송 - 그룹
def send_data_to_all(title, message):
    data_message = {
        "title": title,
        "body": message
    }
    return push_service.topic_subscribers_data_message(topic_name="GBTF", data_message=data_message)


# 데이터 전송 - 개인
def send_data_to_target(token, title, message):
    data_message = {
        "title": title,
        "body": message
    }
    return push_service.single_device_data_message(token, data_message=data_message)
