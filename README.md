# Airflow Celery Docker

This repository is primarily used for local development. It runs Apache Airflow with the Celery Executor using Docker Compose.

## Prerequisites

- Docker
- Docker Compose

## Getting Started
The docker-compose.yml file contains several service definitions:

- **airflow-scheduler**: The scheduler monitors all tasks and DAGs, then triggers the task instances once their dependencies are complete.
- **airflow-webserver**: The webserver is available at [http://localhost:8080](http://localhost:8080).
- **airflow-worker**: The worker that executes the tasks given by the scheduler.
- **airflow-triggerer**: The triggerer runs an event loop for deferrable tasks.
- **airflow-init**: The initialization service.
- **postgres**: The database.
- **redis**: The broker that forwards messages from scheduler to worker.

Optionally, you can enable Flower by adding the `--profile flower` option, e.g., `docker compose --profile flower up`, or by explicitly specifying it on the command line, e.g., `docker compose up flower`.

- **flower**: The Flower app for monitoring the environment. It is available at [http://localhost:5555](http://localhost:5555).

All these services allow you to run Airflow with CeleryExecutor. For more information, see the [Architecture Overview](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/overview.html).

Some directories in the container are mounted, which means that their contents are synchronized between your computer and the container:

- `./dags`: You can put your DAG files here.
- `./logs`: Contains logs from task execution and scheduler.
- `./config`: You can add a custom log parser or add `airflow_local_settings.py` to configure cluster policy.
- `./plugins`: You can put your custom plugins here.



1. Clone the repository:
    ```sh
    git clone https://github.com/nukima/airflow-celery-docker.git
    cd airflow-celery-docker
    ```

2. Start the Airflow services:
    ```sh
    # run database migrations and create first user account
    docker compose up airflow-init
    # start the services
    docker compose --profile flower up
    ```

3. Access the Airflow web interface:
    - Open your browser and go to `http://localhost:8080`
    - Default login credentials:
        - Username: `airflow`
        - Password: `airflow`

## Configuration

You can configure Airflow by modifying the `airflow.cfg` file located in the `config` directory.

## Stopping the Services

To stop the Airflow services, run:
```sh
docker compose down --volumes --remove-orphans
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## Contact

For any questions or support, please open an issue in this repository.
