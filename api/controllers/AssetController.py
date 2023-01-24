from flask import request, jsonify, Blueprint
from flask_jwt_extended import jwt_required
from http import HTTPStatus
from ..models.AssetModel import AssetModel, AssetSchema

asset_api = Blueprint('assets', __name__)

AssetSchemas = AssetSchema(many=True)
AssetSchema = AssetSchema()


@asset_api.route('/assets', methods=["GET"])
# @jwt_required()
def get_all_assets():
    assets = AssetModel.query.all()
    output = []
    if assets:
        for asset in assets:
            data = {
                'id': asset.id,
                'name': asset.name,
                'serial_number': asset.serial_number,
                'model': asset.model,
                'created_at': asset.created_at,
                'updated_at': asset.updated_at
                # 'password': user.password
            }
            output.append(data)

    # return jsonify({'assets': output})
    return AssetSchemas.jsonify(output)


@asset_api.route('/assets', methods=["POST"])
def add_asset():
    json_data = request.get_json()

    name = json_data.get('name')
    serial_number = json_data.get('serial_number')
    model = json_data.get('model')
    category_id = json_data.get('category_id')

    asset = AssetModel(name=name, serial_number=serial_number, model=model, category_id=category_id)
    asset.save()

    data = {
        'id': asset.id,
        'name': asset.name,
        'serial_number': asset.serial_number,
        'model': asset.model,
        'category_id': asset.category_id,
        'created_at': asset.created_at,
        'updated_at': asset.updated_at
    }

    return AssetSchema.jsonify(data)


@asset_api.route('/asset/<int:asset_id>', methods=['GET'])
def get_asset(asset_id):
    asset = AssetModel.get_by_id(asset_id=asset_id)

    if asset is None:
        return {'message': 'asset not found'}

    data = {
        'id': asset.id,
        'name': asset.name,
        'model': asset.model,
        'serial number': asset.serial_number,
        'category': asset.category_id
    }

    return AssetSchema.jsonify(data)
