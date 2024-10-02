import itertools

from simulator.config import Config


class Locomotive(object):
    def __init__(self, env, global_setting, start_track, conf: Config, id: int = 1):
        self.env = env
        self.global_setting = global_setting
        self.conf = conf

        self.id = id
        self.coupled_with = []
        self.non_idle_time = 0
        self.cur_track = start_track

        # Start the run process everytime an instance is created.
        self.action = env.process(self.run())

    def log(self):
        return {
            "lokomotiveId": self.id,
            "coupledWith:": [wagon.log() for wagon in self.coupled_with],
            "position": self.cur_track.name,
        }

    def run(self):

        self.env.process(
            self.global_setting.tracks.workshop_tracks[1].change_coupling_system()
        )
        while self.global_setting.tracks.toBeRetrofitted.wagons + list(
            itertools.chain.from_iterable(
                [track.wagons for track in self.global_setting.tracks.workshop_tracks]
            )
        ):

            available_workshop = self.global_setting.get_available_workshop()
            if available_workshop:
                yield self.env.process(self.run_routine(available_workshop))
                self.env.process(available_workshop.change_coupling_system())
            else:
                print("waiting")
                yield self.env.timeout(self.conf.loco_wait_time)
        self.global_setting.final_time = self.env.now

    def run_routine(self, workshop_track):
        starting_time = self.env.now
        print("Starting in Kopf %d" % starting_time)
        self.global_setting.log_global_state()

        # drive to workshop
        yield self.env.process(self.drive_to(workshop_track))

        # get wagons
        yield self.env.process(self.coupling())

        # drive to C
        yield self.env.process(self.drive_to(self.global_setting.tracks.retrofitted))

        # uncoupling
        yield self.env.process(self.uncoupling())

        # drive to from C to a
        yield self.env.process(
            self.drive_to(self.global_setting.tracks.toBeRetrofitted)
        )

        # coupling
        yield self.env.process(self.coupling())

        # drive from a to b1

        yield self.env.process(self.drive_to(workshop_track))

        # uncoupling
        yield self.env.process(self.uncoupling())

        # drive from b1 to kopf

        yield self.env.process(self.drive_to(self.global_setting.tracks.head_track))

        self.non_idle_time += self.env.now - starting_time

        self.global_setting.log_global_state()

    def coupling(self, duration=5):
        print("start coupling %d" % self.env.now)
        yield self.env.timeout(duration)
        self.coupled_with += self.cur_track.wagons[:3]
        print("finished coupling %d" % self.env.now)

        self.global_setting.log_global_state()

    def uncoupling(self, duration=5):
        print("start uncoupling %d" % self.env.now)
        yield self.env.timeout(duration)
        self.coupled_with = []
        print("finished uncoupling %d" % self.env.now)
        self.global_setting.log_global_state()

    def drive_to(self, target_track):
        print(
            f"start driving from {self.cur_track.name} to {target_track.name} - {self.env.now}"
        )

        # compute driving time
        driving_time = (
            self.conf.movement_time
            if "kopf" in [self.cur_track.name, target_track.name]
            else self.conf.shunting_time
        )
        yield self.env.timeout(driving_time)

        for wagon in self.coupled_with:
            # remove wagons from old track
            self.cur_track.wagons.remove(wagon)

        # add to new track
        target_track.wagons = self.coupled_with + target_track.wagons

        # change track of locomotive
        self.cur_track = target_track

        print(f"arrived {target_track.name} - {self.env.now}")
        self.global_setting.log_global_state()
