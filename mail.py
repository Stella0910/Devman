import os
from dotenv import load_dotenv
import smtplib

load_dotenv()
login = os.getenv('login')
password = os.getenv('password')

server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
server.login(login, password)

letter = """\
From: i@stellad.ru
To: i@stellad.ru
Subject: Приглашение!
Content-Type: text/plain; charset="UTF-8";

Привет, {friend}! {sender} приглашает тебя на сайт {website}!

{website} — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на {website}? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → {website}  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл."""

friend_name = "Клим"

sender_name = "Стелла"

website = "https://dvmn.org/profession-ref-program/aniretake0910/yS1WO/"

letter = letter.format(friend=friend_name, sender=sender_name, website=website).encode("UTF-8")

server.sendmail('i@stellad.ru', 'i@stellad.ru', letter)
server.quit()
