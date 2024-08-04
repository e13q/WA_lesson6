# Публикация комиксов

В данном проекте реализована публикация комиксов в телеграм канале от [xkcd](https://xkcd.com/) с помощью [API](https://xkcd.com/json.html).

### Как установить

Python3 должен быть установлен. 
Используйте `pip` для установки зависимостей:
```
pip install -r requirements.txt
```

#### Telegram Bot
[Как создать бота и получить access токен](https://way23.ru/%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D0%B1%D0%BE%D1%82%D0%B0-%D0%B2-telegram.html)

Пример токена (unusable):
```
3871579594:BBE2p_C131bghARhYe7-qLsvnA2LqZRQT8V
```
После получения токена Вам необходимо создать файл .env и поместить токен в него.
Пример заполнения .env:
![image](https://github.com/e13q/WA_lesson4/assets/110967581/20aea039-5294-4f30-8db1-cdf8321ea40e)

Также, Вам понадобиться указать адрес телеграм канала в .env файле.
Пример заполнения .env:
![image](https://github.com/e13q/WA_lesson4/assets/110967581/aeb5f422-7dce-480b-a4c5-a08764b764f3)

Запустить скрипт можно выполнив команду:

```python3 main.py```

### Пример работы скрипта

![example5](https://github.com/user-attachments/assets/1cb3c944-c6ca-49b7-b04a-e37fa06e3423)


### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
