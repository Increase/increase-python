# File generated from our OpenAPI spec by Stainless.

from . import types
from ._types import NoneType, Transport, ProxiesTypes
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
    ProxiesTypes,
    AsyncIncrease,
    RequestOptions,
)
from ._version import __title__, __version__
from ._exceptions import (
    APIError,
    ConflictError,
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
    IdempotencyConflictError,
    UnprocessableEntityError,
    APIResponseValidationError,
    InsufficientPermissionsError,
    IdempotencyUnprocessableError,
    UniqueIdentifierAlreadyExistsError,
)

__all__ = [
    "types",
    "__version__",
    "__title__",
    "NoneType",
    "Transport",
    "ProxiesTypes",
    "APIError",
    "APIConnectionError",
    "APIResponseValidationError",
    "APIStatusError",
    "APITimeoutError",
    "AuthenticationError",
    "BadRequestError",
    "ConflictError",
    "InternalServerError",
    "NotFoundError",
    "PermissionDeniedError",
    "RateLimitError",
    "UnprocessableEntityError",
    "APIMethodNotFoundError",
    "EnvironmentMismatchError",
    "IdempotencyConflictError",
    "IdempotencyUnprocessableError",
    "InsufficientPermissionsError",
    "InvalidAPIKeyError",
    "InvalidOperationError",
    "InvalidParametersError",
    "MalformedRequestError",
    "ObjectNotFoundError",
    "PrivateFeatureError",
    "RateLimitedError",
    "UniqueIdentifierAlreadyExistsError",
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
]

# Update the __module__ attribute for exported symbols so that
# error messages point to this module instead of the module
# it was originally defined in, e.g.
# increase._base_exceptions.NotFoundError -> increase.NotFoundError
__locals = locals()
for __name in __all__:
    if not __name.startswith("__"):
        try:
            setattr(__locals[__name], "__module__", "increase")
        except (TypeError, AttributeError):
            # Some of our exported symbols are builtins which we can't set attributes for.
            pass
