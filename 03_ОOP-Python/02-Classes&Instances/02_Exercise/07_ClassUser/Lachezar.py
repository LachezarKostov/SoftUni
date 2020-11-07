from dataclasses import dataclass


@dataclass
class Me:
    name: str = "Lachezar Kostov"
    mail: str = "LachezarKostov@abv.bg"
    job: str = ""

    def job(self):
        if self.job:
            return "Yhea! You did it !"
        self.search_for_job()
        return "Good luck this time!"
