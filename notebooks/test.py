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

  def __init__(self, name):
     self.name = name
     self.wagons = []

  def log(self):
     return {
        self.name: self.wagons
     }
  
class globalSetting(object):
   
   env = simpy.Environment()
  loc = locomotive(env)
  env.run()
    

class waggon(object):
    
    def __init__(self, id, length, couplerType, env):
        
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
    def __init__(self, env, id=1, ):
        self.env = env

        self.id = id
        self.coupled_with = []
        self.position = "kopf"

        # Start the run process everytime an instance is created.
        self.action = env.process(self.run())

    def log(self):
      return {
          "lokomotive": {
            "lokomotiveId": self.id,
            "coupledWith:": self.coupled_with,
          "position": self.position,
        }
      }

    def run(self):
        print('Starting in Kopf %d' % self.env.now)

        # drive to b1
        
        yield self.env.process(self.drive_to("b1"))
       


        yield self.env.process(self.coupling())


        # drive to C
        
        yield self.env.process(self.drive_to("b1", "c"))
        

        # uncoupling

        yield self.env.process(self.uncoupling())


        # drive to from C to a
        
        yield self.env.process(self.drive_to("c", "a"))
        

        # coupling
        yield self.env.process(self.coupling())

        # drive from a to b1
        
        yield self.env.process(self.drive_to("a", "b1"))
        

        # uncoupling
        yield self.env.process(self.uncoupling())

        # drive from b1 to kopf
        
        yield self.env.process(self.drive_to("b1", "kopf"))
       

        print('finished %d' % self.env.now)


    def coupling(self, duration=5):
        print('start coupling %d' % self.env.now)
        yield self.env.timeout(duration)
        print('finished coupling %d' % self.env.now)
    
    def uncoupling(self, duration=5):
        print('start uncoupling %d' % self.env.now)
        yield self.env.timeout(duration)
        print('finished uncoupling %d' % self.env.now)
    
    def drive_to(self, target):
        print(f"start driving from {self.position} to {target} - {self.env.now}")
  
        # compute driving time
        driving_time = DRIVE_TIMES[self.position][target]
        yield self.env.timeout(driving_time)
  
        print(f"arrived {target} - {self.env.now}")
        log_change(locomove, waggon1, waggon2, ...)
# %%

env = simpy.Environment()
loc = locomotive(env)
env.run()
# %%
