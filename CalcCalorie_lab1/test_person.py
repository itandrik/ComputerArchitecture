from unittest import mock

class A:

with mock.patch.object(ProductionClass, 'method', return_value=None) as mock_method:
     thing = ProductionClass()
     thing.method(1, 2, 3)

mock_method.assert_called_once_with(1, 2, 3)