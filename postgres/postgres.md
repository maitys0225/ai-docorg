# Installing PostgreSQL in Docker and Accessing It

## 1. Pull the PostgreSQL Docker Image
First, pull the PostgreSQL Docker image from Docker Hub:

```sh
docker pull postgres:latest
```

## 2. Run the PostgreSQL Container with a Volume
Run a new container with the PostgreSQL image, using a Docker volume to persist data. Replace `Password1234` with a secure password:

```sh
docker run --name postgres-container -e POSTGRES_PASSWORD=Password1234 -d -p 5432:5432 -v postgres-data:/var/lib/postgresql/data postgres:latest
```

## 3. Verify the Container is Running
Check if the PostgreSQL container is running:

```sh
docker ps
```

## 4. Install `psql` (PostgreSQL Command-Line Tool) on macOS
To access PostgreSQL using the `psql` command-line tool, you need to install it on your macOS machine.

### On macOS
If you are using macOS, you can install `psql` using Homebrew:

1. **Install Homebrew** (if you haven't already):
   Open your terminal and run the following command to install Homebrew:

   ```sh
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **Install PostgreSQL**:
   Once Homebrew is installed, you can install PostgreSQL, which includes the `psql` tool:

   ```sh
   brew install postgresql
   ```

3. **Verify Installation**:
   After the installation is complete, verify that `psql` is installed by running:

   ```sh
   psql --version
   ```

## 5. Access PostgreSQL
You can access PostgreSQL in several ways:

### a. Using `psql` Command-Line Tool
If you have `psql` installed on your host machine, you can connect to the PostgreSQL container:

```sh
psql -h localhost -p 5432 -U postgres
```

You will be prompted to enter the password you set (`Password1234`).

### b. Using Docker Exec
You can also access the PostgreSQL container directly using Docker:

```sh
docker exec -it postgres-container psql -U postgres
```

### c. Using a GUI Tool
You can use a GUI tool like pgAdmin, DBeaver, or any other database client. Connect to PostgreSQL using the following details:
- **Host**: `localhost`
- **Port**: `5432`
- **Username**: `postgres`
- **Password**: `Password1234`

## Example `docker-compose.yml` File
Alternatively, you can use Docker Compose to manage your PostgreSQL container with a volume. Create a `docker-compose.yml` file with the following content:

```yaml
version: '3.1'

services:
  db:
    image: postgres:latest
    environment:
      POSTGRES_PASSWORD: Password1234
    ports:
      - "5432:5432"
    volumes:
      - postgres-data:/var/lib/postgresql/data
    networks:
      - pgnetwork

  pgadmin:
    image: dpage/pgadmin4
    environment:
      PGADMIN_DEFAULT_EMAIL: maitys@rainswork.com
      PGADMIN_DEFAULT_PASSWORD: Password1234
    ports:
      - "80:80"
    volumes:
      - /Users/maitys/repos/ai-docorg/postgres/servers.json:/pgadmin4/servers.json
    networks:
      - pgnetwork

networks:
  pgnetwork:

volumes:
  postgres-data:
```

Run the following command to start the PostgreSQL and pgAdmin containers:

```sh
docker-compose up -d
```

## Installing pgAdmin in Docker
To install pgAdmin in Docker and access the PostgreSQL database, follow these steps:

### 1. Pull the pgAdmin Docker Image
First, pull the pgAdmin Docker image from Docker Hub:

```sh
docker pull dpage/pgadmin4
```

### 2. Run the pgAdmin Container
Run a new container with the pgAdmin image. Replace `your_email` and `your_password` with your email and a secure password:

```sh
docker run --name pgadmin-container -e PGADMIN_DEFAULT_EMAIL=maitys@rainswork.com -e PGADMIN_DEFAULT_PASSWORD=Password1234 -d -p 80:80 dpage/pgadmin4
```

### 3. Access pgAdmin
Open your web browser and go to `http://localhost`. Log in with the email and password you set in the previous step.

### 4. Connect pgAdmin to PostgreSQL
1. After logging in to pgAdmin, click on "Add New Server".
2. In the "General" tab, enter a name for the server (e.g., `PostgreSQL`).
3. In the "Connection" tab, enter the following details:
   - **Host name/address**: `host.docker.internal`
   - **Port**: `5432`
   - **Username**: `postgres`
   - **Password**: `Password1234`
4. Click "Save" to connect to the PostgreSQL database.

## Creating a PostgreSQL Database
Once connected to PostgreSQL, you can create a new database using the following steps:

### a. Using `psql` Command-Line Tool
1. Access the PostgreSQL container using `psql` or Docker Exec.
2. Run the following command to create a new database:

```sh
CREATE DATABASE mydatabase;
```

### b. Using pgAdmin
1. In pgAdmin, right-click on the "Databases" node in the Browser panel.
2. Select "Create" > "Database...".
3. In the "General" tab, enter the name of the database (e.g., `mydatabase`).
4. Click "Save" to create the database.

These steps will help you install pgAdmin in Docker and access the PostgreSQL database using pgAdmin, as well as persist your PostgreSQL data using Docker volumes and preconfigure pgAdmin with connection settings.