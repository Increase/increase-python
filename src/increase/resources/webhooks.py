# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import hmac
import json
import hashlib
from typing import Dict

from .._types import (
    HeadersLike,
)
from .._utils import (
    get_required_header,
)
from .._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["Webhooks", "AsyncWebhooks"]


class Webhooks(SyncAPIResource):
    def unwrap(
        self,
        payload: str | bytes,
        headers: HeadersLike,
        *,
        secret: str | None = None,
    ) -> object:
        """Validates that the given payload was sent by Increase and parses the payload."""
        if secret is not None:
            self.verify_signature(payload=payload, headers=headers, secret=secret)
        return json.loads(payload)

    def verify_signature(
        self,
        payload: str | bytes,
        headers: HeadersLike,
        *,
        secret: str | None = None,
    ) -> None:
        """Validates whether or not the webhook payload was sent by Increase.

        An error will be raised if the webhook payload was not sent by Increase.
        """
        if secret is None:
            secret = self._client.webhook_secret

        if secret is None:
            raise ValueError(
                "The webhook secret must either be set using the env var, INCREASE_WEBHOOK_SECRET, on the client class, Increase(webhook_secret='123'), or passed to this function"
            )

        def parse_kv_pairs(text: str, item_sep: str = ",", value_sep: str = "=") -> Dict[str, str]:
            return dict(t.split(value_sep) for t in text.split(item_sep))

        raw_signature = get_required_header(headers, "Increase-Webhook-Signature")
        try:
            parsed_signature = parse_kv_pairs(raw_signature)
        except ValueError as err:
            raise ValueError("Unable to parse Increase-Webhook-Signature header.") from err

        timestamp, signature = parsed_signature["t"], parsed_signature["v1"]

        # create the signature
        body = payload.decode("utf-8") if isinstance(payload, bytes) else payload
        if not isinstance(body, str):  # pyright: ignore[reportUnnecessaryIsInstance]
            raise ValueError(
                "Webhook body should be a string of JSON (or bytes which can be decoded to a utf-8 string), not a parsed dictionary."
            )

        to_sign = f"{timestamp}.{body}".encode()
        expected_signature = hmac.new(secret.encode(), to_sign, hashlib.sha256).hexdigest()

        if hmac.compare_digest(expected_signature, signature):
            # valid!
            return None

        raise ValueError("None of the given webhook signatures match the expected signature.")


class AsyncWebhooks(AsyncAPIResource):
    def unwrap(
        self,
        payload: str | bytes,
        headers: HeadersLike,
        *,
        secret: str | None = None,
    ) -> object:
        """Validates that the given payload was sent by Increase and parses the payload."""
        if secret is not None:
            self.verify_signature(payload=payload, headers=headers, secret=secret)
        return json.loads(payload)

    def verify_signature(
        self,
        payload: str | bytes,
        headers: HeadersLike,
        *,
        secret: str | None = None,
    ) -> None:
        """Validates whether or not the webhook payload was sent by Increase.

        An error will be raised if the webhook payload was not sent by Increase.
        """
        if secret is None:
            secret = self._client.webhook_secret

        if secret is None:
            raise ValueError(
                "The webhook secret must either be set using the env var, INCREASE_WEBHOOK_SECRET, on the client class, Increase(webhook_secret='123'), or passed to this function"
            )

        def parse_kv_pairs(text: str, item_sep: str = ",", value_sep: str = "=") -> Dict[str, str]:
            return dict(t.split(value_sep) for t in text.split(item_sep))

        raw_signature = get_required_header(headers, "Increase-Webhook-Signature")
        try:
            parsed_signature = parse_kv_pairs(raw_signature)
        except ValueError as err:
            raise ValueError("Unable to parse Increase-Webhook-Signature header.") from err

        timestamp, signature = parsed_signature["t"], parsed_signature["v1"]

        # create the signature
        body = payload.decode("utf-8") if isinstance(payload, bytes) else payload
        if not isinstance(body, str):  # pyright: ignore[reportUnnecessaryIsInstance]
            raise ValueError(
                "Webhook body should be a string of JSON (or bytes which can be decoded to a utf-8 string), not a parsed dictionary."
            )

        to_sign = f"{timestamp}.{body}".encode()
        expected_signature = hmac.new(secret.encode(), to_sign, hashlib.sha256).hexdigest()

        if hmac.compare_digest(expected_signature, signature):
            # valid!
            return None

        raise ValueError("None of the given webhook signatures match the expected signature.")
