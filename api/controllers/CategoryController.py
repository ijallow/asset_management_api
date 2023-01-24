from flask import Blueprint, request, jsonify

from ..models.CategoryModel import CategoryModel, CategorySchema

category_api = Blueprint('categories', __name__)

Category_Schemas = CategorySchema(many=True)
Category_Schema = CategorySchema()


@category_api.route('/categories', methods=["GET"])
def get_all_categories():
    categories = CategoryModel.query.all()
    output = []
    # print(categories)
    if categories:
        for category in categories:
            data = {
                'id': category.id,
                'name': category.name,
                'created_at': category.created_at
            }

            output.append(data)

    return Category_Schemas.jsonify(output)


@category_api.route('/categories', methods=['POST'])
def add_category():
    json_data = request.get_json()

    name = json_data.get('name')

    category = CategoryModel(name=name)
    category.save()

    data = {
        'id': category.id,
        'name': category.name
    }

    return Category_Schema.jsonify(data)


@category_api.route('/categories/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    category = CategoryModel.get_by_id(category_id=category_id)

    if category is None:
        return {'message':'category not found'}

    category.delete()

    return {}

