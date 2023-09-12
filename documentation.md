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
<div class="mxgraph" style="max-width:100%;border:1px solid transparent;" data-mxgraph="{&quot;highlight&quot;:&quot;#000000&quot;,&quot;nav&quot;:true,&quot;resize&quot;:true,&quot;toolbar&quot;:&quot;zoom layers tags lightbox&quot;,&quot;edit&quot;:&quot;_blank&quot;,&quot;xml&quot;:&quot;&lt;mxfile&gt;&lt;diagram id=\&quot;C5RBs43oDa-KdzZeNtuy\&quot; name=\&quot;Page-1\&quot;&gt;&lt;mxGraphModel dx=\&quot;608\&quot; dy=\&quot;507\&quot; grid=\&quot;1\&quot; gridSize=\&quot;10\&quot; guides=\&quot;1\&quot; tooltips=\&quot;1\&quot; connect=\&quot;1\&quot; arrows=\&quot;1\&quot; fold=\&quot;1\&quot; page=\&quot;1\&quot; pageScale=\&quot;1\&quot; pageWidth=\&quot;827\&quot; pageHeight=\&quot;1169\&quot; math=\&quot;0\&quot; shadow=\&quot;0\&quot;&gt;&lt;root&gt;&lt;mxCell id=\&quot;WIyWlLk6GJQsqaUBKTNV-0\&quot;/&gt;&lt;mxCell id=\&quot;WIyWlLk6GJQsqaUBKTNV-1\&quot; parent=\&quot;WIyWlLk6GJQsqaUBKTNV-0\&quot;/&gt;&lt;mxCell id=\&quot;zkfFHV4jXpPFQw0GAbJ--0\&quot; value=\&quot;Person\&quot; style=\&quot;swimlane;fontStyle=2;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=26;horizontalStack=0;resizeParent=1;resizeLast=0;collapsible=1;marginBottom=0;rounded=0;shadow=0;strokeWidth=1;\&quot; parent=\&quot;WIyWlLk6GJQsqaUBKTNV-1\&quot; vertex=\&quot;1\&quot;&gt;&lt;mxGeometry x=\&quot;220\&quot; y=\&quot;120\&quot; width=\&quot;140\&quot; height=\&quot;120\&quot; as=\&quot;geometry\&quot;&gt;&lt;mxRectangle x=\&quot;230\&quot; y=\&quot;140\&quot; width=\&quot;160\&quot; height=\&quot;26\&quot; as=\&quot;alternateBounds\&quot;/&gt;&lt;/mxGeometry&gt;&lt;/mxCell&gt;&lt;mxCell id=\&quot;zkfFHV4jXpPFQw0GAbJ--1\&quot; value=\&quot;Id\&quot; style=\&quot;text;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;\&quot; parent=\&quot;zkfFHV4jXpPFQw0GAbJ--0\&quot; vertex=\&quot;1\&quot;&gt;&lt;mxGeometry y=\&quot;26\&quot; width=\&quot;140\&quot; height=\&quot;26\&quot; as=\&quot;geometry\&quot;/&gt;&lt;/mxCell&gt;&lt;mxCell id=\&quot;zkfFHV4jXpPFQw0GAbJ--3\&quot; value=\&quot;Name\&quot; style=\&quot;text;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;rounded=0;shadow=0;html=0;\&quot; parent=\&quot;zkfFHV4jXpPFQw0GAbJ--0\&quot; vertex=\&quot;1\&quot;&gt;&lt;mxGeometry y=\&quot;52\&quot; width=\&quot;140\&quot; height=\&quot;26\&quot; as=\&quot;geometry\&quot;/&gt;&lt;/mxCell&gt;&lt;mxCell id=\&quot;4nCdWEAtjM7COThYeFx4-1\&quot; value=\&quot;&amp;lt;div&amp;gt;&amp;amp;nbsp;Age&amp;lt;/div&amp;gt;\&quot; style=\&quot;text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;\&quot; parent=\&quot;zkfFHV4jXpPFQw0GAbJ--0\&quot; vertex=\&quot;1\&quot;&gt;&lt;mxGeometry y=\&quot;78\&quot; width=\&quot;140\&quot; height=\&quot;30\&quot; as=\&quot;geometry\&quot;/&gt;&lt;/mxCell&gt;&lt;/root&gt;&lt;/mxGraphModel&gt;&lt;/diagram&gt;&lt;/mxfile&gt;&quot;}"></div>
<script type="text/javascript" src="https://viewer.diagrams.net/js/viewer-static.min.js"></script> 