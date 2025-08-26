# Accounts

Types:

```python
from increase.types import Account, BalanceLookup
```

Methods:

- <code title="post /accounts">client.accounts.<a href="./src/increase/resources/accounts.py">create</a>(\*\*<a href="src/increase/types/account_create_params.py">params</a>) -> <a href="./src/increase/types/account.py">Account</a></code>
- <code title="get /accounts/{account_id}">client.accounts.<a href="./src/increase/resources/accounts.py">retrieve</a>(account_id) -> <a href="./src/increase/types/account.py">Account</a></code>
- <code title="patch /accounts/{account_id}">client.accounts.<a href="./src/increase/resources/accounts.py">update</a>(account_id, \*\*<a href="src/increase/types/account_update_params.py">params</a>) -> <a href="./src/increase/types/account.py">Account</a></code>
- <code title="get /accounts">client.accounts.<a href="./src/increase/resources/accounts.py">list</a>(\*\*<a href="src/increase/types/account_list_params.py">params</a>) -> <a href="./src/increase/types/account.py">SyncPage[Account]</a></code>
- <code title="get /accounts/{account_id}/balance">client.accounts.<a href="./src/increase/resources/accounts.py">balance</a>(account_id, \*\*<a href="src/increase/types/account_balance_params.py">params</a>) -> <a href="./src/increase/types/balance_lookup.py">BalanceLookup</a></code>
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

# Cards

Types:

```python
from increase.types import Card, CardDetails, CardIframeURL
```

Methods:

- <code title="post /cards">client.cards.<a href="./src/increase/resources/cards.py">create</a>(\*\*<a href="src/increase/types/card_create_params.py">params</a>) -> <a href="./src/increase/types/card.py">Card</a></code>
- <code title="get /cards/{card_id}">client.cards.<a href="./src/increase/resources/cards.py">retrieve</a>(card_id) -> <a href="./src/increase/types/card.py">Card</a></code>
- <code title="patch /cards/{card_id}">client.cards.<a href="./src/increase/resources/cards.py">update</a>(card_id, \*\*<a href="src/increase/types/card_update_params.py">params</a>) -> <a href="./src/increase/types/card.py">Card</a></code>
- <code title="get /cards">client.cards.<a href="./src/increase/resources/cards.py">list</a>(\*\*<a href="src/increase/types/card_list_params.py">params</a>) -> <a href="./src/increase/types/card.py">SyncPage[Card]</a></code>
- <code title="post /cards/{card_id}/create_details_iframe">client.cards.<a href="./src/increase/resources/cards.py">create_details_iframe</a>(card_id, \*\*<a href="src/increase/types/card_create_details_iframe_params.py">params</a>) -> <a href="./src/increase/types/card_iframe_url.py">CardIframeURL</a></code>
- <code title="get /cards/{card_id}/details">client.cards.<a href="./src/increase/resources/cards.py">details</a>(card_id) -> <a href="./src/increase/types/card_details.py">CardDetails</a></code>

# CardPayments

Types:

```python
from increase.types import CardPayment
```

Methods:

- <code title="get /card_payments/{card_payment_id}">client.card_payments.<a href="./src/increase/resources/card_payments.py">retrieve</a>(card_payment_id) -> <a href="./src/increase/types/card_payment.py">CardPayment</a></code>
- <code title="get /card_payments">client.card_payments.<a href="./src/increase/resources/card_payments.py">list</a>(\*\*<a href="src/increase/types/card_payment_list_params.py">params</a>) -> <a href="./src/increase/types/card_payment.py">SyncPage[CardPayment]</a></code>

# CardPurchaseSupplements

Types:

```python
from increase.types import CardPurchaseSupplement
```

Methods:

- <code title="get /card_purchase_supplements/{card_purchase_supplement_id}">client.card_purchase_supplements.<a href="./src/increase/resources/card_purchase_supplements.py">retrieve</a>(card_purchase_supplement_id) -> <a href="./src/increase/types/card_purchase_supplement.py">CardPurchaseSupplement</a></code>
- <code title="get /card_purchase_supplements">client.card_purchase_supplements.<a href="./src/increase/resources/card_purchase_supplements.py">list</a>(\*\*<a href="src/increase/types/card_purchase_supplement_list_params.py">params</a>) -> <a href="./src/increase/types/card_purchase_supplement.py">SyncPage[CardPurchaseSupplement]</a></code>

# CardDisputes

Types:

```python
from increase.types import CardDispute
```

Methods:

- <code title="post /card_disputes">client.card_disputes.<a href="./src/increase/resources/card_disputes.py">create</a>(\*\*<a href="src/increase/types/card_dispute_create_params.py">params</a>) -> <a href="./src/increase/types/card_dispute.py">CardDispute</a></code>
- <code title="get /card_disputes/{card_dispute_id}">client.card_disputes.<a href="./src/increase/resources/card_disputes.py">retrieve</a>(card_dispute_id) -> <a href="./src/increase/types/card_dispute.py">CardDispute</a></code>
- <code title="get /card_disputes">client.card_disputes.<a href="./src/increase/resources/card_disputes.py">list</a>(\*\*<a href="src/increase/types/card_dispute_list_params.py">params</a>) -> <a href="./src/increase/types/card_dispute.py">SyncPage[CardDispute]</a></code>

# PhysicalCards

Types:

```python
from increase.types import PhysicalCard
```

Methods:

- <code title="post /physical_cards">client.physical_cards.<a href="./src/increase/resources/physical_cards.py">create</a>(\*\*<a href="src/increase/types/physical_card_create_params.py">params</a>) -> <a href="./src/increase/types/physical_card.py">PhysicalCard</a></code>
- <code title="get /physical_cards/{physical_card_id}">client.physical_cards.<a href="./src/increase/resources/physical_cards.py">retrieve</a>(physical_card_id) -> <a href="./src/increase/types/physical_card.py">PhysicalCard</a></code>
- <code title="patch /physical_cards/{physical_card_id}">client.physical_cards.<a href="./src/increase/resources/physical_cards.py">update</a>(physical_card_id, \*\*<a href="src/increase/types/physical_card_update_params.py">params</a>) -> <a href="./src/increase/types/physical_card.py">PhysicalCard</a></code>
- <code title="get /physical_cards">client.physical_cards.<a href="./src/increase/resources/physical_cards.py">list</a>(\*\*<a href="src/increase/types/physical_card_list_params.py">params</a>) -> <a href="./src/increase/types/physical_card.py">SyncPage[PhysicalCard]</a></code>

# DigitalCardProfiles

Types:

```python
from increase.types import DigitalCardProfile
```

Methods:

- <code title="post /digital_card_profiles">client.digital_card_profiles.<a href="./src/increase/resources/digital_card_profiles.py">create</a>(\*\*<a href="src/increase/types/digital_card_profile_create_params.py">params</a>) -> <a href="./src/increase/types/digital_card_profile.py">DigitalCardProfile</a></code>
- <code title="get /digital_card_profiles/{digital_card_profile_id}">client.digital_card_profiles.<a href="./src/increase/resources/digital_card_profiles.py">retrieve</a>(digital_card_profile_id) -> <a href="./src/increase/types/digital_card_profile.py">DigitalCardProfile</a></code>
- <code title="get /digital_card_profiles">client.digital_card_profiles.<a href="./src/increase/resources/digital_card_profiles.py">list</a>(\*\*<a href="src/increase/types/digital_card_profile_list_params.py">params</a>) -> <a href="./src/increase/types/digital_card_profile.py">SyncPage[DigitalCardProfile]</a></code>
- <code title="post /digital_card_profiles/{digital_card_profile_id}/archive">client.digital_card_profiles.<a href="./src/increase/resources/digital_card_profiles.py">archive</a>(digital_card_profile_id) -> <a href="./src/increase/types/digital_card_profile.py">DigitalCardProfile</a></code>
- <code title="post /digital_card_profiles/{digital_card_profile_id}/clone">client.digital_card_profiles.<a href="./src/increase/resources/digital_card_profiles.py">clone</a>(digital_card_profile_id, \*\*<a href="src/increase/types/digital_card_profile_clone_params.py">params</a>) -> <a href="./src/increase/types/digital_card_profile.py">DigitalCardProfile</a></code>

# PhysicalCardProfiles

Types:

```python
from increase.types import PhysicalCardProfile
```

Methods:

- <code title="post /physical_card_profiles">client.physical_card_profiles.<a href="./src/increase/resources/physical_card_profiles.py">create</a>(\*\*<a href="src/increase/types/physical_card_profile_create_params.py">params</a>) -> <a href="./src/increase/types/physical_card_profile.py">PhysicalCardProfile</a></code>
- <code title="get /physical_card_profiles/{physical_card_profile_id}">client.physical_card_profiles.<a href="./src/increase/resources/physical_card_profiles.py">retrieve</a>(physical_card_profile_id) -> <a href="./src/increase/types/physical_card_profile.py">PhysicalCardProfile</a></code>
- <code title="get /physical_card_profiles">client.physical_card_profiles.<a href="./src/increase/resources/physical_card_profiles.py">list</a>(\*\*<a href="src/increase/types/physical_card_profile_list_params.py">params</a>) -> <a href="./src/increase/types/physical_card_profile.py">SyncPage[PhysicalCardProfile]</a></code>
- <code title="post /physical_card_profiles/{physical_card_profile_id}/archive">client.physical_card_profiles.<a href="./src/increase/resources/physical_card_profiles.py">archive</a>(physical_card_profile_id) -> <a href="./src/increase/types/physical_card_profile.py">PhysicalCardProfile</a></code>
- <code title="post /physical_card_profiles/{physical_card_profile_id}/clone">client.physical_card_profiles.<a href="./src/increase/resources/physical_card_profiles.py">clone</a>(physical_card_profile_id, \*\*<a href="src/increase/types/physical_card_profile_clone_params.py">params</a>) -> <a href="./src/increase/types/physical_card_profile.py">PhysicalCardProfile</a></code>

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

- <code title="post /pending_transactions">client.pending_transactions.<a href="./src/increase/resources/pending_transactions.py">create</a>(\*\*<a href="src/increase/types/pending_transaction_create_params.py">params</a>) -> <a href="./src/increase/types/pending_transaction.py">PendingTransaction</a></code>
- <code title="get /pending_transactions/{pending_transaction_id}">client.pending_transactions.<a href="./src/increase/resources/pending_transactions.py">retrieve</a>(pending_transaction_id) -> <a href="./src/increase/types/pending_transaction.py">PendingTransaction</a></code>
- <code title="get /pending_transactions">client.pending_transactions.<a href="./src/increase/resources/pending_transactions.py">list</a>(\*\*<a href="src/increase/types/pending_transaction_list_params.py">params</a>) -> <a href="./src/increase/types/pending_transaction.py">SyncPage[PendingTransaction]</a></code>
- <code title="post /pending_transactions/{pending_transaction_id}/release">client.pending_transactions.<a href="./src/increase/resources/pending_transactions.py">release</a>(pending_transaction_id) -> <a href="./src/increase/types/pending_transaction.py">PendingTransaction</a></code>

# DeclinedTransactions

Types:

```python
from increase.types import DeclinedTransaction
```

Methods:

- <code title="get /declined_transactions/{declined_transaction_id}">client.declined_transactions.<a href="./src/increase/resources/declined_transactions.py">retrieve</a>(declined_transaction_id) -> <a href="./src/increase/types/declined_transaction.py">DeclinedTransaction</a></code>
- <code title="get /declined_transactions">client.declined_transactions.<a href="./src/increase/resources/declined_transactions.py">list</a>(\*\*<a href="src/increase/types/declined_transaction_list_params.py">params</a>) -> <a href="./src/increase/types/declined_transaction.py">SyncPage[DeclinedTransaction]</a></code>

# AccountTransfers

Types:

```python
from increase.types import AccountTransfer
```

Methods:

- <code title="post /account_transfers">client.account_transfers.<a href="./src/increase/resources/account_transfers.py">create</a>(\*\*<a href="src/increase/types/account_transfer_create_params.py">params</a>) -> <a href="./src/increase/types/account_transfer.py">AccountTransfer</a></code>
- <code title="get /account_transfers/{account_transfer_id}">client.account_transfers.<a href="./src/increase/resources/account_transfers.py">retrieve</a>(account_transfer_id) -> <a href="./src/increase/types/account_transfer.py">AccountTransfer</a></code>
- <code title="get /account_transfers">client.account_transfers.<a href="./src/increase/resources/account_transfers.py">list</a>(\*\*<a href="src/increase/types/account_transfer_list_params.py">params</a>) -> <a href="./src/increase/types/account_transfer.py">SyncPage[AccountTransfer]</a></code>
- <code title="post /account_transfers/{account_transfer_id}/approve">client.account_transfers.<a href="./src/increase/resources/account_transfers.py">approve</a>(account_transfer_id) -> <a href="./src/increase/types/account_transfer.py">AccountTransfer</a></code>
- <code title="post /account_transfers/{account_transfer_id}/cancel">client.account_transfers.<a href="./src/increase/resources/account_transfers.py">cancel</a>(account_transfer_id) -> <a href="./src/increase/types/account_transfer.py">AccountTransfer</a></code>

# ACHTransfers

Types:

```python
from increase.types import ACHTransfer
```

Methods:

- <code title="post /ach_transfers">client.ach_transfers.<a href="./src/increase/resources/ach_transfers.py">create</a>(\*\*<a href="src/increase/types/ach_transfer_create_params.py">params</a>) -> <a href="./src/increase/types/ach_transfer.py">ACHTransfer</a></code>
- <code title="get /ach_transfers/{ach_transfer_id}">client.ach_transfers.<a href="./src/increase/resources/ach_transfers.py">retrieve</a>(ach_transfer_id) -> <a href="./src/increase/types/ach_transfer.py">ACHTransfer</a></code>
- <code title="get /ach_transfers">client.ach_transfers.<a href="./src/increase/resources/ach_transfers.py">list</a>(\*\*<a href="src/increase/types/ach_transfer_list_params.py">params</a>) -> <a href="./src/increase/types/ach_transfer.py">SyncPage[ACHTransfer]</a></code>
- <code title="post /ach_transfers/{ach_transfer_id}/approve">client.ach_transfers.<a href="./src/increase/resources/ach_transfers.py">approve</a>(ach_transfer_id) -> <a href="./src/increase/types/ach_transfer.py">ACHTransfer</a></code>
- <code title="post /ach_transfers/{ach_transfer_id}/cancel">client.ach_transfers.<a href="./src/increase/resources/ach_transfers.py">cancel</a>(ach_transfer_id) -> <a href="./src/increase/types/ach_transfer.py">ACHTransfer</a></code>

# ACHPrenotifications

Types:

```python
from increase.types import ACHPrenotification
```

Methods:

- <code title="post /ach_prenotifications">client.ach_prenotifications.<a href="./src/increase/resources/ach_prenotifications.py">create</a>(\*\*<a href="src/increase/types/ach_prenotification_create_params.py">params</a>) -> <a href="./src/increase/types/ach_prenotification.py">ACHPrenotification</a></code>
- <code title="get /ach_prenotifications/{ach_prenotification_id}">client.ach_prenotifications.<a href="./src/increase/resources/ach_prenotifications.py">retrieve</a>(ach_prenotification_id) -> <a href="./src/increase/types/ach_prenotification.py">ACHPrenotification</a></code>
- <code title="get /ach_prenotifications">client.ach_prenotifications.<a href="./src/increase/resources/ach_prenotifications.py">list</a>(\*\*<a href="src/increase/types/ach_prenotification_list_params.py">params</a>) -> <a href="./src/increase/types/ach_prenotification.py">SyncPage[ACHPrenotification]</a></code>

# InboundACHTransfers

Types:

```python
from increase.types import InboundACHTransfer
```

Methods:

- <code title="get /inbound_ach_transfers/{inbound_ach_transfer_id}">client.inbound_ach_transfers.<a href="./src/increase/resources/inbound_ach_transfers.py">retrieve</a>(inbound_ach_transfer_id) -> <a href="./src/increase/types/inbound_ach_transfer.py">InboundACHTransfer</a></code>
- <code title="get /inbound_ach_transfers">client.inbound_ach_transfers.<a href="./src/increase/resources/inbound_ach_transfers.py">list</a>(\*\*<a href="src/increase/types/inbound_ach_transfer_list_params.py">params</a>) -> <a href="./src/increase/types/inbound_ach_transfer.py">SyncPage[InboundACHTransfer]</a></code>
- <code title="post /inbound_ach_transfers/{inbound_ach_transfer_id}/create_notification_of_change">client.inbound_ach_transfers.<a href="./src/increase/resources/inbound_ach_transfers.py">create_notification_of_change</a>(inbound_ach_transfer_id, \*\*<a href="src/increase/types/inbound_ach_transfer_create_notification_of_change_params.py">params</a>) -> <a href="./src/increase/types/inbound_ach_transfer.py">InboundACHTransfer</a></code>
- <code title="post /inbound_ach_transfers/{inbound_ach_transfer_id}/decline">client.inbound_ach_transfers.<a href="./src/increase/resources/inbound_ach_transfers.py">decline</a>(inbound_ach_transfer_id, \*\*<a href="src/increase/types/inbound_ach_transfer_decline_params.py">params</a>) -> <a href="./src/increase/types/inbound_ach_transfer.py">InboundACHTransfer</a></code>
- <code title="post /inbound_ach_transfers/{inbound_ach_transfer_id}/transfer_return">client.inbound_ach_transfers.<a href="./src/increase/resources/inbound_ach_transfers.py">transfer_return</a>(inbound_ach_transfer_id, \*\*<a href="src/increase/types/inbound_ach_transfer_transfer_return_params.py">params</a>) -> <a href="./src/increase/types/inbound_ach_transfer.py">InboundACHTransfer</a></code>

# WireTransfers

Types:

```python
from increase.types import WireTransfer
```

Methods:

- <code title="post /wire_transfers">client.wire_transfers.<a href="./src/increase/resources/wire_transfers.py">create</a>(\*\*<a href="src/increase/types/wire_transfer_create_params.py">params</a>) -> <a href="./src/increase/types/wire_transfer.py">WireTransfer</a></code>
- <code title="get /wire_transfers/{wire_transfer_id}">client.wire_transfers.<a href="./src/increase/resources/wire_transfers.py">retrieve</a>(wire_transfer_id) -> <a href="./src/increase/types/wire_transfer.py">WireTransfer</a></code>
- <code title="get /wire_transfers">client.wire_transfers.<a href="./src/increase/resources/wire_transfers.py">list</a>(\*\*<a href="src/increase/types/wire_transfer_list_params.py">params</a>) -> <a href="./src/increase/types/wire_transfer.py">SyncPage[WireTransfer]</a></code>
- <code title="post /wire_transfers/{wire_transfer_id}/approve">client.wire_transfers.<a href="./src/increase/resources/wire_transfers.py">approve</a>(wire_transfer_id) -> <a href="./src/increase/types/wire_transfer.py">WireTransfer</a></code>
- <code title="post /wire_transfers/{wire_transfer_id}/cancel">client.wire_transfers.<a href="./src/increase/resources/wire_transfers.py">cancel</a>(wire_transfer_id) -> <a href="./src/increase/types/wire_transfer.py">WireTransfer</a></code>

# InboundWireTransfers

Types:

```python
from increase.types import InboundWireTransfer
```

Methods:

- <code title="get /inbound_wire_transfers/{inbound_wire_transfer_id}">client.inbound_wire_transfers.<a href="./src/increase/resources/inbound_wire_transfers.py">retrieve</a>(inbound_wire_transfer_id) -> <a href="./src/increase/types/inbound_wire_transfer.py">InboundWireTransfer</a></code>
- <code title="get /inbound_wire_transfers">client.inbound_wire_transfers.<a href="./src/increase/resources/inbound_wire_transfers.py">list</a>(\*\*<a href="src/increase/types/inbound_wire_transfer_list_params.py">params</a>) -> <a href="./src/increase/types/inbound_wire_transfer.py">SyncPage[InboundWireTransfer]</a></code>
- <code title="post /inbound_wire_transfers/{inbound_wire_transfer_id}/reverse">client.inbound_wire_transfers.<a href="./src/increase/resources/inbound_wire_transfers.py">reverse</a>(inbound_wire_transfer_id, \*\*<a href="src/increase/types/inbound_wire_transfer_reverse_params.py">params</a>) -> <a href="./src/increase/types/inbound_wire_transfer.py">InboundWireTransfer</a></code>

# WireDrawdownRequests

Types:

```python
from increase.types import WireDrawdownRequest
```

Methods:

- <code title="post /wire_drawdown_requests">client.wire_drawdown_requests.<a href="./src/increase/resources/wire_drawdown_requests.py">create</a>(\*\*<a href="src/increase/types/wire_drawdown_request_create_params.py">params</a>) -> <a href="./src/increase/types/wire_drawdown_request.py">WireDrawdownRequest</a></code>
- <code title="get /wire_drawdown_requests/{wire_drawdown_request_id}">client.wire_drawdown_requests.<a href="./src/increase/resources/wire_drawdown_requests.py">retrieve</a>(wire_drawdown_request_id) -> <a href="./src/increase/types/wire_drawdown_request.py">WireDrawdownRequest</a></code>
- <code title="get /wire_drawdown_requests">client.wire_drawdown_requests.<a href="./src/increase/resources/wire_drawdown_requests.py">list</a>(\*\*<a href="src/increase/types/wire_drawdown_request_list_params.py">params</a>) -> <a href="./src/increase/types/wire_drawdown_request.py">SyncPage[WireDrawdownRequest]</a></code>

# InboundWireDrawdownRequests

Types:

```python
from increase.types import InboundWireDrawdownRequest
```

Methods:

- <code title="get /inbound_wire_drawdown_requests/{inbound_wire_drawdown_request_id}">client.inbound_wire_drawdown_requests.<a href="./src/increase/resources/inbound_wire_drawdown_requests.py">retrieve</a>(inbound_wire_drawdown_request_id) -> <a href="./src/increase/types/inbound_wire_drawdown_request.py">InboundWireDrawdownRequest</a></code>
- <code title="get /inbound_wire_drawdown_requests">client.inbound_wire_drawdown_requests.<a href="./src/increase/resources/inbound_wire_drawdown_requests.py">list</a>(\*\*<a href="src/increase/types/inbound_wire_drawdown_request_list_params.py">params</a>) -> <a href="./src/increase/types/inbound_wire_drawdown_request.py">SyncPage[InboundWireDrawdownRequest]</a></code>

# CheckTransfers

Types:

```python
from increase.types import CheckTransfer
```

Methods:

- <code title="post /check_transfers">client.check_transfers.<a href="./src/increase/resources/check_transfers.py">create</a>(\*\*<a href="src/increase/types/check_transfer_create_params.py">params</a>) -> <a href="./src/increase/types/check_transfer.py">CheckTransfer</a></code>
- <code title="get /check_transfers/{check_transfer_id}">client.check_transfers.<a href="./src/increase/resources/check_transfers.py">retrieve</a>(check_transfer_id) -> <a href="./src/increase/types/check_transfer.py">CheckTransfer</a></code>
- <code title="get /check_transfers">client.check_transfers.<a href="./src/increase/resources/check_transfers.py">list</a>(\*\*<a href="src/increase/types/check_transfer_list_params.py">params</a>) -> <a href="./src/increase/types/check_transfer.py">SyncPage[CheckTransfer]</a></code>
- <code title="post /check_transfers/{check_transfer_id}/approve">client.check_transfers.<a href="./src/increase/resources/check_transfers.py">approve</a>(check_transfer_id) -> <a href="./src/increase/types/check_transfer.py">CheckTransfer</a></code>
- <code title="post /check_transfers/{check_transfer_id}/cancel">client.check_transfers.<a href="./src/increase/resources/check_transfers.py">cancel</a>(check_transfer_id) -> <a href="./src/increase/types/check_transfer.py">CheckTransfer</a></code>
- <code title="post /check_transfers/{check_transfer_id}/stop_payment">client.check_transfers.<a href="./src/increase/resources/check_transfers.py">stop_payment</a>(check_transfer_id, \*\*<a href="src/increase/types/check_transfer_stop_payment_params.py">params</a>) -> <a href="./src/increase/types/check_transfer.py">CheckTransfer</a></code>

# InboundCheckDeposits

Types:

```python
from increase.types import InboundCheckDeposit
```

Methods:

- <code title="get /inbound_check_deposits/{inbound_check_deposit_id}">client.inbound_check_deposits.<a href="./src/increase/resources/inbound_check_deposits.py">retrieve</a>(inbound_check_deposit_id) -> <a href="./src/increase/types/inbound_check_deposit.py">InboundCheckDeposit</a></code>
- <code title="get /inbound_check_deposits">client.inbound_check_deposits.<a href="./src/increase/resources/inbound_check_deposits.py">list</a>(\*\*<a href="src/increase/types/inbound_check_deposit_list_params.py">params</a>) -> <a href="./src/increase/types/inbound_check_deposit.py">SyncPage[InboundCheckDeposit]</a></code>
- <code title="post /inbound_check_deposits/{inbound_check_deposit_id}/decline">client.inbound_check_deposits.<a href="./src/increase/resources/inbound_check_deposits.py">decline</a>(inbound_check_deposit_id) -> <a href="./src/increase/types/inbound_check_deposit.py">InboundCheckDeposit</a></code>
- <code title="post /inbound_check_deposits/{inbound_check_deposit_id}/return">client.inbound*check_deposits.<a href="./src/increase/resources/inbound_check_deposits.py">return*</a>(inbound_check_deposit_id, \*\*<a href="src/increase/types/inbound_check_deposit_return_params.py">params</a>) -> <a href="./src/increase/types/inbound_check_deposit.py">InboundCheckDeposit</a></code>

# RealTimePaymentsTransfers

Types:

```python
from increase.types import RealTimePaymentsTransfer
```

Methods:

- <code title="post /real_time_payments_transfers">client.real_time_payments_transfers.<a href="./src/increase/resources/real_time_payments_transfers.py">create</a>(\*\*<a href="src/increase/types/real_time_payments_transfer_create_params.py">params</a>) -> <a href="./src/increase/types/real_time_payments_transfer.py">RealTimePaymentsTransfer</a></code>
- <code title="get /real_time_payments_transfers/{real_time_payments_transfer_id}">client.real_time_payments_transfers.<a href="./src/increase/resources/real_time_payments_transfers.py">retrieve</a>(real_time_payments_transfer_id) -> <a href="./src/increase/types/real_time_payments_transfer.py">RealTimePaymentsTransfer</a></code>
- <code title="get /real_time_payments_transfers">client.real_time_payments_transfers.<a href="./src/increase/resources/real_time_payments_transfers.py">list</a>(\*\*<a href="src/increase/types/real_time_payments_transfer_list_params.py">params</a>) -> <a href="./src/increase/types/real_time_payments_transfer.py">SyncPage[RealTimePaymentsTransfer]</a></code>
- <code title="post /real_time_payments_transfers/{real_time_payments_transfer_id}/approve">client.real_time_payments_transfers.<a href="./src/increase/resources/real_time_payments_transfers.py">approve</a>(real_time_payments_transfer_id) -> <a href="./src/increase/types/real_time_payments_transfer.py">RealTimePaymentsTransfer</a></code>
- <code title="post /real_time_payments_transfers/{real_time_payments_transfer_id}/cancel">client.real_time_payments_transfers.<a href="./src/increase/resources/real_time_payments_transfers.py">cancel</a>(real_time_payments_transfer_id) -> <a href="./src/increase/types/real_time_payments_transfer.py">RealTimePaymentsTransfer</a></code>

# InboundRealTimePaymentsTransfers

Types:

```python
from increase.types import InboundRealTimePaymentsTransfer
```

Methods:

- <code title="get /inbound_real_time_payments_transfers/{inbound_real_time_payments_transfer_id}">client.inbound_real_time_payments_transfers.<a href="./src/increase/resources/inbound_real_time_payments_transfers.py">retrieve</a>(inbound_real_time_payments_transfer_id) -> <a href="./src/increase/types/inbound_real_time_payments_transfer.py">InboundRealTimePaymentsTransfer</a></code>
- <code title="get /inbound_real_time_payments_transfers">client.inbound_real_time_payments_transfers.<a href="./src/increase/resources/inbound_real_time_payments_transfers.py">list</a>(\*\*<a href="src/increase/types/inbound_real_time_payments_transfer_list_params.py">params</a>) -> <a href="./src/increase/types/inbound_real_time_payments_transfer.py">SyncPage[InboundRealTimePaymentsTransfer]</a></code>

# CheckDeposits

Types:

```python
from increase.types import CheckDeposit
```

Methods:

- <code title="post /check_deposits">client.check_deposits.<a href="./src/increase/resources/check_deposits.py">create</a>(\*\*<a href="src/increase/types/check_deposit_create_params.py">params</a>) -> <a href="./src/increase/types/check_deposit.py">CheckDeposit</a></code>
- <code title="get /check_deposits/{check_deposit_id}">client.check_deposits.<a href="./src/increase/resources/check_deposits.py">retrieve</a>(check_deposit_id) -> <a href="./src/increase/types/check_deposit.py">CheckDeposit</a></code>
- <code title="get /check_deposits">client.check_deposits.<a href="./src/increase/resources/check_deposits.py">list</a>(\*\*<a href="src/increase/types/check_deposit_list_params.py">params</a>) -> <a href="./src/increase/types/check_deposit.py">SyncPage[CheckDeposit]</a></code>

# Lockboxes

Types:

```python
from increase.types import Lockbox
```

Methods:

- <code title="post /lockboxes">client.lockboxes.<a href="./src/increase/resources/lockboxes.py">create</a>(\*\*<a href="src/increase/types/lockbox_create_params.py">params</a>) -> <a href="./src/increase/types/lockbox.py">Lockbox</a></code>
- <code title="get /lockboxes/{lockbox_id}">client.lockboxes.<a href="./src/increase/resources/lockboxes.py">retrieve</a>(lockbox_id) -> <a href="./src/increase/types/lockbox.py">Lockbox</a></code>
- <code title="patch /lockboxes/{lockbox_id}">client.lockboxes.<a href="./src/increase/resources/lockboxes.py">update</a>(lockbox_id, \*\*<a href="src/increase/types/lockbox_update_params.py">params</a>) -> <a href="./src/increase/types/lockbox.py">Lockbox</a></code>
- <code title="get /lockboxes">client.lockboxes.<a href="./src/increase/resources/lockboxes.py">list</a>(\*\*<a href="src/increase/types/lockbox_list_params.py">params</a>) -> <a href="./src/increase/types/lockbox.py">SyncPage[Lockbox]</a></code>

# InboundMailItems

Types:

```python
from increase.types import InboundMailItem
```

Methods:

- <code title="get /inbound_mail_items/{inbound_mail_item_id}">client.inbound_mail_items.<a href="./src/increase/resources/inbound_mail_items.py">retrieve</a>(inbound_mail_item_id) -> <a href="./src/increase/types/inbound_mail_item.py">InboundMailItem</a></code>
- <code title="get /inbound_mail_items">client.inbound_mail_items.<a href="./src/increase/resources/inbound_mail_items.py">list</a>(\*\*<a href="src/increase/types/inbound_mail_item_list_params.py">params</a>) -> <a href="./src/increase/types/inbound_mail_item.py">SyncPage[InboundMailItem]</a></code>

# RoutingNumbers

Types:

```python
from increase.types import RoutingNumberListResponse
```

Methods:

- <code title="get /routing_numbers">client.routing_numbers.<a href="./src/increase/resources/routing_numbers.py">list</a>(\*\*<a href="src/increase/types/routing_number_list_params.py">params</a>) -> <a href="./src/increase/types/routing_number_list_response.py">SyncPage[RoutingNumberListResponse]</a></code>

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

# Entities

Types:

```python
from increase.types import Entity
```

Methods:

- <code title="post /entities">client.entities.<a href="./src/increase/resources/entities.py">create</a>(\*\*<a href="src/increase/types/entity_create_params.py">params</a>) -> <a href="./src/increase/types/entity.py">Entity</a></code>
- <code title="get /entities/{entity_id}">client.entities.<a href="./src/increase/resources/entities.py">retrieve</a>(entity_id) -> <a href="./src/increase/types/entity.py">Entity</a></code>
- <code title="get /entities">client.entities.<a href="./src/increase/resources/entities.py">list</a>(\*\*<a href="src/increase/types/entity_list_params.py">params</a>) -> <a href="./src/increase/types/entity.py">SyncPage[Entity]</a></code>
- <code title="post /entities/{entity_id}/archive">client.entities.<a href="./src/increase/resources/entities.py">archive</a>(entity_id) -> <a href="./src/increase/types/entity.py">Entity</a></code>
- <code title="post /entities/{entity_id}/archive_beneficial_owner">client.entities.<a href="./src/increase/resources/entities.py">archive_beneficial_owner</a>(entity_id, \*\*<a href="src/increase/types/entity_archive_beneficial_owner_params.py">params</a>) -> <a href="./src/increase/types/entity.py">Entity</a></code>
- <code title="post /entities/{entity_id}/confirm">client.entities.<a href="./src/increase/resources/entities.py">confirm</a>(entity_id, \*\*<a href="src/increase/types/entity_confirm_params.py">params</a>) -> <a href="./src/increase/types/entity.py">Entity</a></code>
- <code title="post /entities/{entity_id}/create_beneficial_owner">client.entities.<a href="./src/increase/resources/entities.py">create_beneficial_owner</a>(entity_id, \*\*<a href="src/increase/types/entity_create_beneficial_owner_params.py">params</a>) -> <a href="./src/increase/types/entity.py">Entity</a></code>
- <code title="post /entities/{entity_id}/update_address">client.entities.<a href="./src/increase/resources/entities.py">update_address</a>(entity_id, \*\*<a href="src/increase/types/entity_update_address_params.py">params</a>) -> <a href="./src/increase/types/entity.py">Entity</a></code>
- <code title="post /entities/{entity_id}/update_beneficial_owner_address">client.entities.<a href="./src/increase/resources/entities.py">update_beneficial_owner_address</a>(entity_id, \*\*<a href="src/increase/types/entity_update_beneficial_owner_address_params.py">params</a>) -> <a href="./src/increase/types/entity.py">Entity</a></code>
- <code title="post /entities/{entity_id}/update_industry_code">client.entities.<a href="./src/increase/resources/entities.py">update_industry_code</a>(entity_id, \*\*<a href="src/increase/types/entity_update_industry_code_params.py">params</a>) -> <a href="./src/increase/types/entity.py">Entity</a></code>

# SupplementalDocuments

Types:

```python
from increase.types import EntitySupplementalDocument
```

Methods:

- <code title="post /entity_supplemental_documents">client.supplemental_documents.<a href="./src/increase/resources/supplemental_documents.py">create</a>(\*\*<a href="src/increase/types/supplemental_document_create_params.py">params</a>) -> <a href="./src/increase/types/entity_supplemental_document.py">EntitySupplementalDocument</a></code>
- <code title="get /entity_supplemental_documents">client.supplemental_documents.<a href="./src/increase/resources/supplemental_documents.py">list</a>(\*\*<a href="src/increase/types/supplemental_document_list_params.py">params</a>) -> <a href="./src/increase/types/entity_supplemental_document.py">SyncPage[EntitySupplementalDocument]</a></code>

# Programs

Types:

```python
from increase.types import Program
```

Methods:

- <code title="get /programs/{program_id}">client.programs.<a href="./src/increase/resources/programs.py">retrieve</a>(program_id) -> <a href="./src/increase/types/program.py">Program</a></code>
- <code title="get /programs">client.programs.<a href="./src/increase/resources/programs.py">list</a>(\*\*<a href="src/increase/types/program_list_params.py">params</a>) -> <a href="./src/increase/types/program.py">SyncPage[Program]</a></code>

# AccountStatements

Types:

```python
from increase.types import AccountStatement
```

Methods:

- <code title="get /account_statements/{account_statement_id}">client.account_statements.<a href="./src/increase/resources/account_statements.py">retrieve</a>(account_statement_id) -> <a href="./src/increase/types/account_statement.py">AccountStatement</a></code>
- <code title="get /account_statements">client.account_statements.<a href="./src/increase/resources/account_statements.py">list</a>(\*\*<a href="src/increase/types/account_statement_list_params.py">params</a>) -> <a href="./src/increase/types/account_statement.py">SyncPage[AccountStatement]</a></code>

# Files

Types:

```python
from increase.types import File
```

Methods:

- <code title="post /files">client.files.<a href="./src/increase/resources/files.py">create</a>(\*\*<a href="src/increase/types/file_create_params.py">params</a>) -> <a href="./src/increase/types/file.py">File</a></code>
- <code title="get /files/{file_id}">client.files.<a href="./src/increase/resources/files.py">retrieve</a>(file_id) -> <a href="./src/increase/types/file.py">File</a></code>
- <code title="get /files">client.files.<a href="./src/increase/resources/files.py">list</a>(\*\*<a href="src/increase/types/file_list_params.py">params</a>) -> <a href="./src/increase/types/file.py">SyncPage[File]</a></code>

# FileLinks

Types:

```python
from increase.types import FileLink
```

Methods:

- <code title="post /file_links">client.file_links.<a href="./src/increase/resources/file_links.py">create</a>(\*\*<a href="src/increase/types/file_link_create_params.py">params</a>) -> <a href="./src/increase/types/file_link.py">FileLink</a></code>

# Documents

Types:

```python
from increase.types import Document
```

Methods:

- <code title="post /documents">client.documents.<a href="./src/increase/resources/documents.py">create</a>(\*\*<a href="src/increase/types/document_create_params.py">params</a>) -> <a href="./src/increase/types/document.py">Document</a></code>
- <code title="get /documents/{document_id}">client.documents.<a href="./src/increase/resources/documents.py">retrieve</a>(document_id) -> <a href="./src/increase/types/document.py">Document</a></code>
- <code title="get /documents">client.documents.<a href="./src/increase/resources/documents.py">list</a>(\*\*<a href="src/increase/types/document_list_params.py">params</a>) -> <a href="./src/increase/types/document.py">SyncPage[Document]</a></code>

# Exports

Types:

```python
from increase.types import Export
```

Methods:

- <code title="post /exports">client.exports.<a href="./src/increase/resources/exports.py">create</a>(\*\*<a href="src/increase/types/export_create_params.py">params</a>) -> <a href="./src/increase/types/export.py">Export</a></code>
- <code title="get /exports/{export_id}">client.exports.<a href="./src/increase/resources/exports.py">retrieve</a>(export_id) -> <a href="./src/increase/types/export.py">Export</a></code>
- <code title="get /exports">client.exports.<a href="./src/increase/resources/exports.py">list</a>(\*\*<a href="src/increase/types/export_list_params.py">params</a>) -> <a href="./src/increase/types/export.py">SyncPage[Export]</a></code>

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

# RealTimeDecisions

Types:

```python
from increase.types import RealTimeDecision
```

Methods:

- <code title="get /real_time_decisions/{real_time_decision_id}">client.real_time_decisions.<a href="./src/increase/resources/real_time_decisions.py">retrieve</a>(real_time_decision_id) -> <a href="./src/increase/types/real_time_decision.py">RealTimeDecision</a></code>
- <code title="post /real_time_decisions/{real_time_decision_id}/action">client.real_time_decisions.<a href="./src/increase/resources/real_time_decisions.py">action</a>(real_time_decision_id, \*\*<a href="src/increase/types/real_time_decision_action_params.py">params</a>) -> <a href="./src/increase/types/real_time_decision.py">RealTimeDecision</a></code>

# BookkeepingAccounts

Types:

```python
from increase.types import BookkeepingAccount, BookkeepingBalanceLookup
```

Methods:

- <code title="post /bookkeeping_accounts">client.bookkeeping_accounts.<a href="./src/increase/resources/bookkeeping_accounts.py">create</a>(\*\*<a href="src/increase/types/bookkeeping_account_create_params.py">params</a>) -> <a href="./src/increase/types/bookkeeping_account.py">BookkeepingAccount</a></code>
- <code title="patch /bookkeeping_accounts/{bookkeeping_account_id}">client.bookkeeping_accounts.<a href="./src/increase/resources/bookkeeping_accounts.py">update</a>(bookkeeping_account_id, \*\*<a href="src/increase/types/bookkeeping_account_update_params.py">params</a>) -> <a href="./src/increase/types/bookkeeping_account.py">BookkeepingAccount</a></code>
- <code title="get /bookkeeping_accounts">client.bookkeeping_accounts.<a href="./src/increase/resources/bookkeeping_accounts.py">list</a>(\*\*<a href="src/increase/types/bookkeeping_account_list_params.py">params</a>) -> <a href="./src/increase/types/bookkeeping_account.py">SyncPage[BookkeepingAccount]</a></code>
- <code title="get /bookkeeping_accounts/{bookkeeping_account_id}/balance">client.bookkeeping_accounts.<a href="./src/increase/resources/bookkeeping_accounts.py">balance</a>(bookkeeping_account_id, \*\*<a href="src/increase/types/bookkeeping_account_balance_params.py">params</a>) -> <a href="./src/increase/types/bookkeeping_balance_lookup.py">BookkeepingBalanceLookup</a></code>

# BookkeepingEntrySets

Types:

```python
from increase.types import BookkeepingEntrySet
```

Methods:

- <code title="post /bookkeeping_entry_sets">client.bookkeeping_entry_sets.<a href="./src/increase/resources/bookkeeping_entry_sets.py">create</a>(\*\*<a href="src/increase/types/bookkeeping_entry_set_create_params.py">params</a>) -> <a href="./src/increase/types/bookkeeping_entry_set.py">BookkeepingEntrySet</a></code>
- <code title="get /bookkeeping_entry_sets/{bookkeeping_entry_set_id}">client.bookkeeping_entry_sets.<a href="./src/increase/resources/bookkeeping_entry_sets.py">retrieve</a>(bookkeeping_entry_set_id) -> <a href="./src/increase/types/bookkeeping_entry_set.py">BookkeepingEntrySet</a></code>
- <code title="get /bookkeeping_entry_sets">client.bookkeeping_entry_sets.<a href="./src/increase/resources/bookkeeping_entry_sets.py">list</a>(\*\*<a href="src/increase/types/bookkeeping_entry_set_list_params.py">params</a>) -> <a href="./src/increase/types/bookkeeping_entry_set.py">SyncPage[BookkeepingEntrySet]</a></code>

# BookkeepingEntries

Types:

```python
from increase.types import BookkeepingEntry
```

Methods:

- <code title="get /bookkeeping_entries/{bookkeeping_entry_id}">client.bookkeeping_entries.<a href="./src/increase/resources/bookkeeping_entries.py">retrieve</a>(bookkeeping_entry_id) -> <a href="./src/increase/types/bookkeeping_entry.py">BookkeepingEntry</a></code>
- <code title="get /bookkeeping_entries">client.bookkeeping_entries.<a href="./src/increase/resources/bookkeeping_entries.py">list</a>(\*\*<a href="src/increase/types/bookkeeping_entry_list_params.py">params</a>) -> <a href="./src/increase/types/bookkeeping_entry.py">SyncPage[BookkeepingEntry]</a></code>

# Groups

Types:

```python
from increase.types import Group
```

Methods:

- <code title="get /groups/current">client.groups.<a href="./src/increase/resources/groups.py">retrieve</a>() -> <a href="./src/increase/types/group.py">Group</a></code>

# OAuthApplications

Types:

```python
from increase.types import OAuthApplication
```

Methods:

- <code title="get /oauth_applications/{oauth_application_id}">client.oauth_applications.<a href="./src/increase/resources/oauth_applications.py">retrieve</a>(oauth_application_id) -> <a href="./src/increase/types/oauth_application.py">OAuthApplication</a></code>
- <code title="get /oauth_applications">client.oauth_applications.<a href="./src/increase/resources/oauth_applications.py">list</a>(\*\*<a href="src/increase/types/oauth_application_list_params.py">params</a>) -> <a href="./src/increase/types/oauth_application.py">SyncPage[OAuthApplication]</a></code>

# OAuthConnections

Types:

```python
from increase.types import OAuthConnection
```

Methods:

- <code title="get /oauth_connections/{oauth_connection_id}">client.oauth_connections.<a href="./src/increase/resources/oauth_connections.py">retrieve</a>(oauth_connection_id) -> <a href="./src/increase/types/oauth_connection.py">OAuthConnection</a></code>
- <code title="get /oauth_connections">client.oauth_connections.<a href="./src/increase/resources/oauth_connections.py">list</a>(\*\*<a href="src/increase/types/oauth_connection_list_params.py">params</a>) -> <a href="./src/increase/types/oauth_connection.py">SyncPage[OAuthConnection]</a></code>

# OAuthTokens

Types:

```python
from increase.types import OAuthToken
```

Methods:

- <code title="post /oauth/tokens">client.oauth_tokens.<a href="./src/increase/resources/oauth_tokens.py">create</a>(\*\*<a href="src/increase/types/oauth_token_create_params.py">params</a>) -> <a href="./src/increase/types/oauth_token.py">OAuthToken</a></code>

# IntrafiAccountEnrollments

Types:

```python
from increase.types import IntrafiAccountEnrollment
```

Methods:

- <code title="post /intrafi_account_enrollments">client.intrafi_account_enrollments.<a href="./src/increase/resources/intrafi_account_enrollments.py">create</a>(\*\*<a href="src/increase/types/intrafi_account_enrollment_create_params.py">params</a>) -> <a href="./src/increase/types/intrafi_account_enrollment.py">IntrafiAccountEnrollment</a></code>
- <code title="get /intrafi_account_enrollments/{intrafi_account_enrollment_id}">client.intrafi_account_enrollments.<a href="./src/increase/resources/intrafi_account_enrollments.py">retrieve</a>(intrafi_account_enrollment_id) -> <a href="./src/increase/types/intrafi_account_enrollment.py">IntrafiAccountEnrollment</a></code>
- <code title="get /intrafi_account_enrollments">client.intrafi_account_enrollments.<a href="./src/increase/resources/intrafi_account_enrollments.py">list</a>(\*\*<a href="src/increase/types/intrafi_account_enrollment_list_params.py">params</a>) -> <a href="./src/increase/types/intrafi_account_enrollment.py">SyncPage[IntrafiAccountEnrollment]</a></code>
- <code title="post /intrafi_account_enrollments/{intrafi_account_enrollment_id}/unenroll">client.intrafi_account_enrollments.<a href="./src/increase/resources/intrafi_account_enrollments.py">unenroll</a>(intrafi_account_enrollment_id) -> <a href="./src/increase/types/intrafi_account_enrollment.py">IntrafiAccountEnrollment</a></code>

# IntrafiBalances

Types:

```python
from increase.types import IntrafiBalance
```

Methods:

- <code title="get /accounts/{account_id}/intrafi_balance">client.intrafi_balances.<a href="./src/increase/resources/intrafi_balances.py">intrafi_balance</a>(account_id) -> <a href="./src/increase/types/intrafi_balance.py">IntrafiBalance</a></code>

# IntrafiExclusions

Types:

```python
from increase.types import IntrafiExclusion
```

Methods:

- <code title="post /intrafi_exclusions">client.intrafi_exclusions.<a href="./src/increase/resources/intrafi_exclusions.py">create</a>(\*\*<a href="src/increase/types/intrafi_exclusion_create_params.py">params</a>) -> <a href="./src/increase/types/intrafi_exclusion.py">IntrafiExclusion</a></code>
- <code title="get /intrafi_exclusions/{intrafi_exclusion_id}">client.intrafi_exclusions.<a href="./src/increase/resources/intrafi_exclusions.py">retrieve</a>(intrafi_exclusion_id) -> <a href="./src/increase/types/intrafi_exclusion.py">IntrafiExclusion</a></code>
- <code title="get /intrafi_exclusions">client.intrafi_exclusions.<a href="./src/increase/resources/intrafi_exclusions.py">list</a>(\*\*<a href="src/increase/types/intrafi_exclusion_list_params.py">params</a>) -> <a href="./src/increase/types/intrafi_exclusion.py">SyncPage[IntrafiExclusion]</a></code>
- <code title="post /intrafi_exclusions/{intrafi_exclusion_id}/archive">client.intrafi_exclusions.<a href="./src/increase/resources/intrafi_exclusions.py">archive</a>(intrafi_exclusion_id) -> <a href="./src/increase/types/intrafi_exclusion.py">IntrafiExclusion</a></code>

# Webhooks

Methods:

- <code>client.webhooks.<a href="./src/increase/resources/webhooks.py">unwrap</a>(\*args) -> object</code>
- <code>client.webhooks.<a href="./src/increase/resources/webhooks.py">verify_signature</a>(\*args) -> None</code>

# CardTokens

Types:

```python
from increase.types import CardToken, CardTokenCapabilities
```

Methods:

- <code title="get /card_tokens/{card_token_id}">client.card_tokens.<a href="./src/increase/resources/card_tokens.py">retrieve</a>(card_token_id) -> <a href="./src/increase/types/card_token.py">CardToken</a></code>
- <code title="get /card_tokens">client.card_tokens.<a href="./src/increase/resources/card_tokens.py">list</a>(\*\*<a href="src/increase/types/card_token_list_params.py">params</a>) -> <a href="./src/increase/types/card_token.py">SyncPage[CardToken]</a></code>
- <code title="get /card_tokens/{card_token_id}/capabilities">client.card_tokens.<a href="./src/increase/resources/card_tokens.py">capabilities</a>(card_token_id) -> <a href="./src/increase/types/card_token_capabilities.py">CardTokenCapabilities</a></code>

# CardPushTransfers

Types:

```python
from increase.types import CardPushTransfer
```

Methods:

- <code title="post /card_push_transfers">client.card_push_transfers.<a href="./src/increase/resources/card_push_transfers.py">create</a>(\*\*<a href="src/increase/types/card_push_transfer_create_params.py">params</a>) -> <a href="./src/increase/types/card_push_transfer.py">CardPushTransfer</a></code>
- <code title="get /card_push_transfers/{card_push_transfer_id}">client.card_push_transfers.<a href="./src/increase/resources/card_push_transfers.py">retrieve</a>(card_push_transfer_id) -> <a href="./src/increase/types/card_push_transfer.py">CardPushTransfer</a></code>
- <code title="get /card_push_transfers">client.card_push_transfers.<a href="./src/increase/resources/card_push_transfers.py">list</a>(\*\*<a href="src/increase/types/card_push_transfer_list_params.py">params</a>) -> <a href="./src/increase/types/card_push_transfer.py">SyncPage[CardPushTransfer]</a></code>
- <code title="post /card_push_transfers/{card_push_transfer_id}/approve">client.card_push_transfers.<a href="./src/increase/resources/card_push_transfers.py">approve</a>(card_push_transfer_id) -> <a href="./src/increase/types/card_push_transfer.py">CardPushTransfer</a></code>
- <code title="post /card_push_transfers/{card_push_transfer_id}/cancel">client.card_push_transfers.<a href="./src/increase/resources/card_push_transfers.py">cancel</a>(card_push_transfer_id) -> <a href="./src/increase/types/card_push_transfer.py">CardPushTransfer</a></code>

# CardValidations

Types:

```python
from increase.types import CardValidation
```

Methods:

- <code title="post /card_validations">client.card_validations.<a href="./src/increase/resources/card_validations.py">create</a>(\*\*<a href="src/increase/types/card_validation_create_params.py">params</a>) -> <a href="./src/increase/types/card_validation.py">CardValidation</a></code>
- <code title="get /card_validations/{card_validation_id}">client.card_validations.<a href="./src/increase/resources/card_validations.py">retrieve</a>(card_validation_id) -> <a href="./src/increase/types/card_validation.py">CardValidation</a></code>
- <code title="get /card_validations">client.card_validations.<a href="./src/increase/resources/card_validations.py">list</a>(\*\*<a href="src/increase/types/card_validation_list_params.py">params</a>) -> <a href="./src/increase/types/card_validation.py">SyncPage[CardValidation]</a></code>

# Simulations

## InterestPayments

Methods:

- <code title="post /simulations/interest_payments">client.simulations.interest_payments.<a href="./src/increase/resources/simulations/interest_payments.py">create</a>(\*\*<a href="src/increase/types/simulations/interest_payment_create_params.py">params</a>) -> <a href="./src/increase/types/transaction.py">Transaction</a></code>

## CardAuthorizations

Types:

```python
from increase.types.simulations import CardAuthorizationCreateResponse
```

Methods:

- <code title="post /simulations/card_authorizations">client.simulations.card_authorizations.<a href="./src/increase/resources/simulations/card_authorizations.py">create</a>(\*\*<a href="src/increase/types/simulations/card_authorization_create_params.py">params</a>) -> <a href="./src/increase/types/simulations/card_authorization_create_response.py">CardAuthorizationCreateResponse</a></code>

## CardAuthorizationExpirations

Methods:

- <code title="post /simulations/card_authorization_expirations">client.simulations.card_authorization_expirations.<a href="./src/increase/resources/simulations/card_authorization_expirations.py">create</a>(\*\*<a href="src/increase/types/simulations/card_authorization_expiration_create_params.py">params</a>) -> <a href="./src/increase/types/card_payment.py">CardPayment</a></code>

## CardSettlements

Methods:

- <code title="post /simulations/card_settlements">client.simulations.card_settlements.<a href="./src/increase/resources/simulations/card_settlements.py">create</a>(\*\*<a href="src/increase/types/simulations/card_settlement_create_params.py">params</a>) -> <a href="./src/increase/types/transaction.py">Transaction</a></code>

## CardReversals

Methods:

- <code title="post /simulations/card_reversals">client.simulations.card_reversals.<a href="./src/increase/resources/simulations/card_reversals.py">create</a>(\*\*<a href="src/increase/types/simulations/card_reversal_create_params.py">params</a>) -> <a href="./src/increase/types/card_payment.py">CardPayment</a></code>

## CardIncrements

Methods:

- <code title="post /simulations/card_increments">client.simulations.card_increments.<a href="./src/increase/resources/simulations/card_increments.py">create</a>(\*\*<a href="src/increase/types/simulations/card_increment_create_params.py">params</a>) -> <a href="./src/increase/types/card_payment.py">CardPayment</a></code>

## CardFuelConfirmations

Methods:

- <code title="post /simulations/card_fuel_confirmations">client.simulations.card_fuel_confirmations.<a href="./src/increase/resources/simulations/card_fuel_confirmations.py">create</a>(\*\*<a href="src/increase/types/simulations/card_fuel_confirmation_create_params.py">params</a>) -> <a href="./src/increase/types/card_payment.py">CardPayment</a></code>

## CardRefunds

Methods:

- <code title="post /simulations/card_refunds">client.simulations.card_refunds.<a href="./src/increase/resources/simulations/card_refunds.py">create</a>(\*\*<a href="src/increase/types/simulations/card_refund_create_params.py">params</a>) -> <a href="./src/increase/types/transaction.py">Transaction</a></code>

## CardDisputes

Methods:

- <code title="post /simulations/card_disputes/{card_dispute_id}/action">client.simulations.card_disputes.<a href="./src/increase/resources/simulations/card_disputes.py">action</a>(card_dispute_id, \*\*<a href="src/increase/types/simulations/card_dispute_action_params.py">params</a>) -> <a href="./src/increase/types/card_dispute.py">CardDispute</a></code>

## PhysicalCards

Methods:

- <code title="post /simulations/physical_cards/{physical_card_id}/advance_shipment">client.simulations.physical_cards.<a href="./src/increase/resources/simulations/physical_cards.py">advance_shipment</a>(physical_card_id, \*\*<a href="src/increase/types/simulations/physical_card_advance_shipment_params.py">params</a>) -> <a href="./src/increase/types/physical_card.py">PhysicalCard</a></code>
- <code title="post /simulations/physical_cards/{physical_card_id}/tracking_updates">client.simulations.physical_cards.<a href="./src/increase/resources/simulations/physical_cards.py">tracking_updates</a>(physical_card_id, \*\*<a href="src/increase/types/simulations/physical_card_tracking_updates_params.py">params</a>) -> <a href="./src/increase/types/physical_card.py">PhysicalCard</a></code>

## DigitalWalletTokenRequests

Types:

```python
from increase.types.simulations import DigitalWalletTokenRequestCreateResponse
```

Methods:

- <code title="post /simulations/digital_wallet_token_requests">client.simulations.digital_wallet_token_requests.<a href="./src/increase/resources/simulations/digital_wallet_token_requests.py">create</a>(\*\*<a href="src/increase/types/simulations/digital_wallet_token_request_create_params.py">params</a>) -> <a href="./src/increase/types/simulations/digital_wallet_token_request_create_response.py">DigitalWalletTokenRequestCreateResponse</a></code>

## PendingTransactions

Methods:

- <code title="post /simulations/pending_transactions/{pending_transaction_id}/release_inbound_funds_hold">client.simulations.pending_transactions.<a href="./src/increase/resources/simulations/pending_transactions.py">release_inbound_funds_hold</a>(pending_transaction_id) -> <a href="./src/increase/types/pending_transaction.py">PendingTransaction</a></code>

## AccountTransfers

Methods:

- <code title="post /simulations/account_transfers/{account_transfer_id}/complete">client.simulations.account_transfers.<a href="./src/increase/resources/simulations/account_transfers.py">complete</a>(account_transfer_id) -> <a href="./src/increase/types/account_transfer.py">AccountTransfer</a></code>

## ACHTransfers

Methods:

- <code title="post /simulations/ach_transfers/{ach_transfer_id}/acknowledge">client.simulations.ach_transfers.<a href="./src/increase/resources/simulations/ach_transfers.py">acknowledge</a>(ach_transfer_id) -> <a href="./src/increase/types/ach_transfer.py">ACHTransfer</a></code>
- <code title="post /simulations/ach_transfers/{ach_transfer_id}/create_notification_of_change">client.simulations.ach_transfers.<a href="./src/increase/resources/simulations/ach_transfers.py">create_notification_of_change</a>(ach_transfer_id, \*\*<a href="src/increase/types/simulations/ach_transfer_create_notification_of_change_params.py">params</a>) -> <a href="./src/increase/types/ach_transfer.py">ACHTransfer</a></code>
- <code title="post /simulations/ach_transfers/{ach_transfer_id}/return">client.simulations.ach*transfers.<a href="./src/increase/resources/simulations/ach_transfers.py">return*</a>(ach_transfer_id, \*\*<a href="src/increase/types/simulations/ach_transfer_return_params.py">params</a>) -> <a href="./src/increase/types/ach_transfer.py">ACHTransfer</a></code>
- <code title="post /simulations/ach_transfers/{ach_transfer_id}/settle">client.simulations.ach_transfers.<a href="./src/increase/resources/simulations/ach_transfers.py">settle</a>(ach_transfer_id) -> <a href="./src/increase/types/ach_transfer.py">ACHTransfer</a></code>
- <code title="post /simulations/ach_transfers/{ach_transfer_id}/submit">client.simulations.ach_transfers.<a href="./src/increase/resources/simulations/ach_transfers.py">submit</a>(ach_transfer_id) -> <a href="./src/increase/types/ach_transfer.py">ACHTransfer</a></code>

## InboundACHTransfers

Methods:

- <code title="post /simulations/inbound_ach_transfers">client.simulations.inbound_ach_transfers.<a href="./src/increase/resources/simulations/inbound_ach_transfers.py">create</a>(\*\*<a href="src/increase/types/simulations/inbound_ach_transfer_create_params.py">params</a>) -> <a href="./src/increase/types/inbound_ach_transfer.py">InboundACHTransfer</a></code>

## WireTransfers

Methods:

- <code title="post /simulations/wire_transfers/{wire_transfer_id}/reverse">client.simulations.wire_transfers.<a href="./src/increase/resources/simulations/wire_transfers.py">reverse</a>(wire_transfer_id) -> <a href="./src/increase/types/wire_transfer.py">WireTransfer</a></code>
- <code title="post /simulations/wire_transfers/{wire_transfer_id}/submit">client.simulations.wire_transfers.<a href="./src/increase/resources/simulations/wire_transfers.py">submit</a>(wire_transfer_id) -> <a href="./src/increase/types/wire_transfer.py">WireTransfer</a></code>

## InboundWireTransfers

Methods:

- <code title="post /simulations/inbound_wire_transfers">client.simulations.inbound_wire_transfers.<a href="./src/increase/resources/simulations/inbound_wire_transfers.py">create</a>(\*\*<a href="src/increase/types/simulations/inbound_wire_transfer_create_params.py">params</a>) -> <a href="./src/increase/types/inbound_wire_transfer.py">InboundWireTransfer</a></code>

## WireDrawdownRequests

Methods:

- <code title="post /simulations/wire_drawdown_requests/{wire_drawdown_request_id}/refuse">client.simulations.wire_drawdown_requests.<a href="./src/increase/resources/simulations/wire_drawdown_requests.py">refuse</a>(wire_drawdown_request_id) -> <a href="./src/increase/types/wire_drawdown_request.py">WireDrawdownRequest</a></code>
- <code title="post /simulations/wire_drawdown_requests/{wire_drawdown_request_id}/submit">client.simulations.wire_drawdown_requests.<a href="./src/increase/resources/simulations/wire_drawdown_requests.py">submit</a>(wire_drawdown_request_id) -> <a href="./src/increase/types/wire_drawdown_request.py">WireDrawdownRequest</a></code>

## InboundWireDrawdownRequests

Methods:

- <code title="post /simulations/inbound_wire_drawdown_requests">client.simulations.inbound_wire_drawdown_requests.<a href="./src/increase/resources/simulations/inbound_wire_drawdown_requests.py">create</a>(\*\*<a href="src/increase/types/simulations/inbound_wire_drawdown_request_create_params.py">params</a>) -> <a href="./src/increase/types/inbound_wire_drawdown_request.py">InboundWireDrawdownRequest</a></code>

## CheckTransfers

Methods:

- <code title="post /simulations/check_transfers/{check_transfer_id}/mail">client.simulations.check_transfers.<a href="./src/increase/resources/simulations/check_transfers.py">mail</a>(check_transfer_id) -> <a href="./src/increase/types/check_transfer.py">CheckTransfer</a></code>

## InboundCheckDeposits

Methods:

- <code title="post /simulations/inbound_check_deposits">client.simulations.inbound_check_deposits.<a href="./src/increase/resources/simulations/inbound_check_deposits.py">create</a>(\*\*<a href="src/increase/types/simulations/inbound_check_deposit_create_params.py">params</a>) -> <a href="./src/increase/types/inbound_check_deposit.py">InboundCheckDeposit</a></code>

## RealTimePaymentsTransfers

Methods:

- <code title="post /simulations/real_time_payments_transfers/{real_time_payments_transfer_id}/complete">client.simulations.real_time_payments_transfers.<a href="./src/increase/resources/simulations/real_time_payments_transfers.py">complete</a>(real_time_payments_transfer_id, \*\*<a href="src/increase/types/simulations/real_time_payments_transfer_complete_params.py">params</a>) -> <a href="./src/increase/types/real_time_payments_transfer.py">RealTimePaymentsTransfer</a></code>

## InboundRealTimePaymentsTransfers

Methods:

- <code title="post /simulations/inbound_real_time_payments_transfers">client.simulations.inbound_real_time_payments_transfers.<a href="./src/increase/resources/simulations/inbound_real_time_payments_transfers.py">create</a>(\*\*<a href="src/increase/types/simulations/inbound_real_time_payments_transfer_create_params.py">params</a>) -> <a href="./src/increase/types/inbound_real_time_payments_transfer.py">InboundRealTimePaymentsTransfer</a></code>

## CheckDeposits

Methods:

- <code title="post /simulations/check_deposits/{check_deposit_id}/reject">client.simulations.check_deposits.<a href="./src/increase/resources/simulations/check_deposits.py">reject</a>(check_deposit_id) -> <a href="./src/increase/types/check_deposit.py">CheckDeposit</a></code>
- <code title="post /simulations/check_deposits/{check_deposit_id}/return">client.simulations.check*deposits.<a href="./src/increase/resources/simulations/check_deposits.py">return*</a>(check_deposit_id) -> <a href="./src/increase/types/check_deposit.py">CheckDeposit</a></code>
- <code title="post /simulations/check_deposits/{check_deposit_id}/submit">client.simulations.check_deposits.<a href="./src/increase/resources/simulations/check_deposits.py">submit</a>(check_deposit_id) -> <a href="./src/increase/types/check_deposit.py">CheckDeposit</a></code>

## InboundMailItems

Methods:

- <code title="post /simulations/inbound_mail_items">client.simulations.inbound_mail_items.<a href="./src/increase/resources/simulations/inbound_mail_items.py">create</a>(\*\*<a href="src/increase/types/simulations/inbound_mail_item_create_params.py">params</a>) -> <a href="./src/increase/types/inbound_mail_item.py">InboundMailItem</a></code>

## Programs

Methods:

- <code title="post /simulations/programs">client.simulations.programs.<a href="./src/increase/resources/simulations/programs.py">create</a>(\*\*<a href="src/increase/types/simulations/program_create_params.py">params</a>) -> <a href="./src/increase/types/program.py">Program</a></code>

## AccountStatements

Methods:

- <code title="post /simulations/account_statements">client.simulations.account_statements.<a href="./src/increase/resources/simulations/account_statements.py">create</a>(\*\*<a href="src/increase/types/simulations/account_statement_create_params.py">params</a>) -> <a href="./src/increase/types/account_statement.py">AccountStatement</a></code>

## Documents

Methods:

- <code title="post /simulations/documents">client.simulations.documents.<a href="./src/increase/resources/simulations/documents.py">create</a>(\*\*<a href="src/increase/types/simulations/document_create_params.py">params</a>) -> <a href="./src/increase/types/document.py">Document</a></code>

## CardTokens

Methods:

- <code title="post /simulations/card_tokens">client.simulations.card_tokens.<a href="./src/increase/resources/simulations/card_tokens.py">create</a>(\*\*<a href="src/increase/types/simulations/card_token_create_params.py">params</a>) -> <a href="./src/increase/types/card_token.py">CardToken</a></code>
