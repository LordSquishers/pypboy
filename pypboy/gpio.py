from gpiozero import Button

class RotaryEncoder:
    def __init__(self, pin_a, pin_b, pull_up = True):
        self.when_rotated = lambda *args: None

        self.gpio_a = Button(pin_a, pull_up)
        self.gpio_b = Button(pin_b, pull_up)

        self.lev_a = 0
        self.lev_b = 0

        self.last_gpio = None

        self.gpio_a.when_pressed = lambda *args: self._pulse(self.gpio_a, 1)
        self.gpio_a.when_released = lambda *args: self._pulse(self.gpio_a, 0)

        self.gpio_b.when_pressed = lambda *args: self._pulse(self.gpio_b, 1)
        self.gpio_b.when_released = lambda *args: self._pulse(self.gpio_b, 0)

    def _pulse(self, gpio, level):
        #             +---------+         +---------+      0
        #             |         |         |         |
        #   A         |         |         |         |
        #             |         |         |         |
        #   +---------+         +---------+         +----- 1
        #
        #       +---------+         +---------+            0
        #       |         |         |         |
        #   B   |         |         |         |
        #       |         |         |         |
        #   ----+         +---------+         +---------+  1
        if gpio == self.gpio_a:
            self.lev_a = level
        else:
            self.lev_b = level

        if gpio != self.last_gpio:
            self.last_gpio = gpio

            if (gpio == self.gpio_a) and (level == 0):
                if self.lev_b == 0:
                    self.when_rotated(1)
            elif (gpio == self.gpio_b) and (level == 1):
                if self.lev_a != 0:
                    self.when_rotated(-1)

class RotaryEncoderClickable:
    def __init__(self, pin_a, pin_b, button_pin, encoder_pull_up = True, button_pull_up = True):
        self.rotary_encoder = RotaryEncoder(pin_a, pin_b, encoder_pull_up)
        self.button = Button(button_pin, button_pull_up)

    @property
    def when_rotated(self):
        return self.rotary_encoder.when_rotated

    @when_rotated.setter
    def when_rotated(self, action):
        self.rotary_encoder.when_rotated = action

    @property
    def when_pressed(self):
        return self.button.when_pressed

    @when_pressed.setter
    def when_pressed(self, action):
        self.button.when_pressed = action
