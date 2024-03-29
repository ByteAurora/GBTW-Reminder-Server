from pyfcm import FCMNotification

APIKEY = ""

push_service = FCMNotification(APIKEY)


# 공지 전송 - 전체
def send_notify_to_all(title, message):
    return push_service.notify_topic_subscribers(topic_name="GBTF", message_title=title, message_body=message)


# 공지 전송 - 그룹
def send_notify_to_group(topic_name, title, message):
    return push_service.notify_topic_subscribers(topic_name=topic_name, message_title=title, message_body=message)


# 공지 전송 - 개인
def send_notify_to_target(token, title, message):
    return push_service.notify_single_device(registration_id=token, message_title=title, message_body=message)


# 데이터 전송 - 전체
def send_data_to_all(title, message):
    data_message = {
        "title": title,
        "body": message
    }
    return push_service.topic_subscribers_data_message(topic_name="GBTF", data_message=data_message)


# 데이터 전송 - 그룹
def send_data_to_group(topic_name, title, message):
    data_message = {
        "title": title,
        "body": message
    }
    return push_service.topic_subscribers_data_message(topic_name=topic_name, data_message=data_message)


# 데이터 전송 - 개인
def send_data_to_target(token, title, message):
    data_message = {
        "title": title,
        "body": message
    }
    return push_service.single_device_data_message(token, data_message=data_message)


# 데이터 전송(추가 데이터) - 전체
def send_data_to_all(data_message):
    return push_service.topic_subscribers_data_message(topic_name="GBTF", data_message=data_message)


# 데이터 전송(추가 데이터) - 그룹
def send_data_to_group(topic_name, data_message):
    return push_service.topic_subscribers_data_message(topic_name=topic_name, data_message=data_message)


# 데이터 전송(추가 데이터) - 개인
def send_data_to_target(token, data_message):
    return push_service.single_device_data_message(token, data_message=data_message)

