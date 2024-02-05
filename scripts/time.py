class Timer:
    def __init__(self, end_tick: int = float("inf"), start_on=True, func=None) -> None:
        self.func = func

        self.end_tick = end_tick
        self.current_tick = 0

        self.active = start_on

    def deactivate(self):
        self.active = False
        self.current_tick = 0

    def activate(self):
        self.active = True
        self.current_tick = 0

    def update(self) -> float:
        if self.active:
            self.current_tick += 1
            if self.current_tick >= self.end_tick:
                self.deactivate()
                if self.func:
                    self.func()
        return 0


class TimersGroup:
    def __init__(self):
        self.timers = {}

    def __getitem__(self, item):
        return self.timers[item].current_tick

    def __setitem__(self, key, value):
        self.timers[key] = value

    def update(self):
        for key in self.timers.keys():
            self.timers[key].update()
