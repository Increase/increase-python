# Shared Types

```python
from increase.types import Entity, InboundDigitalWalletTokenRequestSimulationResult
```

# Accounts

Types:

```python
from increase.types import Account
```

Methods:

- <code title="post /accounts">client.accounts.<a href="./src/increase/resources/accounts.py">create</a>(\*\*<a href="src/increase/types/account_create_params.py">params</a>) -> <a href="./src/increase/types/account.py">Account</a></code>
- <code title="get /accounts/{account_id}">client.accounts.<a href="./src/increase/resources/accounts.py">retrieve</a>(account_id) -> <a href="./src/increase/types/account.py">Account</a></code>
- <code title="patch /accounts/{account_id}">client.accounts.<a href="./src/increase/resources/accounts.py">update</a>(account_id, \*\*<a href="src/increase/types/account_update_params.py">params</a>) -> <a href="./src/increase/types/account.py">Account</a></code>
- <code title="get /accounts">client.accounts.<a href="./src/increase/resources/accounts.py">list</a>(\*\*<a href="src/increase/types/account_list_params.py">params</a>) -> <a href="./src/increase/types/account.py">SyncPage[Account]</a></code>
- <code title="post /accounts/{account_id}/close">client.accounts.<a href="./src/increase/resources/accounts.py">close</a>(account_id) -> <a href="./src/increase/types/account.py">Account</a></code>

# AccountNumbers

Types:

```python
from increase.types import AccountNumber
```

Methods:

- <code title="post /account_numbers">client.account_numbers.<a href="./src/increase/resources/account_numbers.py">create</a>(\*\*<a href="src/increase/types/account_number_create_params.py">params</a>) -> <a href="./src/increase/types/account_number.py">AccountNumber</a></code>
- <code title="get /account_numbers/{account_number_id}">client.account_numbers.<a href="./src/increase/resources/account_numbers.py">retrieve</a>(account_number_id) -> <a href="./src/increase/types/account_number.py">AccountNumber</a></code>
- <code title="patch /account_numbers/{account_number_id}">client.account_numbers.<a href="./src/increase/resources/account_numbers.py">update</a>(account_number_id, \*\*<a href="src/increase/types/account_number_update_params.py">params</a>) -> <a href="./src/increase/types/account_number.py">AccountNumber</a></code>
- <code title="get /account_numbers">client.account_numbers.<a href="./src/increase/resources/account_numbers.py">list</a>(\*\*<a href="src/increase/types/account_number_list_params.py">params</a>) -> <a href="./src/increase/types/account_number.py">SyncPage[AccountNumber]</a></code>

# RealTimeDecisions

Types:

```python
from increase.types import RealTimeDecision
```

Methods:

- <code title="get /real_time_decisions/{real_time_decision_id}">client.real_time_decisions.<a href="./src/increase/resources/real_time_decisions.py">retrieve</a>(real_time_decision_id) -> <a href="./src/increase/types/real_time_decision.py">RealTimeDecision</a></code>
- <code title="post /real_time_decisions/{real_time_decision_id}/action">client.real_time_decisions.<a href="./src/increase/resources/real_time_decisions.py">action</a>(real_time_decision_id, \*\*<a href="src/increase/types/real_time_decision_action_params.py">params</a>) -> <a href="./src/increase/types/real_time_decision.py">RealTimeDecision</a></code>

# Cards

Types:

```python
from increase.types import Card, CardDetails
```

Methods:

- <code title="post /cards">client.cards.<a href="./src/increase/resources/cards.py">create</a>(\*\*<a href="src/increase/types/card_create_params.py">params</a>) -> <a href="./src/increase/types/card.py">Card</a></code>
- <code title="get /cards/{card_id}">client.cards.<a href="./src/increase/resources/cards.py">retrieve</a>(card_id) -> <a href="./src/increase/types/card.py">Card</a></code>
- <code title="patch /cards/{card_id}">client.cards.<a href="./src/increase/resources/cards.py">update</a>(card_id, \*\*<a href="src/increase/types/card_update_params.py">params</a>) -> <a href="./src/increase/types/card.py">Card</a></code>
- <code title="get /cards">client.cards.<a href="./src/increase/resources/cards.py">list</a>(\*\*<a href="src/increase/types/card_list_params.py">params</a>) -> <a href="./src/increase/types/card.py">SyncPage[Card]</a></code>
- <code title="get /cards/{card_id}/details">client.cards.<a href="./src/increase/resources/cards.py">retrieve_sensitive_details</a>(card_id) -> <a href="./src/increase/types/card_details.py">CardDetails</a></code>

# CardDisputes

Types:

```python
from increase.types import CardDispute
```

Methods:

- <code title="post /card_disputes">client.card_disputes.<a href="./src/increase/resources/card_disputes.py">create</a>(\*\*<a href="src/increase/types/card_dispute_create_params.py">params</a>) -> <a href="./src/increase/types/card_dispute.py">CardDispute</a></code>
- <code title="get /card_disputes/{card_dispute_id}">client.card_disputes.<a href="./src/increase/resources/card_disputes.py">retrieve</a>(card_dispute_id) -> <a href="./src/increase/types/card_dispute.py">CardDispute</a></code>
- <code title="get /card_disputes">client.card_disputes.<a href="./src/increase/resources/card_disputes.py">list</a>(\*\*<a href="src/increase/types/card_dispute_list_params.py">params</a>) -> <a href="./src/increase/types/card_dispute.py">SyncPage[CardDispute]</a></code>

# CardProfiles

Types:

```python
from increase.types import CardProfile
```

Methods:

- <code title="post /card_profiles">client.card_profiles.<a href="./src/increase/resources/card_profiles.py">create</a>(\*\*<a href="src/increase/types/card_profile_create_params.py">params</a>) -> <a href="./src/increase/types/card_profile.py">CardProfile</a></code>
- <code title="get /card_profiles/{card_profile_id}">client.card_profiles.<a href="./src/increase/resources/card_profiles.py">retrieve</a>(card_profile_id) -> <a href="./src/increase/types/card_profile.py">CardProfile</a></code>
- <code title="get /card_profiles">client.card_profiles.<a href="./src/increase/resources/card_profiles.py">list</a>(\*\*<a href="src/increase/types/card_profile_list_params.py">params</a>) -> <a href="./src/increase/types/card_profile.py">SyncPage[CardProfile]</a></code>

# ExternalAccounts

Types:

```python
from increase.types import ExternalAccount
```

Methods:

- <code title="post /external_accounts">client.external_accounts.<a href="./src/increase/resources/external_accounts.py">create</a>(\*\*<a href="src/increase/types/external_account_create_params.py">params</a>) -> <a href="./src/increase/types/external_account.py">ExternalAccount</a></code>
- <code title="get /external_accounts/{external_account_id}">client.external_accounts.<a href="./src/increase/resources/external_accounts.py">retrieve</a>(external_account_id) -> <a href="./src/increase/types/external_account.py">ExternalAccount</a></code>
- <code title="patch /external_accounts/{external_account_id}">client.external_accounts.<a href="./src/increase/resources/external_accounts.py">update</a>(external_account_id, \*\*<a href="src/increase/types/external_account_update_params.py">params</a>) -> <a href="./src/increase/types/external_account.py">ExternalAccount</a></code>
- <code title="get /external_accounts">client.external_accounts.<a href="./src/increase/resources/external_accounts.py">list</a>(\*\*<a href="src/increase/types/external_account_list_params.py">params</a>) -> <a href="./src/increase/types/external_account.py">SyncPage[ExternalAccount]</a></code>

# DigitalWalletTokens

Types:

```python
from increase.types import DigitalWalletToken
```

Methods:

- <code title="get /digital_wallet_tokens/{digital_wallet_token_id}">client.digital_wallet_tokens.<a href="./src/increase/resources/digital_wallet_tokens.py">retrieve</a>(digital_wallet_token_id) -> <a href="./src/increase/types/digital_wallet_token.py">DigitalWalletToken</a></code>
- <code title="get /digital_wallet_tokens">client.digital_wallet_tokens.<a href="./src/increase/resources/digital_wallet_tokens.py">list</a>(\*\*<a href="src/increase/types/digital_wallet_token_list_params.py">params</a>) -> <a href="./src/increase/types/digital_wallet_token.py">SyncPage[DigitalWalletToken]</a></code>

# Transactions

Types:

```python
from increase.types import Transaction
```

Methods:

- <code title="get /transactions/{transaction_id}">client.transactions.<a href="./src/increase/resources/transactions.py">retrieve</a>(transaction_id) -> <a href="./src/increase/types/transaction.py">Transaction</a></code>
- <code title="get /transactions">client.transactions.<a href="./src/increase/resources/transactions.py">list</a>(\*\*<a href="src/increase/types/transaction_list_params.py">params</a>) -> <a href="./src/increase/types/transaction.py">SyncPage[Transaction]</a></code>

# PendingTransactions

Types:

```python
from increase.types import PendingTransaction
```

Methods:

- <code title="get /pending_transactions/{pending_transaction_id}">client.pending_transactions.<a href="./src/increase/resources/pending_transactions.py">retrieve</a>(pending_transaction_id) -> <a href="./src/increase/types/pending_transaction.py">PendingTransaction</a></code>
- <code title="get /pending_transactions">client.pending_transactions.<a href="./src/increase/resources/pending_transactions.py">list</a>(\*\*<a href="src/increase/types/pending_transaction_list_params.py">params</a>) -> <a href="./src/increase/types/pending_transaction.py">SyncPage[PendingTransaction]</a></code>

# DeclinedTransactions

Types:

```python
from increase.types import DeclinedTransaction
```

Methods:

- <code title="get /declined_transactions/{declined_transaction_id}">client.declined_transactions.<a href="./src/increase/resources/declined_transactions.py">retrieve</a>(declined_transaction_id) -> <a href="./src/increase/types/declined_transaction.py">DeclinedTransaction</a></code>
- <code title="get /declined_transactions">client.declined_transactions.<a href="./src/increase/resources/declined_transactions.py">list</a>(\*\*<a href="src/increase/types/declined_transaction_list_params.py">params</a>) -> <a href="./src/increase/types/declined_transaction.py">SyncPage[DeclinedTransaction]</a></code>

# Limits

Types:

```python
from increase.types import Limit
```

Methods:

- <code title="post /limits">client.limits.<a href="./src/increase/resources/limits.py">create</a>(\*\*<a href="src/increase/types/limit_create_params.py">params</a>) -> <a href="./src/increase/types/limit.py">Limit</a></code>
- <code title="get /limits/{limit_id}">client.limits.<a href="./src/increase/resources/limits.py">retrieve</a>(limit_id) -> <a href="./src/increase/types/limit.py">Limit</a></code>
- <code title="patch /limits/{limit_id}">client.limits.<a href="./src/increase/resources/limits.py">update</a>(limit_id, \*\*<a href="src/increase/types/limit_update_params.py">params</a>) -> <a href="./src/increase/types/limit.py">Limit</a></code>
- <code title="get /limits">client.limits.<a href="./src/increase/resources/limits.py">list</a>(\*\*<a href="src/increase/types/limit_list_params.py">params</a>) -> <a href="./src/increase/types/limit.py">SyncPage[Limit]</a></code>

# AccountTransfers

Types:

```python
from increase.types import AccountTransfer
```

Methods:

- <code title="post /account_transfers">client.account_transfers.<a href="./src/increase/resources/account_transfers.py">create</a>(\*\*<a href="src/increase/types/account_transfer_create_params.py">params</a>) -> <a href="./src/increase/types/account_transfer.py">AccountTransfer</a></code>
- <code title="get /account_transfers/{account_transfer_id}">client.account_transfers.<a href="./src/increase/resources/account_transfers.py">retrieve</a>(account_transfer_id) -> <a href="./src/increase/types/account_transfer.py">AccountTransfer</a></code>
- <code title="get /account_transfers">client.account_transfers.<a href="./src/increase/resources/account_transfers.py">list</a>(\*\*<a href="src/increase/types/account_transfer_list_params.py">params</a>) -> <a href="./src/increase/types/account_transfer.py">SyncPage[AccountTransfer]</a></code>

# ACHTransfers

Types:

```python
from increase.types import ACHTransfer
```

Methods:

- <code title="post /ach_transfers">client.ach_transfers.<a href="./src/increase/resources/ach_transfers.py">create</a>(\*\*<a href="src/increase/types/ach_transfer_create_params.py">params</a>) -> <a href="./src/increase/types/ach_transfer.py">ACHTransfer</a></code>
- <code title="get /ach_transfers/{ach_transfer_id}">client.ach_transfers.<a href="./src/increase/resources/ach_transfers.py">retrieve</a>(ach_transfer_id) -> <a href="./src/increase/types/ach_transfer.py">ACHTransfer</a></code>
- <code title="get /ach_transfers">client.ach_transfers.<a href="./src/increase/resources/ach_transfers.py">list</a>(\*\*<a href="src/increase/types/ach_transfer_list_params.py">params</a>) -> <a href="./src/increase/types/ach_transfer.py">SyncPage[ACHTransfer]</a></code>

# ACHPrenotifications

Types:

```python
from increase.types import ACHPrenotification
```

Methods:

- <code title="post /ach_prenotifications">client.ach_prenotifications.<a href="./src/increase/resources/ach_prenotifications.py">create</a>(\*\*<a href="src/increase/types/ach_prenotification_create_params.py">params</a>) -> <a href="./src/increase/types/ach_prenotification.py">ACHPrenotification</a></code>
- <code title="get /ach_prenotifications/{ach_prenotification_id}">client.ach_prenotifications.<a href="./src/increase/resources/ach_prenotifications.py">retrieve</a>(ach_prenotification_id) -> <a href="./src/increase/types/ach_prenotification.py">ACHPrenotification</a></code>
- <code title="get /ach_prenotifications">client.ach_prenotifications.<a href="./src/increase/resources/ach_prenotifications.py">list</a>(\*\*<a href="src/increase/types/ach_prenotification_list_params.py">params</a>) -> <a href="./src/increase/types/ach_prenotification.py">SyncPage[ACHPrenotification]</a></code>

# WireTransfers

Types:

```python
from increase.types import WireTransfer
```

Methods:

- <code title="post /wire_transfers">client.wire_transfers.<a href="./src/increase/resources/wire_transfers.py">create</a>(\*\*<a href="src/increase/types/wire_transfer_create_params.py">params</a>) -> <a href="./src/increase/types/wire_transfer.py">WireTransfer</a></code>
- <code title="get /wire_transfers/{wire_transfer_id}">client.wire_transfers.<a href="./src/increase/resources/wire_transfers.py">retrieve</a>(wire_transfer_id) -> <a href="./src/increase/types/wire_transfer.py">WireTransfer</a></code>
- <code title="get /wire_transfers">client.wire_transfers.<a href="./src/increase/resources/wire_transfers.py">list</a>(\*\*<a href="src/increase/types/wire_transfer_list_params.py">params</a>) -> <a href="./src/increase/types/wire_transfer.py">SyncPage[WireTransfer]</a></code>
- <code title="post /simulations/wire_transfers/{wire_transfer_id}/reverse">client.wire_transfers.<a href="./src/increase/resources/wire_transfers.py">reverse</a>(wire_transfer_id) -> <a href="./src/increase/types/wire_transfer.py">WireTransfer</a></code>
- <code title="post /simulations/wire_transfers/{wire_transfer_id}/submit">client.wire_transfers.<a href="./src/increase/resources/wire_transfers.py">submit</a>(wire_transfer_id) -> <a href="./src/increase/types/wire_transfer.py">WireTransfer</a></code>

# CheckTransfers

Types:

```python
from increase.types import CheckTransfer
```

Methods:

- <code title="post /check_transfers">client.check_transfers.<a href="./src/increase/resources/check_transfers.py">create</a>(\*\*<a href="src/increase/types/check_transfer_create_params.py">params</a>) -> <a href="./src/increase/types/check_transfer.py">CheckTransfer</a></code>
- <code title="get /check_transfers/{check_transfer_id}">client.check_transfers.<a href="./src/increase/resources/check_transfers.py">retrieve</a>(check_transfer_id) -> <a href="./src/increase/types/check_transfer.py">CheckTransfer</a></code>
- <code title="get /check_transfers">client.check_transfers.<a href="./src/increase/resources/check_transfers.py">list</a>(\*\*<a href="src/increase/types/check_transfer_list_params.py">params</a>) -> <a href="./src/increase/types/check_transfer.py">SyncPage[CheckTransfer]</a></code>
- <code title="post /check_transfers/{check_transfer_id}/stop_payment">client.check_transfers.<a href="./src/increase/resources/check_transfers.py">stop_payment</a>(check_transfer_id) -> <a href="./src/increase/types/check_transfer.py">CheckTransfer</a></code>

# Entities

Types:

```python
from increase.types import Entity
```

Methods:

- <code title="post /entities">client.entities.<a href="./src/increase/resources/entities/entities.py">create</a>(\*\*<a href="src/increase/types/entity_create_params.py">params</a>) -> <a href="./src/increase/types/shared/entity.py">shared.Entity</a></code>
- <code title="get /entities/{entity_id}">client.entities.<a href="./src/increase/resources/entities/entities.py">retrieve</a>(entity_id) -> <a href="./src/increase/types/shared/entity.py">shared.Entity</a></code>
- <code title="get /entities">client.entities.<a href="./src/increase/resources/entities/entities.py">list</a>(\*\*<a href="src/increase/types/entity_list_params.py">params</a>) -> <a href="./src/increase/types/shared/entity.py">SyncPage[shared.Entity]</a></code>

## SupplementalDocuments

Types:

```python
from increase.types.entities import Entity
```

Methods:

- <code title="post /entities/{entity_id}/supplemental_documents">client.entities.supplemental_documents.<a href="./src/increase/resources/entities/supplemental_documents.py">create</a>(entity_id, \*\*<a href="src/increase/types/entities/supplemental_document_create_params.py">params</a>) -> <a href="./src/increase/types/shared/entity.py">shared.Entity</a></code>

# WireDrawdownRequests

Types:

```python
from increase.types import WireDrawdownRequest
```

Methods:

- <code title="post /wire_drawdown_requests">client.wire_drawdown_requests.<a href="./src/increase/resources/wire_drawdown_requests.py">create</a>(\*\*<a href="src/increase/types/wire_drawdown_request_create_params.py">params</a>) -> <a href="./src/increase/types/wire_drawdown_request.py">WireDrawdownRequest</a></code>
- <code title="get /wire_drawdown_requests/{wire_drawdown_request_id}">client.wire_drawdown_requests.<a href="./src/increase/resources/wire_drawdown_requests.py">retrieve</a>(wire_drawdown_request_id) -> <a href="./src/increase/types/wire_drawdown_request.py">WireDrawdownRequest</a></code>
- <code title="get /wire_drawdown_requests">client.wire_drawdown_requests.<a href="./src/increase/resources/wire_drawdown_requests.py">list</a>(\*\*<a href="src/increase/types/wire_drawdown_request_list_params.py">params</a>) -> <a href="./src/increase/types/wire_drawdown_request.py">SyncPage[WireDrawdownRequest]</a></code>

# Events

Types:

```python
from increase.types import Event
```

Methods:

- <code title="get /events/{event_id}">client.events.<a href="./src/increase/resources/events.py">retrieve</a>(event_id) -> <a href="./src/increase/types/event.py">Event</a></code>
- <code title="get /events">client.events.<a href="./src/increase/resources/events.py">list</a>(\*\*<a href="src/increase/types/event_list_params.py">params</a>) -> <a href="./src/increase/types/event.py">SyncPage[Event]</a></code>

# EventSubscriptions

Types:

```python
from increase.types import EventSubscription
```

Methods:

- <code title="post /event_subscriptions">client.event_subscriptions.<a href="./src/increase/resources/event_subscriptions.py">create</a>(\*\*<a href="src/increase/types/event_subscription_create_params.py">params</a>) -> <a href="./src/increase/types/event_subscription.py">EventSubscription</a></code>
- <code title="get /event_subscriptions/{event_subscription_id}">client.event_subscriptions.<a href="./src/increase/resources/event_subscriptions.py">retrieve</a>(event_subscription_id) -> <a href="./src/increase/types/event_subscription.py">EventSubscription</a></code>
- <code title="patch /event_subscriptions/{event_subscription_id}">client.event_subscriptions.<a href="./src/increase/resources/event_subscriptions.py">update</a>(event_subscription_id, \*\*<a href="src/increase/types/event_subscription_update_params.py">params</a>) -> <a href="./src/increase/types/event_subscription.py">EventSubscription</a></code>
- <code title="get /event_subscriptions">client.event_subscriptions.<a href="./src/increase/resources/event_subscriptions.py">list</a>(\*\*<a href="src/increase/types/event_subscription_list_params.py">params</a>) -> <a href="./src/increase/types/event_subscription.py">SyncPage[EventSubscription]</a></code>

# Files

Types:

```python
from increase.types import File
```

Methods:

- <code title="post /files">client.files.<a href="./src/increase/resources/files.py">create</a>(\*\*<a href="src/increase/types/file_create_params.py">params</a>) -> <a href="./src/increase/types/file.py">File</a></code>
- <code title="get /files/{file_id}">client.files.<a href="./src/increase/resources/files.py">retrieve</a>(file_id) -> <a href="./src/increase/types/file.py">File</a></code>
- <code title="get /files">client.files.<a href="./src/increase/resources/files.py">list</a>(\*\*<a href="src/increase/types/file_list_params.py">params</a>) -> <a href="./src/increase/types/file.py">SyncPage[File]</a></code>

# Groups

Types:

```python
from increase.types import Group
```

Methods:

- <code title="get /groups/current">client.groups.<a href="./src/increase/resources/groups.py">retrieve_details</a>() -> <a href="./src/increase/types/group.py">Group</a></code>

# OauthConnections

Types:

```python
from increase.types import OauthConnection
```

Methods:

- <code title="get /oauth_connections/{oauth_connection_id}">client.oauth_connections.<a href="./src/increase/resources/oauth_connections.py">retrieve</a>(oauth_connection_id) -> <a href="./src/increase/types/oauth_connection.py">OauthConnection</a></code>
- <code title="get /oauth_connections">client.oauth_connections.<a href="./src/increase/resources/oauth_connections.py">list</a>(\*\*<a href="src/increase/types/oauth_connection_list_params.py">params</a>) -> <a href="./src/increase/types/oauth_connection.py">SyncPage[OauthConnection]</a></code>

# CheckDeposits

Types:

```python
from increase.types import CheckDeposit
```

Methods:

- <code title="post /check_deposits">client.check_deposits.<a href="./src/increase/resources/check_deposits.py">create</a>(\*\*<a href="src/increase/types/check_deposit_create_params.py">params</a>) -> <a href="./src/increase/types/simulations/check_deposit.py">CheckDeposit</a></code>
- <code title="get /check_deposits/{check_deposit_id}">client.check_deposits.<a href="./src/increase/resources/check_deposits.py">retrieve</a>(check_deposit_id) -> <a href="./src/increase/types/simulations/check_deposit.py">CheckDeposit</a></code>
- <code title="get /check_deposits">client.check_deposits.<a href="./src/increase/resources/check_deposits.py">list</a>(\*\*<a href="src/increase/types/check_deposit_list_params.py">params</a>) -> <a href="./src/increase/types/simulations/check_deposit.py">SyncPage[CheckDeposit]</a></code>

# RoutingNumbers

Types:

```python
from increase.types import RoutingNumber
```

Methods:

- <code title="get /routing_numbers">client.routing_numbers.<a href="./src/increase/resources/routing_numbers.py">list</a>(\*\*<a href="src/increase/types/routing_number_list_params.py">params</a>) -> <a href="./src/increase/types/routing_number.py">SyncPage[RoutingNumber]</a></code>

# AccountStatements

Types:

```python
from increase.types import AccountStatement
```

Methods:

- <code title="get /account_statements/{account_statement_id}">client.account_statements.<a href="./src/increase/resources/account_statements.py">retrieve</a>(account_statement_id) -> <a href="./src/increase/types/account_statement.py">AccountStatement</a></code>
- <code title="get /account_statements">client.account_statements.<a href="./src/increase/resources/account_statements.py">list</a>(\*\*<a href="src/increase/types/account_statement_list_params.py">params</a>) -> <a href="./src/increase/types/account_statement.py">SyncPage[AccountStatement]</a></code>

# Simulations

## AccountTransfers

Types:

```python
from increase.types.simulations import AccountTransfer
```

Methods:

- <code title="post /simulations/account_transfers/{account_transfer_id}/complete">client.simulations.account_transfers.<a href="./src/increase/resources/simulations/account_transfers.py">complete</a>(account_transfer_id) -> <a href="./src/increase/types/account_transfer.py">AccountTransfer</a></code>

## AccountStatements

Types:

```python
from increase.types.simulations import AccountStatement
```

Methods:

- <code title="post /simulations/account_statements">client.simulations.account_statements.<a href="./src/increase/resources/simulations/account_statements.py">create</a>(\*\*<a href="src/increase/types/simulations/account_statement_create_params.py">params</a>) -> <a href="./src/increase/types/account_statement.py">AccountStatement</a></code>

## ACHTransfers

Types:

```python
from increase.types.simulations import ACHTransferSimulation, ACHTransfer
```

Methods:

- <code title="post /simulations/inbound_ach_transfers">client.simulations.ach_transfers.<a href="./src/increase/resources/simulations/ach_transfers.py">create_inbound</a>(\*\*<a href="src/increase/types/simulations/ach_transfer_create_inbound_params.py">params</a>) -> <a href="./src/increase/types/simulations/ach_transfer_simulation.py">ACHTransferSimulation</a></code>
- <code title="post /simulations/ach_transfers/{ach_transfer_id}/return">client.simulations.ach*transfers.<a href="./src/increase/resources/simulations/ach_transfers.py">return*</a>(ach_transfer_id) -> <a href="./src/increase/types/ach_transfer.py">ACHTransfer</a></code>
- <code title="post /simulations/ach_transfers/{ach_transfer_id}/submit">client.simulations.ach_transfers.<a href="./src/increase/resources/simulations/ach_transfers.py">submit</a>(ach_transfer_id) -> <a href="./src/increase/types/ach_transfer.py">ACHTransfer</a></code>

## CardDisputes

Types:

```python
from increase.types.simulations import CardDispute
```

Methods:

- <code title="post /simulations/card_disputes/{card_dispute_id}/action">client.simulations.card_disputes.<a href="./src/increase/resources/simulations/card_disputes.py">action</a>(card_dispute_id, \*\*<a href="src/increase/types/simulations/card_dispute_action_params.py">params</a>) -> <a href="./src/increase/types/card_dispute.py">CardDispute</a></code>

## CheckTransfers

Types:

```python
from increase.types.simulations import CheckTransfer
```

Methods:

- <code title="post /simulations/check_transfers/{check_transfer_id}/mail">client.simulations.check_transfers.<a href="./src/increase/resources/simulations/check_transfers.py">mail</a>(check_transfer_id) -> <a href="./src/increase/types/check_transfer.py">CheckTransfer</a></code>

## DigitalWalletTokenRequests

Types:

```python
from increase.types.simulations import InboundDigitalWalletTokenRequestSimulationResult
```

Methods:

- <code title="post /simulations/digital_wallet_token_requests">client.simulations.digital_wallet_token_requests.<a href="./src/increase/resources/simulations/digital_wallet_token_requests.py">create</a>(\*\*<a href="src/increase/types/simulations/digital_wallet_token_request_create_params.py">params</a>) -> <a href="./src/increase/types/shared/inbound_digital_wallet_token_request_simulation_result.py">shared.InboundDigitalWalletTokenRequestSimulationResult</a></code>

## CheckDeposits

Types:

```python
from increase.types.simulations import CheckDeposit
```

Methods:

- <code title="post /simulations/check_deposits/{check_deposit_id}/reject">client.simulations.check_deposits.<a href="./src/increase/resources/simulations/check_deposits.py">reject</a>(check_deposit_id) -> <a href="./src/increase/types/simulations/check_deposit.py">CheckDeposit</a></code>
- <code title="post /simulations/check_deposits/{check_deposit_id}/submit">client.simulations.check_deposits.<a href="./src/increase/resources/simulations/check_deposits.py">submit</a>(check_deposit_id) -> <a href="./src/increase/types/simulations/check_deposit.py">CheckDeposit</a></code>

## WireTransfers

Types:

```python
from increase.types.simulations import WireTransferSimulation
```

Methods:

- <code title="post /simulations/inbound_wire_transfers">client.simulations.wire_transfers.<a href="./src/increase/resources/simulations/wire_transfers.py">create_inbound</a>(\*\*<a href="src/increase/types/simulations/wire_transfer_create_inbound_params.py">params</a>) -> <a href="./src/increase/types/simulations/wire_transfer_simulation.py">WireTransferSimulation</a></code>

## Cards

Types:

```python
from increase.types.simulations import CardAuthorizationSimulation, Transaction
```

Methods:

- <code title="post /simulations/card_authorizations">client.simulations.cards.<a href="./src/increase/resources/simulations/cards.py">authorize</a>(\*\*<a href="src/increase/types/simulations/card_authorize_params.py">params</a>) -> <a href="./src/increase/types/simulations/card_authorization_simulation.py">CardAuthorizationSimulation</a></code>
- <code title="post /simulations/card_settlements">client.simulations.cards.<a href="./src/increase/resources/simulations/cards.py">settlement</a>(\*\*<a href="src/increase/types/simulations/card_settlement_params.py">params</a>) -> <a href="./src/increase/types/transaction.py">Transaction</a></code>

## RealTimePaymentsTransfers

Types:

```python
from increase.types.simulations import InboundRealTimePaymentsTransferSimulationResult
```

Methods:

- <code title="post /simulations/inbound_real_time_payments_transfers">client.simulations.real_time_payments_transfers.<a href="./src/increase/resources/simulations/real_time_payments_transfers.py">create_inbound</a>(\*\*<a href="src/increase/types/simulations/real_time_payments_transfer_create_inbound_params.py">params</a>) -> <a href="./src/increase/types/simulations/inbound_real_time_payments_transfer_simulation_result.py">InboundRealTimePaymentsTransferSimulationResult</a></code>