from typing import ClassVar


class Time:
    hours: int
    minutes: int
    seconds: int

    max_hours: ClassVar[int] = 23
    max_minutes : ClassVar[int] = 59
    max_seconds : ClassVar[int] = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self) -> str:
        return f"{str(self.hours).zfill(2)}:{str(self.minutes).zfill(2)}:{str(self.seconds).zfill(2)}"

    def next_second(self):
        self.seconds = (self.seconds + 1) % 60
        self.minutes = (self.minutes + (self.seconds == 0)) % 60
        self.hours = (self.hours + (self.minutes == 0 and self.seconds == 0)) % 24

        return self.get_time()
