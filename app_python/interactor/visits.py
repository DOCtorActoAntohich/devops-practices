from app_python.use_case import ExtractVisitStatistics


class VisitsInteractor:
    @classmethod
    def statistics(cls) -> str:
        use_case = ExtractVisitStatistics()
        n_visits, last_visit = use_case.execute()
        return (
            f"Total visits since restart: {n_visits}\n"
            f"Last visit: {last_visit}"
        )
