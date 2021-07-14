import time
import requests
import copy

import send_notification as sender

from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from puvritualdisplay import Display

display = Display(visible=0, size=(1024, 768))
display.start()

chrome_driver_path = './chromedriver'

state = True

driver = webdriver.Chrome(chrome_driver_path)

def check_community():
    before_notice_list = list()
    before_update_list = list()
    before_event_list = list()
    before_end_event_list = list()
    before_event_winner_list = list()
    before_youtube_list = list()

    while state:
        new_notice_list = list()
        new_update_list = list()
        new_event_list = list()
        new_end_event_list = list()
        new_event_winner_list = list()
        new_youtube_list = list()

        driver.get('https://www.youtube.com/user/jcenest/videos')

        # 신규 공지 확인
        page = requests.get("https://community.joycity.com/gw/notice")
        soup = bs(page.text, "html.parser")
        elements = soup.select('div.sub_title a')

        for index, element in enumerate(reversed(elements), 1):
            title = element.text.strip()

            new_notice_list.append(title)

            if title not in before_notice_list:
                print('공지사항', element.text.strip())
                print(sender.send_notify_to_group('notice', '공지사항', element.text.strip()))
        before_notice_list = copy.deepcopy(new_notice_list)

        # 신규 업데이트 확인
        page = requests.get("https://community.joycity.com/gw/update")
        soup = bs(page.text, "html.parser")
        elements = soup.select('div.sub_title a')

        for index, element in enumerate(reversed(elements), 1):
            title = element.text.strip()

            new_update_list.append(title)

            if title not in before_update_list:
                if '업데이트' in title:
                    if '완료' in title:
                        print('업데이트 완료: ', element.text.strip())
                        print(sender.send_notify_to_group('update', '업데이트 완료', element.text.strip()))
                    else:
                        print('업데이트 예정: ', element.text.strip())
                        print(sender.send_notify_to_group('update', '신규 업데이트 공지', element.text.strip()))
                elif '정기' in title:
                    if '완료' in title:
                        print('업데이트 완료: ', element.text.strip())
                        print(sender.send_notify_to_group('update', '업데이트 완료', element.text.strip()))
                    else:
                        print('업데이트 예정: ', element.text.strip())
                        print(sender.send_notify_to_group('update', '정기점검 공지', element.text.strip()))
                elif '임시' in title:
                    if '완료' in title:
                        print('임시점검 완료: ', element.text.strip())
                        print(sender.send_notify_to_group('update', '임시점검 완료', element.text.strip()))
                    else:
                        print('임시점검 예정: ', element.text.strip())
                        print(sender.send_notify_to_group('update', '긴급 공지: 임시점검', element.text.strip()))
        before_update_list = copy.deepcopy(new_update_list)

        # 신규 이벤트 확인
        page = requests.get("https://community.joycity.com/gw/event")
        soup = bs(page.text, "html.parser")
        elements = soup.select('div.sub_title a')

        for index, element in enumerate(reversed(elements), 1):
            title = element.text.strip()

            new_event_list.append(title)

            if title not in before_event_list:
                if '쿠폰' in title:
                    print('이벤트(쿠폰): ', element.text.strip())
                    print(sender.send_notify_to_group('event', '신규 이벤트 공지(쿠폰)', element.text.strip()))
                elif '원스토어' in title:
                    print('이벤트(원스토어): ', element.text.strip())
                    print(sender.send_notify_to_group('event', '원스토어 이벤트', element.text.strip()))
                else:
                    print('이벤트: ', element.text.strip())
                    print(sender.send_notify_to_group('event', '신규 이벤트 공지', element.text.strip()))
        before_event_list = copy.deepcopy(new_event_list)

        # 종료 이벤트 확인
        page = requests.get("https://community.joycity.com/gw/endEvent")
        soup = bs(page.text, "html.parser")
        elements = soup.select('div.sub_title a')

        for index, element in enumerate(reversed(elements), 1):
            title = element.text.strip()

            new_end_event_list.append(title)

            if title not in before_end_event_list:
                print('이벤트 종료: ', element.text.strip())
                print(sender.send_notify_to_group('endEvent', '이벤트 종료', element.text.strip()))
        before_end_event_list = copy.deepcopy(new_end_event_list)

        # 이벤트 당첨자 발표
        page = requests.get("https://community.joycity.com/gw/eventResult")
        soup = bs(page.text, "html.parser")
        elements = soup.select('div.sub_title a')

        for index, element in enumerate(reversed(elements), 1):
            title = element.text.strip()

            new_event_winner_list.append(title)

            if title not in before_event_winner_list:
                print('이벤트 당첨자 발표: ', element.text.strip())
                print(sender.send_notify_to_group('eventWinner', '이벤트 당첨자 발표', element.text.strip()))
        before_event_winner_list = copy.deepcopy(new_event_winner_list)

        # 유튜브 신규 영상
        body = driver.find_element_by_tag_name('body')
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        page = driver.page_source
        soup = bs(page, "lxml")
        elements = soup.find_all('a', 'yt-simple-endpoint style-scope ytd-grid-video-renderer')

        for index, element in enumerate(reversed(elements), 1):
            title = element.text.strip()
            new_youtube_list.append(title)
            video_title = title.strip()

            if title not in before_youtube_list and ('건쉽' in video_title or 'Gunship' in video_title):
                notification_title = "유튜브 신규 영상"
                if '쿠폰' in video_title:
                    notification_title = notification_title + "(쿠폰)"
                print(title, element.text.strip())
                print(sender.send_notify_to_group('youtube', notification_title, element.text.strip()))
        before_youtube_list = copy.deepcopy(new_youtube_list)

        time.sleep(5)