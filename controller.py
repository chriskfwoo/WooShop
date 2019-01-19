from models import Product


CART = {}

def get_all_products():
    """"
    Returns all products from the Product Model

    :return: dictionary of products
    """

    products = Product.query.all()
    list_products = [product.to_json() for product in products]
    return list_products


def get_all_available_products():
    """"
    Returns all products from the Product Model that has an inventory 

    :return: dictionary of products
    """

    products = Product.query.all()
    list_available_products = []
    for product in products:
        if product.is_available():
            list_available_products.append(product.to_json())
    return list_available_products


def purchase_product(user_id, product_id):    
    pass


def list_user_cart(user_id=None):
    global CART

    if user_id is None:
        return CART
    else:
        if user_id not in CART:
            return {}
        else:
            return CART[user_id]


def add_product_user_cart(user_id, product_id):
    global CART

    query_product = Product.query.filter_by(id=product_id).first()

    if query_product is None:
        return {'error': 'No product found. '}
    else:
        if user_id not in CART:
            CART[user_id] = {
                'products': [],
                'total': 0
            }
        
        CART[user_id]['products'].append({
            'pid': query_product.id,
            'title': query_product.title,
            'price': query_product.price
        })
    return CART[user_id]


def remove_product_user_cart(user_id, product_id):
    global CART

    if user_id not in CART:
        return {'error': 'User has no products'}

    for product in CART[user_id]['products'][:]:
        if product['pid'] == product_id:
            CART[user_id]['products'].remove(product)
            return CART
    return CART


def update_user_cart_price():
    pass