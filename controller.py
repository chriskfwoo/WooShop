from models import Product


def get_all_products():
    """"
    Returns all products from the Product Model

    :return: dictionary of products
    """

    products = Product.query.all()
    list_products = [product.to_json() for product in products]
    return list_products


def get_all_available_products():
    products = Product.query.all()

    list_available_products = []

    for product in products:
        if product.inventory_count > 0:
            list_available_products.append(product.to_json())




    #list_available_products = [product.to_json() for product in products if product.inventory_count > 0]
    return list_available_products
