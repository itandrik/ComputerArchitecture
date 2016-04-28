from unittest.mock import patch
from model import Model

with patch('model.Model') as mock_class:
    instance = mock_class.return_value
    instance.calculate_calories.return_value = 2546.44268125
    assert Model().calculate_calories(1, 56, 178, 25, 4) == 2546.44268125
