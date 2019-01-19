from flask import Blueprint, jsonify, request

api_bp = Blueprint('api', __name__, url_prefix='/api')


# NOTE THIS IS FOR DEMO PURPOSE. IT CAN BE SET IN ENVIRONMENT SETTINGS AND GITIGNORED.
ACCESS_TOKEN = 'supersecretkey'

# Before every request, check if the user is authenticated
@api_bp.before_request
def before_request():
    if 'token' not in request.headers:
        return jsonify({'error': 'No auth token specify.'})
    else:
        if request.headers['token'] != ACCESS_TOKEN:
            return jsonify({'error': 'Incorrect auth token'})


@api_bp.route('/ping', methods=["GET"])
def ping():
    return jsonify({'msg': 'pong'})


@api_bp.route('/products', methods=["GET"])
def products():
    from controller import get_all_products

    list_products = get_all_products()
    return jsonify({'products': list_products})


@api_bp.route('/products/available', methods=["GET"])
def available_products():
    from controller import get_all_available_products

    list_products = get_all_available_products()
    return jsonify({'products': list_products})


@api_bp.route('/products/purchase', methods=["POST"])
def purchase_products():
    from controller import purchase_product

    if 'pid' in request.args and 'uid' in request.args:
        purchase_product(user_id=uid, product_id=pid)
    else:
        return jsonify({'error': 'Incorrect query params.'})


@api_bp.route('/cart/list', methods=["GET"])
def list_cart():
    from controller import list_user_cart

    cart_details = list_user_cart(user_id=request.args['uid']) if 'uid' in request.args else list_user_cart()
    return jsonify({'cart': cart_details})


@api_bp.route('/cart/add', methods=["POST"])
def add_cart():
    from controller import add_product_user_cart

    if 'pid' in request.args and 'uid' in request.args:
        new_cart = add_product_user_cart(user_id=request.args['uid'], product_id=request.args['pid'])
        return jsonify({'cart': new_cart})
    else:
        return jsonify({'error': 'Incorrect query params.'})


@api_bp.route('/cart/remove', methods=["POST"])
def remove_cart():
    from controller import remove_product_user_cart

    if 'pid' in request.args and 'uid' in request.args:
        test = remove_product_user_cart(user_id=request.args['uid'], product_id=request.args['pid'])
        return jsonify({'products': test})
    else:
        return jsonify({'error': 'Incorrect query params.'})
