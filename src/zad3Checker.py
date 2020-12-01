from zad3Environment import Environment
import datetime


class Checker:
    def __init__(self):
        self.environment = Environment()

    def reminder(self, wav):
        current_time = self.environment.getTime().time()
        was_wav_played = self.environment.wavWasPlayed(wav)
        hour = current_time.hour
        minute = current_time.minute
        if hour >= 17 and minute > 0 and was_wav_played == False:
            self.environment.playWavFile(wav)
            ''' on wchodzi w playwavfile i tam odpala was_wav_played'''
        else:
            self.environment.resetWav(wav)
