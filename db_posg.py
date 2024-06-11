import psycopg

class DbPosg:
    #реквизиты для подключения к PostgreSQL
    dsn = 'dbname=postgres user=postgres password=postgres host=postgres port=5432'
    #Создание таблицы,если не существует
    async def db_create(self):
        async with await psycopg.AsyncConnection.connect(self.dsn) as aconn:
            async with aconn.cursor() as acur:
                await acur.execute(
                    '''CREATE TABLE IF NOT EXISTS requests (
                        request_id SERIAL PRIMARY KEY,
                        user_id BIGINT NOT NULL,
                        model VARCHAR(100) NOT NULL,
                        prompt VARCHAR(4096) NOT NULL,
                        oa_response VARCHAR(4096) NOT NULL)''')
    #добавить в таблицу результаты запроса
    async def add_request(self, user_id, model,prompt, oa_response):
        async with await psycopg.AsyncConnection.connect(self.dsn) as aconn:
            async with aconn.cursor() as acur:
                await acur.execute(" INSERT INTO requests (user_id, model, prompt, oa_response) VALUES (%s, %s,%s,%s)", (user_id,model,prompt, oa_response,))
