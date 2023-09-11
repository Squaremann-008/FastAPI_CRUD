# FastAPI_CRUD API Documentation

This documentation provides details on how to set up and use the FastAPI CRUD API for managing "persons" resources. The API supports Create, Read, Update, and Delete (CRUD) operations for managing person data.

## API Endpoints

### Create a New Person

- **Endpoint:** `/api/`
- **HTTP Method:** POST
- **Request Body (JSON):**

    ```json
    {
        "name": "John Doe",
        "age": 30
    }
    ```

- **Response:**

    ```json
    {
        "id": 1,
        "name": "John Doe",
        "age": 30
    }
    ```

### Read Person by Name

- **Endpoint:** `/api/{user_name}`
- **HTTP Method:** GET
- **Response:**

    ```json
    {
        "id": 1,
        "name": "John Doe",
        "age": 30
    }
    ```

### Update Person by Name

- **Endpoint:** `/api/{user_name}`
- **HTTP Method:** PUT
- **Request Body (JSON):**

    ```json
    {
        "name": "John Doe",
        "age": 35
    }
    ```

- **Response:**

    ```json
    {
        "id": 1,
        "name": "John Doe",
        "age": 35
    }
    ```

### Delete Person by Name

- **Endpoint:** `/api/{user_name}`
- **HTTP Method:** DELETE
- **Response:**

    ```json
    {
        "id": 1,
        "name": "John Doe",
        "age": 35
    }
    ```

## Setting Up the FastAPI Application

Follow these steps to set up and deploy the FastAPI application on a server:

1. **Clone the Repository:**

    Clone the FastAPI CRUD project repository from GitHub to your server using `git clone`.

    ```bash
    git clone https://github.com/yourusername/fastapi-crud.git
    ```

2. **Install Dependencies:**

    Navigate to the project directory and install the required Python packages using `pip`.

    ```bash
    cd fastapi-crud
    pip install -r requirements.txt
    ```

3. **Database Configuration:**

    Configure your database connection in the `alembic.ini` file. Modify the `DATABASE_URL` variable to point to your database.

4. **Run Migrations:**

    Apply the initial database migrations to create the necessary database tables.

    ```bash
    alembic upgrade head
    ```

5. **Run the FastAPI App:**

    Start the FastAPI application using Uvicorn. Replace `app.main:app` with the appropriate import path for your FastAPI application.

    ```bash
    uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
    ```

6. **Access the API:**

    You can access the API by navigating to `http://your-server-ip:8000` in your web browser or using API testing tools like Postman.

7. **API Documentation:**

    For detailed API documentation and usage, refer to the API documentation provided above as well as`http://your-server-ip:8000/docs`.

## Known Limitations

- This API does not implement authentication or authorization mechanisms. Consider adding authentication and authorization layers for production deployments.
