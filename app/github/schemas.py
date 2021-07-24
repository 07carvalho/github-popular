from pydantic import BaseModel


class SuccessPopularityResponse(BaseModel):
    popular: bool


class ErrorResponse(BaseModel):
    detail: str
