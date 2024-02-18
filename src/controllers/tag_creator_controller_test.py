from .tag_creator_controller import TagCreatorController
from src.drivers.barcode_handler import BarcodeHandler
from unittest.mock import patch

@patch.object(BarcodeHandler, 'create_barcode') # Cria um espelho da classe BarcodeHandler (dessa forma não cria uma tag ao rodar o teste)
def test_create(mock_create_barcode):
    mock_value = 'image_path'
    mock_create_barcode.return_value = mock_value
    tag_creator_controller = TagCreatorController()
    result = tag_creator_controller.create(mock_value)

    assert isinstance(result, dict)
    assert 'data' in result
    assert 'type' in result['data']
    assert 'count' in result['data']
    assert 'path' in result['data']

    assert result['data']['type'] == 'Tag Image'
    assert result['data']['count'] == 1
    assert result['data']['path'] == f'{mock_value}.png'