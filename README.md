# 🛒 ShopEasy — Backend Development & Security Guidelines

> **Purpose:** Define the backend architecture, request-processing flow, security rules, and development guidelines for the ShopEasy application.

---

## 📑 Table of Contents

* [1. Core Security Principle](#1-core-security-principle)
* [2. User Data & Profile Security](#2-user-data--profile-security)
* [3. Backend Virtual Environment](#3-backend-virtual-environment)
* [4. Running the FastAPI Application](#4-running-the-fastapi-application)
* [5. Request & Response Security Flow](#5-request--response-security-flow)
* [6. Request Processing Order](#6-request-processing-order)
* [7. Database Data Access](#7-database-data-access)
* [8. Response Validation & Serialization](#8-response-validation--serialization)
* [9. Frontend Access Control](#9-frontend-access-control)
* [10. CQRS Pattern](#10-cqrs-pattern)
* [11. Recommended ShopEasy Architecture](#11-recommended-shopeasy-architecture)
* [12. Security Rules](#12-security-rules)
* [13. Security Example — Profile API](#13-security-example--profile-api)
* [14. Final Security Principle](#14-final-security-principle)
* [15. Development Commands](#15-development-commands)
* [16. Development Goal](#16-development-goal)

---

# 1. Core Security Principle

The **backend must always be the final security authority**.

The frontend is controlled by the user, so the backend must never blindly trust:

* User IDs
* URL parameters
* Query parameters
* Request body values
* Frontend route restrictions
* Client-side validation
* Requests coming from a specific frontend

### Security Rule

> **Never trust the client.**

Every protected request must be independently validated and authorized by the backend.

---

# 2. User Data & Profile Security

## Security Requirement

No user should be able to access another user's profile, personal data, or private information simply by changing:

* URL
* ID
* Query parameter
* Request body
* Any other request value

Authentication alone is **not enough**.

The backend must also verify that the authenticated user is authorized to access the requested resource.

---

## Example of an Unsafe API

```http
GET /api/users/101/profile
```

Suppose User A is authenticated as:

```text
User ID = 101
```

User A changes the URL to:

```http
GET /api/users/102/profile
```

The backend must **not** return User B's private information unless User A has explicit permission.

This type of vulnerability is commonly known as:

* **Broken Object Level Authorization (BOLA)**
* **Insecure Direct Object Reference (IDOR)**

---

## Required Backend Security Flow

```text
Request
   ↓
Authentication
   ↓
Is user logged in?
   │
   ├── NO  → 401 Unauthorized
   │
   └── YES
        ↓
Authorization
   ↓
Does the user have permission?
   │
   ├── NO  → 403 Forbidden
   │
   └── YES
        ↓
Process Request
   ↓
Return Only Allowed Data
```

---

## ⚠️ Never Trust Client-Provided User IDs

Do not rely only on:

```http
/api/users/{user_id}
```

The backend should obtain the authenticated user's identity from the **validated authentication token/session** and compare it with the requested resource.

### Example

```text
Authenticated User = 101
Requested Profile  = 102

101 != 102
   ↓
403 Forbidden
```

---

## Role-Based Access

For administrative functionality, authorization can be based on explicit roles and permissions.

```text
USER
 └── Access own data

ADMIN
 └── Access permitted users/data

SUPER ADMIN
 └── Access permitted administrative data
```

---

# 3. Backend Virtual Environment

ShopEasy uses a Python virtual environment for backend dependencies.

## Activate Virtual Environment

From the backend project directory:

```bash
source venv/bin/activate
```

After activation, the terminal normally displays:

```text
(venv)
```

---

## Deactivate Virtual Environment

Use:

```bash
deactivate
```

> **Note:** `source venv/bin/deactivate` is not the normal command. Use `deactivate`.

---

# 4. Running the FastAPI Application

Start the development server with:

```bash
uvicorn app.main:app --reload
```

### What does `--reload` do?

The `--reload` option automatically restarts the development server whenever source files change.

### Development

```bash
uvicorn app.main:app --reload
```

### Production

Do **not** rely on `--reload` for production deployment.

Production should use an appropriate production deployment configuration.

---

# 5. Request & Response Security Flow

ShopEasy should follow a layered request-processing architecture.

```text
                 CLIENT / FRONTEND
                        │
                        │ Request
                        ▼
              ┌─────────────────────┐
              │ Frontend Validation │
              └─────────────────────┘
                        │
                        ▼
              ┌─────────────────────┐
              │     Backend API     │
              └─────────────────────┘
                        │
                        ▼
              ┌─────────────────────┐
              │ Authentication &    │
              │ Authorization       │
              └─────────────────────┘
                        │
                  Authorized?
                   /        \
                 NO          YES
                 │            │
                 ▼            ▼
             401 / 403   Backend Validation
                              │
                              ▼
                       Business Logic
                              │
                              ▼
                       Data Access Layer
                              │
                              ▼
                           Database
                              │
                              ▼
                    Return Required Data
                              │
                              ▼
                      Response Validation
                              │
                              ▼
                         Frontend
                              │
                              ▼
                         Show Data
```

---

# 6. Request Processing Order

## Step 1 — Frontend Validation

Frontend validation improves the user experience and prevents obviously invalid requests.

### Examples

* Required fields
* Email format
* Password format
* Quantity greater than `0`
* Valid input length

However:

> **Frontend validation is NOT a security boundary.**

A user can bypass the frontend and call the API directly using:

* Postman
* `curl`
* Browser developer tools
* Another custom client

Therefore, every important validation must also exist in the backend.

---

## Step 2 — Backend Validation

The backend must independently validate incoming requests.

### Validate

* Data types
* Required fields
* Allowed values
* String length
* Numeric ranges
* Business rules
* Request structure

### Example

```http
POST /api/orders
```

Request:

```text
quantity = -10
```

Even if the frontend prevents this value, the backend must reject it.

---

## Step 3 — Authentication

Authentication answers:

> **Who is making this request?**

For example:

```http
Authorization: Bearer <access_token>
```

The backend validates the token/session and obtains the authenticated user's identity.

Example:

```text
User ID = 101
Role    = USER
```

If authentication is required but the request does not contain valid credentials:

```http
401 Unauthorized
```

---

## Step 4 — Authorization

Authorization answers:

> **What is this user allowed to do?**

### Example

User `101` requests:

```http
GET /api/users/102/profile
```

Backend checks:

```text
Authenticated User = 101
Requested User     = 102

Authorization Check
        ↓
      FAILED
        ↓
403 Forbidden
```

This check must happen on the backend.

### Never Assume

```text
Frontend hides profile page
        =
Backend data is protected
```

It does **not**.

---

## Step 5 — Data Security

After authentication and authorization, the backend processes the request.

The backend should:

* Use parameterized queries or safe ORM operations
* Never trust client-provided IDs
* Prevent unauthorized object access
* Validate resource ownership
* Apply role/permission checks
* Avoid exposing internal database fields
* Avoid returning unnecessary personal information
* Protect sensitive fields
* Log security-relevant events where appropriate

---

# 7. Database Data Access

The backend should request and return **only the data required for the operation**.

## ❌ Avoid Returning Entire User Records

A database record may contain:

```text
User
├── id
├── name
├── email
├── password_hash
├── phone
├── address
├── internal_notes
├── security_information
└── other_private_data
```

The API should return only what the client actually needs.

## ✅ Example

```json
{
  "id": 101,
  "name": "User Name",
  "email": "user@example.com"
}
```

---

## 🔐 Never Return Sensitive Information

Do not expose fields such as:

```text
password
password_hash
refresh_token
secret keys
internal security data
private administrative notes
```

unless there is a specific, justified,
