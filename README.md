# beers API connector

Данный коннектор позволяет получать данные о сортах пива с https://random-data-api.com и складывать их в БД PostgreSQL.

Шаги для установки (Linux):

```
clone https://github.com/changfenxia/beers_api_connector.git
cd beers_api_connector
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
mv default-db.ini db.ini
```

Далее в db.ini прописать доступы к базе данных.

Если таблица в базе данных не создана, для первоначального создания таблицы запустить скрипт db_init.py:
```
python3 db_init.py
```

Будет создана таблица со следующими полями:
```
id INTEGER PRIMARY KEY,
uid     VARCHAR(255) NOT NULL,
brand VARCHAR(255) NOT NULL,
name VARCHAR(255) NOT NULL,
style VARCHAR(255) NOT NULL,
hop VARCHAR(255) NOT NULL,
yeast VARCHAR(255) NOT NULL,
malts VARCHAR(255) NOT NULL,
ibu INTEGER NOT NULL,
alcohol REAL NOT NULL,
blg REAL NOT NULL
```

В основной папке лежит файл cron_script.sh, который позволяет настроить периодический запуск скрипта.
Чтобы данный скрипт отрабатывал каждые 12 часов, указываем в файле cron_script.sh пути к проекту и добавляем в crontab таск:
```
0 */12 * * * cd /path/to/cron_script && sh cron_script.sh
```
