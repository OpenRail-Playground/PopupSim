import json

import simpy

from simulator.components.locomotive import Locomotive
from simulator.components.track_collection import TrackCollection
from simulator.components.wagon import Wagon

# from simulator.config import Config


class GlobalSetting(object):

    def __init__(self):

        self.env = simpy.Environment()
        # self.conf = conf

        self.global_log = []

        self.setup_scenario()

        self.env.run(until=1500)

        self.save_log_json()

    def setup_scenario(self):
        self.tracks = TrackCollection(self.env)

        # create wagons
        self.wagons = []
        for i in range(20):
            self.wagons.append(Wagon(self.env, i))

        for i in range(3):
            self.wagons[i].couplerType = "dac"

        # add wagons to tracks
        self.tracks.workshop_tracks[0].wagons = self.wagons[:3]
        self.tracks.workshop_tracks[1].wagons = self.wagons[3:6]
        self.tracks.toBeRetrofitted.wagons = self.wagons[6:]

        # create locomotive
        self.locomotive = Locomotive(self.env, self, self.tracks.head_track)

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
    GlobalSetting()
