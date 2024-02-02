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