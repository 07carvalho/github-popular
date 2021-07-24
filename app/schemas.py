from pydantic import BaseModel


class HealthCheckResponse(BaseModel):
    result: str
