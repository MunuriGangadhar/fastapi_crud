# FastAPI JWT MongoDB Authentication System


## Project Structure

```plaintext
fastapi-jwt-mongodb/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── users.py
│   │   ├── admin.py
│   ├── schemas.py
│   ├── utils.py
│   ├── create_admin.py
└── requirements.txt
```

## Prerequisites

- **Python 3.8+**
- **MongoDB** (either local instance or a cloud instance like MongoDB Atlas)
- **FastAPI**
- **Uvicorn** (for running the FastAPI app)
- **JWT** and **Pydantic** for token handling and data validation

## Setup and Installation

### Step 1: Clone the repository

Clone the repository to your local machine:

```bash
git https://github.com/MunuriGangadhar/fastapi_crud.git
cd fastapi_crud
```

### Step 2: Install dependencies

Install the necessary dependencies using `pip`:

```bash
pip install -r requirements.txt
```

### Step 3: Configure MongoDB

1. If you're using **MongoDB Atlas** (cloud), create a MongoDB cluster and get the connection URI.
2. Update the **MongoDB URI** in the `config.py` file:

```python
MONGO_URI = "your-mongodb-atlas-uri"
DATABASE_NAME = "user_auth_db"
```

   - You can find the connection URI on your MongoDB Atlas dashboard.

### Step 4: Create Admin User (Optional)

Before running the app, you can create an admin user to manage users. Run the following script to create the admin:

```bash
python app/create_admin.py
```

This will create an admin with the email `admin@example.com` and the password `adminpassword`. You can modify these in the `config.py` file.

### Step 5: Run the FastAPI Application

Start the FastAPI app using **Uvicorn**:

```bash
uvicorn app.main:app --reload
```

This will start the application at `http://localhost:8000`.

### Step 6: Access the Swagger Docs

FastAPI automatically generates interactive documentation using **Swagger UI**. You can access the API documentation at:

```
http://localhost:8000/docs
```

This allows you to test the API endpoints directly from the browser.

### Step 7: Test the APIs

#### 1. **Login**

- **Endpoint**: `POST /auth/login`
- **Request Body**:

```json
{
    "email": "user@example.com",
    "password": "userpassword"
}
```

- **Response**:

```json
{
    "access_token": "jwt-token-here",
    "token_type": "bearer"
}
```

#### 2. **Create User**

- **Endpoint**: `POST /users/`
- **Request Body**:

```json
{
    "email": "newuser@example.com",
    "password": "newuserpassword",
    "full_name": "New User"
}
```

- **Response**:

```json
{
    "id": "user_id_here",
    "email": "newuser@example.com",
    "full_name": "New User",
    "role": "user"
}
```

#### 3. **Get User Details**

- **Endpoint**: `GET /users/{user_id}`
- **Headers**:

```plaintext
Authorization: Bearer {jwt-token-here}
```

- **Response**:

```json
{
    "id": "user_id_here",
    "email": "newuser@example.com",
    "full_name": "New User",
    "role": "user"
}
```

#### 4. **Update User**

- **Endpoint**: `PUT /users/{user_id}`
- **Request Body**:

```json
{
    "full_name": "Updated User",
    "password": "updatedpassword"
}
```

- **Response**:

```json
{
    "message": "User updated"
}
```

#### 5. **Delete User**

- **Endpoint**: `DELETE /users/{user_id}`
- **Response**:

```json
{
    "message": "User deleted"
}
```

#### 6. **Admin: Get All Users**

- **Endpoint**: `GET /admin/users`
- **Headers**:

```plaintext
Authorization: Bearer {admin-jwt-token-here}
```

- **Response**:

```json
[
    {
        "id": "user_id_here",
        "email": "newuser@example.com",
        "full_name": "New User",
        "role": "user"
    },
    {
        "id": "another_user_id_here",
        "email": "anotheruser@example.com",
        "full_name": "Another User",
        "role": "user"
    }
]
```

