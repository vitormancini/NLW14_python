from cerberus import Validator

def tag_creator_valiator(request: any):
    """
    {
    "product_code": "123-456-789"
    }
    """

    body_validator = Validator({
        'product_code': { 'type': 'string', 'required': True, 'empty': False }
    })

    response = body_validator.validate(request.json)

    return response, body_validator