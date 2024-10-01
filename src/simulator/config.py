class Config:

    workshop_duration: int = 180
    shunting_time: int = 8
    movement_time: int = 5
    coupling_time: int = 8
    number_of_wagons: int = 20
    number_of_workshops: int = 2
    workshop_size: int = 3
    loco_wait_time: int = 5

    def __init__(self, conf):
        # parameters for feature:
        self.workshop_duration: int = conf["parameters"]["workshop"]
        self.shunting_time: int = conf["parameters"]["shuntingMovement"]
        self.movement_time: int = conf["parameters"]["movement"]
        self.coupling_time: int = conf["parameters"]["coupling"]

        self.number_of_wagons: int = 20
        self.number_of_workshops: int = 2
        self.workshop_size: int = 3
        self.loco_wait_time: int = 5
