# File generated from our OpenAPI spec by Stainless.

from typing import Any, List, Mapping, Optional, cast
from typing_extensions import Literal

import httpx

from . import _base_exceptions as exceptions
from ._utils import is_mapping
from ._base_exceptions import APIError as APIError
from ._base_exceptions import ConflictError as ConflictError
from ._base_exceptions import NotFoundError as NotFoundError
from ._base_exceptions import APIStatusError as APIStatusError
from ._base_exceptions import RateLimitError as RateLimitError
from ._base_exceptions import APITimeoutError as APITimeoutError
from ._base_exceptions import BadRequestError as BadRequestError
from ._base_exceptions import APIConnectionError as APIConnectionError
from ._base_exceptions import AuthenticationError as AuthenticationError
from ._base_exceptions import PermissionDeniedError as PermissionDeniedError
from ._base_exceptions import UnprocessableEntityError as UnprocessableEntityError
from ._base_exceptions import APIResponseValidationError as APIResponseValidationError

__all__ = [
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
    "InvalidParametersError",
    "MalformedRequestError",
    "InvalidAPIKeyError",
    "EnvironmentMismatchError",
    "InsufficientPermissionsError",
    "PrivateFeatureError",
    "APIMethodNotFoundError",
    "ObjectNotFoundError",
    "IdempotencyConflictError",
    "InvalidOperationError",
    "UniqueIdentifierAlreadyExistsError",
    "IdempotencyUnprocessableError",
    "RateLimitedError",
]


class InvalidParametersError(exceptions.BadRequestError):
    detail: Optional[str]

    errors: List[object]
    """All errors related to parsing the request parameters."""

    status: Literal[400]

    title: str

    type: Literal["invalid_parameters_error"]

    def __init__(self, message: str, *, body: object, request: httpx.Request, response: httpx.Response) -> None:
        data = cast(Mapping[str, object], body if is_mapping(body) else {})
        title = cast(Any, data.get("title"))
        super().__init__(title or message, request=request, response=response, body=body)

        self.detail = cast(Any, data.get("detail"))
        self.errors = cast(Any, data.get("errors"))
        self.status = cast(Any, data.get("status"))
        self.title = cast(Any, data.get("title"))
        self.type = cast(Any, data.get("type"))


class MalformedRequestError(exceptions.BadRequestError):
    detail: Optional[str]

    status: Literal[400]

    title: str

    type: Literal["malformed_request_error"]

    def __init__(self, message: str, *, body: object, request: httpx.Request, response: httpx.Response) -> None:
        data = cast(Mapping[str, object], body if is_mapping(body) else {})
        title = cast(Any, data.get("title"))
        super().__init__(title or message, request=request, response=response, body=body)

        self.title = title
        self.detail = cast(Any, data.get("detail"))
        self.status = cast(Any, data.get("status"))
        self.type = cast(Any, data.get("type"))


class InvalidAPIKeyError(exceptions.AuthenticationError):
    detail: Optional[str]

    status: Literal[401]

    title: str

    type: Literal["invalid_api_key_error"]

    def __init__(self, message: str, *, body: object, request: httpx.Request, response: httpx.Response) -> None:
        data = cast(Mapping[str, object], body if is_mapping(body) else {})
        title = cast(Any, data.get("title"))
        super().__init__(title or message, request=request, response=response, body=body)

        self.title = title
        self.detail = cast(Any, data.get("detail"))
        self.status = cast(Any, data.get("status"))
        self.type = cast(Any, data.get("type"))


class EnvironmentMismatchError(exceptions.PermissionDeniedError):
    detail: Optional[str]

    status: Literal[403]

    title: str

    type: Literal["environment_mismatch_error"]

    def __init__(self, message: str, *, body: object, request: httpx.Request, response: httpx.Response) -> None:
        data = cast(Mapping[str, object], body if is_mapping(body) else {})
        title = cast(Any, data.get("title"))
        super().__init__(title or message, request=request, response=response, body=body)

        self.title = title
        self.detail = cast(Any, data.get("detail"))
        self.status = cast(Any, data.get("status"))
        self.type = cast(Any, data.get("type"))


class InsufficientPermissionsError(exceptions.PermissionDeniedError):
    detail: Optional[str]

    status: Literal[403]

    title: str

    type: Literal["insufficient_permissions_error"]

    def __init__(self, message: str, *, body: object, request: httpx.Request, response: httpx.Response) -> None:
        data = cast(Mapping[str, object], body if is_mapping(body) else {})
        title = cast(Any, data.get("title"))
        super().__init__(title or message, request=request, response=response, body=body)

        self.title = title
        self.detail = cast(Any, data.get("detail"))
        self.status = cast(Any, data.get("status"))
        self.type = cast(Any, data.get("type"))


class PrivateFeatureError(exceptions.PermissionDeniedError):
    detail: Optional[str]

    status: Literal[403]

    title: str

    type: Literal["private_feature_error"]

    def __init__(self, message: str, *, body: object, request: httpx.Request, response: httpx.Response) -> None:
        data = cast(Mapping[str, object], body if is_mapping(body) else {})
        title = cast(Any, data.get("title"))
        super().__init__(title or message, request=request, response=response, body=body)

        self.title = title
        self.detail = cast(Any, data.get("detail"))
        self.status = cast(Any, data.get("status"))
        self.type = cast(Any, data.get("type"))


class APIMethodNotFoundError(exceptions.NotFoundError):
    detail: Optional[str]

    status: Literal[404]

    title: str

    type: Literal["api_method_not_found_error"]

    def __init__(self, message: str, *, body: object, request: httpx.Request, response: httpx.Response) -> None:
        data = cast(Mapping[str, object], body if is_mapping(body) else {})
        title = cast(Any, data.get("title"))
        super().__init__(title or message, request=request, response=response, body=body)

        self.title = title
        self.detail = cast(Any, data.get("detail"))
        self.status = cast(Any, data.get("status"))
        self.type = cast(Any, data.get("type"))


class ObjectNotFoundError(exceptions.NotFoundError):
    detail: Optional[str]

    status: Literal[404]

    title: str

    type: Literal["object_not_found_error"]

    def __init__(self, message: str, *, body: object, request: httpx.Request, response: httpx.Response) -> None:
        data = cast(Mapping[str, object], body if is_mapping(body) else {})
        title = cast(Any, data.get("title"))
        super().__init__(title or message, request=request, response=response, body=body)

        self.title = title
        self.detail = cast(Any, data.get("detail"))
        self.status = cast(Any, data.get("status"))
        self.type = cast(Any, data.get("type"))


class IdempotencyConflictError(exceptions.ConflictError):
    detail: Optional[str]

    status: Literal[409]

    title: str

    type: Literal["idempotency_conflict_error"]

    def __init__(self, message: str, *, body: object, request: httpx.Request, response: httpx.Response) -> None:
        data = cast(Mapping[str, object], body if is_mapping(body) else {})
        title = cast(Any, data.get("title"))
        super().__init__(title or message, request=request, response=response, body=body)

        self.title = title
        self.detail = cast(Any, data.get("detail"))
        self.status = cast(Any, data.get("status"))
        self.type = cast(Any, data.get("type"))


class InvalidOperationError(exceptions.ConflictError):
    detail: Optional[str]

    status: Literal[409]

    title: str

    type: Literal["invalid_operation_error"]

    def __init__(self, message: str, *, body: object, request: httpx.Request, response: httpx.Response) -> None:
        data = cast(Mapping[str, object], body if is_mapping(body) else {})
        title = cast(Any, data.get("title"))
        super().__init__(title or message, request=request, response=response, body=body)

        self.title = title
        self.detail = cast(Any, data.get("detail"))
        self.status = cast(Any, data.get("status"))
        self.type = cast(Any, data.get("type"))


class UniqueIdentifierAlreadyExistsError(exceptions.ConflictError):
    detail: Optional[str]

    resource_id: str

    status: Literal[409]

    title: str

    type: Literal["unique_identifier_already_exists_error"]

    def __init__(self, message: str, *, body: object, request: httpx.Request, response: httpx.Response) -> None:
        data = cast(Mapping[str, object], body if is_mapping(body) else {})
        title = cast(Any, data.get("title"))
        super().__init__(title or message, request=request, response=response, body=body)

        self.title = title
        self.detail = cast(Any, data.get("detail"))
        self.resource_id = cast(Any, data.get("resource_id"))
        self.status = cast(Any, data.get("status"))
        self.type = cast(Any, data.get("type"))


class IdempotencyUnprocessableError(exceptions.UnprocessableEntityError):
    detail: Optional[str]

    status: Literal[422]

    title: str

    type: Literal["idempotency_unprocessable_error"]

    def __init__(self, message: str, *, body: object, request: httpx.Request, response: httpx.Response) -> None:
        data = cast(Mapping[str, object], body if is_mapping(body) else {})
        title = cast(Any, data.get("title"))
        super().__init__(title or message, request=request, response=response, body=body)

        self.title = title
        self.detail = cast(Any, data.get("detail"))
        self.status = cast(Any, data.get("status"))
        self.type = cast(Any, data.get("type"))


class RateLimitedError(exceptions.RateLimitError):
    detail: Optional[str]

    status: Literal[429]

    title: str

    type: Literal["rate_limited_error"]

    retry_after: Optional[int]

    def __init__(self, message: str, *, body: object, request: httpx.Request, response: httpx.Response) -> None:
        data = cast(Mapping[str, object], body if is_mapping(body) else {})
        title = cast(Any, data.get("title"))
        super().__init__(title or message, request=request, response=response, body=body)

        self.title = title
        self.detail = cast(Any, data.get("detail"))
        self.status = cast(Any, data.get("status"))
        self.type = cast(Any, data.get("type"))
        self.retry_after = cast(Any, data.get("retry_after"))


class InternalServerError(exceptions.InternalServerError):
    detail: Optional[str]

    status: Literal[500]

    title: str

    type: Literal["internal_server_error"]

    def __init__(self, message: str, *, body: object, request: httpx.Request, response: httpx.Response) -> None:
        data = cast(Mapping[str, object], body if is_mapping(body) else {})
        title = cast(Any, data.get("title"))
        super().__init__(title or message, request=request, response=response, body=body)

        self.title = title
        self.detail = cast(Any, data.get("detail"))
        self.status = cast(Any, data.get("status"))
        self.type = cast(Any, data.get("type"))
