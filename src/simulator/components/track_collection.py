from simulator.config import Config


class _Track:

    def __init__(self, env, name):
        self.env = env
        self.name: str = name
        self.wagons: list = []

    def log(self):
        return {
            self.name: [wagon.log() for wagon in self.wagons],
        }

    def add_wagon(self, wagon):
        self.wagons = [wagon] + self.wagons


class _WorkshopTrack(_Track):
    def __init__(self, env, name, changing_time: int):
        self.env = env
        self.name = name
        self.wagons = []
        self.changing_time = changing_time

    def change_coupling_system(self):
        yield self.env.timeout(self.changing_time)
        for wagon in self.wagons:
            wagon.couplerType = "dac"

    def wagons_have_coupling_system(self):
        for wagon in self.wagons:
            if wagon.couplerType != "dac":
                return False
        return True


class TrackCollection(_Track):
    def __init__(self, env, conf: Config) -> None:
        self.head_track = _Track(env, "kopf")
        self.retrofitted = _Track(env, "retrofitted")
        self.toBeRetrofitted = _Track(env, "toBeRetrofitted")
        self.workshop_tracks = [
            _WorkshopTrack(env, f"WorkshopGleis{i}", conf.workshop_duration)
            for i in range(conf.number_of_workshops)
        ]

    def log(self):
        logs = self.retrofitted.log()
        logs.update(self.toBeRetrofitted.log())
        logs.update(
            {
                "workshopGleise": [
                    workshop_track.log() for workshop_track in self.workshop_tracks
                ]
            }
        )
        return logs
