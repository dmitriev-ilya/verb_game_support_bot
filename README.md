# Бот поддержки проекта "Игра Глаголов"

Проект включает в себя ботов поддержки для Telegram и VK, основанные на ИИ от Google - [Dialogflow](https://dialogflow.com/).
Боты предназначены для автоматизации техподдержки пользователей: ответы на самые распространённые вопросы с помощью предобученной модели ИИ.

Пример рабочего Telegram-бота [@VerbGameSupportBot](https://t.me/VerbGameSupportBot):

![image](https://dvmn.org/media/filer_public/7a/08/7a087983-bddd-40a3-b927-a43fb0d2f906/demo_tg_bot.gif)

Пример рабочего VK-бота https://vk.com/club221222850 :

![image](https://dvmn.org/media/filer_public/1e/f6/1ef61183-56ad-4094-b3d0-21800bdb8b09/demo_vk_bot.gif)

## Установка

Скачайте файлы из репозитория. Python3 должен быть уже установлен. 

Затем используйте `pip` (или `pip3`) для установки зависимостей:
```
pip install -r requirements.txt
```
Помимо этого, для работы понадобится создать файл `.env` в корневом каталоге проекта. Данный файл необходим для работы с переменными окружения и должен содержать в себе переменные: 
```
SUPPORT_BOT_TELEGRAM_TOKEN=<SUPPORT_BOT_TELEGRAM_TOKEN>
GCLOUD_PROJECT_ID=<GCLOUD_PROJECT_ID>
TELEGRAM_USER_ID=<TELEGRAM_USER_ID>
VK_GROUP_API_TOKEN=<VK_GROUP_API_TOKEN>
GOOGLE_APPLICATION_CREDENTIALS=<credential path>
```

Для получения `GCLOUD_PROJECT_ID` необходимо создать проект на Google Cloud согласно [инструкции](https://cloud.google.com/dialogflow/es/docs/quick/setup), а затем агента [Dialogflow](https://cloud.google.com/dialogflow/es/docs/quick/build-agent). **Важно, чтобы ID проектов Dialogflow и Google Cloud совпадали!!!**. 

Создайте `API-Key` согласно [туториалу](https://cloud.google.com/docs/authentication/api-keys) и добавьте путь к `credentials.json` в переменную `GOOGLE_APPLICATION_CREDENTIALS`.


Также необходимо создать Telegram-бота для получения `SUPPORT_BOT_TELEGRAM_TOKEN`. Для этого нужно обратиться к [@BotFather](https://telegram.me/BotFather). Подробная инструкция по настройке и созданию бота приведена здесь - [Инструкция по созданию Telegram-бота](https://way23.ru/%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D0%B1%D0%BE%D1%82%D0%B0-%D0%B2-telegram.html)

`TELEGRAM_USER_ID` можно получить, обратившись к боту [@userinfobot](https://t.me/getmyid_bot)

Для получения `VK_GROUP_API_TOKEN` создайте группу [VK](https://vk.com/groups?tab=admin), в настройках группы включите сообщения сообщества и разрешите боту отправку сообщений. Получить токен группы можно также в настройках:

![image](https://github.com/dmitriev-ilya/verb_game_support_bot/assets/67222917/3a1169a7-eb38-48b0-8cb3-0f770bdea080)

## Обучение Dialogflow

Для корректной работы ботов предварительно необходимо обучить Dialogflow работать с нужными фразами от пользователей. Тренировочные фразы содержатся в файле `questions.json`. Для запуска обучающего скрипта используйте команду:
```
python3 dialogflow_bot.py
```

## Использование скриптов

Для запуска ботов в консоли, находясь в папке с проектом, используйте следующую команду:

```
python3 python3 vk_bot.py
```

или 

```
python3 telegram_bot.py
```
