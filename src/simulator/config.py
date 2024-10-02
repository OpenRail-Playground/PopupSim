class Config:

    workshop_duration: int = 180
    shunting_time: int = 8
    movement_time: int = 5
    coupling_time: int = 8
    number_of_wagons: int = 20
    number_of_workshops: int = 2
    wagons_per_workshop: int = 3
    loco_wait_time: int = 5

    def __init__(self, conf):
        # parameters for feature:
        self.workshop_duration: int = conf["parameters"]["workshop"]
        self.shunting_time: int = conf["parameters"]["shuntingMovement"]
        self.movement_time: int = conf["parameters"]["movement"]
        self.coupling_time: int = conf["parameters"]["coupling"]

        self.number_of_wagons: int = 20
        self.wagons_per_workshop: int = conf["parameters"]["wagonsPerWorkshop"]
        self.loco_wait_time: int = 5

        # other:

        self.num_pop_up_site: int = conf["popupSite"]
        self.workshop_track_names = conf["workshops"]
        self.retrofitted_track_name = conf["retrofitted"][0]
        self.toberetrofitted_track_name = conf["toBeRetrofitted"][0]
        self.stationhead_name = conf["stationHead"][0]
        self.parking_names = conf["parking"]
