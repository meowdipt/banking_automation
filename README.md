# Banking Automation

## Описание
Проект для автоматизации обработки банковских выгрузок и первичных документов (счета, акты, накладные) из различных форматов (PDF, Excel, XML, EDI).

## Технологии
- Python 3.8+
- Pandas, Tabula, Bots-EDI
- PostgreSQL
- Airflow
- RabbitMQ
- Docker

## Запуск проекта
1. Клонируйте репозиторий
2. Установите зависимости: `pip install -r requirements.txt`
3. Запустите Docker: `docker-compose up -d`
4. Инициализируйте БД: `docker exec -i banking_automation_postgres_1 psql -U postgres -d banking_docs < init_db.sql`
5. Запустите обработчик: `python main.py`

## Структура проекта
