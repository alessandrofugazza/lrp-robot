from Raspi_MotorHAT.Raspi_PWM_Servo_Driver import PWM

class Servos:
    def __init__(self, addr=0x40, deflect_90_in_ms=1.0):
        """addr: The i2c address of the PWM chip. 
        deflect_90_in_ms: set this to calibrate the servo motors. 
        it is what a deflection of 90 degrees is 
        in terms of a pulse length in milliseconds."""
        self._pwm = PWM(addr)
        pwm_frequency = 50 
        self._pwm.setPWMFreq(pwm_frequency)
        servo_mid_point_ms = 1.5
        period_in_ms = 1000 / pwm_frequency
        pulse_steps = 4096
        steps_per_ms = pulse_steps / period_in_ms
        self.steps_per_degree = (deflect_90_in_ms * steps_per_ms) / 90
        self.servo_mid_point_steps = servo_mid_point_ms * steps_per_ms

        self._channels = (0, 2, 4, 6)

    def stop_all(self): 
        # 0 in start is nothing, 4096 sets the OFF bit. 
        off_bit = 4096 
        for channel in self._channels:
            self._pwm.setPWM(channel, 0, off_bit)

    def _convert_degrees_to_steps(self, position): 
        return int(self.servo_mid_point_steps + (position * self.steps_per_degree))
    
    def set_servo_angle(self, channel, angle): 
        """position: The position in degrees from the center. -90 to 90"""
        if angle > 90 or angle < -90: 
            raise ValueError("Angle outside of range")
        off_step = self._convert_degrees_to_steps(angle) 
        self._pwm.setPWM(self.channels[channel], 0, off_step)