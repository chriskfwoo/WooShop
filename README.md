# Super Cool Shop

- Shopify Backend Challenge 2019 Internship 


## Getting started

- Requirements `python 3.6+` (commands might behave different on Windows)
- For an easy clean install, **`./clean_install.sh`** :dash:
    - Might need permission, `chmod +x clean_install.sh`
- What does it do?
    - Creates a virtual environment (venv)
        - `python3 -m venv venv && source venv/bin/activate`
    - Installs python dependecies in venv 
        - `pip install -r requirements.txt`
    - **Creates a SQLite DB and populates with sample data**
        - `python manage.py recreate-db && python manage.py seed-db`


## Run Application

- First, activate venv, **`source venv/bin/activate`** :warning:
    - Optional: set development mode, `export FLASK_ENV=development`
- Launch application, **`python manage.py run`** :fire: 
    - Running on port 5000
- Run tests: **`python manage.py test`** :hammer_and_wrench:


## Notes

### API (Purchase and Cart)
- All routes are in `project/api.py`
    - All endpoints requires an access token in header
        - For demo purpose ONLY, the token is `'token': supersecretkey`

| Method | Endpoint                       | Params               | Example                                     |
| ------ | ------------------------------ | -------------------- | ------------------------------------------- |
| GET    | /api/ping                      |                      | Test route and connection                   |
| GET    | /api/products                  |                      | All products                                |
| GET    | /api/products/available        |                      | All available products                      |
| GET    | /api/cart/list?uid={}          | uid (int) *optional  | Get all user carts or a specific user cart  |
| POST   | /api/cart/add?pid={}&uid={}    | pid (int), uid (int) | Create user cart if empty, add a product to cart |
| POST   | /api/cart/remove?pid={}&uid={} | pid (int), uid (int) | Remove a product in a user cart, delete cart if empty |
| POST   | /api/cart/checkout?uid={}      | uid (int)            | Purchase all products in a user cart        |
- uid = User ID, pid = Product ID
- **All API errors such as incorrect params or server error returns an error key**
```
{'error': 'Incorrect auth token'}
{'error': 'Server Error'}
{'error': 'Incorrect query params.'}
{'error': 'No product found.'}
{'error': 'Product inventory is empty.'}
{'error': 'User has no items in cart.'}
etc..
```

Examples
- `/api/products/`
```
{
    "products": [
        {
            "id": 1,
            "inventory_count": 5,
            "price": 888.88,
            "title": "Snowboard"
        },
        {
            "id": 2,
            "inventory_count": 0,
            "price": 100,
            "title": "Helmet"
        },
        {
            "id": 3,
            "inventory_count": 10,
            "price": 120,
            "title": "Boots"
        }
    ]
}
```
- `/api/products/available`
```
{
    "products": [
        {
            "id": 1,
            "inventory_count": 5,
            "price": 888.88,
            "title": "Snowboard"
        },
        {
            "id": 3,
            "inventory_count": 10,
            "price": 120,
            "title": "Boots"
        }
    ]
}
```
- `/api/cart/list`
```
{
    "cart": {
        "25": {
            "products": [
                {
                    "pid": 1,
                    "price": 888.88,
                    "title": "Snowboard"
                }
            ],
            "total": 888.88
        },
        "88": {
            "products": [
                {
                    "pid": 3,
                    "price": 120,
                    "title": "Boots"
                },
                {
                    "pid": 1,
                    "price": 888.88,
                    "title": "Snowboard"
                }
            ],
            "total": 1008.88
        }
    }
}

*25 and 88 are user IDs
```
- `/api/cart/list?uid=25`
```
{
    "cart": {
        "products": [
            {
                "pid": 1,
                "price": 888.88,
                "title": "Snowboard"
            }
        ],
        "total": 888.88
    }
}
```



### Database
- ORM Database with [Flask SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.3/quickstart/)
    - Database models define in `project/models.py`

### Controllers
- Controller functions are in `project/controller.py`
    - Handles the communication between API request and DB Models

## Improvements
- Endpoints to add products, remove products
- JWT authentication to handle user id
- Environment and config files to handle development, staging, production
- Continous Integration with Travis CI   