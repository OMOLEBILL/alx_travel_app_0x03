# ALX Travel App

## Description
ALX Travel App is a Django-based API that allows users to manage travel-related data such as listings, bookings, and reviews. The application uses Django REST Framework for API functionality and Swagger for API documentation.

## Features

### Listings Management:
- Create, read, update, and delete travel listings.
- Store details such as title, description, price per night, location, and availability.

### Bookings Management:
- Create, read, update, and delete bookings associated with listings.
- Store details such as user name, check-in date, and check-out date.

### Reviews Management (Optional for Future Development):
- Create, read, update, and delete reviews associated with listings.
- Store details such as user name, rating, and comments.

### Asynchronous Email Notifications:
- Uses Celery to send booking confirmation emails in the background.

### Interactive API Documentation:
- Swagger and Redoc endpoints for easy API exploration and testing.

## API Endpoints

### Listings Endpoints
| Method | Endpoint             | Description                 |
|--------|----------------------|-----------------------------|
| GET    | `/api/listings/`     | Retrieve all listings       |
| POST   | `/api/listings/`     | Create a new listing        |
| GET    | `/api/listings/<id>/` | Retrieve a specific listing |
| PUT    | `/api/listings/<id>/` | Update a specific listing   |
| DELETE | `/api/listings/<id>/` | Delete a specific listing   |

### Bookings Endpoints
| Method | Endpoint            | Description                 |
|--------|---------------------|-----------------------------|
| GET    | `/api/bookings/`     | Retrieve all bookings       |
| POST   | `/api/bookings/`     | Create a new booking        |
| GET    | `/api/bookings/<id>/` | Retrieve a specific booking |
| PUT    | `/api/bookings/<id>/` | Update a specific booking   |
| DELETE | `/api/bookings/<id>/` | Delete a specific booking   |

### Reviews Endpoints (Optional for Future Development)
| Method | Endpoint          | Description                 |
|--------|------------------|-----------------------------|
| GET    | `/api/reviews/`   | Retrieve all reviews        |
| POST   | `/api/reviews/`   | Create a new review         |
| GET    | `/api/reviews/<id>/` | Retrieve a specific review  |
| PUT    | `/api/reviews/<id>/` | Update a specific review    |
| DELETE | `/api/reviews/<id>/` | Delete a specific review    |

### Documentation Endpoints
| Method | Endpoint   | Description                     |
|--------|-----------|---------------------------------|
| GET    | `/swagger/` | Swagger UI for API documentation |
| GET    | `/redoc/`   | ReDoc UI for API documentation  |

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/OMOLEBILL/alx_travel_app_0x03.git
```

### 2. Create a Python Virtual Environment
Navigate into the project directory and create a virtual environment:
```bash
cd alx_travel_app_0x03
python -m venv venv
```
Activate the virtual environment:
- **On Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **On macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

### 3. Install Requirements
```bash
pip install -r alx_travel_app/requirements.txt
```

### 4. Configure the SQL Database
Create a `.env` file in the root of your project (`alx_travel_app/.env`) with the following variables:

```ini
CELERY_BROKER_URL=your_celery_broker_url
CELERY_RESULT_BACKEND=your_celery_result_backend
EMAIL_BACKEND=your_email_backend
EMAIL_HOST=your_email_host
EMAIL_PORT=your_email_port
EMAIL_USE_TLS=True_or_False
EMAIL_HOST_USER=your_email_host_user
EMAIL_HOST_PASSWORD=your_email_host_password

# Database configuration
NAME=your_database_name
USER=your_database_user
PASSWORD=your_database_password
HOST=your_database_host
PORT=your_database_port
```

### 5. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a Superuser (Optional)
For accessing the Django admin interface:
```bash
python manage.py createsuperuser
```

### 7. Running the Server
```bash
python manage.py runserver
```
Visit [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) for the admin panel and [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/) for API endpoints.

### 8. Running Celery Worker
Start the Celery worker (for asynchronous tasks like email notifications):
```bash
python -m celery -A alx_travel_app worker -l info
```

## Development and Contribution

### Branching:
- Use feature branches for new features and bug fixes.

### Testing:
- Write tests to ensure new changes do not break existing functionality.

### Issues & PRs:
- Create issues for any bugs or improvements and submit pull requests for review.

## License
This project is licensed under the BSD License.

## Contact
For any questions or support, please contact [omolebill01@gmail.com](mailto:omolebill01@gmail.com).