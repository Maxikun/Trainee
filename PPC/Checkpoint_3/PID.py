import matplotlib.pyplot as plt
class PIDController:
    def __init__(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.prev_error = 0
        self.integral = 0

    def pid_update(self, curr_error):
        # Calculate proportional term
        p_term = self.kp * curr_error

        # Calculate integral term
        self.integral += curr_error
        i_term = self.ki * self.integral

        # Calculate derivative term
        d_term = self.kd * (curr_error - self.prev_error)
        self.prev_error = curr_error

        # Calculate total PID output
        pid_output = p_term + i_term + d_term

        # Update current error
        curr_error -= pid_output

        return curr_error

# Initialize PID controller
pid = PIDController(kp=0.05, ki=0.001, kd=0.00001)

# Initialize error and time arrays
curr_error = 10
errors = [curr_error]
times = [0]

# Simulate PID controller response over time
dt = 0.01  # time step
t = 0     # initial time
while ((curr_error > 0.00001) or (curr_error < -0.00001)):
    t += dt
    curr_error = pid.pid_update(curr_error)
    errors.append(curr_error)
    times.append(t)

# Plot error vs time
plt.plot(times, errors)
plt.xlabel('Time (s)')
plt.ylabel('Error')
plt.title('PID Response')
plt.grid()
plt.show()
