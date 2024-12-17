import pygame
import game
import pypboy.ui
import config
from config import user_config

if config.gpioAvailable():
    from gpiozero import LED

class BaseModule(game.EntityGroup):

    submodules = []

    def __init__(self, boy, *args, **kwargs):
        super(BaseModule, self).__init__()

        if not hasattr(self, 'GPIO_LED_ID'):
            self.gpio_led_id = None

        if config.gpioAvailable() and self.gpio_led_id:
            self.led = LED(self.gpio_led_id)
            self.led.on()
        else:
            self.led = None

        self.pypboy = boy
        self.position = (0, 40)

        self.footer = pypboy.ui.Footer()
        self.footer.menu = []
        for mod in self.submodules:
            self.footer.menu.append(mod.label)
        self.footer.selected = self.footer.menu[0]
        self.footer.position = (0, user_config['video']['height'].get() - 53)  # 80
        self.add(self.footer)

        self.current_module = 0
        self.switch_submodule(self.current_module)

        self.action_handlers = {
            "pause": self.handle_pause,
            "resume": self.handle_resume
        }
        if user_config['audio']['enabled'].get():
            self.module_change_sfx = pygame.mixer.Sound(
                config.USER_DIR + 'sounds/module_change.ogg')

    def move(self, x, y):
        super(BaseModule, self).move(x, y)
        if hasattr(self, 'active'):
            self.active.move(x, y)

    def switch_submodule(self, module):
        self.current_module = module
        if hasattr(self, 'active') and self.active:
            self.active.handle_action("pause")
            self.remove(self.active)
        if len(self.submodules) > module:
            self.active = self.submodules[module]
            self.active.parent = self
            self.active.handle_action("resume")
            self.footer.select(self.footer.menu[module])
            self.add(self.active)
        else:
            print("No submodule at %d" % module)

    def render(self, interval):
        self.active.render(interval)
        super(BaseModule, self).render(interval)

    def handle_action(self, action, value=0):
        if action.startswith("knob_"):
            kb = action[5:]
            # Up is down and down is up.
            if kb == 'down':
                if self.current_module < (len(self.submodules) - 1):
                    self.switch_submodule(self.current_module + 1)
            elif kb == 'up':
                if self.current_module != 0:
                    self.switch_submodule(self.current_module - 1)
            else:
                num = int(action[-1])
                self.switch_submodule(num - 1)
        elif action in self.action_handlers:
            self.action_handlers[action]()
        else:
            if hasattr(self, 'active') and self.active:
                self.active.handle_action(action, value)

    def handle_event(self, event):
        if hasattr(self, 'active') and self.active:
            self.active.handle_event(event)

    def handle_pause(self):
        self.paused = True
        if self.led:
            self.led.off()

    def handle_resume(self):
        self.paused = False
        if self.led:
            self.led.on()
        if user_config['audio']['enabled'].get():
            self.module_change_sfx.play()


class SubModule(game.EntityGroup):

    def __init__(self, parent, *args, **kwargs):
        super(SubModule, self).__init__()
        self.parent = parent

        self.action_handlers = {
            "pause": self.handle_pause,
            "resume": self.handle_resume
        }

        if user_config['audio']['enabled'].get():
            self.submodule_change_sfx = pygame.mixer.Sound(
                config.USER_DIR + 'sounds/submodule_change.ogg')

    def handle_action(self, action, value=0):
        if action.startswith("dial_"):
            if hasattr(self, "menu"):
                self.menu.handle_action(action)
        elif action in self.action_handlers:
            self.action_handlers[action]()

    def handle_event(self, event):
        pass

    def handle_pause(self):
        self.paused = True

    def handle_resume(self):
        self.paused = False
        if user_config['audio']['enabled'].get():
            self.submodule_change_sfx.play()
