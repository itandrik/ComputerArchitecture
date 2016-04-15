# test_model.py
import mock
from model import Model

# mock the get_name function
@mock.patch('model.Model._calculate_pa') # This won't work as expected!
def test_name(mock_calculate_pa):
    # set a return value for our mock object
    mock_calculate_pa.return_value = 1.4625
    model = Model()
    calculate_pa = model._calculate_pa()
    assert calculate_pa == 1.4625