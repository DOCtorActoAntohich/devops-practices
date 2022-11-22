import datetime

from app_python.use_case import CurrentTimeInTimeZoneUseCase, UpdateVisitStatistics


class TimeInteractor:
    @classmethod
    def get_time_in(cls, iana_time_zone: str) -> str:
        time = CurrentTimeInTimeZoneUseCase(iana_time_zone).execute()

        _ = UpdateVisitStatistics(last_access=datetime.datetime.now()).execute()

        return f"Current time in {iana_time_zone} is: {time}"
