# Инструкции по запуску и настройке бота

## Файл .env

    TOKEN=

    # Redis variables
    REDIS_SERVER=
    REDIS_PORT=
    REDIS_DB=
    REDIS_PASSWORD=

    # postgreSQL variables
    POSTGRES_DRV=
    POSTGRES_DRV_FOR_MIGRATIONS=
    POSTGRES_USER=
    POSTGRES_PASSWORD=
    POSTGRES_SERVER=
    POSTGRES_DB=
    POSTGRES_PORT=







# БД

Ставим PostgreSQL, создаем пользователя с привелегиями создания бд. Этим пользователем создаем бд 
у меня название бд "team_bot". это же название прописываем в переменную `POSTGRES_DB` в файле .env и заполняем остальные переменные. 

по редису проще. ставим редис открываем файл

    $ sudo nano /etc/redis/redix.conf

ищем строку и вставляем свой пароль

    requirepass "YourStrongPassword"

Этот же пароль добавляем к переменной `REDIS_PASSWORD` в файле .env

Перезапускаем редис и пользуемся

    sudo systemctl restart redis.service

# Миграции

В проекте растроены миграции поэтому не надо делать инициализацию для `alembic`!!!

Начинаем сразу с миграции

    $ $ alembic revision --autogenerate -m "initial"

Это создаст записи инициалищации таблицы. Теперь остается мигрировать модели в таблицы БД

    $ alembic upgrade head

Это создаст все нужные таблицы из моделей в проекте. Далее при изменениях таблиц просто нужно делать

    $ alembic upgrade head

При каких то кординальных изменениях таблиц проще всего будет делать сброс данных в них в PstgreSQL:

    $ psql -U username -d dbname
    $ DELETE FROM tablename;

    