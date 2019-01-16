from flask import Blueprint, jsonify, request

api_bp = Blueprint('api', __name__, url_prefix='/api')


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
