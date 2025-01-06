# Factory Management System

## Project Overview

This Flask-based Factory Management System provides an API to manage employees, products, orders, customers, and production records in a factory setting. Additionally, it supports **advanced analytics** for analyzing employee performance, customer lifetime value, and production efficiency. Built with Flask, SQLAlchemy, Flask-Migrate, and Flask-Limiter, it ensures scalability, database migrations, and API rate-limiting.

---

## Features

- **Employee Management:** CRUD operations to manage employees.
- **Product Management:** CRUD operations to manage products.
- **Order Management:** CRUD operations to manage orders.
- **Customer Management:** CRUD operations to manage customers.
- **Production Management:** CRUD operations to manage production records.
- **Advanced Analytics:** SQLAlchemy-powered queries for performance tracking and business insights.
- **Rate Limiting:** Prevents abuse with defined API limits.
- **Database Migrations:** Tracks schema changes using Alembic and Flask-Migrate.
- **Error Logging:** Logs errors and server activities using RotatingFileHandler.

---

## Tech Stack

- **Backend:** Flask (Python)
- **Database:** MySQL with SQLAlchemy ORM
- **API Testing:** Postman
- **Rate Limiting:** Flask-Limiter
- **Migrations:** Flask-Migrate

---

## Folder Structure

```
factory_management/
├── blueprints/                      # Blueprints for modular route management
│   ├── employee_blueprint.py
│   ├── product_blueprint.py
│   ├── order_blueprint.py
│   ├── customer_blueprint.py
│   ├── production_blueprint.py
│   ├── analytics_blueprint.py       # NEW: Analytics API routes for reporting and insights
├── controllers/                     # Controllers for business logic
├── migrations/                      # Database migration files
├── models/                          # Database models
│   ├── __init__.py                  # Initializes database models
│   ├── employee.py
│   ├── product.py
│   ├── order.py
│   ├── customer.py
│   ├── production.py
├── schemas/                         # Schemas for data validation and serialization
│   ├── __init__.py
│   ├── customer_schema.py
│   ├── employee_schema.py
│   ├── order_schema.py
│   ├── product_schema.py
│   ├── production_schema.py
├── services/                        # Business logic for API endpoints
│   ├── __init__.py
│   ├── customer_service.py
│   ├── employee_service.py
│   ├── order_service.py
│   ├── product_service.py
│   ├── production_service.py
├── queries/                         # NEW: Advanced SQLAlchemy queries
│   ├── __init__.py
│   ├── analytic_queries.py          # Complex queries for analytics
├── logs/                            # Logs generated for debugging and monitoring
│   ├── factory_management.log
├── config.py                         # Configuration settings
├── limiter.py                        # Rate limiter setup
├── db_create.py                      # Script to manually create database tables
├── requirements.txt                  # Required Python packages
├── README.md                         # Project documentation
├── app.py                            # Main application entry point
├── utils.py                          # Utility functions
├── install.txt                       # Instructions for installation

---

## Prerequisites

- Python 3.12+
- MySQL Database Server
- Postman (optional for API testing)
- Virtual Environment (recommended)

---

## Setup Instructions

1. **Clone the Repository:**

   ```bash
   git clone <repository-url>
   cd factory_management
   ```

2. **Create Virtual Environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/MacOS
   .\venv\Scripts\activate    # Windows
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Database:**

   - Update database credentials in `config.py`.
   - Create the database manually in MySQL:
     ```sql
     CREATE DATABASE factory_db;
     ```

5. **Initialize Migrations:**

   ```bash
   flask db init
   flask db migrate -m "Initial migration."
   flask db upgrade
   ```

6. **Run the Application:**

   ```bash
   python app.py
   ```

7. **API Testing with Postman:**

   - Import the Postman collection provided (if available).
   - Test CRUD operations and analytics endpoints:
     - `/employees`
     - `/products`
     - `/orders`
     - `/customers`
     - `/production`
     - `/analytics`

---

## New Analytics Endpoints

### 1. Analyze Employee Performance

**Endpoint:**
```
GET /analytics/employee-performance
```
**Description:**
Fetches the total quantity of products each employee has produced.

**Example Response:**
```json
{
  "performance": [
    {"employee_name": "John Doe", "total_quantity": 150},
    {"employee_name": "Jane Smith", "total_quantity": 120}
  ]
}
```

---

### 2. Identify Top-Selling Products

**Endpoint:**
```
GET /analytics/top-products
```
**Description:**
Finds top-selling products based on total quantity ordered.

**Example Response:**
```json
{
  "products": [
    {"product_name": "Widget A", "total_quantity": 200},
    {"product_name": "Gadget B", "total_quantity": 180}
  ]
}
```

---

### 3. Customer Lifetime Value

**Endpoint:**
```
GET /analytics/customer-ltv
```
**Query Parameters:**
- `threshold` (Optional): Minimum total value filter.

**Example Request:**
```
GET /analytics/customer-ltv?threshold=500
```
**Example Response:**
```json
{
  "customers": [
    {"customer_name": "Alice Brown", "total_value": 750.00},
    {"customer_name": "Bob Green", "total_value": 600.00}
  ]
}
```

---

### 4. Production Efficiency

**Endpoint:**
```
GET /analytics/production-efficiency
```
**Query Parameters:**
- `date` (Required): Specific production date (YYYY-MM-DD).

**Example Request:**
```
GET /analytics/production-efficiency?date=2024-01-01
```
**Example Response:**
```json
{
  "efficiency": [
    {"product_name": "Widget A", "total_produced": 100},
    {"product_name": "Gadget B", "total_produced": 50}
  ]
}
```

---

## Environment Variables

| Variable Name             | Description                       | Default Value                                         |
| ------------------------- | --------------------------------- | ----------------------------------------------------- |
| SQLALCHEMY\_DATABASE\_URI | Database connection string        | mysql+pymysql://root:password@localhost/factory_db |
| SECRET\_KEY               | Secret key for session management | your_secret_key_here                               |

---

## Common Issues and Fixes

1. **Migrations Not Detected:**

   ```bash
   flask db migrate -m "Rebuild migration."
   flask db upgrade
   ```

2. **Rate Limiting Error:**

   - Verify `limiter` is properly imported from `limiter.py`.
   - Ensure `limiter.init_app(app)` is called before registering blueprints.

---

## License

This project is licensed under the MIT License.

---

## Contributors

- **Lead Developer:** J. Murillo
- **Backup Support:** Replace me if the lead developer goes missing.

---

## Final Notes

- Validate database configurations and migrations before running.
- Use Postman or cURL to test all endpoints.
- Update `requirements.txt` if dependencies change.

