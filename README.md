# Increase Python API Library

[![PyPI version](https://img.shields.io/pypi/v/increase.svg)](https://pypi.org/project/increase/)

The Increase Python library provides convenient access to the Increase REST API from any Python 3.7+
application. It includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by [httpx](https://github.com/encode/httpx).

## Documentation

The API documentation can be found [here](https://increase.com/documentation).

## Installation

```sh
pip install increase
```

## Usage

```python
from increase import Increase

increase = Increase(
    # defaults to os.environ.get("INCREASE_API_KEY")
    api_key="my api key",
    # defaults to "production".
    environment="sandbox",
)

account = increase.accounts.create(
    name="My First Increase Account",
)
print(account.id)
```

While you can provide an `api_key` keyword argument, we recommend using [python-dotenv](https://pypi.org/project/python-dotenv/)
and adding `INCREASE_API_KEY="my api key"` to your `.env` file so that your API Key is not stored in source control.

## Async Usage

Simply import `AsyncIncrease` instead of `Increase` and use `await` with each API call:

```python
from increase import AsyncIncrease

increase = AsyncIncrease(
    # defaults to os.environ.get("INCREASE_API_KEY")
    api_key="my api key",
    # defaults to "production".
    environment="sandbox",
)


async def main():
    account = await increase.accounts.create(
        name="My First Increase Account",
    )
    print(account.id)


asyncio.run(main())
```

Functionality between the synchronous and asynchronous clients is otherwise identical.

## Using Types

Nested request parameters are [TypedDicts](https://docs.python.org/3/library/typing.html#typing.TypedDict), while responses are [Pydantic](https://pydantic-docs.helpmanual.io/) models. This helps provide autocomplete and documentation within your editor.

If you would like to see type errors in VS Code to help catch bugs earlier, set `python.analysis.typeCheckingMode` to `"basic"`.

## Pagination

List methods in the Increase API are paginated.

This library provides auto-paginating iterators with each list response, so you do not have to request successive pages manually:

```python
import increase

increase = Increase()

all_accounts = []
# Automatically fetches more pages as needed.
for account in increase.accounts.list():
    # Do something with account here
    all_accounts.append(account)
print(all_accounts)
```

Or, asynchronously:

```python
import asyncio
import increase

increase = AsyncIncrease()


async def main() -> None:
    all_accounts = []
    # Iterate through items across all pages, issuing requests as needed.
    async for account in increase.accounts.list():
        all_accounts.append(account)
    print(all_accounts)


asyncio.run(main())
```

Alternatively, you can use the `.has_next_page()`, `.next_page_info()`, or `.get_next_page()` methods for more granular control working with pages:

```python
first_page = await increase.accounts.list()
if first_page.has_next_page():
    print(f"will fetch next page using these details: {first_page.next_page_info()}")
    next_page = await first_page.get_next_page()
    print(f"number of items we just fetched: {len(next_page.data)}")

# Remove `await` for non-async usage.
```

Or just work directly with the returned data:

```python
first_page = await increase.accounts.list()

print(f"next page cursor: {first_page.next_cursor}")  # => "next page cursor: ..."
for account in first_page.data:
    print(account.id)

# Remove `await` for non-async usage.
```

## Nested params

Nested parameters are dictionaries, typed using `TypedDict`, for example:

```python
from increase import Increase

increase = Increase()

increase.accounts.create(
    foo={
        "bar": True,
    },
)
```

## File Uploads

Request parameters that correspond to file uploads can be passed as `bytes` or a tuple of `(filename, contents, media type)`.

```python
from pathlib import Path
from increase import Increase

increase = Increase()

contents = Path("my/file.txt").read_bytes()
increase.files.create(
    file=contents,
    purpose="other",
)
```

The async client uses the exact same interface. This example uses `aiofiles` to asynchronously read the file contents but you can use whatever method you would like.

```python
import aiofiles
from increase import Increase

increase = Increase()

async with aiofiles.open("my/file.txt", mode="rb") as f:
    contents = await f.read()

await increase.files.create(
    file=contents,
    purpose="other",
)
```

## Handling errors

When the library is unable to connect to the API (e.g., due to network connection problems or a timeout), a subclass of `increase.APIConnectionError` is raised.

When the API returns a non-success status code (i.e., 4xx or 5xx
response), a subclass of `increase.APIStatusError` will be raised, containing `status_code` and `response` properties.

All errors inherit from `increase.APIError`.

```python
import increase
from increase import Increase

client = Increase()

try:
    client.accounts.create(
        naem="Oops",
    )
except increase.APIConnectionError as e:
    print("The server could not be reached")
    print(e.__cause__)  # an underlying Exception, likely raised within httpx.
except increase.RateLimitError as e:
    print("A 429 status code was received; we should back off a bit.")
except increase.APIStatusError as e:
    print("Another non-200-range status code was received")
    print(e.status_code)
    print(e.response)
```

Error codes are as followed:

| Status Code | Error Type                 |
| ----------- | -------------------------- |
| 400         | `BadRequestError`          |
| 401         | `AuthenticationError`      |
| 403         | `PermissionDeniedError`    |
| 404         | `NotFoundError`            |
| 422         | `UnprocessableEntityError` |
| 429         | `RateLimitError`           |
| >=500       | `InternalServerError`      |
| N/A         | `APIConnectionError`       |

### Retries

Certain errors will be automatically retried 2 times by default, with a short exponential backoff.
Connection errors (for example, due to a network connectivity problem), 409 Conflict, 429 Rate Limit,
and >=500 Internal errors will all be retried by default.

You can use the `max_retries` option to configure or disable this:

```python
from increase import Increase

# Configure the default for all requests:
increase = Increase(
    # default is 2
    max_retries=0,
)

# Or, configure per-request:
increase.with_options(max_retries=5).accounts.create(
    name="Jack",
)
```

### Timeouts

Requests time out after 60 seconds by default. You can configure this with a `timeout` option,
which accepts a float or an [`httpx.Timeout`](https://www.python-httpx.org/advanced/#fine-tuning-the-configuration):

```python
from increase import Increase

# Configure the default for all requests:
increase = Increase(
    # default is 60s
    timeout=20.0,
)

# More granular control:
increase = Increase(
    timeout=httpx.Timeout(60.0, read=5.0, write=10.0, connect=2.0),
)

# Override per-request:
increase.with_options(timeout=5 * 1000).accounts.list(
    status="open",
)
```

On timeout, an `APITimeoutError` is thrown.

Note that requests which time out will be [retried twice by default](#retries).

## Advanced: Configuring custom URLs, proxies, and transports

You can configure the following keyword arguments when instantiating the client:

```python
import httpx
from increase import Increase

increase = Increase(
    # Use a custom base URL
    base_url="http://my.test.server.example.com:8083",
    proxies="http://my.test.proxy.example.com",
    transport=httpx.HTTPTransport(local_address="0.0.0.0"),
)
```

See the httpx documentation for information about the [`proxies`](https://www.python-httpx.org/advanced/#http-proxying) and [`transport`](https://www.python-httpx.org/advanced/#custom-transports) keyword arguments.

## Status

This package is in beta. Its internals and interfaces are not stable and subject to change without a major semver bump;
please reach out if you rely on any undocumented behavior.

We are keen for your feedback; please open an [issue](https://www.github.com/increase/increase-python/issues) with questions, bugs, or suggestions.

## Requirements

Python 3.7 or higher.
