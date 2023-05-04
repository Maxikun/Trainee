import time
import matplotlib.pyplot as plt
import numpy as np

class PIDController:
    def __init__(self, kp, ki, kd, dt, setpoint):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.dt = dt
        self.setpoint = setpoint
        self.clear()

    def clear(self):
        self.last_error = 0
        self.derivative = 0
        self.last_time = None
        self.integral = 0
        self.errors = []
        self.times = []
        self.outputs = []

    def update(self, process_variable):
        # Calculate time since last update
        now = time.time()
        if self.last_time is None:
            self.last_time = now
            return 0.0
        dt = now - self.last_time

        # Calculate error
        error = self.setpoint - process_variable

        # Calculate derivative term
        self.derivative = (error - self.last_error) / dt if dt > 0 else 0.0

        # Calculate integral term
        self.integral += error * dt


        # Calculate output
        output = self.kp * error + self.ki * self.integral + self.kd * self.derivative

        # Save error, time, and output for plotting
        self.errors.append(error)
        self.times.append(now)
        self.outputs.append(output)

        # Update last error and time
        self.last_error = error
        self.last_time = now

        return output

    def plot(self):
        plt.subplot(2, 1, 1)
        plt.plot(self.times, self.setpoint * np.ones_like(self.times), 'k--', label='Setpoint')
        plt.plot(self.times, self.outputs, label='Output')
        plt.ylabel('Output')
        plt.legend(loc='best')

        plt.subplot(2, 1, 2)
        plt.plot(self.times, self.errors, label='Error')
        plt.ylabel('Error')
        plt.legend(loc='best')
        plt.xlabel('Time (sec)')
        plt.show()


pid = PIDController(kp=0.003, ki=0.5, kd=0.01, dt=0.01, setpoint=0.0)
process_variable = 10.0

for i in range(10000):
    output = pid.update(process_variable)
    process_variable += output
    time.sleep(pid.dt)

pid.plot()
