import hashlib
from typing import Optional

from fastapi_cache import FastAPICache
from starlette.requests import Request
from starlette.responses import Response


def custom_key_builder(
    func,
    namespace: Optional[str] = "",
    request: Optional[Request] = None,
    response: Optional[Response] = None,
    args: Optional[tuple] = None,
    kwargs: Optional[dict] = None,
):
    prefix = f"{FastAPICache.get_prefix()}:{namespace}:"
    cache_key = (
        prefix
        + hashlib.md5(
            f"{func.__module__}:{func.__name__}:{args}:{kwargs}".encode("utf-8")
        ).hexdigest()
    )
    return cache_key
