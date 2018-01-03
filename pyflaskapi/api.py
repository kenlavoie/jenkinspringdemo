from flask import Flask, jsonify
from flasgger import Swagger, Schema

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/meals/<breakfast>')
def breakfast_food(breakfast):
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
              $ref: '#/definitions/meals'
      Meals:
        type: string
    responses:
      200:
        description: Your food choice for Breakfast
        schema:
          $ref: '#/definitions/Breakfast'
        examples:
          toast: ['White', 'Wheat', 'Rye']
    """
    all_breakfast_food = {

        'Eggs': [ 'Over Easy', 'Over Hard', 'Scrambled'],
        'Toast': [ 'White', 'Wheat', 'Rye', 'Pumpernickel'],
        'Coffee': [ 'Yes', 'No']
    }

    if breakfast == 'all':
        result = all_breakfast_food
    else:
        result = {breakfast: all_breakfast_food.get(breakfast)}

    return(jsonify(result))

@app.route('/meals/<lunch>/')
def lunch_food(lunch):
    """
    This is using Swagger to show an API with Docker
    Getting Food info
    ---

    parameters:
      - name: lunch
        in: path
        type: string
        enum: ['Sandwich', 'Salad', 'Burrito']
        required: true
        default: all
    definitions:
      Lunch:
        type: object
        properties:
          lunch_food:
            type: array
            items:
              $ref: '#/definitions/meals'
      Meals:
        type: string
    responses:
      200:
        description: Your food choice for Lunch
        schema:
          $ref: '#/definitions/Lunch'
        examples:
          Sandwich: [ 'Cuban', 'Reuben', 'Club']
    """
    all_lunch_food = {

        'Sandwich': [ 'Cuban', 'Ceuben', 'Club'],
        'Salad': [ 'Caesar', 'Cobb', 'House'],
        'Burrito': [ 'There is No Better Choice!']
    }

    if lunch == 'all':
        result = all_lunch_food
    else:
        result = {lunch: all_lunch_food.get(lunch)}

    return(jsonify(result))

@app.route('/meals/<dinner>/')
def dinner_food(dinner):
    """
    This is using Swagger to show an API with Docker
    Getting Food info
    ---

    parameters:
      - name: dinner
        in: path
        type: string
        enum: ['Healthy', 'UnHealthy', 'Dessert']
        required: true
        default: all
    definitions:
      Dinner:
        type: object
        properties:
          dinner_food:
            type: array
            items:
              $ref: '#/definitions/meals'
      Meals:
        type: string
    responses:
      200:
        description: Your food choice for Dinner
        schema:
          $ref: '#/definitions/Dinner'
        examples:
          Dessert: [ 'Chocolate Cake, Ice Cream']
    """
    all_dinner_food = {

     'Healthy': [ 'Grilled Chicken or Fish with choice of steamed vegtable, and starch'],
     'UnHealthy': [ 'Some form of Pizza and Fried side dish'],
     'Dessert': [ 'Chocolate Cake, Ice Cream']
    }

    if dinner == 'all':
        result = all_dinner_food
    else:
        result = {dinner: all_dinner_food.get(dinner)}

    return(jsonify(result))

app.run(host='0.0.0.0', debug=True)
