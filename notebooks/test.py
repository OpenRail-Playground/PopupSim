# %%
import simpy

# %%

DRIVE_TIMES = {
    "a" : {
        "b1": 5,
        "b2": 5,
        "c": 10,
        "kopf": 5
    },
    "b1" : {
        "a": 5,
        "c": 10,
        "kopf": 5
    },
    "b2" : {
        "a": 5,
        "c": 10,
        "kopf": 5
    },
    "c" : {
        "a": 10,
        "b1": 5,
        "b2": 5,
        "kopf": 5
    },
    "kopf" : {
        "a": 5,
        "b1": 5,
        "b2": 5,
        "c": 10,
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
        self.name: self.wagons
     }
  

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
    def __init__(self, env, global_setting, id=1):
        self.env = env
        self.global_setting = global_setting

        self.id = id
        self.coupled_with = []
        self.position = "kopf"

        # Start the run process everytime an instance is created.
        self.action = env.process(self.run())

    def log(self):
      return {
          "lokomotiveId": self.id,
          "coupledWith:": self.coupled_with,
          "position": self.position,
        }

    def run(self):
        print('Starting in Kopf %d' % self.env.now)
        self.global_setting.log_global_state()

        # drive to b1
        
        yield self.env.process(self.drive_to("b1"))
       


        yield self.env.process(self.coupling())


        # drive to C
        
        yield self.env.process(self.drive_to("c"))
        

        # uncoupling

        yield self.env.process(self.uncoupling())


        # drive to from C to a
        
        yield self.env.process(self.drive_to("a"))
        

        # coupling
        yield self.env.process(self.coupling())

        # drive from a to b1
        
        yield self.env.process(self.drive_to("b1"))
        

        # uncoupling
        yield self.env.process(self.uncoupling())

        # drive from b1 to kopf
        
        yield self.env.process(self.drive_to("kopf"))
       

        self.global_setting.log_global_state()


    def coupling(self, duration=5):
        print('start coupling %d' % self.env.now)
        yield self.env.timeout(duration)
        print('finished coupling %d' % self.env.now)
        self.global_setting.log_global_state()
    
    def uncoupling(self, duration=5):
        print('start uncoupling %d' % self.env.now)
        yield self.env.timeout(duration)
        print('finished uncoupling %d' % self.env.now)
        self.global_setting.log_global_state()
    
    def drive_to(self, target):
        print(f"start driving from {self.position} to {target} - {self.env.now}")
  
        # compute driving time
        driving_time = DRIVE_TIMES[self.position][target]
        yield self.env.timeout(driving_time)
        self.position = target
  
        print(f"arrived {target} - {self.env.now}")
        self.global_setting.log_global_state()
# %%

class globalSetting(object):

  def __init__(self):
   
    self.env = simpy.Environment()

    # create locomotive
    self.locomotive = locomotive(self.env, self)

    # create wagons
    self.wagons = []
    for i in range(20):
      self.wagons.append(wagon(self.env, i))

    # create tracks
    self.retrofitted_track = track(self.env, "retrofitted")
    self.toBeRetrofitted = track(self.env, "toBeRetrofitted")

    # create workshop tracks
    self.workshop_tracks = []
    for i in range(2):
      self.workshop_tracks.append(track(self.env, f"WorkshopGleis{i}"))

  
    self.global_log = []

    self.env.run()

  def log_global_state(self):
     
     self.global_log.append(
        {
           "locomotive": self.locomotive.log(),
           "retrofitted": self.retrofitted_track.log(),
           "toBeRetrofitted": self.toBeRetrofitted.log(),
           "workshopGleise":[ workshop_track.log() for workshop_track in self.workshop_tracks],
           "timestamp": self.env.now
        }
     )
    
     

#%%

# env = simpy.Environment()
# loc = locomotive(env)
# env.run()

gs = globalSetting()
# %%
