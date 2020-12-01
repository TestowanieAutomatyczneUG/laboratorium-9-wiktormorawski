import unittest
from unittest.mock import *
from zad2 import Car


class TestCarMock(unittest.TestCase):
    def setUp(self):
        self.test_object = Car()

    """needsFuel TESTS"""

    @patch.object(Car, 'needsFuel')
    def test_needsFuel_dont(self, mock_method):
        mock_method.return_value = False
        result = self.test_object.needsFuel()
        self.assertEqual(mock_method.return_value, result, "return value of needFuel not equal with False")

    @patch.object(Car, 'needsFuel')
    def test_needsFuel_do(self, mock_method):
        mock_method.return_value = True
        result = self.test_object.needsFuel()
        self.assertEqual(mock_method.return_value, result, "return value of needFuel not equal with True")

    """DriveTo TESTS"""

    @patch.object(Car, 'driveTo')
    def test_driveTo(self, mock_method):
        destination = 'Olsztyn'
        mock_method.return_value = 'On my way to ' + destination
        result = self.test_object.driveTo(destination)
        self.assertEqual(mock_method.return_value, result)

    """GetEngineTemperature TESTS"""

    @patch.object(Car, 'getEngineTemperature')
    def test_getEngineTemperature_temp_under_normal(self, mock_method):
        mock_method.return_value = 'Temperature under normal'
        result = self.test_object.getEngineTemperature()
        self.assertEqual(mock_method.return_value, result, 'Temp not below OK')

    @patch.object(Car, 'getEngineTemperature')
    def test_getEngineTemperature_temp_ok(self, mock_method):
        mock_method.return_value = 'Temperature normal'
        result = self.test_object.getEngineTemperature()
        self.assertEqual(mock_method.return_value, result, 'Temp not OK')

    @patch.object(Car, 'getEngineTemperature')
    def test_getEngineTemperature_temp_above_ok(self, mock_method):
        mock_method.return_value = 'Temperature above normal'
        result = self.test_object.getEngineTemperature()
        self.assertEqual(mock_method.return_value, result, 'Temp not above OK')
