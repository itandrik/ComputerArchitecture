from unittest.mock import patch
from model import Model

with patch('model.Model') as mock_class:
    instance = mock_class.return_value
    instance.calculate_calories.return_value = 2546.44268125
    assert Model(1, 56, 178, 25, 4).calculate_calories() == 2546.44268125
    instance.calculate_calories.return_value = 2283.92605
    assert Model(2, 56, 178, 25, 4).calculate_calories() == 2283.92605


