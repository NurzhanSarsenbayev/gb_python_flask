# FastAPI CRUD Application

This project is a FastAPI-based CRUD (Create, Read, Update, Delete) application. It supports operations on `users`, `items`, and `orders` using an SQLite database.

## Features

- **Users**: Create, Read, Update, Delete
- **Items**: Create, Read, Update, Delete
- **Orders**: Create, Read, Update, Delete with validation

## Requirements

- Python 3.7+
- FastAPI
- SQLAlchemy
- Databases
- Uvicorn (for running the server)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/NurzhanSarsenbayev/gb_python_flask
    cd yourrepository
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the FastAPI application:
    ```bash
    uvicorn homework6.homework6:app --reload
    ```

2. Open your browser and go to `http://127.0.0.1:8000/docs` to access the interactive API documentation.

## Project Structure

- `homework6.py`: The main entry point of the application.
- `models.py`: SQLAlchemy models.
- `schemas.py`: Pydantic models (schemas) for data validation.
- `crud/`: Contains the CRUD operation functions for users, items, and orders.
- `requirements.txt`: List of dependencies.

## Endpoints

### Users
- `POST /users/`: Create a new user.
- `GET /users/`: Retrieve all users.
- `GET /users/{user_id}`: Retrieve a user by ID.
- `PUT /users/{user_id}`: Update a user by ID.
- `DELETE /users/{user_id}`: Delete a user by ID.

### Items
- `POST /items/`: Create a new item.
- `GET /items/`: Retrieve all items.
- `GET /items/{item_id}`: Retrieve an item by ID.
- `PUT /items/{item_id}`: Update an item by ID.
- `DELETE /items/{item_id}`: Delete an item by ID.

### Orders
- `POST /orders/`: Create a new order.
- `GET /orders/`: Retrieve all orders.
- `GET /orders/{order_id}`: Retrieve an order by ID.
- `PUT /orders/{order_id}`: Update an order status by ID.
- `DELETE /orders/{order_id}`: Delete an order by ID.