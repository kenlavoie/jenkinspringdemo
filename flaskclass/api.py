from flask import Flask, jsonify
from flasgger import Schema, Swagger, SwaggerView, fields



class Breakfast(Schema):
    breakfast_foods = fields.Str()
    #menus = fields.Nested(Food, many=True)

class BreakfastView(SwaggerView):
    parameters = [
        {
            "name": "breakfast",
            "in": "path",
            "type": "string",
            "enum": ["Eggs", "Toast", "Coffee"],
            "required": True,
            "default": "all"
        }
    ]
    responses = {
        200: {
            "description": "A list of Breakfast Food",
            "schema": Breakfast
        }
    }

    def get(self, Breakfast):
        """
        Breakfast Food currently on menu
        """
        breakfast_food = {
            'Eggs': ['over easy', 'over hard', 'benedict', 'scrambled']
            'Meat': ['bacon', 'sausage', 'ham']
            'Toast': ['wheat', 'white', 'rye', 'pumpernickel']
        }

        if breakfast == 'all':
            result = breakfast_food
        else:
            result = {breakfast: breakfast_food.get(breakfast)}
        return jsonify(result)

app = Flask(__name__)
swag = Swagger(app)

app.add_url_rule(
    '/menu/<breakfast>',
    view_func=BreakfastView.as_view('food'),
    methods=['GET']

)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
