from datetime import datetime

from increase import Increase

client = Increase(environment="sandbox")

# datetime responses will always be instances of `datetime`
account = client.accounts.list(limit=1).data[0]
assert isinstance(account.created_at, datetime)

dt = datetime.fromisoformat("2023-02-25T18:20:35+00:00")

# both `datetime` instances or datetime strings can be passed as a request param
page = client.events.list(limit=1, created_at={"after": dt})
assert len(page.data) == 1

page = client.events.list(limit=1, created_at={"after": dt.isoformat()})
assert len(page.data) == 1
