# Changelog

## [0.12.0](https://github.com/Increase/increase-python/compare/v0.11.4...v0.12.0) (2023-08-17)


### ⚠ BREAKING CHANGES

* **api:** change `physical_cards.status` value, remove `event_subscription` field, add fields ([#87](https://github.com/Increase/increase-python/issues/87))

### Features

* add support for Pydantic v2 ([#85](https://github.com/Increase/increase-python/issues/85)) ([ccbd518](https://github.com/Increase/increase-python/commit/ccbd518c770913ee83e5af32e80369405d6f4311))
* **api:** change `physical_cards.status` value, remove `event_subscription` field, add fields ([#87](https://github.com/Increase/increase-python/issues/87)) ([f33460e](https://github.com/Increase/increase-python/commit/f33460ee6035bb3b661a40c05f08b6bfc4c9c752))

## [0.11.4](https://github.com/Increase/increase-python/compare/v0.11.3...v0.11.4) (2023-08-16)


### Features

* allow a default timeout to be set for clients ([#80](https://github.com/Increase/increase-python/issues/80)) ([144a621](https://github.com/Increase/increase-python/commit/144a62172249755330ddf08ec00836ea250ac09f))
* **api:** updates ([#75](https://github.com/Increase/increase-python/issues/75)) ([6ec05c8](https://github.com/Increase/increase-python/commit/6ec05c8cb8149b01af86ec618c7e2b283ec4d1da))


### Documentation

* **api:** change description of various fields ([#76](https://github.com/Increase/increase-python/issues/76)) ([2fb161a](https://github.com/Increase/increase-python/commit/2fb161abcef52446b047b599a24a3af0f50e2e56))


### Styles

* prefer importing types directly instead of module names ([#82](https://github.com/Increase/increase-python/issues/82)) ([2c3730e](https://github.com/Increase/increase-python/commit/2c3730e4124b64d61164661acd3311f6ddbad7eb))


### Chores

* assign default reviewers to release PRs ([#83](https://github.com/Increase/increase-python/issues/83)) ([16fc02e](https://github.com/Increase/increase-python/commit/16fc02e625f4d0ebc264edb02bcd4b449fd1341a))
* **deps:** bump typing-extensions to 4.5 ([#77](https://github.com/Increase/increase-python/issues/77)) ([76d1b67](https://github.com/Increase/increase-python/commit/76d1b67144b60cda355cef48008f1ad0c4dcf5a7))
* **internal/deps:** update lock file ([#74](https://github.com/Increase/increase-python/issues/74)) ([dfd056c](https://github.com/Increase/increase-python/commit/dfd056c17a8066234cdaae0f3c7e7980c6a7490a))
* **internal:** bump pytest-asyncio ([#78](https://github.com/Increase/increase-python/issues/78)) ([1348000](https://github.com/Increase/increase-python/commit/13480009ccfe86044dfb3593fc2a89a161765919))
* **internal:** minor formatting change ([#84](https://github.com/Increase/increase-python/issues/84)) ([73711a0](https://github.com/Increase/increase-python/commit/73711a0de1cb6ddbeb17bc0485ffbd678aee3244))
* **internal:** minor import restructuring ([#72](https://github.com/Increase/increase-python/issues/72)) ([1564ce2](https://github.com/Increase/increase-python/commit/1564ce2a8517fb8794dfd502505c3688a6fef173))

## [0.11.3](https://github.com/Increase/increase-python/compare/v0.11.2...v0.11.3) (2023-08-08)


### Features

* **api:** updates ([#67](https://github.com/Increase/increase-python/issues/67)) ([33be21c](https://github.com/Increase/increase-python/commit/33be21ce0c6d9f654f75e6bfc200bc681ac4eb02))


### Documentation

* **readme:** remove beta status + document versioning policy ([#68](https://github.com/Increase/increase-python/issues/68)) ([a8108e0](https://github.com/Increase/increase-python/commit/a8108e079f73533179ddc3aefa9c3d6a99245b95))


### Chores

* **internal:** bump certifi dependency ([#70](https://github.com/Increase/increase-python/issues/70)) ([3883e68](https://github.com/Increase/increase-python/commit/3883e689818f9d895e7415c110d9ddb026198df5))
* **internal:** update mypy to v1.4.1 ([#65](https://github.com/Increase/increase-python/issues/65)) ([a2e700e](https://github.com/Increase/increase-python/commit/a2e700e0a28c5902761b95d79c1b6b94e6119cc9))
* **internal:** update ruff to v0.0.282 ([#69](https://github.com/Increase/increase-python/issues/69)) ([66b2977](https://github.com/Increase/increase-python/commit/66b29777e2f250bae2d69eee6c21c55fca34497d))

## [0.11.2](https://github.com/Increase/increase-python/compare/v0.11.1...v0.11.2) (2023-08-01)


### Features

* **client:** add client close handlers ([#58](https://github.com/Increase/increase-python/issues/58)) ([c79cfcc](https://github.com/Increase/increase-python/commit/c79cfcc1ec7cf7b370cb81f786fc5b3783ee2213))
* **test:** unskip file uploads tests ([#63](https://github.com/Increase/increase-python/issues/63)) ([df3300f](https://github.com/Increase/increase-python/commit/df3300f46249b746116ace54f41aba5ea337578d))


### Bug Fixes

* **client:** correctly handle environment variable access ([#56](https://github.com/Increase/increase-python/issues/56)) ([e39552b](https://github.com/Increase/increase-python/commit/e39552be66f55c565159f1408e9f40171af24c40))


### Chores

* **internal:** bump pyright ([#61](https://github.com/Increase/increase-python/issues/61)) ([a96a677](https://github.com/Increase/increase-python/commit/a96a6776c1dd68d30c408899f71f85f8ea32a87e))
* **internal:** bump pyright ([#62](https://github.com/Increase/increase-python/issues/62)) ([19285fb](https://github.com/Increase/increase-python/commit/19285fb23aa95895ef2f2212049eb647d93ed597))
* **internal:** make demo example runnable and more portable ([#60](https://github.com/Increase/increase-python/issues/60)) ([06735fa](https://github.com/Increase/increase-python/commit/06735fa90e80c07382f7bafd2a9daf0ff74a96d8))
* **internal:** minor reformatting of code ([#59](https://github.com/Increase/increase-python/issues/59)) ([3e1c3ea](https://github.com/Increase/increase-python/commit/3e1c3ea3ae28823a128d3993bd5b3f960e2be62f))

## [0.11.1](https://github.com/Increase/increase-python/compare/v0.11.0...v0.11.1) (2023-07-27)


### Documentation

* **readme:** use `client` everywhere for consistency ([#52](https://github.com/Increase/increase-python/issues/52)) ([8dfab15](https://github.com/Increase/increase-python/commit/8dfab151164e8833d6a51e7d6b356629ba751ff8))


### Chores

* remove unused resource classes ([#54](https://github.com/Increase/increase-python/issues/54)) ([6106201](https://github.com/Increase/increase-python/commit/6106201916d5353269325b4209bbd7eb1d9d935f))

## [0.11.0](https://github.com/Increase/increase-python/compare/v0.10.1...v0.11.0) (2023-07-22)


### ⚠ BREAKING CHANGES

* **api:** reorganize `check_transfer` and `network fields; add `request_details`; add `unknown` ([#46](https://github.com/Increase/increase-python/issues/46))

### Features

* **api:** add fee_period_start and return_of_erroneous_or_reversing_debit ([#50](https://github.com/Increase/increase-python/issues/50)) ([0cb14d0](https://github.com/Increase/increase-python/commit/0cb14d072752bda02d479c0b9b745161d8344b0b))
* **api:** reorganize `check_transfer` and `network fields; add `request_details`; add `unknown` ([#46](https://github.com/Increase/increase-python/issues/46)) ([f1a0a9f](https://github.com/Increase/increase-python/commit/f1a0a9f6b4b7874db8f662cff8108f3a0eba2fd4))


### Chores

* **package:** pin major versions of dependencies ([#37](https://github.com/Increase/increase-python/issues/37)) ([6564f66](https://github.com/Increase/increase-python/commit/6564f66171bae64c3122259957cabc9ea4ee7f6a))
* **package:** pin major versions of dependencies ([#39](https://github.com/Increase/increase-python/issues/39)) ([2878aff](https://github.com/Increase/increase-python/commit/2878affa02c8204f634a1dbf7e9b4f00dae3d61b))


### Documentation

* **api:** update `model_id` documentation ([#49](https://github.com/Increase/increase-python/issues/49)) ([51dfa65](https://github.com/Increase/increase-python/commit/51dfa651b457352bed2f79dcfc4604b4a22e27fa))
* **readme:** reference "client" in errors section and add missing import ([#48](https://github.com/Increase/increase-python/issues/48)) ([fee1917](https://github.com/Increase/increase-python/commit/fee1917212136fc089567af491f7fd42f5f315a5))

## [0.10.1](https://github.com/Increase/increase-python/compare/v0.10.0...v0.10.1) (2023-07-17)


### Features

* **api:** add physical_card_id ([#42](https://github.com/Increase/increase-python/issues/42)) ([c76422f](https://github.com/Increase/increase-python/commit/c76422f17e18a9c44a43fe779bc424b88b609758))


### Chores

* **internal:** add `codegen.log` to `.gitignore` ([#44](https://github.com/Increase/increase-python/issues/44)) ([83b722c](https://github.com/Increase/increase-python/commit/83b722c8e12aa5d3c0caf8ee4ef2733844887abb))
* **package:** pin major versions of dependencies ([#37](https://github.com/Increase/increase-python/issues/37)) ([8e58b27](https://github.com/Increase/increase-python/commit/8e58b27706c7c57d0f7234a307e3599e410084a8))
* **package:** pin major versions of dependencies ([#39](https://github.com/Increase/increase-python/issues/39)) ([80af0b1](https://github.com/Increase/increase-python/commit/80af0b16befec2be951f16285922db87c9c55c5e))

## [0.10.0](https://github.com/Increase/increase-python/compare/v0.9.0...v0.10.0) (2023-07-12)


### ⚠ BREAKING CHANGES

* **api:** add unique_identifier, driver's license backs, inbound funds holds, and more ([#40](https://github.com/Increase/increase-python/issues/40))

### Features

* **api:** add unique_identifier, driver's license backs, inbound funds holds, and more ([#40](https://github.com/Increase/increase-python/issues/40)) ([6bfd843](https://github.com/Increase/increase-python/commit/6bfd8435c03c86371c0b72987da9ee58779cd101))


### Chores

* **package:** pin major versions of dependencies ([#37](https://github.com/Increase/increase-python/issues/37)) ([5a7d645](https://github.com/Increase/increase-python/commit/5a7d645db59e7b340a2ba3fc58b5ec04a8fc7d12))
* **package:** pin major versions of dependencies ([#39](https://github.com/Increase/increase-python/issues/39)) ([fafe6ee](https://github.com/Increase/increase-python/commit/fafe6eeb7d0732e68710d644a6cda21b19597f56))

## [0.9.0](https://github.com/Increase/increase-python/compare/v0.8.1...v0.9.0) (2023-07-07)


### ⚠ BREAKING CHANGES

* **api:** add card profiles simulation method ([#35](https://github.com/Increase/increase-python/issues/35))

### Features

* **api:** add card profiles simulation method ([#35](https://github.com/Increase/increase-python/issues/35)) ([5045fa6](https://github.com/Increase/increase-python/commit/5045fa66d25b1a0b5ed59e7223786b8e73450a14))


### Chores

* **internal:** update lock file ([#32](https://github.com/Increase/increase-python/issues/32)) ([f6cc52f](https://github.com/Increase/increase-python/commit/f6cc52f40500fa9e092e1da87e5b2ea75a9856fd))


### Documentation

* **types:** add documentation for enum members ([#34](https://github.com/Increase/increase-python/issues/34)) ([40e9d0a](https://github.com/Increase/increase-python/commit/40e9d0ac216dadf745d98c8b84e1162f728dff67))

## [0.8.1](https://github.com/Increase/increase-python/compare/v0.8.0...v0.8.1) (2023-07-01)


### Bug Fixes

* **deps:** pin pydantic to less than v2.0 ([#29](https://github.com/Increase/increase-python/issues/29)) ([1dfdbc0](https://github.com/Increase/increase-python/commit/1dfdbc0a1463f651c8ca35b3fcde3704a43b6a33))

## [0.8.0](https://github.com/Increase/increase-python/compare/v0.7.1...v0.8.0) (2023-06-29)


### ⚠ BREAKING CHANGES

* **api:** remove many enum members from document category ([#24](https://github.com/Increase/increase-python/issues/24))

### Features

* **api/types:** mark more check transfer intention properties as nullable ([#23](https://github.com/Increase/increase-python/issues/23)) ([22a6aa3](https://github.com/Increase/increase-python/commit/22a6aa33ecc3ac9e2ef5800cc4c43f9a49abe02e))


### Refactors

* **api:** remove `other` from reason enum ([#21](https://github.com/Increase/increase-python/issues/21)) ([0110ffd](https://github.com/Increase/increase-python/commit/0110ffd691ef3f9640dfe950fa369bcf5235f0d5))
* **api:** remove many enum members from document category ([#24](https://github.com/Increase/increase-python/issues/24)) ([d7aab0d](https://github.com/Increase/increase-python/commit/d7aab0d1c50e367a942829c7bf51a9372163a317))


### Chores

* **deps:** update certifi ([#25](https://github.com/Increase/increase-python/issues/25)) ([791e90f](https://github.com/Increase/increase-python/commit/791e90f67323f8a97e3a7aa8bcac73b939583fbe))


### Documentation

* add trailing newlines ([#26](https://github.com/Increase/increase-python/issues/26)) ([936f415](https://github.com/Increase/increase-python/commit/936f4156a7ad098e242a911e23c1b0c71c9385bd))


### Styles

* minor reordering of types and properties ([#27](https://github.com/Increase/increase-python/issues/27)) ([b8a4d8b](https://github.com/Increase/increase-python/commit/b8a4d8bbe68dca79fed45907a97138b6b9632aa8))

## [0.7.1](https://github.com/Increase/increase-python/compare/v0.7.0...v0.7.1) (2023-06-19)


### Chores

* **internal:** add overloads to `client.get` for streaming ([#17](https://github.com/Increase/increase-python/issues/17)) ([5b0137d](https://github.com/Increase/increase-python/commit/5b0137d1dba6aba7552a630d5a09dddaed2a63c8))


### Refactors

* **api:** remove unused properties and enum members ([#19](https://github.com/Increase/increase-python/issues/19)) ([9b94033](https://github.com/Increase/increase-python/commit/9b940336b331dcba54b6c51d61e50d37b8e615ca))

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
