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

class waggon(object):
    
    
    def __init__(self, id, env):
        
        self.status = "waiting"
        self.id = id
    


class locomotive(object):
    def __init__(self, env):
        self.env = env
        # Start the run process everytime an instance is created.
        self.action = env.process(self.run())

    def run(self):
        print('Starting in Kopf %d' % self.env.now)

        # drive to b1
        
        yield self.env.process(self.drive("kopf", "b1"))
       


        yield self.env.process(self.coupling())


        # drive to C
        
        yield self.env.process(self.drive("b1", "c"))
        

        # uncoupling

        yield self.env.process(self.uncoupling())


        # drive to from C to a
        
        yield self.env.process(self.drive("c", "a"))
        

        # coupling
        yield self.env.process(self.coupling())

        # drive from a to b1
        
        yield self.env.process(self.drive("a", "b1"))
        

        # uncoupling
        yield self.env.process(self.uncoupling())

        # drive from b1 to kopf
        
        yield self.env.process(self.drive("b1", "kopf"))
       

        print('finished %d' % self.env.now)


    def coupling(self, duration=5):
        print('start coupling %d' % self.env.now)
        yield self.env.timeout(duration)
        print('finished coupling %d' % self.env.now)
    
    def uncoupling(self, duration=5):
        print('start uncoupling %d' % self.env.now)
        yield self.env.timeout(duration)
        print('finished uncoupling %d' % self.env.now)
    
    def drive(self, start, end):
        print(f"start driving from {start} to {end} - {self.env.now}")
  
        # compute driving time
        driving_time = DRIVE_TIMES[start][end]
        yield self.env.timeout(driving_time)
  
        print(f"arrived {end} - {self.env.now}")
# %%

env = simpy.Environment()
loc = locomotive(env)
env.run()
# %%
