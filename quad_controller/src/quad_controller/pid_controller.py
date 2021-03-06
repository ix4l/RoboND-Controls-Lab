# Copyright (C) 2017 Udacity Inc.
# All Rights Reserved.

# Author: Brandon Kinman


class PIDController:
    def __init__(self, kp = 0.0, ki = 0.0, kd = 0.0, max_windup = 10):
        #TODO
        # PID Controller uses specific kp, ki, kd values
        self.kp = float(kp)
        self.ki = float(ki)
        self.kd = float(kd)

        # set max_windup
        self.max_windup_ = float(max_windup)

        # Store relevant data
        self.last_timestamp_ = 0.0
        self.target_ = 0.0
        self.error_sum_ = 0.0
        self.last_error_ =0.0

    def reset(self):
        #TODO
        self.target_ = 0.0
        self.kp_ = 0.0
        self.ki_ = 0.0
        self.kd_ = 0.0

        self.last_timestamp_ = 0.0
        self.error_sum_ = 0.0
        self.last_error_ = 0.0

    def setTarget(self, target):
        #TODO
        self.target_ = float(target)

    def setKP(self, kp):
        #TODO
        self.kp_ = float(kp)

    def setKI(self, ki):
        #TODO
        self.ki_ = float(ki)

    def setKD(self, kd):
        #TODO
        self.kd = float(kd)

    def setMaxWindup(self, max_windup):
        #TODO
        self.max_windup_ = flaot(max_windup)

    def update(self, measured_value, timestamp):
        #TODO
        delta_time = timestamp - self.last_timestamp_
        if delta_time == 0:
            return 0

        #calculate the error
        error = self.target_ - measured_value
        #set the last_timestamp_
        self.last_timestamp_ = timestamp
        #sum the errors
        self.error_sum_ += error * delta_time
        # update past error
        self.last_error_ = error
        # Find delta error
        delta_error = error - self.last_error_

        # address max_windup
        if self.error_sum_ > self.max_windup_:
            self.error_sum_ = self.max_windup_
        elif self.error_sum_ < -self.max_windup_:
            self.error_sum_ = -self.max_windup_

        # Proportional, intergral, derivative error
        p = self.kp_ * error
        i = self.ki_ * self.error_sum_
        d = self.kd_ * delta_error

        # Set control effort
        u = p + i + d

        return u 
