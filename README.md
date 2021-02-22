# IAB 실무응용2
## IoT, 인공지능, 빅데이터(IAB)의 실무응용2 개인 프로젝트 (2020년 동계)<br>
- 연구자: 지구환경과학부/연합전공 인공지능반도체공학 김현진<br>
- 연구 주제: 손동작을 이용한 라즈베이 파이 동작<br>
- 연구 기간: 2020.12.22. Tue.~2021.01.22. Fri.<br>
- 코딩기술서: [서울대학교 글로벌공학교육센터 GECE](http://gece.snu.ac.kr/gecexe/index.php?mid=gece_lms&category=51919&document_srl=57165)

----------

## 손동작을 이용한 라즈베이 파이 동작
- 이 프로젝트에서는 직접 손을 대지 않고도 기기를 조작하고자 하는 기조를 따라서, 카메라를 이용해 손동작을 인식하고, 인식한 손동작에 따라서 기기가 움직이는 일련의 과정을 구현했다. YOLOv4-tiny를 이용해서 손 모양을 학습시키고, OpenCV에 학습된 모델을 불러와 사물을 탐지, gpiozero를 이용해서 탐지된 동작에 맞는 라즈베리 파이 동작을 했다. 추가적으로 라즈베리 파이와 Apache 서버 간의 php 통신을 이용해 휴대전화, 노트북 등 라즈베리 파이와 같은 와이파이에 연결된 기기로 동작을 제어할 수 있는 기능을 추가했다. 라즈베리 파이에서 일어나는 동작에는 화면 캡쳐와 모터 작동이 있다.

## 개요
- 사물인식 (myYoloIsTiny)
  - 데이터 수집
  - CNN 기반 모델을 이용한 학습 (YOLOv4-tiny)
- 라즈베리 파이 동작 (raspberryPiCode)
  - MyYoloIsVeryTiny.py
- php 통신 (phpCode)
  - pjServer.php

## 참고한 페이지
- https://github.com/puzzledqs/BBox-Label-Tool 
