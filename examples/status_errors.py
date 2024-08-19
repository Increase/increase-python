#!/usr/bin/env -S poetry run python

from increase import Increase, InvalidAPIKeyError

client = Increase(api_key="invalid api key")

try:
    client.accounts.retrieve("<account id>")
except InvalidAPIKeyError as exc:
    print(f"Raised {type(exc)}: {exc}")
    print(f"type={exc.type} title={exc.title}")
    print(repr(exc))
