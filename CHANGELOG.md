# Changelog

## [0.7.0](https://github.com/Increase/increase-python/compare/v0.6.1...v0.7.0) (2023-06-13)


### ⚠ BREAKING CHANGES

* **api:** rename return reason enum member ([#14](https://github.com/Increase/increase-python/issues/14))

### Chores

* **internal:** improve internal test helper ([#10](https://github.com/Increase/increase-python/issues/10)) ([85560b9](https://github.com/Increase/increase-python/commit/85560b95f167e3b929f88383eb31cd9072264cb8))


### Refactors

* **api:** rename return reason enum member ([#14](https://github.com/Increase/increase-python/issues/14)) ([c99e844](https://github.com/Increase/increase-python/commit/c99e844a4f07b44a64d026c705c17c6498238962))


### Documentation

* point to github repo instead of email contact ([#15](https://github.com/Increase/increase-python/issues/15)) ([cab1b9a](https://github.com/Increase/increase-python/commit/cab1b9ac76794d1cb9ec1916a2182e1265b1c88b))
* slight improvement to file uploads example ([#12](https://github.com/Increase/increase-python/issues/12)) ([c7241e3](https://github.com/Increase/increase-python/commit/c7241e3216834a577ca338713bb1747afb69487f))

## [0.6.1](https://github.com/Increase/increase-python/compare/v0.6.0...v0.6.1) (2023-06-09)


### Features

* **api:** add new endpoints + properties + enums ([#8](https://github.com/Increase/increase-python/issues/8)) ([0a436a0](https://github.com/Increase/increase-python/commit/0a436a0b3bd426a4b68e24df1ec9a011b9748a3e))
* **docs:** always document positional arguments & options arguments ([#7](https://github.com/Increase/increase-python/issues/7)) ([964afd3](https://github.com/Increase/increase-python/commit/964afd3dc73ca2be23792eb2363007b537431294))

## [0.6.0](https://github.com/Increase/increase-python/compare/v0.5.0...v0.6.0) (2023-05-31)


### ⚠ BREAKING CHANGES

* **api:** replace notification_of_change with a list, and add merchant_acceptor_id

### Features

* add timeout option to methods ([c9f0b8c](https://github.com/Increase/increase-python/commit/c9f0b8cd994e2642520024e38cddf820c7ae43d2))
* **api:** add `at_time` property for balance lookups ([3ff9c8a](https://github.com/Increase/increase-python/commit/3ff9c8ac61c24d0fa7bd12b6e722985b8345a907))
* **api:** add `collection_receivable` to transaction source category enum ([c580763](https://github.com/Increase/increase-python/commit/c58076323cdc1fd67eeca4217fc4beba9c695248))
* **api:** add `expires_at` property ([3fc4320](https://github.com/Increase/increase-python/commit/3fc43203d284b17be7cee7b3504a1235872d763d))
* **api:** add `simulations.check_transfers.return_()` method ([c2effd4](https://github.com/Increase/increase-python/commit/c2effd41518618aa8e3b3e7ad31148e9ae2ff5a6))
* **api:** add bookkeeping accounts, entries, and entry sets, and several other changes ([49ce9e8](https://github.com/Increase/increase-python/commit/49ce9e8edc87fde418e632c3d963fe638619fae4))
* **api:** add new enum members ([a5b57e5](https://github.com/Increase/increase-python/commit/a5b57e545a968f5b5bf8f82f21c2e34569bca938))
* **api:** add new fields ([d8ebc38](https://github.com/Increase/increase-python/commit/d8ebc384d9d405dacca76759e5c36322878a1416))
* **api:** add optional `pending_transaction_id` field to pending transaction ([8b9c430](https://github.com/Increase/increase-python/commit/8b9c4305921add7d49e6286d32d2045d59f8844d))
* **api:** add wire decline object ([2cc188d](https://github.com/Increase/increase-python/commit/2cc188d15a88b887213c28d33726dab1dfb479f0))
* **api:** enum updates ([35bbd10](https://github.com/Increase/increase-python/commit/35bbd103609a2a3961523d3058da0b645f6ad15e))
* **api:** make route_type an enum & add ACHTransfer.effective_date ([e97240c](https://github.com/Increase/increase-python/commit/e97240cd682f1cc74f592739875c4975e253682f))
* **api:** make route_type an enum & add ACHTransfer.effective_date ([e97240c](https://github.com/Increase/increase-python/commit/e97240cd682f1cc74f592739875c4975e253682f))
* **api:** remove card_settlement_transaction_id ([f9d83dd](https://github.com/Increase/increase-python/commit/f9d83ddd964983d746f9efbca47824abf5efff24))
* **api:** replace notification_of_change with a list, and add merchant_acceptor_id ([511d0be](https://github.com/Increase/increase-python/commit/511d0beb161acf34dca425d3beca63261b78b079))
* **api:** updates ([d380ad2](https://github.com/Increase/increase-python/commit/d380ad26bf0af1e693cedc7bc2152965361b5541))
* **docs:** updates ([77a2b53](https://github.com/Increase/increase-python/commit/77a2b53c48a920ca59e003f623db353da790e235))
* improve error message for missing authentication ([21c5a12](https://github.com/Increase/increase-python/commit/21c5a12062622eb63c8974dd3eff74be7be8b60d))
* improve error message for missing authentication ([21c5a12](https://github.com/Increase/increase-python/commit/21c5a12062622eb63c8974dd3eff74be7be8b60d))
* **internal:** add support for positional params ([77c479b](https://github.com/Increase/increase-python/commit/77c479b629ef3d9417b6a3f6fdccd8eb9b66be0d))
* **internal:** add support for positional params ([77c479b](https://github.com/Increase/increase-python/commit/77c479b629ef3d9417b6a3f6fdccd8eb9b66be0d))


### Bug Fixes

* **sse:** small improvement to handling server-sent events ([54f563a](https://github.com/Increase/increase-python/commit/54f563aabe17356f458d2891237e0a2609367128))


### Refactors

* **types:** use builtin `dict` types in a couple of places ([d4b2257](https://github.com/Increase/increase-python/commit/d4b2257b3f317b72d7081d134b3baa1ce7fb923d))
* **types:** use builtin `dict` types in a couple of places ([d4b2257](https://github.com/Increase/increase-python/commit/d4b2257b3f317b72d7081d134b3baa1ce7fb923d))
