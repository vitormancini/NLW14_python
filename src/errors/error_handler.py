from src.views.http_types.http_response import HttpResponse

class ErrorHandler(Exception):
    def __init__(self, name: str, message: str, status_code: int):
        super().__init__(message)
        self.name = name
        self.message = message
        self.status_code = status_code

# Função separada da classe para permitir futuramente enviar dados para um log, email
def handle_errors(error: Exception) -> HttpResponse:
    return HttpResponse(
        status_code=error.status_code, 
        body={
            'errors': [{
                'title': error.name,
                'detail': error.message
            }]
    })

