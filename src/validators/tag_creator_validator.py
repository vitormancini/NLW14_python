from src.drivers.cerberus_handler import tag_creator_valiator
from src.errors.error_handler import ErrorHandler

def tag_creator_validator(request: any) -> None:
    (response, body_validator) = tag_creator_valiator(request)
    
    if response is False:
        raise ErrorHandler('UnprocessableEntity', body_validator.errors, 422)