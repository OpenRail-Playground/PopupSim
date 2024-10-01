from simulator.track import Track


class WorkshopTrack(Track):
    def __init__(self, env, name):
        self.env = env
        self.name = name
        self.wagons = []
        self.is_done = False

    def change_coupling_system(self):
        yield self.env.timeout(180)
        for wagon in self.wagons:
            wagon.couplerType = "dac"

    def wagons_have_coupling_system(self):
        for wagon in self.wagons:
            if wagon.couplerType != "dac":
                return False
        return True
