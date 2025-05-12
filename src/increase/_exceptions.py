# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, List, Mapping, Optional, cast
from typing_extensions import Literal

import httpx

from ._utils import is_mapping
from ._models import construct_type

__all__ = [
    "BadRequestError",
    "AuthenticationError",
    "PermissionDeniedError",
    "NotFoundError",
    "ConflictError",
    "UnprocessableEntityError",
    "RateLimitError",
    "InvalidParametersError",
    "MalformedRequestError",
    "InvalidAPIKeyError",
    "EnvironmentMismatchError",
    "InsufficientPermissionsError",
    "PrivateFeatureError",
    "APIMethodNotFoundError",
    "ObjectNotFoundError",
    "IdempotencyKeyAlreadyUsedError",
    "InvalidOperationError",
    "RateLimitedError",
    "InternalServerError",
]


class IncreaseError(Exception):
    pass


class APIError(IncreaseError):
    message: str
    request: httpx.Request

    body: object | None
    """The API response body.

    If the API responded with a valid JSON structure then this property will be the
    decoded result.

    If it isn't a valid JSON structure then this will be the raw response.

    If there was no response associated with this error then it will be `None`.
    """

    def __init__(self, message: str, request: httpx.Request, *, body: object | None) -> None:  # noqa: ARG002
        super().__init__(message)
        self.request = request
        self.message = message
        self.body = body


class APIResponseValidationError(APIError):
    response: httpx.Response
    status_code: int

    def __init__(self, response: httpx.Response, body: object | None, *, message: str | None = None) -> None:
        super().__init__(message or "Data returned by API invalid for expected schema.", response.request, body=body)
        self.response = response
        self.status_code = response.status_code


class APIStatusError(APIError):
    """Raised when an API response has a status code of 4xx or 5xx."""

    response: httpx.Response
    status_code: int

    def __init__(self, message: str, *, response: httpx.Response, body: object | None) -> None:
        super().__init__(message, response.request, body=body)
        self.response = response
        self.status_code = response.status_code


class APIConnectionError(APIError):
    def __init__(self, *, message: str = "Connection error.", request: httpx.Request) -> None:
        super().__init__(message, request, body=None)


class APITimeoutError(APIConnectionError):
    def __init__(self, request: httpx.Request) -> None:
        super().__init__(message="Request timed out.", request=request)


class BadRequestError(APIStatusError):
    status_code: Literal[400] = 400  # pyright: ignore[reportIncompatibleVariableOverride]


class AuthenticationError(APIStatusError):
    status_code: Literal[401] = 401  # pyright: ignore[reportIncompatibleVariableOverride]


class PermissionDeniedError(APIStatusError):
    status_code: Literal[403] = 403  # pyright: ignore[reportIncompatibleVariableOverride]


class NotFoundError(APIStatusError):
    status_code: Literal[404] = 404  # pyright: ignore[reportIncompatibleVariableOverride]


class ConflictError(APIStatusError):
    status_code: Literal[409] = 409  # pyright: ignore[reportIncompatibleVariableOverride]


class UnprocessableEntityError(APIStatusError):
    status_code: Literal[422] = 422  # pyright: ignore[reportIncompatibleVariableOverride]


class RateLimitError(APIStatusError):
    status_code: Literal[429] = 429  # pyright: ignore[reportIncompatibleVariableOverride]


class InvalidParametersError(BadRequestError):
    detail: Optional[str] = None

    errors: List[object]
    """All errors related to parsing the request parameters."""

    status: Literal[400]

    title: str

    type: Literal["invalid_parameters_error"]

    def __init__(self, message: str, *, body: object, response: httpx.Response) -> None:
        data = cast(Mapping[str, object], body if is_mapping(body) else {})
        title = cast(Any, construct_type(type_=str, value=data.get("title")))
        super().__init__(title or message, response=response, body=body)

        self.title = title
        self.detail = cast(Any, construct_type(type_=Optional[str], value=data.get("detail")))
        self.errors = cast(Any, construct_type(type_=List[object], value=data.get("errors")))
        self.status = cast(Any, construct_type(type_=Literal[400], value=data.get("status")))
        self.type = cast(Any, construct_type(type_=Literal["invalid_parameters_error"], value=data.get("type")))


class MalformedRequestError(BadRequestError):
    detail: Optional[str] = None

    status: Literal[400]

    title: str

    type: Literal["malformed_request_error"]

    def __init__(self, message: str, *, body: object, response: httpx.Response) -> None:
        data = cast(Mapping[str, object], body if is_mapping(body) else {})
        title = cast(Any, construct_type(type_=str, value=data.get("title")))
        super().__init__(title or message, response=response, body=body)

        self.title = title
        self.detail = cast(Any, construct_type(type_=Optional[str], value=data.get("detail")))
        self.status = cast(Any, construct_type(type_=Literal[400], value=data.get("status")))
        self.type = cast(Any, construct_type(type_=Literal["malformed_request_error"], value=data.get("type")))


class InvalidAPIKeyError(AuthenticationError):
    detail: Optional[str] = None

    reason: Literal[
        "deleted_credential", "expired_credential", "no_credential", "no_header", "no_api_access", "wrong_environment"
    ]
    """
    - `deleted_credential` - deleted_credential
    - `expired_credential` - expired_credential
    - `no_credential` - no_credential
    - `no_header` - no_header
    - `no_api_access` - no_api_access
    - `wrong_environment` - wrong_environment
    """

    status: Literal[401]

    title: str

    type: Literal["invalid_api_key_error"]

    def __init__(self, message: str, *, body: object, response: httpx.Response) -> None:
        data = cast(Mapping[str, object], body if is_mapping(body) else {})
        title = cast(Any, construct_type(type_=str, value=data.get("title")))
        super().__init__(title or message, response=response, body=body)

        self.title = title
        self.detail = cast(Any, construct_type(type_=Optional[str], value=data.get("detail")))
        self.reason = cast(
            Any,
            construct_type(
                type_=Literal[
                    "deleted_credential",
                    "expired_credential",
                    "no_credential",
                    "no_header",
                    "no_api_access",
                    "wrong_environment",
                ],
                value=data.get("reason"),
            ),
        )
        self.status = cast(Any, construct_type(type_=Literal[401], value=data.get("status")))
        self.type = cast(Any, construct_type(type_=Literal["invalid_api_key_error"], value=data.get("type")))


class EnvironmentMismatchError(PermissionDeniedError):
    detail: Optional[str] = None

    status: Literal[403]

    title: str

    type: Literal["environment_mismatch_error"]

    def __init__(self, message: str, *, body: object, response: httpx.Response) -> None:
        data = cast(Mapping[str, object], body if is_mapping(body) else {})
        title = cast(Any, construct_type(type_=str, value=data.get("title")))
        super().__init__(title or message, response=response, body=body)

        self.title = title
        self.detail = cast(Any, construct_type(type_=Optional[str], value=data.get("detail")))
        self.status = cast(Any, construct_type(type_=Literal[403], value=data.get("status")))
        self.type = cast(Any, construct_type(type_=Literal["environment_mismatch_error"], value=data.get("type")))


class InsufficientPermissionsError(PermissionDeniedError):
    detail: Optional[str] = None

    status: Literal[403]

    title: str

    type: Literal["insufficient_permissions_error"]

    def __init__(self, message: str, *, body: object, response: httpx.Response) -> None:
        data = cast(Mapping[str, object], body if is_mapping(body) else {})
        title = cast(Any, construct_type(type_=str, value=data.get("title")))
        super().__init__(title or message, response=response, body=body)

        self.title = title
        self.detail = cast(Any, construct_type(type_=Optional[str], value=data.get("detail")))
        self.status = cast(Any, construct_type(type_=Literal[403], value=data.get("status")))
        self.type = cast(Any, construct_type(type_=Literal["insufficient_permissions_error"], value=data.get("type")))


class PrivateFeatureError(PermissionDeniedError):
    detail: Optional[str] = None

    status: Literal[403]

    title: str

    type: Literal["private_feature_error"]

    def __init__(self, message: str, *, body: object, response: httpx.Response) -> None:
        data = cast(Mapping[str, object], body if is_mapping(body) else {})
        title = cast(Any, construct_type(type_=str, value=data.get("title")))
        super().__init__(title or message, response=response, body=body)

        self.title = title
        self.detail = cast(Any, construct_type(type_=Optional[str], value=data.get("detail")))
        self.status = cast(Any, construct_type(type_=Literal[403], value=data.get("status")))
        self.type = cast(Any, construct_type(type_=Literal["private_feature_error"], value=data.get("type")))


class APIMethodNotFoundError(NotFoundError):
    detail: Optional[str] = None

    status: Literal[404]

    title: str

    type: Literal["api_method_not_found_error"]

    def __init__(self, message: str, *, body: object, response: httpx.Response) -> None:
        data = cast(Mapping[str, object], body if is_mapping(body) else {})
        title = cast(Any, construct_type(type_=str, value=data.get("title")))
        super().__init__(title or message, response=response, body=body)

        self.title = title
        self.detail = cast(Any, construct_type(type_=Optional[str], value=data.get("detail")))
        self.status = cast(Any, construct_type(type_=Literal[404], value=data.get("status")))
        self.type = cast(Any, construct_type(type_=Literal["api_method_not_found_error"], value=data.get("type")))


class ObjectNotFoundError(NotFoundError):
    detail: Optional[str] = None

    status: Literal[404]

    title: str

    type: Literal["object_not_found_error"]

    def __init__(self, message: str, *, body: object, response: httpx.Response) -> None:
        data = cast(Mapping[str, object], body if is_mapping(body) else {})
        title = cast(Any, construct_type(type_=str, value=data.get("title")))
        super().__init__(title or message, response=response, body=body)

        self.title = title
        self.detail = cast(Any, construct_type(type_=Optional[str], value=data.get("detail")))
        self.status = cast(Any, construct_type(type_=Literal[404], value=data.get("status")))
        self.type = cast(Any, construct_type(type_=Literal["object_not_found_error"], value=data.get("type")))


class IdempotencyKeyAlreadyUsedError(ConflictError):
    detail: Optional[str] = None

    resource_id: str

    status: Literal[409]

    title: str

    type: Literal["idempotency_key_already_used_error"]

    def __init__(self, message: str, *, body: object, response: httpx.Response) -> None:
        data = cast(Mapping[str, object], body if is_mapping(body) else {})
        title = cast(Any, construct_type(type_=str, value=data.get("title")))
        super().__init__(title or message, response=response, body=body)

        self.title = title
        self.detail = cast(Any, construct_type(type_=Optional[str], value=data.get("detail")))
        self.resource_id = cast(Any, construct_type(type_=str, value=data.get("resource_id")))
        self.status = cast(Any, construct_type(type_=Literal[409], value=data.get("status")))
        self.type = cast(
            Any, construct_type(type_=Literal["idempotency_key_already_used_error"], value=data.get("type"))
        )


class InvalidOperationError(ConflictError):
    detail: Optional[str] = None

    status: Literal[409]

    title: str

    type: Literal["invalid_operation_error"]

    def __init__(self, message: str, *, body: object, response: httpx.Response) -> None:
        data = cast(Mapping[str, object], body if is_mapping(body) else {})
        title = cast(Any, construct_type(type_=str, value=data.get("title")))
        super().__init__(title or message, response=response, body=body)

        self.title = title
        self.detail = cast(Any, construct_type(type_=Optional[str], value=data.get("detail")))
        self.status = cast(Any, construct_type(type_=Literal[409], value=data.get("status")))
        self.type = cast(Any, construct_type(type_=Literal["invalid_operation_error"], value=data.get("type")))


class RateLimitedError(RateLimitError):
    detail: Optional[str] = None

    status: Literal[429]

    title: str

    type: Literal["rate_limited_error"]

    retry_after: Optional[int] = None

    def __init__(self, message: str, *, body: object, response: httpx.Response) -> None:
        data = cast(Mapping[str, object], body if is_mapping(body) else {})
        title = cast(Any, construct_type(type_=str, value=data.get("title")))
        super().__init__(title or message, response=response, body=body)

        self.title = title
        self.detail = cast(Any, construct_type(type_=Optional[str], value=data.get("detail")))
        self.status = cast(Any, construct_type(type_=Literal[429], value=data.get("status")))
        self.type = cast(Any, construct_type(type_=Literal["rate_limited_error"], value=data.get("type")))
        self.retry_after = cast(Any, construct_type(type_=Optional[int], value=data.get("retry_after")))


class InternalServerError(APIStatusError):
    detail: Optional[str] = None

    status: Literal[500]

    title: str

    type: Literal["internal_server_error"]

    def __init__(self, message: str, *, body: object, response: httpx.Response) -> None:
        data = cast(Mapping[str, object], body if is_mapping(body) else {})
        title = cast(Any, construct_type(type_=str, value=data.get("title")))
        super().__init__(title or message, response=response, body=body)

        self.title = title
        self.detail = cast(Any, construct_type(type_=Optional[str], value=data.get("detail")))
        self.status = cast(Any, construct_type(type_=Literal[500], value=data.get("status")))
        self.type = cast(Any, construct_type(type_=Literal["internal_server_error"], value=data.get("type")))
