![main_banner_top_133](https://user-images.githubusercontent.com/17138123/230913056-9f8285b3-25c3-4c34-9b7b-94254f8a0b27.png)

# GBTW Reminder Server

GBTW Reminder Server는 건쉽배틀 : 토탈워페어 홈페이지와 공식 유튜브에서 업데이트된 내용이 있을 경우, 해당 업데이트에 대한 알림을 설정한 클라이언트들에게 Notification을 보내주는 역할을 하는 서버입니다.
<br><br>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Amazon AWS-232F3E?style=flat-square&logo=amazonaws&logoColor=white"/>
  <img src="https://img.shields.io/badge/Firebase Cloud Messaging-FFCA28?style=flat-square&logo=firebase&logoColor=black"/>
  <br>
  <a href = "https://github.com/ILoveGameCoding/GBTW-Reminder-Client"><img src="https://img.shields.io/badge/CLIENT REPO-GBTW REMINDER CLIENT-informatoinal?style=for-the-badge"/></a>
  <br>
</p>

<br>

# 동작 원리
#### 1) 사이트에서 카테고리별로 변경사항이 있는지 탐색합니다. 카테고리는 다음과 같습니다.

```
- 공지사항: https://community.joycity.com/gw/notice
- 공지사항 세부정보 링크: https://community.joycity.com/gw/notice/view?boardUrl=notice&boardItemNo=

- 업데이트: https://community.joycity.com/gw/update
- 업데이트 세부정보 링크: https://community.joycity.com/gw/update/view?boardUrl=update&boardItemNo=

- CM채널: https://community.joycity.com/gw/cm
- CM채널 세부정보 링크: https://community.joycity.com/gw/cm/view?boardUrl=cm&boardItemNo=

- 이벤트: https://community.joycity.com/gw/event
- 이벤트 세부정보 링크: https://community.joycity.com/gw/event/view?boardUrl=event&boardItemNo=

- 이벤트 종료: https://community.joycity.com/gw/endEvent
- 이벤트 종료 세부정보 링크: https://community.joycity.com/gw/endEvent/view?boardUrl=endEvent&boardItemNo=

- 이벤트 당첨자 발표: https://community.joycity.com/gw/eventResult
- 이벤트 당첨자 발표 세부정보 링크: https://community.joycity.com/gw/eventResult/view?boardUrl=eventResult&boardItemNo=

- 공식 유튜브: https://www.youtube.com/user/jcenest/videos
```

<br>

#### 2) 변경된 정보가 있을 경우 해당 게시물의 OnClick에 해당되는 부분에서 게시물의 고유 번호를 가져옵니다

<br>

#### 3) Firebase Cloud Messaging을 이용하여 각 카테고리 알림을 구독한 클라이언트들에게 Notification을 전송합니다. 
이때 2) 에서 얻었던 게시물 ID를 각 카테고리 세부정보 링크 뒤에 추가하여 세부정보로 이동할 수 있는 링크를 생성합니다.
```
Notification 정보
- title: 알림 제목(ex. 공지사항, 업데이트 완료, 정기점검 완료 등)
- body: 변경된 게시물 제목(ex. 2월 15일 정기 점검 안내)
- link: 해당 게시물의 세부정보 링크
```

<br>

#### 4) Youtube의 경우, 홈페이지 크롤링과는 다른 방식으로 동작합니다.
```
1) Selenium 라이브러리의 웹 드라이버를 사용하여 페이지의 Body 요소를 찾고 페이지를 아래로 스크롤
- 동적으로 로드되는 웹 페이지의 콘텐츠를 크롤링하기 위함
- 일부 사이트의 경우 스크롤을 내릴 때 추가 콘텐츠가 로드되는데, Youtube도 이러한 형식

2) 1초 동안 대기 후 웹 드라이버로부터 페이지를 가져와 크롤링
- 바로 가져오려고 할 경우 페이지를 불러오지 못하는 경우가 있음

3) 찾은 동영상 요소들과 이전에 크롤링한 동영상 목록을 비교하여 새로운 동영상이 있는지 확인

4) 동영상 제목에 '건쉽' 또는 'Gunship'이 포함된 경우에만 Youtube 알림을 구독한 클라이언트들에게 Notification 전송

Notification 정보
- title: 유튜브 신규 영상
- body: 유튜브 동영상 제목(ex. [건쉽배틀 토탈워페어] 전투지휘사관학교 특강_연합과 연합혜택 모음.zip)
- link: 해당 유튜브 영상 링크
```

<br>

#### 5) 위의 과정이 종료되면 1분 뒤에 다시 해당 과정을 반복합니다.
