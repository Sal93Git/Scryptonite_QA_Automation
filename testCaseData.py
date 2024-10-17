# test_case_data.py
class TestCaseData:
    def __init__(self):
        self.trialString = "https://unity.com/"
        self.data = {}

    def set(self, key, value):
        self.data[key] = value

    def get(self, key):
        return self.data.get(key)

    def trial(self):
        return self.trialString

    def settrial(self, trialtxt):
        self.trialString = trialtxt
