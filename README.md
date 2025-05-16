# Django User Management API

This is a Django REST Framework (DRF) based API for user management. It provides features for user registration, login, profile updates, password changes, and account deletion using token-based authentication.

## Features

- ✅ User registration with password validation
- ✅ Login via token authentication
- ✅ Logout and token invalidation
- ✅ Retrieve and update own user profile
- ✅ Change password securely
- ✅ Admin access to all user records
- ✅ Delete user account

## Technologies Used

- Python 3
- Django
- Django REST Framework
- Token Authentication

## API Endpoints

| Method | Endpoint             | Description                          | Permissions         |
|--------|----------------------|--------------------------------------|---------------------|
| GET    | `/users/`            | List all users (admin only)          | Admin               |
| POST   | `/users/`            | Register a new user                  | Public              |
| GET    | `/users/<id>/`       | Retrieve user by ID                  | Authenticated       |
| PUT    | `/users/<id>/`       | Update user by ID                    | Admin               |
| DELETE | `/users/<id>/`       | Delete user by ID                    | Admin               |
| GET    | `/profile/`          | Get logged-in user's profile         | Authenticated       |
| PUT    | `/profile/`          | Update logged-in user's profile      | Authenticated       |
| PATCH  | `/profile/`          | Partially update user's profile      | Authenticated       |
| POST   | `/change-password/`  | Change user password                 | Authenticated       |
| POST   | `/login/`            | Authenticate user and return token   | Public              |
| POST   | `/logout/`           | Logout and revoke user token         | Authenticated       |
| DELETE | `/delete-account/`   | Delete own account                   | Authenticated       |

## Models

This project uses a `Profile` model with fields like:
- `bio`
- `location`
- `birth_date`

Each user is expected to have a one-to-one relationship with a `Profile`.

## Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
