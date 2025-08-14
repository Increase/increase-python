# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import (
    Entity,
)
from increase._utils import parse_date, parse_datetime
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEntities:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        entity = client.entities.create(
            structure="corporation",
        )
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        entity = client.entities.create(
            structure="corporation",
            corporation={
                "address": {
                    "city": "New York",
                    "line1": "33 Liberty Street",
                    "state": "NY",
                    "zip": "10045",
                    "line2": "x",
                },
                "beneficial_owners": [
                    {
                        "individual": {
                            "address": {
                                "city": "New York",
                                "country": "x",
                                "line1": "33 Liberty Street",
                                "line2": "x",
                                "state": "NY",
                                "zip": "10045",
                            },
                            "date_of_birth": parse_date("1970-01-31"),
                            "identification": {
                                "method": "social_security_number",
                                "number": "078051120",
                                "drivers_license": {
                                    "expiration_date": parse_date("2019-12-27"),
                                    "file_id": "file_id",
                                    "state": "x",
                                    "back_file_id": "back_file_id",
                                },
                                "other": {
                                    "country": "x",
                                    "description": "x",
                                    "file_id": "file_id",
                                    "back_file_id": "back_file_id",
                                    "expiration_date": parse_date("2019-12-27"),
                                },
                                "passport": {
                                    "country": "x",
                                    "expiration_date": parse_date("2019-12-27"),
                                    "file_id": "file_id",
                                },
                            },
                            "name": "Ian Crease",
                            "confirmed_no_us_tax_id": True,
                        },
                        "prongs": ["control"],
                        "company_title": "CEO",
                    }
                ],
                "name": "National Phonograph Company",
                "tax_identifier": "602214076",
                "beneficial_ownership_exemption_reason": "regulated_financial_institution",
                "incorporation_state": "NY",
                "industry_code": "x",
                "website": "https://example.com",
            },
            description="x",
            government_authority={
                "address": {
                    "city": "x",
                    "line1": "x",
                    "state": "x",
                    "zip": "x",
                    "line2": "x",
                },
                "authorized_persons": [{"name": "x"}],
                "category": "municipality",
                "name": "x",
                "tax_identifier": "x",
                "website": "website",
            },
            joint={
                "individuals": [
                    {
                        "address": {
                            "city": "x",
                            "line1": "x",
                            "state": "x",
                            "zip": "x",
                            "line2": "x",
                        },
                        "date_of_birth": parse_date("2019-12-27"),
                        "identification": {
                            "method": "social_security_number",
                            "number": "xxxx",
                            "drivers_license": {
                                "expiration_date": parse_date("2019-12-27"),
                                "file_id": "file_id",
                                "state": "x",
                                "back_file_id": "back_file_id",
                            },
                            "other": {
                                "country": "x",
                                "description": "x",
                                "file_id": "file_id",
                                "back_file_id": "back_file_id",
                                "expiration_date": parse_date("2019-12-27"),
                            },
                            "passport": {
                                "country": "x",
                                "expiration_date": parse_date("2019-12-27"),
                                "file_id": "file_id",
                            },
                        },
                        "name": "x",
                        "confirmed_no_us_tax_id": True,
                    }
                ]
            },
            natural_person={
                "address": {
                    "city": "x",
                    "line1": "x",
                    "state": "x",
                    "zip": "x",
                    "line2": "x",
                },
                "date_of_birth": parse_date("2019-12-27"),
                "identification": {
                    "method": "social_security_number",
                    "number": "xxxx",
                    "drivers_license": {
                        "expiration_date": parse_date("2019-12-27"),
                        "file_id": "file_id",
                        "state": "x",
                        "back_file_id": "back_file_id",
                    },
                    "other": {
                        "country": "x",
                        "description": "x",
                        "file_id": "file_id",
                        "back_file_id": "back_file_id",
                        "expiration_date": parse_date("2019-12-27"),
                    },
                    "passport": {
                        "country": "x",
                        "expiration_date": parse_date("2019-12-27"),
                        "file_id": "file_id",
                    },
                },
                "name": "x",
                "confirmed_no_us_tax_id": True,
            },
            supplemental_documents=[{"file_id": "file_makxrc67oh9l6sg7w9yc"}],
            third_party_verification={
                "reference": "x",
                "vendor": "alloy",
            },
            trust={
                "address": {
                    "city": "x",
                    "line1": "x",
                    "state": "x",
                    "zip": "x",
                    "line2": "x",
                },
                "category": "revocable",
                "name": "x",
                "trustees": [
                    {
                        "structure": "individual",
                        "individual": {
                            "address": {
                                "city": "x",
                                "line1": "x",
                                "state": "x",
                                "zip": "x",
                                "line2": "x",
                            },
                            "date_of_birth": parse_date("2019-12-27"),
                            "identification": {
                                "method": "social_security_number",
                                "number": "xxxx",
                                "drivers_license": {
                                    "expiration_date": parse_date("2019-12-27"),
                                    "file_id": "file_id",
                                    "state": "x",
                                    "back_file_id": "back_file_id",
                                },
                                "other": {
                                    "country": "x",
                                    "description": "x",
                                    "file_id": "file_id",
                                    "back_file_id": "back_file_id",
                                    "expiration_date": parse_date("2019-12-27"),
                                },
                                "passport": {
                                    "country": "x",
                                    "expiration_date": parse_date("2019-12-27"),
                                    "file_id": "file_id",
                                },
                            },
                            "name": "x",
                            "confirmed_no_us_tax_id": True,
                        },
                    }
                ],
                "formation_document_file_id": "formation_document_file_id",
                "formation_state": "x",
                "grantor": {
                    "address": {
                        "city": "x",
                        "line1": "x",
                        "state": "x",
                        "zip": "x",
                        "line2": "x",
                    },
                    "date_of_birth": parse_date("2019-12-27"),
                    "identification": {
                        "method": "social_security_number",
                        "number": "xxxx",
                        "drivers_license": {
                            "expiration_date": parse_date("2019-12-27"),
                            "file_id": "file_id",
                            "state": "x",
                            "back_file_id": "back_file_id",
                        },
                        "other": {
                            "country": "x",
                            "description": "x",
                            "file_id": "file_id",
                            "back_file_id": "back_file_id",
                            "expiration_date": parse_date("2019-12-27"),
                        },
                        "passport": {
                            "country": "x",
                            "expiration_date": parse_date("2019-12-27"),
                            "file_id": "file_id",
                        },
                    },
                    "name": "x",
                    "confirmed_no_us_tax_id": True,
                },
                "tax_identifier": "x",
            },
        )
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.entities.with_raw_response.create(
            structure="corporation",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Increase) -> None:
        with client.entities.with_streaming_response.create(
            structure="corporation",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(Entity, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        entity = client.entities.retrieve(
            "entity_id",
        )
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.entities.with_raw_response.retrieve(
            "entity_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Increase) -> None:
        with client.entities.with_streaming_response.retrieve(
            "entity_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(Entity, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
            client.entities.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        entity = client.entities.list()
        assert_matches_type(SyncPage[Entity], entity, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        entity = client.entities.list(
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="cursor",
            idempotency_key="x",
            limit=1,
            status={"in": ["active"]},
        )
        assert_matches_type(SyncPage[Entity], entity, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Increase) -> None:
        response = client.entities.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(SyncPage[Entity], entity, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Increase) -> None:
        with client.entities.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(SyncPage[Entity], entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_archive(self, client: Increase) -> None:
        entity = client.entities.archive(
            "entity_id",
        )
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    def test_raw_response_archive(self, client: Increase) -> None:
        response = client.entities.with_raw_response.archive(
            "entity_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    def test_streaming_response_archive(self, client: Increase) -> None:
        with client.entities.with_streaming_response.archive(
            "entity_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(Entity, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_archive(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
            client.entities.with_raw_response.archive(
                "",
            )

    @parametrize
    def test_method_archive_beneficial_owner(self, client: Increase) -> None:
        entity = client.entities.archive_beneficial_owner(
            entity_id="entity_n8y8tnk2p9339ti393yi",
            beneficial_owner_id="entity_setup_beneficial_owner_submission_vgkyk7dj5eb4sfhdbkx7",
        )
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    def test_raw_response_archive_beneficial_owner(self, client: Increase) -> None:
        response = client.entities.with_raw_response.archive_beneficial_owner(
            entity_id="entity_n8y8tnk2p9339ti393yi",
            beneficial_owner_id="entity_setup_beneficial_owner_submission_vgkyk7dj5eb4sfhdbkx7",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    def test_streaming_response_archive_beneficial_owner(self, client: Increase) -> None:
        with client.entities.with_streaming_response.archive_beneficial_owner(
            entity_id="entity_n8y8tnk2p9339ti393yi",
            beneficial_owner_id="entity_setup_beneficial_owner_submission_vgkyk7dj5eb4sfhdbkx7",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(Entity, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_archive_beneficial_owner(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
            client.entities.with_raw_response.archive_beneficial_owner(
                entity_id="",
                beneficial_owner_id="entity_setup_beneficial_owner_submission_vgkyk7dj5eb4sfhdbkx7",
            )

    @parametrize
    def test_method_confirm(self, client: Increase) -> None:
        entity = client.entities.confirm(
            entity_id="entity_n8y8tnk2p9339ti393yi",
        )
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    def test_method_confirm_with_all_params(self, client: Increase) -> None:
        entity = client.entities.confirm(
            entity_id="entity_n8y8tnk2p9339ti393yi",
            confirmed_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    def test_raw_response_confirm(self, client: Increase) -> None:
        response = client.entities.with_raw_response.confirm(
            entity_id="entity_n8y8tnk2p9339ti393yi",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    def test_streaming_response_confirm(self, client: Increase) -> None:
        with client.entities.with_streaming_response.confirm(
            entity_id="entity_n8y8tnk2p9339ti393yi",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(Entity, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_confirm(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
            client.entities.with_raw_response.confirm(
                entity_id="",
            )

    @parametrize
    def test_method_create_beneficial_owner(self, client: Increase) -> None:
        entity = client.entities.create_beneficial_owner(
            entity_id="entity_n8y8tnk2p9339ti393yi",
            beneficial_owner={
                "individual": {
                    "address": {
                        "city": "New York",
                        "country": "US",
                        "line1": "33 Liberty Street",
                    },
                    "date_of_birth": parse_date("1970-01-31"),
                    "identification": {
                        "method": "social_security_number",
                        "number": "078051120",
                    },
                    "name": "Ian Crease",
                },
                "prongs": ["control"],
            },
        )
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    def test_method_create_beneficial_owner_with_all_params(self, client: Increase) -> None:
        entity = client.entities.create_beneficial_owner(
            entity_id="entity_n8y8tnk2p9339ti393yi",
            beneficial_owner={
                "individual": {
                    "address": {
                        "city": "New York",
                        "country": "US",
                        "line1": "33 Liberty Street",
                        "line2": "x",
                        "state": "NY",
                        "zip": "10045",
                    },
                    "date_of_birth": parse_date("1970-01-31"),
                    "identification": {
                        "method": "social_security_number",
                        "number": "078051120",
                        "drivers_license": {
                            "expiration_date": parse_date("2019-12-27"),
                            "file_id": "file_id",
                            "state": "x",
                            "back_file_id": "back_file_id",
                        },
                        "other": {
                            "country": "x",
                            "description": "x",
                            "file_id": "file_id",
                            "back_file_id": "back_file_id",
                            "expiration_date": parse_date("2019-12-27"),
                        },
                        "passport": {
                            "country": "x",
                            "expiration_date": parse_date("2019-12-27"),
                            "file_id": "file_id",
                        },
                    },
                    "name": "Ian Crease",
                    "confirmed_no_us_tax_id": True,
                },
                "prongs": ["control"],
                "company_title": "CEO",
            },
        )
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    def test_raw_response_create_beneficial_owner(self, client: Increase) -> None:
        response = client.entities.with_raw_response.create_beneficial_owner(
            entity_id="entity_n8y8tnk2p9339ti393yi",
            beneficial_owner={
                "individual": {
                    "address": {
                        "city": "New York",
                        "country": "US",
                        "line1": "33 Liberty Street",
                    },
                    "date_of_birth": parse_date("1970-01-31"),
                    "identification": {
                        "method": "social_security_number",
                        "number": "078051120",
                    },
                    "name": "Ian Crease",
                },
                "prongs": ["control"],
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    def test_streaming_response_create_beneficial_owner(self, client: Increase) -> None:
        with client.entities.with_streaming_response.create_beneficial_owner(
            entity_id="entity_n8y8tnk2p9339ti393yi",
            beneficial_owner={
                "individual": {
                    "address": {
                        "city": "New York",
                        "country": "US",
                        "line1": "33 Liberty Street",
                    },
                    "date_of_birth": parse_date("1970-01-31"),
                    "identification": {
                        "method": "social_security_number",
                        "number": "078051120",
                    },
                    "name": "Ian Crease",
                },
                "prongs": ["control"],
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(Entity, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_beneficial_owner(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
            client.entities.with_raw_response.create_beneficial_owner(
                entity_id="",
                beneficial_owner={
                    "individual": {
                        "address": {
                            "city": "New York",
                            "country": "US",
                            "line1": "33 Liberty Street",
                        },
                        "date_of_birth": parse_date("1970-01-31"),
                        "identification": {
                            "method": "social_security_number",
                            "number": "078051120",
                        },
                        "name": "Ian Crease",
                    },
                    "prongs": ["control"],
                },
            )

    @parametrize
    def test_method_update_address(self, client: Increase) -> None:
        entity = client.entities.update_address(
            entity_id="entity_n8y8tnk2p9339ti393yi",
            address={
                "city": "New York",
                "line1": "33 Liberty Street",
                "state": "NY",
                "zip": "10045",
            },
        )
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    def test_method_update_address_with_all_params(self, client: Increase) -> None:
        entity = client.entities.update_address(
            entity_id="entity_n8y8tnk2p9339ti393yi",
            address={
                "city": "New York",
                "line1": "33 Liberty Street",
                "state": "NY",
                "zip": "10045",
                "line2": "Unit 2",
            },
        )
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    def test_raw_response_update_address(self, client: Increase) -> None:
        response = client.entities.with_raw_response.update_address(
            entity_id="entity_n8y8tnk2p9339ti393yi",
            address={
                "city": "New York",
                "line1": "33 Liberty Street",
                "state": "NY",
                "zip": "10045",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    def test_streaming_response_update_address(self, client: Increase) -> None:
        with client.entities.with_streaming_response.update_address(
            entity_id="entity_n8y8tnk2p9339ti393yi",
            address={
                "city": "New York",
                "line1": "33 Liberty Street",
                "state": "NY",
                "zip": "10045",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(Entity, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_address(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
            client.entities.with_raw_response.update_address(
                entity_id="",
                address={
                    "city": "New York",
                    "line1": "33 Liberty Street",
                    "state": "NY",
                    "zip": "10045",
                },
            )

    @parametrize
    def test_method_update_beneficial_owner_address(self, client: Increase) -> None:
        entity = client.entities.update_beneficial_owner_address(
            entity_id="entity_n8y8tnk2p9339ti393yi",
            address={
                "city": "New York",
                "country": "US",
                "line1": "33 Liberty Street",
            },
            beneficial_owner_id="entity_setup_beneficial_owner_submission_vgkyk7dj5eb4sfhdbkx7",
        )
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    def test_method_update_beneficial_owner_address_with_all_params(self, client: Increase) -> None:
        entity = client.entities.update_beneficial_owner_address(
            entity_id="entity_n8y8tnk2p9339ti393yi",
            address={
                "city": "New York",
                "country": "US",
                "line1": "33 Liberty Street",
                "line2": "Unit 2",
                "state": "NY",
                "zip": "10045",
            },
            beneficial_owner_id="entity_setup_beneficial_owner_submission_vgkyk7dj5eb4sfhdbkx7",
        )
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    def test_raw_response_update_beneficial_owner_address(self, client: Increase) -> None:
        response = client.entities.with_raw_response.update_beneficial_owner_address(
            entity_id="entity_n8y8tnk2p9339ti393yi",
            address={
                "city": "New York",
                "country": "US",
                "line1": "33 Liberty Street",
            },
            beneficial_owner_id="entity_setup_beneficial_owner_submission_vgkyk7dj5eb4sfhdbkx7",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    def test_streaming_response_update_beneficial_owner_address(self, client: Increase) -> None:
        with client.entities.with_streaming_response.update_beneficial_owner_address(
            entity_id="entity_n8y8tnk2p9339ti393yi",
            address={
                "city": "New York",
                "country": "US",
                "line1": "33 Liberty Street",
            },
            beneficial_owner_id="entity_setup_beneficial_owner_submission_vgkyk7dj5eb4sfhdbkx7",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(Entity, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_beneficial_owner_address(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
            client.entities.with_raw_response.update_beneficial_owner_address(
                entity_id="",
                address={
                    "city": "New York",
                    "country": "US",
                    "line1": "33 Liberty Street",
                },
                beneficial_owner_id="entity_setup_beneficial_owner_submission_vgkyk7dj5eb4sfhdbkx7",
            )

    @parametrize
    def test_method_update_industry_code(self, client: Increase) -> None:
        entity = client.entities.update_industry_code(
            entity_id="entity_n8y8tnk2p9339ti393yi",
            industry_code="5132",
        )
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    def test_raw_response_update_industry_code(self, client: Increase) -> None:
        response = client.entities.with_raw_response.update_industry_code(
            entity_id="entity_n8y8tnk2p9339ti393yi",
            industry_code="5132",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    def test_streaming_response_update_industry_code(self, client: Increase) -> None:
        with client.entities.with_streaming_response.update_industry_code(
            entity_id="entity_n8y8tnk2p9339ti393yi",
            industry_code="5132",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(Entity, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_industry_code(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
            client.entities.with_raw_response.update_industry_code(
                entity_id="",
                industry_code="5132",
            )


class TestAsyncEntities:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncIncrease) -> None:
        entity = await async_client.entities.create(
            structure="corporation",
        )
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncIncrease) -> None:
        entity = await async_client.entities.create(
            structure="corporation",
            corporation={
                "address": {
                    "city": "New York",
                    "line1": "33 Liberty Street",
                    "state": "NY",
                    "zip": "10045",
                    "line2": "x",
                },
                "beneficial_owners": [
                    {
                        "individual": {
                            "address": {
                                "city": "New York",
                                "country": "x",
                                "line1": "33 Liberty Street",
                                "line2": "x",
                                "state": "NY",
                                "zip": "10045",
                            },
                            "date_of_birth": parse_date("1970-01-31"),
                            "identification": {
                                "method": "social_security_number",
                                "number": "078051120",
                                "drivers_license": {
                                    "expiration_date": parse_date("2019-12-27"),
                                    "file_id": "file_id",
                                    "state": "x",
                                    "back_file_id": "back_file_id",
                                },
                                "other": {
                                    "country": "x",
                                    "description": "x",
                                    "file_id": "file_id",
                                    "back_file_id": "back_file_id",
                                    "expiration_date": parse_date("2019-12-27"),
                                },
                                "passport": {
                                    "country": "x",
                                    "expiration_date": parse_date("2019-12-27"),
                                    "file_id": "file_id",
                                },
                            },
                            "name": "Ian Crease",
                            "confirmed_no_us_tax_id": True,
                        },
                        "prongs": ["control"],
                        "company_title": "CEO",
                    }
                ],
                "name": "National Phonograph Company",
                "tax_identifier": "602214076",
                "beneficial_ownership_exemption_reason": "regulated_financial_institution",
                "incorporation_state": "NY",
                "industry_code": "x",
                "website": "https://example.com",
            },
            description="x",
            government_authority={
                "address": {
                    "city": "x",
                    "line1": "x",
                    "state": "x",
                    "zip": "x",
                    "line2": "x",
                },
                "authorized_persons": [{"name": "x"}],
                "category": "municipality",
                "name": "x",
                "tax_identifier": "x",
                "website": "website",
            },
            joint={
                "individuals": [
                    {
                        "address": {
                            "city": "x",
                            "line1": "x",
                            "state": "x",
                            "zip": "x",
                            "line2": "x",
                        },
                        "date_of_birth": parse_date("2019-12-27"),
                        "identification": {
                            "method": "social_security_number",
                            "number": "xxxx",
                            "drivers_license": {
                                "expiration_date": parse_date("2019-12-27"),
                                "file_id": "file_id",
                                "state": "x",
                                "back_file_id": "back_file_id",
                            },
                            "other": {
                                "country": "x",
                                "description": "x",
                                "file_id": "file_id",
                                "back_file_id": "back_file_id",
                                "expiration_date": parse_date("2019-12-27"),
                            },
                            "passport": {
                                "country": "x",
                                "expiration_date": parse_date("2019-12-27"),
                                "file_id": "file_id",
                            },
                        },
                        "name": "x",
                        "confirmed_no_us_tax_id": True,
                    }
                ]
            },
            natural_person={
                "address": {
                    "city": "x",
                    "line1": "x",
                    "state": "x",
                    "zip": "x",
                    "line2": "x",
                },
                "date_of_birth": parse_date("2019-12-27"),
                "identification": {
                    "method": "social_security_number",
                    "number": "xxxx",
                    "drivers_license": {
                        "expiration_date": parse_date("2019-12-27"),
                        "file_id": "file_id",
                        "state": "x",
                        "back_file_id": "back_file_id",
                    },
                    "other": {
                        "country": "x",
                        "description": "x",
                        "file_id": "file_id",
                        "back_file_id": "back_file_id",
                        "expiration_date": parse_date("2019-12-27"),
                    },
                    "passport": {
                        "country": "x",
                        "expiration_date": parse_date("2019-12-27"),
                        "file_id": "file_id",
                    },
                },
                "name": "x",
                "confirmed_no_us_tax_id": True,
            },
            supplemental_documents=[{"file_id": "file_makxrc67oh9l6sg7w9yc"}],
            third_party_verification={
                "reference": "x",
                "vendor": "alloy",
            },
            trust={
                "address": {
                    "city": "x",
                    "line1": "x",
                    "state": "x",
                    "zip": "x",
                    "line2": "x",
                },
                "category": "revocable",
                "name": "x",
                "trustees": [
                    {
                        "structure": "individual",
                        "individual": {
                            "address": {
                                "city": "x",
                                "line1": "x",
                                "state": "x",
                                "zip": "x",
                                "line2": "x",
                            },
                            "date_of_birth": parse_date("2019-12-27"),
                            "identification": {
                                "method": "social_security_number",
                                "number": "xxxx",
                                "drivers_license": {
                                    "expiration_date": parse_date("2019-12-27"),
                                    "file_id": "file_id",
                                    "state": "x",
                                    "back_file_id": "back_file_id",
                                },
                                "other": {
                                    "country": "x",
                                    "description": "x",
                                    "file_id": "file_id",
                                    "back_file_id": "back_file_id",
                                    "expiration_date": parse_date("2019-12-27"),
                                },
                                "passport": {
                                    "country": "x",
                                    "expiration_date": parse_date("2019-12-27"),
                                    "file_id": "file_id",
                                },
                            },
                            "name": "x",
                            "confirmed_no_us_tax_id": True,
                        },
                    }
                ],
                "formation_document_file_id": "formation_document_file_id",
                "formation_state": "x",
                "grantor": {
                    "address": {
                        "city": "x",
                        "line1": "x",
                        "state": "x",
                        "zip": "x",
                        "line2": "x",
                    },
                    "date_of_birth": parse_date("2019-12-27"),
                    "identification": {
                        "method": "social_security_number",
                        "number": "xxxx",
                        "drivers_license": {
                            "expiration_date": parse_date("2019-12-27"),
                            "file_id": "file_id",
                            "state": "x",
                            "back_file_id": "back_file_id",
                        },
                        "other": {
                            "country": "x",
                            "description": "x",
                            "file_id": "file_id",
                            "back_file_id": "back_file_id",
                            "expiration_date": parse_date("2019-12-27"),
                        },
                        "passport": {
                            "country": "x",
                            "expiration_date": parse_date("2019-12-27"),
                            "file_id": "file_id",
                        },
                    },
                    "name": "x",
                    "confirmed_no_us_tax_id": True,
                },
                "tax_identifier": "x",
            },
        )
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIncrease) -> None:
        response = await async_client.entities.with_raw_response.create(
            structure="corporation",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIncrease) -> None:
        async with async_client.entities.with_streaming_response.create(
            structure="corporation",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(Entity, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncIncrease) -> None:
        entity = await async_client.entities.retrieve(
            "entity_id",
        )
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncIncrease) -> None:
        response = await async_client.entities.with_raw_response.retrieve(
            "entity_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncIncrease) -> None:
        async with async_client.entities.with_streaming_response.retrieve(
            "entity_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(Entity, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
            await async_client.entities.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncIncrease) -> None:
        entity = await async_client.entities.list()
        assert_matches_type(AsyncPage[Entity], entity, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncIncrease) -> None:
        entity = await async_client.entities.list(
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="cursor",
            idempotency_key="x",
            limit=1,
            status={"in": ["active"]},
        )
        assert_matches_type(AsyncPage[Entity], entity, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncIncrease) -> None:
        response = await async_client.entities.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(AsyncPage[Entity], entity, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncIncrease) -> None:
        async with async_client.entities.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(AsyncPage[Entity], entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_archive(self, async_client: AsyncIncrease) -> None:
        entity = await async_client.entities.archive(
            "entity_id",
        )
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    async def test_raw_response_archive(self, async_client: AsyncIncrease) -> None:
        response = await async_client.entities.with_raw_response.archive(
            "entity_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    async def test_streaming_response_archive(self, async_client: AsyncIncrease) -> None:
        async with async_client.entities.with_streaming_response.archive(
            "entity_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(Entity, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_archive(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
            await async_client.entities.with_raw_response.archive(
                "",
            )

    @parametrize
    async def test_method_archive_beneficial_owner(self, async_client: AsyncIncrease) -> None:
        entity = await async_client.entities.archive_beneficial_owner(
            entity_id="entity_n8y8tnk2p9339ti393yi",
            beneficial_owner_id="entity_setup_beneficial_owner_submission_vgkyk7dj5eb4sfhdbkx7",
        )
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    async def test_raw_response_archive_beneficial_owner(self, async_client: AsyncIncrease) -> None:
        response = await async_client.entities.with_raw_response.archive_beneficial_owner(
            entity_id="entity_n8y8tnk2p9339ti393yi",
            beneficial_owner_id="entity_setup_beneficial_owner_submission_vgkyk7dj5eb4sfhdbkx7",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    async def test_streaming_response_archive_beneficial_owner(self, async_client: AsyncIncrease) -> None:
        async with async_client.entities.with_streaming_response.archive_beneficial_owner(
            entity_id="entity_n8y8tnk2p9339ti393yi",
            beneficial_owner_id="entity_setup_beneficial_owner_submission_vgkyk7dj5eb4sfhdbkx7",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(Entity, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_archive_beneficial_owner(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
            await async_client.entities.with_raw_response.archive_beneficial_owner(
                entity_id="",
                beneficial_owner_id="entity_setup_beneficial_owner_submission_vgkyk7dj5eb4sfhdbkx7",
            )

    @parametrize
    async def test_method_confirm(self, async_client: AsyncIncrease) -> None:
        entity = await async_client.entities.confirm(
            entity_id="entity_n8y8tnk2p9339ti393yi",
        )
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    async def test_method_confirm_with_all_params(self, async_client: AsyncIncrease) -> None:
        entity = await async_client.entities.confirm(
            entity_id="entity_n8y8tnk2p9339ti393yi",
            confirmed_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    async def test_raw_response_confirm(self, async_client: AsyncIncrease) -> None:
        response = await async_client.entities.with_raw_response.confirm(
            entity_id="entity_n8y8tnk2p9339ti393yi",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    async def test_streaming_response_confirm(self, async_client: AsyncIncrease) -> None:
        async with async_client.entities.with_streaming_response.confirm(
            entity_id="entity_n8y8tnk2p9339ti393yi",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(Entity, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_confirm(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
            await async_client.entities.with_raw_response.confirm(
                entity_id="",
            )

    @parametrize
    async def test_method_create_beneficial_owner(self, async_client: AsyncIncrease) -> None:
        entity = await async_client.entities.create_beneficial_owner(
            entity_id="entity_n8y8tnk2p9339ti393yi",
            beneficial_owner={
                "individual": {
                    "address": {
                        "city": "New York",
                        "country": "US",
                        "line1": "33 Liberty Street",
                    },
                    "date_of_birth": parse_date("1970-01-31"),
                    "identification": {
                        "method": "social_security_number",
                        "number": "078051120",
                    },
                    "name": "Ian Crease",
                },
                "prongs": ["control"],
            },
        )
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    async def test_method_create_beneficial_owner_with_all_params(self, async_client: AsyncIncrease) -> None:
        entity = await async_client.entities.create_beneficial_owner(
            entity_id="entity_n8y8tnk2p9339ti393yi",
            beneficial_owner={
                "individual": {
                    "address": {
                        "city": "New York",
                        "country": "US",
                        "line1": "33 Liberty Street",
                        "line2": "x",
                        "state": "NY",
                        "zip": "10045",
                    },
                    "date_of_birth": parse_date("1970-01-31"),
                    "identification": {
                        "method": "social_security_number",
                        "number": "078051120",
                        "drivers_license": {
                            "expiration_date": parse_date("2019-12-27"),
                            "file_id": "file_id",
                            "state": "x",
                            "back_file_id": "back_file_id",
                        },
                        "other": {
                            "country": "x",
                            "description": "x",
                            "file_id": "file_id",
                            "back_file_id": "back_file_id",
                            "expiration_date": parse_date("2019-12-27"),
                        },
                        "passport": {
                            "country": "x",
                            "expiration_date": parse_date("2019-12-27"),
                            "file_id": "file_id",
                        },
                    },
                    "name": "Ian Crease",
                    "confirmed_no_us_tax_id": True,
                },
                "prongs": ["control"],
                "company_title": "CEO",
            },
        )
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    async def test_raw_response_create_beneficial_owner(self, async_client: AsyncIncrease) -> None:
        response = await async_client.entities.with_raw_response.create_beneficial_owner(
            entity_id="entity_n8y8tnk2p9339ti393yi",
            beneficial_owner={
                "individual": {
                    "address": {
                        "city": "New York",
                        "country": "US",
                        "line1": "33 Liberty Street",
                    },
                    "date_of_birth": parse_date("1970-01-31"),
                    "identification": {
                        "method": "social_security_number",
                        "number": "078051120",
                    },
                    "name": "Ian Crease",
                },
                "prongs": ["control"],
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    async def test_streaming_response_create_beneficial_owner(self, async_client: AsyncIncrease) -> None:
        async with async_client.entities.with_streaming_response.create_beneficial_owner(
            entity_id="entity_n8y8tnk2p9339ti393yi",
            beneficial_owner={
                "individual": {
                    "address": {
                        "city": "New York",
                        "country": "US",
                        "line1": "33 Liberty Street",
                    },
                    "date_of_birth": parse_date("1970-01-31"),
                    "identification": {
                        "method": "social_security_number",
                        "number": "078051120",
                    },
                    "name": "Ian Crease",
                },
                "prongs": ["control"],
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(Entity, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_beneficial_owner(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
            await async_client.entities.with_raw_response.create_beneficial_owner(
                entity_id="",
                beneficial_owner={
                    "individual": {
                        "address": {
                            "city": "New York",
                            "country": "US",
                            "line1": "33 Liberty Street",
                        },
                        "date_of_birth": parse_date("1970-01-31"),
                        "identification": {
                            "method": "social_security_number",
                            "number": "078051120",
                        },
                        "name": "Ian Crease",
                    },
                    "prongs": ["control"],
                },
            )

    @parametrize
    async def test_method_update_address(self, async_client: AsyncIncrease) -> None:
        entity = await async_client.entities.update_address(
            entity_id="entity_n8y8tnk2p9339ti393yi",
            address={
                "city": "New York",
                "line1": "33 Liberty Street",
                "state": "NY",
                "zip": "10045",
            },
        )
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    async def test_method_update_address_with_all_params(self, async_client: AsyncIncrease) -> None:
        entity = await async_client.entities.update_address(
            entity_id="entity_n8y8tnk2p9339ti393yi",
            address={
                "city": "New York",
                "line1": "33 Liberty Street",
                "state": "NY",
                "zip": "10045",
                "line2": "Unit 2",
            },
        )
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    async def test_raw_response_update_address(self, async_client: AsyncIncrease) -> None:
        response = await async_client.entities.with_raw_response.update_address(
            entity_id="entity_n8y8tnk2p9339ti393yi",
            address={
                "city": "New York",
                "line1": "33 Liberty Street",
                "state": "NY",
                "zip": "10045",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    async def test_streaming_response_update_address(self, async_client: AsyncIncrease) -> None:
        async with async_client.entities.with_streaming_response.update_address(
            entity_id="entity_n8y8tnk2p9339ti393yi",
            address={
                "city": "New York",
                "line1": "33 Liberty Street",
                "state": "NY",
                "zip": "10045",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(Entity, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_address(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
            await async_client.entities.with_raw_response.update_address(
                entity_id="",
                address={
                    "city": "New York",
                    "line1": "33 Liberty Street",
                    "state": "NY",
                    "zip": "10045",
                },
            )

    @parametrize
    async def test_method_update_beneficial_owner_address(self, async_client: AsyncIncrease) -> None:
        entity = await async_client.entities.update_beneficial_owner_address(
            entity_id="entity_n8y8tnk2p9339ti393yi",
            address={
                "city": "New York",
                "country": "US",
                "line1": "33 Liberty Street",
            },
            beneficial_owner_id="entity_setup_beneficial_owner_submission_vgkyk7dj5eb4sfhdbkx7",
        )
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    async def test_method_update_beneficial_owner_address_with_all_params(self, async_client: AsyncIncrease) -> None:
        entity = await async_client.entities.update_beneficial_owner_address(
            entity_id="entity_n8y8tnk2p9339ti393yi",
            address={
                "city": "New York",
                "country": "US",
                "line1": "33 Liberty Street",
                "line2": "Unit 2",
                "state": "NY",
                "zip": "10045",
            },
            beneficial_owner_id="entity_setup_beneficial_owner_submission_vgkyk7dj5eb4sfhdbkx7",
        )
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    async def test_raw_response_update_beneficial_owner_address(self, async_client: AsyncIncrease) -> None:
        response = await async_client.entities.with_raw_response.update_beneficial_owner_address(
            entity_id="entity_n8y8tnk2p9339ti393yi",
            address={
                "city": "New York",
                "country": "US",
                "line1": "33 Liberty Street",
            },
            beneficial_owner_id="entity_setup_beneficial_owner_submission_vgkyk7dj5eb4sfhdbkx7",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    async def test_streaming_response_update_beneficial_owner_address(self, async_client: AsyncIncrease) -> None:
        async with async_client.entities.with_streaming_response.update_beneficial_owner_address(
            entity_id="entity_n8y8tnk2p9339ti393yi",
            address={
                "city": "New York",
                "country": "US",
                "line1": "33 Liberty Street",
            },
            beneficial_owner_id="entity_setup_beneficial_owner_submission_vgkyk7dj5eb4sfhdbkx7",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(Entity, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_beneficial_owner_address(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
            await async_client.entities.with_raw_response.update_beneficial_owner_address(
                entity_id="",
                address={
                    "city": "New York",
                    "country": "US",
                    "line1": "33 Liberty Street",
                },
                beneficial_owner_id="entity_setup_beneficial_owner_submission_vgkyk7dj5eb4sfhdbkx7",
            )

    @parametrize
    async def test_method_update_industry_code(self, async_client: AsyncIncrease) -> None:
        entity = await async_client.entities.update_industry_code(
            entity_id="entity_n8y8tnk2p9339ti393yi",
            industry_code="5132",
        )
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    async def test_raw_response_update_industry_code(self, async_client: AsyncIncrease) -> None:
        response = await async_client.entities.with_raw_response.update_industry_code(
            entity_id="entity_n8y8tnk2p9339ti393yi",
            industry_code="5132",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    async def test_streaming_response_update_industry_code(self, async_client: AsyncIncrease) -> None:
        async with async_client.entities.with_streaming_response.update_industry_code(
            entity_id="entity_n8y8tnk2p9339ti393yi",
            industry_code="5132",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(Entity, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_industry_code(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
            await async_client.entities.with_raw_response.update_industry_code(
                entity_id="",
                industry_code="5132",
            )
