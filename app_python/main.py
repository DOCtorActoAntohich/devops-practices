from fastapi import FastAPI
from starlette.responses import JSONResponse
from starlette.requests import Request as StarletteRequest
from starlette.status import HTTP_400_BAD_REQUEST
from prometheus_fastapi_instrumentator import Instrumentator

from app_python.errors import InvalidTimeZoneError
from app_python.interactor import TimeInteractor, VisitsInteractor


app = FastAPI()


@app.exception_handler(InvalidTimeZoneError)
async def on_invalid_id_error(_request: StarletteRequest, exc: InvalidTimeZoneError):
    return JSONResponse({"error_details": f"{exc}"}, status_code=HTTP_400_BAD_REQUEST)


@app.on_event("startup")
async def startup():
    Instrumentator().instrument(app).expose(app)


@app.get("/")
async def read_root() -> str:
    return TimeInteractor.get_time_in("Europe/Moscow")


@app.get("/visits")
async def get_visits_statistics() -> str:
    return VisitsInteractor.statistics()


@app.get("/zone/{iana_time_zone:path}")
async def read_by_timezone(iana_time_zone: str) -> str:
    return TimeInteractor.get_time_in(iana_time_zone)
