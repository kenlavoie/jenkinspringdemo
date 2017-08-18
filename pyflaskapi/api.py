from flask import Flask, jsonify
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/meals/<breakfast>/')
def meals(breakfast):
    """
    This is using Swagger to show an API with Docker 
    Getting Food info
    ---
   
    parameters:
      - name: breakfast
        in: path
        type: string
        enum: ['Eggs', 'Toast', 'Coffee']
        required: true
        default: all
    definitions:
      Breakfast: 
        type: object 
        properties: 
          breakfast_food: 
            type: array
            items: 
              $ref: '#/definitions/Meals'
      Meals: 
        type: string
    responses:
      200:
        description: Your food choice for breakfast
        schema: 
          $ref: '#/definitions/Breakfast' 
        examples:
          toast: ['white', 'wheat', 'rye'] 
    """
    all_breakfast_food = { 

        'Eggs': [ 'over easy', 'over hard', 'scrambled'],
        'Toast': [ 'white', 'wheat', 'rye', 'pumpernickel'],
        'Coffee': [ 'Yes', 'No']
    }

    if breakfast == 'all': 
        result = all_breakfast_food
    else: 
        result = {breakfast: all_breakfast_food.get(breakfast)}

    return(jsonify(result))

app.run(host='0.0.0.0', debug=True)