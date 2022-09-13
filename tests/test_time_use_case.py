import datetime
import pytz

import pytest

from app_python.errors import InvalidTimeZoneError
from app_python.use_case import CurrentTimeInTimeZoneUseCase


def test_timezones():
    moscow_use_case = CurrentTimeInTimeZoneUseCase("Europe/Moscow")
    krasnoyarsk_use_case = CurrentTimeInTimeZoneUseCase("Asia/Krasnoyarsk")

    moscow_time = moscow_use_case.execute()
    krasnoyarsk_time = krasnoyarsk_use_case.execute()

    current_moscow_time = datetime.datetime.now(tz=pytz.timezone("Europe/Moscow"))

    moscow_dt = current_moscow_time - moscow_time
    krasnoyarsk_moscow_dt = krasnoyarsk_time - moscow_time
    assert moscow_dt.seconds < 1, "Invalid time in Moscow timezone"
    assert krasnoyarsk_moscow_dt.seconds < 1, (
        "Time delta between Moscow and Krasnoyarsk should be "
        "negligibly small because timezones are ignored"
    )

    real_moscow_utc_offset = current_moscow_time.utcoffset()
    moscow_utc_offset = moscow_time.utcoffset()
    krasnoyarsk_utc_offset = krasnoyarsk_time.utcoffset()
    offset_delta = krasnoyarsk_utc_offset - moscow_utc_offset
    assert moscow_utc_offset == real_moscow_utc_offset, "Invalid Moscow UTC offset"
    assert (
        offset_delta.seconds == 4 * 60 * 60
    ), "Invalid UTC offset between Moscow and Krasnoyarsk"


def test_non_existent_timezone():
    failing_use_case = CurrentTimeInTimeZoneUseCase("what")

    with pytest.raises(InvalidTimeZoneError):
        _ = failing_use_case.execute()
