# %%
import simpy

# %%

DRIVE_TIMES = {
    "toBeRetrofitted" : {
        "WorkshopGleis0": 5,
        "WorkshopGleis1": 5,
        "retrofitted": 10,
        "kopf": 5
    },
    "WorkshopGleis0" : {
        "toBeRetrofitted": 5,
        "retrofitted": 10,
        "kopf": 5
    },
    "WorkshopGleis1" : {
        "toBeRetrofitted": 5,
        "retrofitted": 10,
        "kopf": 5
    },
    "retrofitted" : {
        "toBeRetrofitted": 10,
        "WorkshopGleis0": 5,
        "WorkshopGleis1": 5,
        "kopf": 5
    },
    "kopf" : {
        "toBeRetrofitted": 5,
        "WorkshopGleis0": 5,
        "WorkshopGleis1": 5,
        "retrofitted": 10,
        "kopf": 5
    },

}

class globalLogger():
  pass

class track(object):

  def __init__(self, env, name):
     self.env = env
     self.name = name
     self.wagons = []

  def log(self):
     return {
        self.name: [wagon.log() for wagon in self.wagons],
     }
  
  def add_wagon(self, wagon):
     self.wagons = [wagon] + self.wagons
  

class WorkshopTrack(track):
   def __init__(self, env, name):
     self.env = env
     self.name = name
     self.wagons = []
     self.is_done = False

   def change_coupling_system(self):
      yield self.env.timeout(180) 
      for wagon in self.wagons:
         wagon.couplerType = 'dac'

   def wagons_have_coupling_system(self):
      for wagon in self.wagons:
         if wagon.couplerType != 'dac':
            return False
      return True
   
class wagon(object):
    
    def __init__(self, env, id, length=20, couplerType="sc"):
        self.env = env
        self.id = id
        self.length = length
        self.couplerType = couplerType

    def log(self):
     return {
        "wagonId": self.id,
        "length": self.length,
        "couplerType": self.couplerType
     }



class locomotive(object):
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
      self.env.process(self.global_setting.tracks.workshop_tracks[1].change_coupling_system())
      while (self.global_setting.tracks.toBeRetrofitted.wagons + self.global_setting.tracks.workshop_tracks[0].wagons + self.global_setting.tracks.workshop_tracks[1].wagons):

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
        
        print('Starting in Kopf %d' % self.env.now)
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
        yield self.env.process(self.drive_to(self.global_setting.tracks.toBeRetrofitted))
        

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
        print('start coupling %d' % self.env.now)
        yield self.env.timeout(duration)
        self.coupled_with += self.cur_track.wagons[:3]
        print('finished coupling %d' % self.env.now)

        self.global_setting.log_global_state()
    
    def uncoupling(self, duration=5):
        print('start uncoupling %d' % self.env.now)
        yield self.env.timeout(duration)
        self.coupled_with = []
        print('finished uncoupling %d' % self.env.now)
        self.global_setting.log_global_state()
    
    def drive_to(self, target_track):
        print(f"start driving from {self.cur_track.name} to {target_track.name} - {self.env.now}")
  
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
# %%
class TrackCollection(object):
  def __init__(self, env) -> None:
      self.head_track = track(env, "kopf")
      self.retrofitted = track(env, "retrofitted")
      self.toBeRetrofitted = track(env, "toBeRetrofitted")
      self.workshop_tracks = [
         WorkshopTrack(env, f"WorkshopGleis{i}") for i in range(2)
      ]

  def log(self):
      logs = self.retrofitted.log()
      logs.update(self.toBeRetrofitted.log())
      logs.update({"workshopGleise":[ workshop_track.log() for workshop_track in self.workshop_tracks]})
      return logs
    


class globalSetting(object):

  def __init__(self):
   
    self.env = simpy.Environment()

    # create tracks
    self.tracks = TrackCollection(self.env)

    # create wagons
    self.wagons = []
    for i in range(20):
      self.wagons.append(wagon(self.env, i))

    for i in range(3):
      self.wagons[i].couplerType = 'dac'

    # add wagons to tracks
    self.tracks.workshop_tracks[0].wagons = self.wagons[:3]
    self.tracks.workshop_tracks[1].wagons = self.wagons[3:6]
    self.tracks.toBeRetrofitted.wagons = self.wagons[6:]

    # self.workshop_1 = simpy.Resource(self.env, 1)
    # self.workshop_2 = simpy.Resource(self.env, 1)

    # create locomotive
    self.locomotive = locomotive(self.env, self, self.tracks.head_track)

    # create workshop tracks

  
    self.global_log = []

    self.env.run(until=1500)

  def log_global_state(self):
     
     self.global_log.append(
        {
           "locomotive": self.locomotive.log(),
           "timestamp": self.env.now,
           "tracks": self.tracks.log()
        }
     )

  def get_available_workshop(self):
     for track in self.tracks.workshop_tracks:
        if track.wagons_have_coupling_system():
           return track
     return None
    
     

#%%

# env = simpy.Environment()
# loc = locomotive(env)
# env.run()

gs = globalSetting()
# %%
