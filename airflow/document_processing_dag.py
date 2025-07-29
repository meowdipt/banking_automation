from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from main import process_documents

default_args = {
    'owner': 'banking_team',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'document_processing',
    default_args=default_args,
    schedule_interval=timedelta(hours=1),
    catchup=False
)

process_task = PythonOperator(
    task_id='process_documents',
    python_callable=process_documents,
    dag=dag,
)