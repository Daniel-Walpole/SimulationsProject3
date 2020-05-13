import math
import matplotlib.pyplot as plt
import dynamics


class PredatorPrey(dynamics.Dynamics):
    def __init__(self, preyBirth, preyDeath, predBirth, predDeath, time_step):
        numEquations = 3                            # set the number of state equations

        # set constants
        self.preyInc = preyBirth
        self.preyDec = preyDeath
        self.predInc = predBirth
        self.predDec = predDeath

        super().__init__(numEquations, time_step)   # initialize super class dynamics (Euler Method)

        # create variables to hold the state history for plotting
        self.Q = [[] for i in range(numEquations)]
        self.T = []

    def initialize(self, preyWeight, predWeight, pestWeight):
        # set state variable initial values
        self.q[0] = preyWeight
        self.q[1] = predWeight
        self.q[2] = pestWeight
        # initialize state history used for plotting
        self.Q = [[self.q[i]] for i in range(len(self.q))]
        self.T = [0.0]

    def advance(self, count):
        # compute "count" updates of the state equations
        for i in range(count):
            self.dq[0] = (self.preyInc * self.q[0]) - (self.preyDec * self.q[0] * self.q[1]) -(0.1 * self.dq[2]) #prey function
            self.dq[1] = (self.predInc * self.q[0] * self.q[1]) - (self.predDec * self.q[1]) - (0.3 * self.dq[2]) #predator function
            self.dq[2] = - (.005 * self.q[2]) #pest function 
            self.step()
        # save the updated state variables after the "count" updates for plotting
        [self.Q[i].append(self.q[i]) for i in range(len(self.q))]
        self.T.append(self.now())

    def print(self):
        # custom print for current simulation
        print('time={0:10f} prey={1:10f} predator={2:10f} pesticide={3:10f}'.format(self.time, self.q[0], self.q[1], self.q[2]))

    def plot(self):
        # custom plot for current simulation
        plt.figure()
        plt.subplot(311)
        plt.plot(self.T, self.Q[0], 'k')
        plt.ylabel('prey')

        plt.subplot(312)
        plt.plot(self.T, self.Q[1], 'r')
        plt.ylabel('predator')

        plt.subplot(313)
        plt.plot(self.T, self.Q[2], 'b')
        plt.ylabel('pesticide')

        plt.figure()
        plt.plot(self.T, self.Q[0], 'k', self.T, self.Q[1], 'r--')
        plt.ylabel('prey - predator')
        plt.xlabel('time')

        plt.figure()
        plt.plot(self.Q[0], self.Q[1], 'b')
        plt.ylabel('predator')
        plt.xlabel('prey')

        plt.show()


# set parameters for predator-prey simulation
d
# parameters describing the simulation time
endTime = 1000.0       # length of simulation (i.e. end time)
dt = 0.005             # time step size used to update state equations

# parameters describing the real system
preyBirth = 0.0005
preyDeath = 0.001
predBirth = 0.0005
predDeath = 0.01
initPreyWt = 150.0
initPredWt = 50.0
initPest = 100.0



# create the simulation and initialize state variables
P = PredatorPrey(preyBirth, preyDeath, predBirth, predDeath, dt)
P.initialize(initPreyWt, initPredWt, initPest)

# run the simulation
displayInterval = 1         # number of state updates before saving state
P.print()
while P.now() < endTime:
    P.advance(displayInterval)
    P.print()               # call print to see numeric values of state per display interval

P.plot()                    # call custom plot
