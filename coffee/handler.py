from random import randint

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """

    coffee = {
        "mild": ["Caffe Misto", "White Chocolate Mocha", "Peppermint Mocha", "Toasted Graham Latte", "Smoked Butterscotch Latte", "Tiramisu Latte", "Pumpkin Spice", "Salted Caramel Mocha"],
        "medium": ["Blonde Caffè Latte", "Molten Chocolate Latte", "Caffe Mocha", "Flat White"],
        "strong": ["Blonde Flat White", "Pike Place Brewed Coffee", "Blonde Roast", "Feature Dark Roast", "Reserve roasts", "Cordusio Mocha", "Reserve Latte"],
    }

    if (req not in coffee.keys()):
        return 'Invalid request, request can be either "mild", "medium" or "strong"'
    else:
        preferred_coffee = coffee[req]
        return preferred_coffee[randint(0, len(preferred_coffee))]
