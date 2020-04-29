import re
class Preprocess:
    def __init__(self, code):
        self.code = code
        
    def Removecomm(self):
        res = re.sub(r"𝄾.*(?s)𝄾", "",self.code)
        res = re.sub(r"\\n", "",res)
        return res