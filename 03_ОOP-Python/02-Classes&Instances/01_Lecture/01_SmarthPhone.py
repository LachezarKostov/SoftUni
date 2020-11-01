class Smartphone:
    def __init__(self, memory: int, ):
        self.memory = memory
        self.apps = []
        self.is_on = False
        self.used_memory = 0

    def power(self):
        self.is_on = not self.is_on

    def install(self, app, app_memory):
        if not self.is_on:
            return f"Turn on your phone to install {app}"
        if self.memory <= (self.used_memory + app_memory):
            return f"Not enough memory to install {app}"

        self.used_memory += app_memory
        self.apps.append(app)
        return f"Installing {app}"

    def status(self):
        total_apps_count = len(self.apps)
        memory_left = self.memory - self.used_memory
        return f"Total apps: {total_apps_count}. Memory left:{memory_left}"
