from app_python.use_case import CurrentTimeInTimeZoneUseCase


class TimeInteractor:
    @classmethod
    def get_time_in(cls, iana_time_zone: str) -> str:
        use_case = CurrentTimeInTimeZoneUseCase(iana_time_zone)
        time = use_case.execute()
        return f"Current time in {iana_time_zone} is: {time}"
