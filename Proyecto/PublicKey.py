
class PublicKey:

    def __int__(self):
        self.module = 0
        self.exponent = 0

    def __init__(self, module, exponent):
        self.module = module
        self.exponent = exponent
