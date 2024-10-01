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


class TrackCollection(_Track):
    def __init__(self, env) -> None:
        self.head_track = _Track(env, "kopf")
        self.retrofitted = _Track(env, "retrofitted")
        self.toBeRetrofitted = _Track(env, "toBeRetrofitted")
        self.workshop_tracks = [
            _WorkshopTrack(env, f"WorkshopGleis{i}") for i in range(2)
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
