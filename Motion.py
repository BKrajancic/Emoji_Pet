class Motion():
    def __init__(self, acceleration, velocity, position, terminal_velocity):
        self.acceleration = acceleration
        self.velocity = velocity
        self.position = position
        self.terminal_velocity = terminal_velocity

    def apply_velocity(self):
        self.position += self.velocity

    def apply_acceleration(self):
        previous_velocity = self.velocity
        self.velocity += self.acceleration
        neg_to_pos: bool = (previous_velocity < 0 and self.velocity >= 0)
        pos_to_neg: bool = (previous_velocity > 0 and self.velocity <= 0)
        if (neg_to_pos or pos_to_neg):
            self.acceleration = 0
            self.velocity = 0

    def constrain(self, padding_to_max, padding_to_min, max_pos, min_pos):
        if (self.position + padding_to_max > max_pos):
            self.velocity = -abs(self.velocity)
        elif (self.position - padding_to_min < min_pos):
            self.velocity = abs(self.velocity)

    def apply_gravity(self, scene_height, gravity):
        if (self.position < scene_height):
            self.acceleration = gravity
        if (abs(self.position - scene_height) < 1):
            if (self.velocity == 0):
                self.position = scene_height

    def apply_drag(self, drag):
        if self.velocity > 0:
            self.acceleration = -drag
        elif self.velocity < 0:
            self.acceleration = drag

    def apply_terminal_velocity(self):
        if (self.velocity < -self.terminal_velocity):
            self.velocity = -self.terminal_velocity
        elif (self.velocity > self.terminal_velocity):
            self.velocity = self.terminal_velocity

    def set_motion(self, velocity, acceleration):
        self.velocity = velocity
        self.acceleration = acceleration
