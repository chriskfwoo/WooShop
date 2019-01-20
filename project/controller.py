from project.models import Product


# STORE THE CART IN-MEMORY
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


def list_user_cart(user_id=None):
    """"
    Returns all products from all user carts or a specific cart from a single user

    :param user_id: ID of a user
    :return: dictionary of cart
    """

    global CART

    if user_id is None:
        return CART
    else:
        if user_id not in CART:
            return {}
        else:
            return CART[user_id]


def add_product_user_cart(user_id, product_id):
    """"
    Add a product to a user cart and update total price

    :param user_id: ID of a user
    :param product_id: ID of a product
    :return: dictionary of updated cart
    """

    global CART

    query_product = Product.query.filter_by(id=product_id).first()

    if query_product is None:
        return {'error': 'No product found.'}
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
    update_user_cart_price(user_id)
    return CART[user_id]


def remove_product_user_cart(user_id, product_id):
    """"
    Remove a product to a user cart and update total price

    :param user_id: ID of a user
    :param product_id: ID of a product
    :return: dictionary of updated cart
    """

    global CART

    if user_id not in CART:
        return {'error': 'No product found.'}
    for product in CART[user_id]['products'][:]:
        if product['pid'] == int(product_id):
            CART[user_id]['products'].remove(product)
            break

    if len(CART[user_id]['products']) == 0:
        # remove user cart since there no items
        CART.pop(user_id, None)
        return {}
    update_user_cart_price(user_id)
    return CART[user_id]


def checkout_cart(user_id):
    """"
    Purchase all the user items in cart

    :param user_id: ID of a user
    :return: total price of purchase
    """

    global CART

    if user_id not in CART:
        return {'error': 'User has no items in cart.'}

    total_price = 0
    for product in CART[user_id]['products']:
        query_product = Product.query.filter_by(id=product['pid']).first()
        if query_product.is_available():
            query_product.remove_inventory(1)
        total_price = total_price + query_product.price

    # remove all the items in the user cart
    CART.pop(user_id, None)
    return {'price': float(f'{total_price:.2f}')}


def update_user_cart_price(user_id):
    """"
    Helper function to update the total price of a user cart

    :param user_id: ID of a user
    """

    global CART

    if user_id in CART:
        total = 0
        for product in CART[user_id]['products']:
            total += product['price']
        CART[user_id]['total'] = float(f'{total:.2f}')
