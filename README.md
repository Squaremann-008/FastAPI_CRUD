# FastAPI_CRUD
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

    For detailed API documentation and usage, refer to the documentation.md file.

