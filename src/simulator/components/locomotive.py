DRIVE_TIMES = {
    "toBeRetrofitted": {
        "WorkshopGleis0": 5,
        "WorkshopGleis1": 5,
        "retrofitted": 10,
        "kopf": 5,
    },
    "WorkshopGleis0": {"toBeRetrofitted": 5, "retrofitted": 10, "kopf": 5},
    "WorkshopGleis1": {"toBeRetrofitted": 5, "retrofitted": 10, "kopf": 5},
    "retrofitted": {
        "toBeRetrofitted": 10,
        "WorkshopGleis0": 5,
        "WorkshopGleis1": 5,
        "kopf": 5,
    },
    "kopf": {
        "toBeRetrofitted": 5,
        "WorkshopGleis0": 5,
        "WorkshopGleis1": 5,
        "retrofitted": 10,
        "kopf": 5,
    },
}


class Locomotive(object):
    def __init__(self, env, global_setting, start_track, id=1):
        self.env = env
        self.global_setting = global_setting

        self.id = id
        self.coupled_with = []
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

        # yield self.env.process(self.run_routine(self.global_setting.tracks.workshop_tracks[0]))
        self.env.process(
            self.global_setting.tracks.workshop_tracks[1].change_coupling_system()
        )
        while (
            self.global_setting.tracks.toBeRetrofitted.wagons
            + self.global_setting.tracks.workshop_tracks[0].wagons
            + self.global_setting.tracks.workshop_tracks[1].wagons
        ):

            available_workshop = self.global_setting.get_available_workshop()
            if available_workshop:
                yield self.env.process(self.run_routine(available_workshop))
                self.env.process(available_workshop.change_coupling_system())
            else:
                print("waiting")
                yield self.env.timeout(5)
            # wait for workshop to finish
            # with self.global_setting.workshop_2.request() as req:
            #     yield req
            #     yield self.env.process(self.run_routine(self.global_setting.tracks.workshop_tracks[2]))

            # with self.global_setting.workshop_1.request() as req:
            #     yield req
            #     yield self.env.process(self.run_routine(self.global_setting.tracks.workshop_tracks[0]))

    def run_routine(self, workshop_track):

        print("Starting in Kopf %d" % self.env.now)
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
        driving_time = DRIVE_TIMES[self.cur_track.name][target_track.name]
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
