# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebhooks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    payload = '{"id":"event_123abc","created_at":"2020-01-31T23:59:59Z"}'
    signature = "Dwa0AHInLL3XFo2sxcHamOQDrJNi7F654S3L6skMAOI="
    headers = {
        "Increase-Webhook-Signature": f"t=2022-01-31T23:59:59Z,v1=3f9c3dcc820ca3adfae8e196d05b09dfef63b91db5ce5ac1407090f2aa424a6f",
    }
    secret = "whsec_zlFsbBZ8Xcodlpcu6NDTdSzZRLSdhkst"

    def test_unwrap_with_secret(self, client: Increase) -> None:
        payload = self.payload
        headers = self.headers
        secret = self.secret

        expected = {"created_at": "2020-01-31T23:59:59Z", "id": "event_123abc"}
        unwrapped = client.webhooks.unwrap(payload, headers, secret=secret)

        assert unwrapped == expected

    def test_unwrap_no_secret(self, client: Increase) -> None:
        payload = self.payload
        headers = self.headers

        expected = {"created_at": "2020-01-31T23:59:59Z", "id": "event_123abc"}
        unwrapped = client.webhooks.unwrap(payload, headers)

        assert unwrapped == expected

    def test_verify_signature(self, client: Increase) -> None:
        payload = self.payload
        headers = self.headers
        secret = self.secret
        verify = client.webhooks.verify_signature

        assert verify(payload=payload, headers=headers, secret=secret) is None

        # wrong secret
        with pytest.raises(ValueError, match=r"None of the given webhook signatures match the expected signature."):
            verify(payload=payload, headers=headers, secret="invalid secret")


class TestAsyncWebhooks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    payload = '{"id":"event_123abc","created_at":"2020-01-31T23:59:59Z"}'
    signature = "Dwa0AHInLL3XFo2sxcHamOQDrJNi7F654S3L6skMAOI="
    headers = {
        "Increase-Webhook-Signature": f"t=2022-01-31T23:59:59Z,v1=3f9c3dcc820ca3adfae8e196d05b09dfef63b91db5ce5ac1407090f2aa424a6f",
    }
    secret = "whsec_zlFsbBZ8Xcodlpcu6NDTdSzZRLSdhkst"

    def test_unwrap_with_secret(self, async_client: AsyncIncrease) -> None:
        payload = self.payload
        headers = self.headers
        secret = self.secret

        expected = {"created_at": "2020-01-31T23:59:59Z", "id": "event_123abc"}
        unwrapped = async_client.webhooks.unwrap(payload, headers, secret=secret)

        assert unwrapped == expected

    def test_unwrap_no_secret(self, async_client: AsyncIncrease) -> None:
        payload = self.payload
        headers = self.headers

        expected = {"created_at": "2020-01-31T23:59:59Z", "id": "event_123abc"}
        unwrapped = async_client.webhooks.unwrap(payload, headers)

        assert unwrapped == expected

    def test_verify_signature(self, async_client: AsyncIncrease) -> None:
        payload = self.payload
        headers = self.headers
        secret = self.secret
        verify = async_client.webhooks.verify_signature

        assert verify(payload=payload, headers=headers, secret=secret) is None

        # wrong secret
        with pytest.raises(ValueError, match=r"None of the given webhook signatures match the expected signature."):
            verify(payload=payload, headers=headers, secret="invalid secret")
