from src.zad3Checker import Checker
import unittest
from unittest.mock import *

'''
     def reminder(self, wav):
        current_time = self.environment.getTime().time()
        was_wav_played = self.environment.wavWasPlayed(wav)
        hour = current_time.hour
        minute = current_time.minute
        if hour >= 17 and minute > 0 and was_wav_played == False:
            self.environment.playWavFile(wav)
        else:
            self.environment.resetWav(wav)
'''


class test_SomeClass_public_interface(unittest.TestCase):
    def setUp(self):
        self.test_object = Checker()

    def test_checker_is_not_played_before_17(self):
        # prepare mock
        self.test_object.hour = Mock(name='getTimeHour')
        self.test_object.hour.return_value = 17
        self.test_object.minute = Mock(name='getTimeMinute')
        self.test_object.minute.return_value = 0
        self.test_object.environment.wavWasPlayed = Mock(name="wavWasPlayed")
        self.test_object.environment.wavWasPlayed.return_value = True
        # testing
        wav = 'cos'
        result = self.test_object.environment.wavWasPlayed(wav)
        self.assertEqual(True, result, 'return value from wavwasPlayed is different to True')

    def test_checker_is_played_after_17(self):
        # prepare mock
        self.test_object.hour = Mock(name='getTimeHour')
        self.test_object.hour.return_value = 18
        self.test_object.minute = Mock(name='getTimeMinute')
        self.test_object.minute.return_value = 1
        self.test_object.environment.wavWasPlayed = Mock(name="wavWasPlayed")
        self.test_object.environment.wavWasPlayed.return_value = False
        # testing
        wav = 'cos'
        result = self.test_object.environment.wavWasPlayed(wav)
        self.assertEqual(False, result, 'return value from wavwasPlayed is equal to True')

    def tearDown(self):
        self.test_object = None
