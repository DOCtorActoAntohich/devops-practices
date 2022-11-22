import datetime
import pathlib

VisitsFile = pathlib.Path("/app/data/visits")


class ExtractVisitStatistics:
    def execute(self) -> tuple[int, str]:
        if not VisitsFile.exists():
            return 0, str(datetime.datetime.now())

        with VisitsFile.open() as file:
            n_visits = int(file.readline().strip())
            last_access = file.readline().strip()
        return n_visits, last_access


class UpdateVisitStatistics:
    def __init__(self, last_access: datetime.datetime) -> None:
        self.last_access = last_access

    def execute(self) -> tuple[int, str]:
        n_visits, _ = ExtractVisitStatistics().execute()  # bad but lazy.
        n_visits += 1
        with VisitsFile.open(mode="w") as file:
            file.write(f"{n_visits}\n{self.last_access}\n")
        return n_visits, str(self.last_access)
