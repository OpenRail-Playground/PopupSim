import json

import simpy

from simulator.components.locomotive import Locomotive
from simulator.components.track_collection import TrackCollection
from simulator.components.wagon import Wagon
from simulator.config import Config


class GlobalSetting(object):

    def __init__(self, conf: Config):
        self.env = simpy.Environment()
        self.conf = conf
        self.global_log = []

        self.setup_scenario()
        self.env.run(until=1500)
        self.save_log_json()

    def setup_scenario(self):
        self.tracks = TrackCollection(self.env, self.conf)

        # create wagons
        self.wagons = []
        for i in range(self.conf.number_of_wagons):
            self.wagons.append(Wagon(self.env, i))

        for i in range(self.conf.workshop_size):
            self.wagons[i].couplerType = "dac"

        # add wagons to tracks
        for i in range(self.conf.number_of_workshops):
            self.tracks.workshop_tracks[i].wagons = self.wagons[
                i * self.conf.workshop_size : (i + 1) * self.conf.workshop_size
            ]
            # self.tracks.workshop_tracks[1].wagons = self.wagons[self.conf.workshop_size:self.conf.workshop_size*2]
        self.tracks.toBeRetrofitted.wagons = self.wagons[
            self.conf.number_of_workshops * self.conf.workshop_size :
        ]

        # create locomotive
        self.locomotive = Locomotive(self.env, self, self.tracks.head_track, self.conf)

    def log_global_state(self):

        self.global_log.append(
            {
                "locomotive": self.locomotive.log(),
                "timestamp": self.env.now,
                "tracks": self.tracks.log(),
            }
        )

    def get_available_workshop(self):
        for track in self.tracks.workshop_tracks:
            if track.wagons_have_coupling_system():
                return track
        return None

    def save_log_json(self):
        with open("data.json", "w") as fp:
            json.dump(self.global_log, fp, indent=4)


if __name__ == "__main__":
    GlobalSetting(Config())
