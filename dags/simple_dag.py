from datetime import datetime, timedelta

from airflow.decorators import task, dag
from airflow.models import Variable
from airflow.configuration import conf

default_args = {
    "owner": "manhnk9",
    "depends_on_past": False,
    "start_date": datetime(2021, 6, 29, 18),
    "email": ["manhnk9@ghtk.co"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(seconds=30),
}


@dag(
    "simple_dag",
    default_args=default_args,
    description="Ingest ClickHouse query log",
    schedule="0 0 * * *",
    catchup=False,
    is_paused_upon_creation=True,
)
def simple_dag():
    @task()
    def print_hello():
        print("Hello")
        print(conf)

    print_hello()

dag_obj = simple_dag()

if __name__ == "__main__":
    dag_obj.test()
