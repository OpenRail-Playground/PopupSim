class Wagon:

    def __init__(self, env, id, length=20, couplerType="sc"):
        self.env = env
        self.id = id
        self.length = length
        self.couplerType = couplerType

    def log(self):
        return {
            "wagonId": self.id,
            "length": self.length,
            "couplerType": self.couplerType,
        }
