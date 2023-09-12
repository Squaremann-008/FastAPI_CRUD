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

    You can access the API by navigating to `http://your-server-ip:8000/api` in your web browser or using API testing tools like Postman.

7. **API Documentation:**

    For detailed API documentation and usage, refer to the API documentation provided above as well as`http://your-server-ip:8000/docs` for an interactive API.

## Known Limitations

- This API does not implement authentication or authorization mechanisms. Consider adding authentication and authorization layers for production deployments.

## DATABASE MODEL
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" width="381px" height="121px" viewBox="-0.5 -0.5 381 121" content="&lt;mxfile&gt;&lt;diagram id=&quot;C5RBs43oDa-KdzZeNtuy&quot; name=&quot;Page-1&quot;&gt;5VjbdtsoFP0aPyZLF0t2H23l0nTS1q3bpn0kAks0CFSEYytf34OE7nLitMk8zKzllehsDiD23sCxJ26Q7C8lSuP3AhM2cSy8n7hnE8fxrTn81UBeAp41K4FIUlxCdgOs6QMxoGXQLcUk6yQqIZiiaRcMBeckVB0MSSl23bSNYN1ZUxSRAbAOERuiNxSruETnzqzB3xIaxdXMtv+mbElQlWxWksUIi10Lcs8nbiCFUOVTsg8I09xVvNxc5Tfs+s6/fPcp+4W+Lv/58uHbSTnYxXO61EuQhKs/HvrhbnPx9tv05/d0dfFpZ10ubt+dmC7WPWJbw9eKyExws2KVVzRmO5owxCFabgRXa9MCJCwRoxGH5xDejkgA7olUFBRYmAYlUkDDmDJ8jXKx1WvIFArvqmgZC0kfYFjEoMkGAJqlMmZy/E7GWvcE2AJUkgxyVhUxdg1do0yZnFAwhtKM3hYvrFMSJCPKl0IpkVQDiS3HBJuoVroIlBR3tXd0/yPlMLJpNsi+ZUYjzyURCVEyhxTTWjvNbDW7ineNce2pweK2aatEZDZLVI9dT/cZNhfiEZDQzOf25puOzOePzAeKdKZDDITnSJGlpjFr2xAeWkttoMKczzCqPTDqFR6YFHhWLUMyslEH7ZilKKQ8ui5yzqYN8tmsU0MC+m5YYYWYYkx4YRWFFCrdpP2RCspVQYS3hA/QFVin3sSDFwogtpsYPjpdqkBwcBWihX0IWHVHtF1HjPXopn3aWHlXr6d81Ne1baOOoM9Vzx2o9wEl5D+n3yOnSKwSZh5fS2XP+fdUnvIA35wv1M/3s+Djl/gHudhPR/boxPGZJgbTe3iMSo/7KNEC8ttM/1vA9W2yYNJO4rg7DJN2fTQHggm4ds64KK8nylgPesJQCVhDT7LcxVSRNdhIz7iDcmig6WtpN5sfp537yEF/rHbDO39AdbNo+wAtLRUOrPXYG/LgdTid964nf+R6ckZI8l+ApDEv90giHC90gapLH4ayjIZV4TKEW3QBJTL/3g5+GHMVwdm+E+VVtKdKdzqxTi3HM0DR8dR3XRM3fXXQ7gpVHQUOdHnW8jHBg9r5uJomE1sZko6dYN0RUU+dDkOxW2J6I1pWmCQMKXrffd1Hyp2VPtVbXpr1vPSm55FyRaZXu4ruDeT2aia3vyNLHgYDgSVQ3kozt87fVUrOwKQBo6R43TV863qFE/Rgjf/sM/TlzwvP7mk88wbnxVg1+xJn6rDAWayuADjnOK2t8P+Rwu0f3SNSzF9GCgibr+DlHmp+x3DPfwM=&lt;/diagram&gt;&lt;/mxfile&gt;"><defs><clipPath id="mx-clip-4-31-132-26-0"><rect x="4" y="31" width="132" height="26"/></clipPath><clipPath id="mx-clip-4-57-132-26-0"><rect x="4" y="57" width="132" height="26"/></clipPath></defs><g><path d="M 0 26 L 0 0 L 140 0 L 140 26" fill="rgb(255, 255, 255)" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="all"/><path d="M 0 26 L 0 120 L 140 120 L 140 26" fill="none" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="none"/><path d="M 0 26 L 140 26" fill="none" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="none"/><g fill="rgb(0, 0, 0)" font-family="Helvetica" font-style="italic" pointer-events="none" text-anchor="middle" font-size="12px"><text x="69.5" y="17.5">Person</text></g><g fill="rgb(0, 0, 0)" font-family="Helvetica" pointer-events="none" clip-path="url(#mx-clip-4-31-132-26-0)" font-size="12px"><text x="5.5" y="43.5">Id</text></g><g fill="rgb(0, 0, 0)" font-family="Helvetica" pointer-events="none" clip-path="url(#mx-clip-4-57-132-26-0)" font-size="12px"><text x="5.5" y="69.5">Name</text></g><g transform="translate(-0.5 -0.5)"><switch><foreignObject pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility" style="overflow: visible; text-align: left;"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe flex-start; width: 138px; height: 1px; padding-top: 93px; margin-left: 2px;"><div data-drawio-colors="color: rgb(0, 0, 0); " style="box-sizing: border-box; font-size: 0px; text-align: left;"><div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: none; white-space: normal; overflow-wrap: normal;"><div> Age</div></div></div></div></foreignObject><text x="2" y="97" fill="rgb(0, 0, 0)" font-family="Helvetica" font-size="12px"> Age</text></switch></g><rect x="260" y="40" width="120" height="60" rx="9" ry="9" fill="rgb(255, 255, 255)" stroke="rgb(0, 0, 0)" pointer-events="none"/><path d="M 250.63 77.98 L 146.37 78" fill="none" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="none"/><path d="M 255.88 77.98 L 248.88 81.48 L 250.63 77.98 L 248.88 74.48 Z" fill="rgb(0, 0, 0)" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="none"/><path d="M 141.12 78 L 148.12 74.5 L 146.37 78 L 148.12 81.5 Z" fill="rgb(0, 0, 0)" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="none"/><g transform="translate(-0.5 -0.5)"><switch><foreignObject pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility" style="overflow: visible; text-align: left;"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 58px; height: 1px; padding-top: 70px; margin-left: 291px;"><div data-drawio-colors="color: rgb(0, 0, 0); " style="box-sizing: border-box; font-size: 0px; text-align: center;"><div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: none; white-space: normal; overflow-wrap: normal;">Client Side</div></div></div></foreignObject><text x="320" y="74" fill="rgb(0, 0, 0)" font-family="Helvetica" font-size="12px" text-anchor="middle">Client Side</text></switch></g><g transform="translate(-0.5 -0.5)"><switch><foreignObject pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility" style="overflow: visible; text-align: left;"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 78px; height: 1px; padding-top: 70px; margin-left: 161px;"><div data-drawio-colors="color: rgb(0, 0, 0); " style="box-sizing: border-box; font-size: 0px; text-align: center;"><div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: none; white-space: normal; overflow-wrap: normal;">API Endpoint</div></div></div></foreignObject><text x="200" y="74" fill="rgb(0, 0, 0)" font-family="Helvetica" font-size="12px" text-anchor="middle">API Endpoint</text></switch></g></g><switch><g requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"/><a transform="translate(0,-5)" xlink:href="https://www.diagrams.net/doc/faq/svg-export-text-problems" target="_blank"><text text-anchor="middle" font-size="10px" x="50%" y="100%">Text is not SVG - cannot display</text></a></switch></svg>