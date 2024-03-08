# File generated from our OpenAPI spec by Stainless.

from . import types
from ._types import NOT_GIVEN, NoneType, NotGiven, Transport, ProxiesTypes
from ._utils import file_from_path
from ._client import (
    ENVIRONMENTS,
    Client,
    Stream,
    Timeout,
    Increase,
    Transport,
    AsyncClient,
    AsyncStream,
    AsyncIncrease,
    RequestOptions,
)
from ._models import BaseModel
from ._version import __title__, __version__
from ._response import APIResponse as APIResponse, AsyncAPIResponse as AsyncAPIResponse
from ._exceptions import (
    APIError,
    ConflictError,
    IncreaseError,
    NotFoundError,
    APIStatusError,
    RateLimitError,
    APITimeoutError,
    BadRequestError,
    RateLimitedError,
    APIConnectionError,
    InvalidAPIKeyError,
    AuthenticationError,
    InternalServerError,
    ObjectNotFoundError,
    PrivateFeatureError,
    InvalidOperationError,
    MalformedRequestError,
    PermissionDeniedError,
    APIMethodNotFoundError,
    InvalidParametersError,
    EnvironmentMismatchError,
    UnprocessableEntityError,
    APIResponseValidationError,
    InsufficientPermissionsError,
    IdempotencyKeyAlreadyUsedError,
)
from ._utils._logs import setup_logging as _setup_logging

__all__ = [
    "types",
    "__version__",
    "__title__",
    "NoneType",
    "Transport",
    "ProxiesTypes",
    "NotGiven",
    "NOT_GIVEN",
    "IncreaseError",
    "APIError",
    "APIStatusError",
    "APITimeoutError",
    "APIConnectionError",
    "APIResponseValidationError",
    "BadRequestError",
    "AuthenticationError",
    "PermissionDeniedError",
    "NotFoundError",
    "ConflictError",
    "UnprocessableEntityError",
    "RateLimitError",
    "InternalServerError",
    "APIMethodNotFoundError",
    "EnvironmentMismatchError",
    "IdempotencyKeyAlreadyUsedError",
    "InsufficientPermissionsError",
    "InvalidAPIKeyError",
    "InvalidOperationError",
    "InvalidParametersError",
    "MalformedRequestError",
    "ObjectNotFoundError",
    "PrivateFeatureError",
    "RateLimitedError",
    "Timeout",
    "RequestOptions",
    "Client",
    "AsyncClient",
    "Stream",
    "AsyncStream",
    "Increase",
    "AsyncIncrease",
    "ENVIRONMENTS",
    "file_from_path",
    "BaseModel",
]

_setup_logging()

# Update the __module__ attribute for exported symbols so that
# error messages point to this module instead of the module
# it was originally defined in, e.g.
# increase._exceptions.NotFoundError -> increase.NotFoundError
__locals = locals()
for __name in __all__:
    if not __name.startswith("__"):
        try:
            __locals[__name].__module__ = "increase"
        except (TypeError, AttributeError):
            # Some of our exported symbols are builtins which we can't set attributes for.
            pass
