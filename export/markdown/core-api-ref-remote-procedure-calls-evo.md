# BLS

*Added in Dash Core 0.13.0*

The [`bls` RPC](core-api-ref-remote-procedure-calls-evo#bls) provides a set of commands to execute BLS-related actions.

## BLS Generate

The `bls generate` RPC creates a new BLS secret/public key pair.

*Parameters: none*

*Result---a secret/public key pair*

Name | Type | Presence | Description
--- | --- | --- | ---
`result` | object | Required<br>(exactly 1) | BLS key pair
→<br>`secret` | string (hex) | Required<br>(exactly 1) | A BLS secret key
→<br>`public` | string (hex) | Required<br>(exactly 1) | A BLS public key

*Example from Dash Core 0.13.0*

``` bash
dash-cli -testnet bls generate
```

Result:
``` json
{
  "secret": "52f35cd3d977a505485f2474e7e71ef3f60f859603d72ad6b0fa7f7bd163e144",
  "public": "885d01d746c3e4d2093b0975de2d8c1f3e5a2c3e8fdaaed929f86fc9fbb278a095248163c101a2456650b415776b7990"
}
```

## BLS FromSecret

The `bls fromsecret` RPC parses a BLS secret key and returns the secret/public key pair.

*Parameter #1---secret key*

Name | Type | Presence | Description
--- | --- | --- | ---
`secret` | string (hex) | Required<br>(exactly 1) | The BLS secret key

*Result---the secret/public key pair*

Name | Type | Presence | Description
--- | --- | --- | ---
`result` | object | Required<br>(exactly 1) | BLS key pair
→<br>`secret` | string (hex) | Required<br>(exactly 1) | A BLS secret key
→<br>`public` | string (hex) | Required<br>(exactly 1) | A BLS public key

*Example from Dash Core 0.14.0*

``` bash
dash-cli -testnet bls fromsecret 52f35cd3d977a505485f2474e7e71ef3f60f859603d72ad6b0fa7f7bd163e144
```

Result:
``` json
{
  "secret": "52f35cd3d977a505485f2474e7e71ef3f60f859603d72ad6b0fa7f7bd163e144",
  "public": "885d01d746c3e4d2093b0975de2d8c1f3e5a2c3e8fdaaed929f86fc9fbb278a095248163c101a2456650b415776b7990"
}
```

*See also: none*

# ProTx

*Added in Dash Core 0.13.0*

The [`protx` RPC](core-api-ref-remote-procedure-calls-evo#protx) provides a set of commands to execute ProTx related actions.

## ProTx Register

The `protx register` RPC creates a ProRegTx referencing an existing collateral and and sends it to the network.

*Parameter #1---collateral address*

Name | Type | Presence | Description
--- | --- | --- | ---
`collateralHash` | string (hex) | Required<br>(exactly 1) | The collateral transaction hash

*Parameter #2---collateral index*

Name | Type | Presence | Description
--- | --- | --- | ---
`collateralIndex` | string (hex) | Required<br>(exactly 1) | The collateral transaction output index

*Parameter #3---IP Address and port*

Name | Type | Presence | Description
--- | --- | --- | ---
`ipAndPort` | string | Required<br>(exactly 1) | IP and port in the form 'IP:PORT'.<br>Must be unique on the network.<br>Can be set to '0', which will require a ProUpServTx afterwards.

*Parameter #4---owner address*

Name | Type | Presence | Description
--- | --- | --- | ---
`ownerAddress` | string (hex) | Required<br>(exactly 1) | The owner key used for payee updates and proposal voting. The private key belonging to this address be known in your wallet. The address must be unused and must differ from the `collateralAddress`.

*Parameter #5---operator public key*

Name | Type | Presence | Description
--- | --- | --- | ---
`operatorPubKey` | string (hex) | Required<br>(exactly 1) |  The operator public key. The private key does not have to be known. It has to match the private key which is later used when operating the masternode.

*Parameter #6---voting address*

Name | Type | Presence | Description
--- | --- | --- | ---
`votingAddress` | string (hex) | Required<br>(exactly 1) | The voting address. The private key does not have to be known by your wallet. It has to match the private key which is later used when voting on proposals. If set to an empty string, `ownerAddress` will be used.

*Parameter #7---operator reward*

Name | Type | Presence | Description
--- | --- | --- | ---
`operatorReward` | number | Required<br>(exactly 1) | The fraction in % to share with the operator. If non-zero, `ipAndPort` must be zero as well.<br>The value must be between '0.00' and '100.00'.

*Parameter #8---payout address*

Name | Type | Presence | Description
--- | --- | --- | ---
`payoutAddress` | string | Required<br>(exactly 1) | The Dash address to use for masternode reward payments.

*Parameter #9---fee source address*

Name | Type | Presence | Description
--- | --- | --- | ---
`feeSourceAddress` | string | Optional<br>(0 or 1) | If specified, the wallet will only use coins from this address to fund the ProTx. If not specified, `payoutAddress` will be used. The private key belonging to this address must be known in your wallet.

*Result---provider registration transaction hash*

Name | Type | Presence | Description
--- | --- | --- | ---
`result` | string (hex) | Required<br>(exactly 1) | Provider registration transaction (ProRegTx) hash

*Example from Dash Core 0.13.0*

``` bash
dash-cli -testnet protx register\
 8b2eab3413abb6e04d17d1defe2b71039ba6b6f72ea1e5dab29bb10e7b745948 1\
 2.3.4.5:2345 yNLuVTXJbjbxgrQX5LSMi7hV19We8hT2d6\
 88d719278eef605d9c19037366910b59bc28d437de4a8db4d76fda6d6985dbdf10404fb9bb5cd0e8c22f4a914a6c5566\
 yNLuVTXJbjbxgrQX5LSMi7hV19We8hT2d6 5 yjJJLkYDUN6X8gWjXbCoKEXoiLeKxxMMRt
```

Result:
``` bash
61e6d780178d353940c4cb9b3073ac0c50792bbcf0b15c1750d2028b71e34929
```

## ProTx Register Fund

The `protx register_fund` RPC creates and funds a ProRegTx with the 1,000 DASH necessary for a masternode and then sends it to the network.

*Parameter #1---collateral address*

Name | Type | Presence | Description
--- | --- | --- | ---
`collateralAddress` | string (hex) | Required<br>(exactly 1) | The Dash address to send the collateral to

*Parameter #2---IP Address and port*

Name | Type | Presence | Description
--- | --- | --- | ---
`ipAndPort` | string | Required<br>(exactly 1) | IP and port in the form 'IP:PORT'.<br>Must be unique on the network.<br>Can be set to '0', which will require a ProUpServTx afterwards.

*Parameter #3---owner address*

Name | Type | Presence | Description
--- | --- | --- | ---
`ownerAddress` | string (hex) | Required<br>(exactly 1) | The owner key used for payee updates and proposal voting. The private key belonging to this address be known in your wallet. The address must be unused and must differ from the `collateralAddress`.

*Parameter #4---operator public key*

Name | Type | Presence | Description
--- | --- | --- | ---
`operatorPubKey` | string (hex) | Required<br>(exactly 1) |  The operator public key. The private key does not have to be known. It has to match the private key which is later used when operating the masternode.

*Parameter #5---voting address*

Name | Type | Presence | Description
--- | --- | --- | ---
`votingAddress` | string (hex) | Required<br>(exactly 1) | The voting address. The private key does not have to be known by your wallet. It has to match the private key which is later used when voting on proposals. If set to an empty string, `ownerAddress` will be used.

*Parameter #6---operator reward*

Name | Type | Presence | Description
--- | --- | --- | ---
`operatorReward` | number | Required<br>(exactly 1) | The fraction in % to share with the operator.<br>The value must be between '0.00' and '100.00'.

*Parameter #7---payout address*

Name | Type | Presence | Description
--- | --- | --- | ---
`payoutAddress` | string | Required<br>(exactly 1) | The Dash address to use for masternode reward payments.

*Parameter #8---fund address*

Name | Type | Presence | Description
--- | --- | --- | ---
`fundAddress` | string | Optional<br>(0 or 1) | If specified, the wallet will only use coins from this address to fund the ProTx. If not specified, `payoutAddress` will be used. The private key belonging to this address must be known in your wallet.

*Result---provider registration transaction hash*

Name | Type | Presence | Description
--- | --- | --- | ---
`result` | string (hex) | Required<br>(exactly 1) | Provider registration transaction (ProRegTx) hash

*Example from Dash Core 0.13.0*

``` bash
dash-cli -testnet protx register_fund yakx4mMRptKhgfjedNzX5FGQq7kSSBF2e7\
 3.4.5.6:3456 yX2cDS4kcJ4LK4uq9Hd4TG7kURV3sGLZrw\
 0e02146e9c34cfbcb3f3037574a1abb35525e2ca0c3c6901dbf82ac591e30218d1711223b7ca956edf39f3d984d06d51\
 yX2cDS4kcJ4LK4uq9Hd4TG7kURV3sGLZrw 5 yakx4mMRptKhgfjedNzX5FGQq7kSSBF2e7
```

Result:
``` bash
ba1b3330e16a0876b7a186e7ceb689f03ec646e611e91d7139de021bbf13afdd
```

## ProTx Register Prepare

The `protx register_prepare` RPC creates an unsigned ProTx and
returns it. The ProTx must be signed externally with the collateral key and then
passed to "protx register_submit". The prepared transaction will also contain inputs
and outputs to cover fees.

*Parameter #1---collateral address*

Name | Type | Presence | Description
--- | --- | --- | ---
`collateralHash` | string (hex) | Required<br>(exactly 1) | The collateral transaction hash

*Parameter #2---collateral index*

Name | Type | Presence | Description
--- | --- | --- | ---
`collateralIndex` | string (hex) | Required<br>(exactly 1) | The collateral transaction output index

*Parameter #3---IP Address and port*

Name | Type | Presence | Description
--- | --- | --- | ---
`ipAndPort` | string | Required<br>(exactly 1) | IP and port in the form 'IP:PORT'.<br>Must be unique on the network.<br>Can be set to '0', which will require a ProUpServTx afterwards.

*Parameter #4---owner address*

Name | Type | Presence | Description
--- | --- | --- | ---
`ownerAddress` | string (hex) | Required<br>(exactly 1) | The owner key used for payee updates and proposal voting. The private key belonging to this address be known in your wallet. The address must be unused and must differ from the `collateralAddress`.

*Parameter #5---operator public key*

Name | Type | Presence | Description
--- | --- | --- | ---
`operatorPubKey` | string (hex) | Required<br>(exactly 1) |  The operator public key. The private key does not have to be known. It has to match the private key which is later used when operating the masternode.

*Parameter #6---voting address*

Name | Type | Presence | Description
--- | --- | --- | ---
`votingAddress` | string (hex) | Required<br>(exactly 1) | The voting address. The private key does not have to be known by your wallet. It has to match the private key which is later used when voting on proposals. If set to an empty string, `ownerAddress` will be used.

*Parameter #7---operator reward*

Name | Type | Presence | Description
--- | --- | --- | ---
`operatorReward` | number | Required<br>(exactly 1) | The fraction in % to share with the operator.<br>The value must be between '0.00' and '100.00'.

*Parameter #8---payout address*

Name | Type | Presence | Description
--- | --- | --- | ---
`payoutAddress` | string (hex) | Required<br>(exactly 1) | The Dash address to use for masternode reward payments.

*Parameter #9---fee source address*

Name | Type | Presence | Description
--- | --- | --- | ---
`feeSourceAddress` | string | Optional<br>(0 or 1) | If specified, the wallet will only use coins from this address to fund the ProTx. If not specified, `payoutAddress` will be used. The private key belonging to this address must be known in your wallet.

*Result---unsigned transaction and message to sign*

Name | Type | Presence | Description
--- | --- | --- | ---
`result` | object | Required<br>(exactly 1) | JSON object containing an unsigned provider transaction and the message to be signed externally, or JSON `null` if an error occurred
→<br>`tx` | string (hex) | Required<br>(exactly 1) | The serialized ProRegTx in hex format
→<br>`collateralAddress` | string (hex) | Required<br>(exactly 1) | The collateral address
→<br>`signMessage` | string (base64) | Required<br>(exactly 1) | The string message that needs to be signed with the collateral key.

*Example from Dash Core 0.13.0*

``` bash
dash-cli -testnet protx register_prepare\
 df41e398bb245e973340d434d386f431dbd69735a575721b0b6833856e7d31ec 1 \
 9.8.7.6:9876 yemjhGQ99V5ayJMjoyGGPtxteahii6G1Jz\
 06849865d01e4f73a6d5a025117e48f50b897e14235800501c8bfb8a6365cc8dbf5ddb67a3635d0f1dcc7d46a7ee280c\
 yemjhGQ99V5ayJMjoyGGPtxteahii6G1Jz 1.2 yjJJLkYDUN6X8gWjXbCoKEXoiLeKxxMMRt
```

Result:
``` json
{
  "tx": "0300010001912b88876fee2f8e43e23b5e81276c163cf23d867bad4148170cb106ef9023700000000000feffffff0125623ba40b0000001976a914736e155c1039a269d4019c66219d2a18f0fee27588ac00000000d1010000000000ec317d6e8533680b1b7275a53597d6db31f486d334d44033975e24bb98e341df0100000000000000000000000000ffff090807062694ca6b243168b30461d1f19e2bb89a965a5bac067e06849865d01e4f73a6d5a025117e48f50b897e14235800501c8bfb8a6365cc8dbf5ddb67a3635d0f1dcc7d46a7ee280cca6b243168b30461d1f19e2bb89a965a5bac067e78001976a914fc136008111fcc7a05be6cec66f97568727a9e5188ace5f6b70ac55411727e25178bd417b9b03f837ad7155d90ad286f3a427203fb9f00",
  "collateralAddress": "yWuKWhDzGQqZL8rw6kGxGrfe6P8bUC2S4f",
  "signMessage": "yjJJLkYDUN6X8gWjXbCoKEXoiLeKxxMMRt|120|yemjhGQ99V5ayJMjoyGGPtxteahii6G1Jz|yemjhGQ99V5ayJMjoyGGPtxteahii6G1Jz|69a49e18c1253b90d39322f7e2f7af74524401bc33a27645e697e74a214e3e1e"
}
```

## ProTx Register Submit

The `protx register_submit` RPC submits the specified ProTx to the
network. This command will also sign the inputs of the transaction which were
previously added by `protx register_prepare` to cover transaction fees.

*Parameter #1---collateral address*

Name | Type | Presence | Description
--- | --- | --- | ---
`tx` | string (hex) | Required<br>(exactly 1) | The serialized transaction previously returned by `protx register_prepare`

*Parameter #2---collateral index*

Name | Type | Presence | Description
--- | --- | --- | ---
`sig` | string (base64) | Required<br>(exactly 1) | The signature signed with the collateral key. Must be in base64 format.

*Result---provider registration transaction hash*

Name | Type | Presence | Description
--- | --- | --- | ---
`result` | string (hex) | Required<br>(exactly 1) | Provider registration transaction (ProRegTx) hash

*Example from Dash Core 0.13.0*

``` bash
dash-cli -testnet protx register_submit\
 03000100012d988526d5d1efd32320023c92eff09c2963dcb021b0de9761\
 17e5e37dc7a7870000000000feffffff015f603ba40b0000001976a9140c\
 37e07eb5c608961769e6506c23c11e9f9fe00988ac00000000d101000000\
 00002d988526d5d1efd32320023c92eff09c2963dcb021b0de976117e5e3\
 7dc7a7870100000000000000000000000000ffff05060708162e243dd366\
 bf4a329968d77eac9fb63481a600938d125e1b7cba03ca2a097e402185e6\
 160232ea53e6d62898a3be8617b06ff347d967543228bd9b605547c3d478\
 b0a838ca243dd366bf4a329968d77eac9fb63481a600938dc4091976a914\
 e9bf4e6f26fecf1dfc1e04dde43472df378628b888ac6a048e7f645e8adc\
 305ccfd8652066046a0702596af13b8ac97803ade256da2900\
 \
 H90IvqVtFjZkwLJb08yMEgGixs0/FpcdvwImBcir4cYLJhD3pdX+lKD2GsPl6KNxghVXNk5/HpOdBoWAHo9u++Y=
```

Result:
``` bash
273ce3ebe24183ee4117b10e054cdbb108a3bde5d2f286129e29480d46a3f573
```

## ProTx List

The `protx list` RPC returns a list of provider transactions.

Lists all ProTxs in your wallet or on-chain, depending on the given type. If
`type` is not specified, it defaults to `registered`. All types have the optional
argument `detailed` which if set to `true` will result in a detailed list being
returned. If set to `false`, only the hashes of the ProTx will be returned.

*Parameter #1---type*

Name | Type | Presence | Description
--- | --- | --- | ---
`type` | string | Optional<br>(0 or 1) | The type of ProTxs to list:<br>`registered` - all ProTxs registered at height<br>`valid` - all active/valid ProTxs at height<br>`wallet` - all ProTxs found in the current wallet<br><br>Height defaults to current chain-tip if one is not provided

*Parameter #2---detailed*

Name | Type | Presence | Description
--- | --- | --- | ---
`detailed` | bool | Optional<br>(0 or 1) | If set to `false` (default), only ProTx hashes are returned. If set to `true`, a detailed list of ProTx details is returned.

*Parameter #3---height*

Name | Type | Presence | Description
--- | --- | --- | ---
`height` | bool | Optional<br>(0 or 1) | List ProTxs from this height (default: current chain tip).

*Result (if `detailed` was `false`)---provider registration transaction hash*

Name | Type | Presence | Description
--- | --- | --- | ---
`result` | string (hex): array | Required<br>(exactly 1) | Array of provider transaction (ProTx) hashes

*Result (if `detailed` was `true`)---JSON provider registration transaction details*

Name | Type | Presence | Description
--- | --- | --- | ---
`result` | array | Required<br>(exactly 1) | An array of objects each containing a provider transaction, or JSON `null` if an error occurred
<br>Provider Transaction | object/null | Required<br>(exactly 1) | An object containing a provider transaction
→<br>`proTxHash` | string (hex) | Required<br>(exactly 1) | The hash of the provider transaction as hex in RPC byte order
→<br>`collateralHash` | string (hex) | Required<br>(exactly 1) | The hash of the collateral transaction as hex in RPC byte order
→<br>`collateralIndex` | number (int) | Required<br>(exactly 1) | The collateral index
→ →<br>`collateralAddress` | string (hex) | Required<br>(exactly 1) | The collateral address
→<br>`operatorReward` | number (int) | Required<br>(exactly 1) | The operator reward %
→<br>`state` | object/null | Required<br>(exactly 1) | An object containing a provider transaction state
→ →<br>`service` | string | Required<br>(exactly 1) | The masternode's IP:Port
→ →<br>`registeredHeight` | number (int) | Required<br>(exactly 1) | The height where the masternode was registered
→ →<br>`lastPaidHeight` | number (int) | Required<br>(exactly 1) | The height where the masternode was last paid
→ →<br>`PoSePenalty` | number (int) | Required<br>(exactly 1) | The masternode's proof of service penalty
→ →<br>`PoSeRevivedHeight` | number (int) | Required<br>(exactly 1) | The height where the masternode recovered from a proof of service ban
→ →<br>`PoSeBanHeight` | number (int) | Required<br>(exactly 1) | The height where the masternode was banned for proof of service violations
→ →<br>`revocationReason` | number (int) | Required<br>(exactly 1) | The reason for a ProUpRegTx revocation
→ →<br>`ownerAddress` | string (hex) | Required<br>(exactly 1) | The owner address
→ →<br>`votingAddress` | string (hex) | Required<br>(exactly 1) | The voting address
→ →<br>`payoutAddress` | string (hex) | Required<br>(exactly 1) | The owner's payout address
→ →<br>`pubKeyOperator` | string (hex) | Required<br>(exactly 1) | The operator public key
→ →<br>`operatorPayoutAddress` | string (hex) | Required<br>(exactly 1) | The operator's payout address
→<br>`confirmations` | number (int) | Required<br>(exactly 1) | The number of confirmations this ProTx has
→<br>`wallet` | object/null | Required<br>(exactly 1) | An object containing a wallet details related to this ProTx
→ →<br>`hasOwnerKey` | bool | Required<br>(exactly 1) | The owner key is present in this wallet
→ →<br>`hasOperatorKey` | bool | Required<br>(exactly 1) | The operator key is present in this wallet
→ →<br>`hasVotingKey` | bool | Required<br>(exactly 1) | The voting key is present in this wallet
→ →<br>`ownsCollateral` | bool | Required<br>(exactly 1) | The collateral is owned by this wallet
→ →<br>`ownsPayeeScript` | bool | Required<br>(exactly 1) | The payee script is owned by this wallet
→ →<br>`ownsOperatorRewardScript` | bool | Required<br>(exactly 1) | The operator reward script is owned by this wallet
→<br>`metaInfo` | object/null | Required<br>(exactly 1) | **Added in Dash Core 0.16.0**<br><br>An object containing a metainfo related to this ProTx
→ →<br>`lastDSQ` | string | Required<br>(exactly 1) | The owner key is present in this wallet
→ →<br>`mixingTxCount` | string | Required<br>(exactly 1) | The operator key is present in this wallet
→ →<br>`lastOutboundAttempt` | integer | Required<br>(exactly 1) | Unix epoch time of the last outbound attempted
→ →<br>`lastOutboundAttemptElapsed` | integer | Required<br>(exactly 1) | Elapsed time since last outbound attempt
→ →<br>`lastOutboundSuccess` | integer | Required<br>(exactly 1) |  Unix epoch time of the last successful outbound connection
→ →<br>`lastOutboundSuccessElapsed` | integer | Required<br>(exactly 1) | Elapsed time since last successful outbound attempt

*Example from Dash Core 0.16.0*

``` bash
dash-cli -testnet protx list
```

Result:
``` json
[
  "2b4a07a9b04dc42a0c19b85edb60954a27acaadfe3ee21d0171385778f34e1c2",
  "61e6d780178d353940c4cb9b3073ac0c50792bbcf0b15c1750d2028b71e34929",
  "ca193751f3cbed2aa4f1b33b0acc48c7ed8b9a3679858d69cf23157a4f545176",
  "ba1b3330e16a0876b7a186e7ceb689f03ec646e611e91d7139de021bbf13afdd"
]
```

List of ProTxs which are active/valid at the given chain height.

``` bash
dash-cli -testnet protx list valid false 7090
```

Result:
``` json
[
  "c48a44a9493eae641bea36992bc8c27eaaa33adb1884960f55cd259608d26d2f"
]
```

Detailed list of ProTxs which are active/valid at the given chain height.

``` bash
dash-cli -testnet protx list valid true 7090
```

Result:
``` json
[
  {
    "proTxHash": "c48a44a9493eae641bea36992bc8c27eaaa33adb1884960f55cd259608d26d2f",
    "collateralHash": "e3270ff48c4b802d56ee58d3d53777f7f9c289964e4df0842518075fc81345b1",
    "collateralIndex": 3,
    "collateralAddress": "yYpzTXjVx7A5uohsmW8sRy7TJp4tihVuZg",
    "operatorReward": 0,
    "state": {
      "service": "173.61.30.231:19013",
      "registeredHeight": 7090,
      "lastPaidHeight": 0,
      "PoSePenalty": 0,
      "PoSeRevivedHeight": -1,
      "PoSeBanHeight": -1,
      "revocationReason": 0,
      "ownerAddress": "yTMDce5yEpiPqmgPrPmTj7yAmQPJERUSVy",
      "votingAddress": "yTMDce5yEpiPqmgPrPmTj7yAmQPJERUSVy",
      "payoutAddress": "yU3UdrmS6KpWwBDLQTkp1KjXePwWsMbYdj",
      "pubKeyOperator": "8700add55a28ef22ec042a2f28e25fb4ef04b3024a7c56ad7eed4aebc736f312d18f355370dfb6a5fec9258f464b227e"
    },
    "confirmations": 292830,
    "wallet": {
      "hasOwnerKey": false,
      "hasOperatorKey": false,
      "hasVotingKey": false,
      "ownsCollateral": false,
      "ownsPayeeScript": false,
      "ownsOperatorRewardScript": false
    },
    "metaInfo": {
      "lastDSQ": 0,
      "mixingTxCount": 0,
      "lastOutboundAttempt": 0,
      "lastOutboundAttemptElapsed": 1588171141,
      "lastOutboundSuccess": 0,
      "lastOutboundSuccessElapsed": 1588171141
    }
  }
]
```

## ProTx Info

The `protx info` RPC returns detailed information about a deterministic masternode.

Name | Type | Presence | Description
--- | --- | --- | ---
`result` | object | Required<br>(exactly 1) | An JSON object containing a provider transaction, or JSON `null` if an error occurred
<br>Provider Transaction | object/null | Required<br>(exactly 1) | An object containing a provider transaction
→<br>`proTxHash` | string (hex) | Required<br>(exactly 1) | The hash of the provider transaction as hex in RPC byte order
→<br>`collateralHash` | string (hex) | Required<br>(exactly 1) | The hash of the collateral transaction as hex in RPC byte order
→<br>`collateralIndex` | number (int) | Required<br>(exactly 1) | The collateral index
→ →<br>`collateralAddress` | string (hex) | Required<br>(exactly 1) | The collateral address
→<br>`operatorReward` | number (int) | Required<br>(exactly 1) | The operator reward %
→<br>`state` | object/null | Required<br>(exactly 1) | An object containing a provider transaction state
→ →<br>`service` | string | Required<br>(exactly 1) | The masternode's IP:Port
→ →<br>`registeredHeight` | number (int) | Required<br>(exactly 1) | The height where the masternode was registered
→ →<br>`lastPaidHeight` | number (int) | Required<br>(exactly 1) | The height where the masternode was last paid
→ →<br>`PoSePenalty` | number (int) | Required<br>(exactly 1) | The masternode's proof of service penalty
→ →<br>`PoSeRevivedHeight` | number (int) | Required<br>(exactly 1) | The height where the masternode recovered from a proof of service ban
→ →<br>`PoSeBanHeight` | number (int) | Required<br>(exactly 1) | The height where the masternode was banned for proof of service violations
→ →<br>`revocationReason` | number (int) | Required<br>(exactly 1) | The reason for a ProUpRegTx revocation
→ →<br>`ownerAddress` | string (hex) | Required<br>(exactly 1) | The owner address
→ →<br>`votingAddress` | string (hex) | Required<br>(exactly 1) | The voting address
→ →<br>`payoutAddress` | string (hex) | Required<br>(exactly 1) | The owner's payout address
→ →<br>`pubKeyOperator` | string (hex) | Required<br>(exactly 1) | The operator public key
→ →<br>`operatorPayoutAddress` | string (hex) | Required<br>(exactly 1) | The operator's payout address
→<br>`confirmations` | number (int) | Required<br>(exactly 1) | The number of confirmations this ProTx has
→<br>`wallet` | object/null | Required<br>(exactly 1) | An object containing a wallet details related to this ProTx
→ →<br>`hasOwnerKey` | bool | Required<br>(exactly 1) | The owner key is present in this wallet
→ →<br>`hasOperatorKey` | bool | Required<br>(exactly 1) | The operator key is present in this wallet
→ →<br>`hasVotingKey` | bool | Required<br>(exactly 1) | The voting key is present in this wallet
→ →<br>`ownsCollateral` | bool | Required<br>(exactly 1) | The collateral is owned by this wallet
→ →<br>`ownsPayeeScript` | bool | Required<br>(exactly 1) | The payee script is owned by this wallet
→ →<br>`ownsOperatorRewardScript` | bool | Required<br>(exactly 1) | The operator reward script is owned by this wallet
→<br>`metaInfo` | object/null | Required<br>(exactly 1) | **Added in Dash Core 0.16.0**<br><br>An object containing a metainfo related to this ProTx
→ →<br>`lastDSQ` | string | Required<br>(exactly 1) | The owner key is present in this wallet
→ →<br>`mixingTxCount` | string | Required<br>(exactly 1) | The operator key is present in this wallet
→ →<br>`lastOutboundAttempt` | integer | Required<br>(exactly 1) | Unix epoch time of the last outbound attempted
→ →<br>`lastOutboundAttemptElapsed` | integer | Required<br>(exactly 1) | Elapsed time since last outbound attempt
→ →<br>`lastOutboundSuccess` | integer | Required<br>(exactly 1) |  Unix epoch time of the last successful outbound connection
→ →<br>`lastOutboundSuccessElapsed` | integer | Required<br>(exactly 1) | Elapsed time since last successful outbound attempt


*Example from Dash Core 0.16.0*

``` bash
dash-cli -testnet protx info\
 c48a44a9493eae641bea36992bc8c27eaaa33adb1884960f55cd259608d26d2f
```

Result:
``` json
{
  "proTxHash": "c48a44a9493eae641bea36992bc8c27eaaa33adb1884960f55cd259608d26d2f",
  "collateralHash": "e3270ff48c4b802d56ee58d3d53777f7f9c289964e4df0842518075fc81345b1",
  "collateralIndex": 3,
  "collateralAddress": "yYpzTXjVx7A5uohsmW8sRy7TJp4tihVuZg",
  "operatorReward": 0,
  "state": {
    "service": "173.61.30.231:19013",
    "registeredHeight": 7090,
    "lastPaidHeight": 134608,
    "PoSePenalty": 334,
    "PoSeRevivedHeight": 96516,
    "PoSeBanHeight": 134819,
    "revocationReason": 0,
    "ownerAddress": "yTMDce5yEpiPqmgPrPmTj7yAmQPJERUSVy",
    "votingAddress": "yTMDce5yEpiPqmgPrPmTj7yAmQPJERUSVy",
    "payoutAddress": "yU3UdrmS6KpWwBDLQTkp1KjXePwWsMbYdj",
    "pubKeyOperator": "8700add55a28ef22ec042a2f28e25fb4ef04b3024a7c56ad7eed4aebc736f312d18f355370dfb6a5fec9258f464b227e"
  },
  "confirmations": 292831,
  "wallet": {
    "hasOwnerKey": false,
    "hasOperatorKey": false,
    "hasVotingKey": false,
    "ownsCollateral": false,
    "ownsPayeeScript": false,
    "ownsOperatorRewardScript": false
  },
  "metaInfo": {
    "lastDSQ": 0,
    "mixingTxCount": 0,
    "lastOutboundAttempt": 0,
    "lastOutboundAttemptElapsed": 1588171300,
    "lastOutboundSuccess": 0,
    "lastOutboundSuccessElapsed": 1588171300
  }
}
```

## ProTx Update Service

The `protx update_service` RPC creates and sends a ProUpServTx to the network.

*Parameter #1---initial provider registration transaction hash*

Name | Type | Presence | Description
--- | --- | --- | ---
`proTxHash` | string (hex) | Required<br>(exactly 1) | The hash of the provider transaction as hex in RPC byte order

*Parameter #2---IP Address and port*

Name | Type | Presence | Description
--- | --- | --- | ---
`ipAndPort` | string | Required<br>(exactly 1) | IP and port in the form 'IP:PORT'.<br>Must be unique on the network.

*Parameter #3---operator public key*

Name | Type | Presence | Description
--- | --- | --- | ---
`operatorPubKey` | string (hex) | Required<br>(exactly 1) |  The operator public key. The private key does not have to be known. It has to match the private key which is later used when operating the masternode.

*Parameter #4---operator payout address*

Name | Type | Presence | Description
--- | --- | --- | ---
`operatorPayoutAddress` | string (hex) | Optional<br>(0 or 1) | The Dash address used for operator reward payments. Only allowed when the ProRegTx had a non-zero `operatorReward` value. If set to an empty string, the currently active payout address is reused.

*Parameter #5---fee source address*

Name | Type | Presence | Description
--- | --- | --- | ---
`feeSourceAddress` | string | Optional<br>(0 or 1) | If specified, the wallet will only use coins from this address to fund the ProTx. If not specified, `operatorPayoutAddress` will be used. The private key belonging to this address must be known in your wallet.

*Result---provider update service transaction hash*

Name | Type | Presence | Description
--- | --- | --- | ---
`result` | string (hex) | Required<br>(exactly 1) | Provider update service transaction (ProUpServTx) hash

*Example from Dash Core 0.13.0*

``` bash
dash-cli -testnet protx update_service\
 ba1b3330e16a0876b7a186e7ceb689f03ec646e611e91d7139de021bbf13afdd\
 "4.3.2.1:4321"\
 4da7e1ea30fb9e55c73ad23df0b9d3d34342acb24facf4b19420e1a26ae272d1
```

Result:
``` bash
5b6cfa1bdd3c8b7e0b9550b9c4e809381f81a410bc7f241d3879dd736fd51270
```

## ProTx Update Registrar

The `protx update_registrar` RPC creates and sends a ProUpRegTx to the network.

*Parameter #1---initial provider registration transaction hash*

Name | Type | Presence | Description
--- | --- | --- | ---
`proTxHash` | string (hex) | Required<br>(exactly 1) | The hash of the provider transaction as hex in RPC byte order

*Parameter #2---operator public key*

Name | Type | Presence | Description
--- | --- | --- | ---
`operatorPubKey` | string (hex) | Required<br>(exactly 1) | The operator public key. The private key does not have to be known. It has to match the private key which is later used when operating the masternode. If set to an empty string, the currently active operator BLS public key is reused.

*Parameter #3---voting address*

Name | Type | Presence | Description
--- | --- | --- | ---
`votingAddress` | string (hex) | Required<br>(exactly 1) | The voting address. The private key does not have to be known by your wallet. It has to match the private key which is later used when voting on proposals. If set to an empty string, the currently active voting key address is reused.

*Parameter #4---operator payout address*

Name | Type | Presence | Description
--- | --- | --- | ---
`payoutAddress` | string (hex) | Optional<br>(0 or 1) | The Dash address to use for masternode reward payments. If set to an empty string, the currently active payout address is reused.

*Parameter #5---fee source address*

Name | Type | Presence | Description
--- | --- | --- | ---
`feeSourceAddress` | string | Optional<br>(0 or 1) | If specified, the wallet will only use coins from this address to fund the ProTx. If not specified, `payoutAddress` will be used. The private key belonging to this address must be known in your wallet.

*Result---provider update registrar transaction hash*

Name | Type | Presence | Description
--- | --- | --- | ---
`result` | string (hex) | Required<br>(exactly 1) | Provider update registrar transaction (ProUpRegTx) hash

*Example from Dash Core 0.13.0*

``` bash
dash-cli -testnet protx update_registrar\
 "ba1b3330e16a0876b7a186e7ceb689f03ec646e611e91d7139de021bbf13afdd"\
 "0e02146e9c34cfbcb3f3037574a1abb35525e2ca0c3c6901dbf82ac591e30218d1711223b7ca956edf39f3d984d06d51"\
 "yX2cDS4kcJ4LK4uq9Hd4TG7kURV3sGLZrw" "yakx4mMRptKhgfjedNzX5FGQq7kSSBF2e7"
```

Result:
``` bash
702390ef06b10c174841ad7b863df23c166c27815e3be2438e2fee6f87882b91
```

## ProTx Revoke

The `protx revoke` RPC creates and sends a ProUpRevTx to the network.

*Parameter #1---initial provider registration transaction hash*

Name | Type | Presence | Description
--- | --- | --- | ---
`proTxHash` | string (hex) | Required<br>(exactly 1) | The hash of the provider transaction as hex in RPC byte order

*Parameter #2---operator private key*

Name | Type | Presence | Description
--- | --- | --- | ---
`operatorPubKey` | string (hex) | Required<br>(exactly 1) |  The operator private key belonging to the registered operator public key.

*Parameter #3---reason*

Name | Type | Presence | Description
--- | --- | --- | ---
`reason` | number | Required<br>(exactly 1) | The reason for revocation.

*Parameter #4---fee source address*

Name | Type | Presence | Description
--- | --- | --- | ---
`feeSourceAddress` | string | Optional<br>(0 or 1) | If specified, the wallet will only use coins from this address to fund the ProTx. If not specified, `payoutAddress` will be used. The private key belonging to this address must be known in your wallet.

*Result---provider update revoke transaction hash*

Name | Type | Presence | Description
--- | --- | --- | ---
`result` | string (hex) | Required<br>(exactly 1) | Provider update revoke transaction (ProUpRevTx) hash

*Example from Dash Core 0.13.0*

``` bash
dash-cli -testnet protx revoke\
 "ba1b3330e16a0876b7a186e7ceb689f03ec646e611e91d7139de021bbf13afdd"\
 "4da7e1ea30fb9e55c73ad23df0b9d3d34342acb24facf4b19420e1a26ae272d1"
```

Result:
``` bash
2aad36dd2ab254bee06b0b5dad51e7603691b72058d5806fd94e1d2d19a7c209
```

## ProTx Diff

The `protx diff` RPC calculates a diff and a proof between two masternode list.

*Parameter #1---start block height*

Name | Type | Presence | Description
--- | --- | --- | ---
`baseBlock` | number (int) | Required<br>(Exactly 1) |

*Parameter #2---end block height*

Name | Type | Presence | Description
--- | --- | --- | ---
`block` | bool | Required<br>(Exactly 1) |

*Result---JSON provider registration transaction details*

Name | Type | Presence | Description
--- | --- | --- | ---
`result` | array | Required<br>(exactly 1) | An array of objects each containing a provider transaction, or JSON `null` if an error occurred
→<br>`baseBlockHash` | string (hex) | Required<br>(exactly 1) | The hash of the base block as hex in RPC byte order
→<br>`blockHash` | string (hex) | Required<br>(exactly 1) | The hash of the ending block as hex in RPC byte order
→<br>`cbTxMerkleTree` | string (hex) | Required<br>(exactly 1) | The coinbase transaction merkle tree
→<br>`cbTx` | string (hex) | Required<br>(exactly 1) | The coinbase transaction
→<br>`deletedMNs` | array | Required<br>(exactly 1) | An array of deleted masternode hashes
→<br>`mnlist` | array | Required<br>(exactly 1) | An array of masternode details
→ →<br>`proRegTxHash` | string (hex) | Required<br>(exactly 1) | The hash of the initial provider registration transaction as hex in RPC byte order
→ →<br>`confirmedHash` | string (hex) | Required<br>(exactly 1) | The hash of the block where the ProRegTx was mined
→ →<br>`service` | string | Required<br>(exactly 1) | The IP address/Port of the masternode
→ →<br>`pubKeyOperator` | string (hex) | Required<br>(exactly 1) | The operator public key
→ →<br>`votingAddress` | string (hex) | Required<br>(exactly 1) | The voting address
→ →<br>`isValid` | bool | Required<br>(exactly 1) | Set to `true` if masternode is valid
→<br>`deletedQuorums` | array | Required<br>(exactly 1) | An array of deleted quorums
→ →<br>`llmqType` | number | Required<br>(exactly 1) | The quorum type
→ →<br>`quorumHash` | string (hex) | Required<br>(exactly 1) | The hash of the quorum
→<br>`newQuorums` | array | Required<br>(exactly 1) | An array of new quorums
→ →<br>`version` | number | Required<br>(exactly 1) | The quorum version
→ →<br>`llmqType` | number | Required<br>(exactly 1) | The quorum type
→ →<br>`quorumHash` | string (hex) | Required<br>(exactly 1) | The hash of the quorum
→ →<br>`signersCount` | number | Required<br>(exactly 1) | The number of signers for the quorum
→ →<br>`signers` | string (hex) | Required<br>(exactly 1) | **Added in Dash Core 0.16.0**<br><br>Bitset representing the aggregated signers of this final commitment
→ →<br>`validMembersCount` | number | Required<br>(exactly 1) | The number of valid members in the quorum
→ →<br>`validMembers` | string (hex) | Required<br>(exactly 1) | **Added in Dash Core 0.16.0**<br><br>Bitset of valid members in this commitment
→ →<br>`quorumPublicKey` | string (hex) | Required<br>(exactly 1) | The public key of the quorum
→ →<br>`quorumVvecHash` | string (hex) | Required<br>(exactly 1) | **Added in Dash Core 0.16.0**<br><br>The SHA256 hash of the quorum verification vector
→ →<br>`quorumSig` | string (hex) | Required<br>(exactly 1) | **Added in Dash Core 0.16.0**<br><br>Recovered threshold signature
→ →<br>`membersSig` | string (hex) | Required<br>(exactly 1) | **Added in Dash Core 0.16.0**<br><br>Aggregated BLS signatures from all included commitments
→<br>`merkleRootMNList` | string (hex) | Required<br>(exactly 1) | Merkle root of the masternode list
→<br>`merkleRootQuorums` | string (hex) | Required<br>(exactly 1) | *Added in Coinbase Transaction version 2 (Dash Core 0.14.0)*<br><br>Merkle root of the masternode list

*Example from Dash Core 0.16.0*

``` bash
dash-cli -testnet protx diff 75000 76000
```

Result (truncated):
``` json
{
  "baseBlockHash": "0000000003deb00bba101ee581cdc4e1cbd1243ec5cd190472ae93eff07c8881",
  "blockHash": "0000000000c0279636003ed0042c9a454b4c39e9a6c49bb92d420e0bf4e0f49b",
  "cbTxMerkleTree": "01000000015ef8245e2a381174f5e2cc701d5d067d9f16945179380a3ce54415114426eb510101",
  "cbTx": "03000500010000000000000000000000000000000000000000000000000000000000000000ffffffff4c03e02801043619ab5c08fabe6d6d736170747365743a7265737574736574d6e48c2ebd4e147373617074736574730100000000000000380000ae250000000d2f6e6f64655374726174756d2f000000000340230e43000000001976a914cb594917ad4e5849688ec63f29a0f7f3badb5da688ac4cfe1c3e000000001976a91470da282ad16926e127064b7d3d787d7f3793014788acf424f104000000001976a914312d9ccd4e73f2e66006e45701bce17125ba681e88ac00000000260100e0280100d26df127ba2765c8f098ab71199c82c59509418efe26cdf02f7c92ce738e2247",
  "deletedMNs": [
  ],
  "mnList": [
    {
      "proRegTxHash": "fef106ff6420f9c6638c9676988a8fc655750caafb506c98cb5ff3d4fea99a41",
      "confirmedHash": "0000000005d5635228f113b50fb5ad66995a7476ed20374e6e159f1f9e62347b",
      "service": "45.48.177.222:19999",
      "pubKeyOperator": "842476e8d82327adfb9b617a7ac3f62868946c0c4b6b0e365747cfb8825b8b79ba0eb1fa62e8583ae7102f59bf70c7c7",
      "votingAddress": "yf7QHemCfbmKEncwZxroTj8JtShXsC28V6",
      "isValid": true
    },
    {
      "proRegTxHash": "7d56a2cf814b344f54ac4b6485a7a5b2b5a439ea796defff67f2a5872c9df5c3",
      "confirmedHash": "00000c66555eea6272e5c7bcdb2648e1a63fd5b23a6d1d4c3f9dc5df43c6a5a8",
      "service": "178.151.192.107:19999",
      "pubKeyOperator": "8631b1ba19ed23fdab61db7a81c9aa1356eaf37d0a29a14cc493e2f863080bf909b4d3e23d536be1d18e4c842566ed67",
      "votingAddress": "yP2LXCZTVVjBFQiN2bhghQvNwdUQG8NMX8",
      "isValid": true
    },
    {
      "proRegTxHash": "be32ec53dbbfb64e5ba29e25e3716f6f4024291914ce4c858cd69f0b4e371dda",
      "confirmedHash": "0000000015717296254a7c6139a50c34ad481dc8fdf7b0ea4c8320dc3fff2759",
      "service": "173.61.30.231:19025",
      "pubKeyOperator": "86ce02e551a46f1ca9a734104b4e387984d733ba99930eb677aae126fa142f201049842422ab2f105e3c9805f1bd54e8",
      "votingAddress": "ySBU7oXuuTSJqtmUArMRFsKefJPtEDkESG",
      "isValid": false
    }
  ],
  "deletedQuorums": [
    {
      "llmqType": 1,
      "quorumHash": "00000000052b95b036c87f82d19878f69bf940e6acf9f03cd818bd07a5686d0e"
    },
    {
      "llmqType": 1,
      "quorumHash": "0000000000e8b557ea26921f4bb143e961dd35209cf8c1c7b73397322c1a5018"
    },
    {
      "llmqType": 1,
      "quorumHash": "000000000b259f422fe3b647b8f1553b846d95dc8c79699d60e48a81dcf14747"
    },
    {
      "llmqType": 1,
      "quorumHash": "00000000143365adb3c3de6a35ae247120df8ca53a61afd82cd6fd4126ca8a4d"
    }
  ],
  "newQuorums": [
    {
      "version": 1,
      "llmqType": 1,
      "quorumHash": "0000000001427858db64213ed3ef32ffb2546ca7f2a096adbefc197437b90612",
      "signersCount": 50,
      "signers": "ffffffffffff03",
      "validMembersCount": 50,
      "validMembers": "ffffffffffff03",
      "quorumPublicKey": "922e3683358f09a2619efb9e8329f90d5a8a608a18e26db212613ef7f95818eb6f68372fb313edbf96fdd2cdee20a66d",
      "quorumVvecHash": "2da4253e43adb732b06d88324384025a4cd0c2803bc6400462f9eb89ea314da8",
      "quorumSig": "949882d7912d7d3fef46dd856bcd6c70a080b2e5484a3c900bea04b902abd12c5f75e78d13cbdc5d352187db0e15c1b40715b9d89e998bb99437ad7ae97a1b23f922d55b6fc5cca290c05b44eda564782a3440c7ef3756fc3e9895d1ac34d3d0",
      "membersSig": "9736d9cbc7ff7189f6ef543fabc9bfc2785f60ffd4493ea4c272343da51fa61ec9867cd46b681c82a1c22a9830f8b86b0a02e34e9e71212010231024fd61cb95143591be2cace53760dba03a325e178e5fcae6a748073fadf3ab34268c8ed2bc"
    },
    {
      "version": 1,
      "llmqType": 1,
      "quorumHash": "000000000148a6fced08763f3f31dd68a3d88d2d4f2d48eef44eb9311de66129",
      "signersCount": 50,
      "signers": "ffffffffffff03",
      "validMembersCount": 50,
      "validMembers": "ffffffffffff03",
      "quorumPublicKey": "814973fcf54892fa4edbf9e732341ff1227e2a89bf59cb22b52082e940f7c3ac8a7c25163cb375b3cfe3654e86eaa65d",
      "quorumVvecHash": "a91c4721c576850971313b9eb5ee7a886fd4dd4564e98ac0094e7a46e4351240",
      "quorumSig": "16abcfa4137c1900899970533cd52b0c264000b48ca6bd1d29cc9baab1ef883b378d5cdb8c1dd8bb7765e154bcc8ee360cfcdc008584e2d7c29f5be8361fecf3a4cafcdea29f1cb2e75c5d67057d0557e0d6cfa65cf85ae6ed65971b8f29a913",
      "membersSig": "18151a0b15e9ec892ae7ebc97b9e014bbe8a7f8344d24fe9f2925dae094e01500c6d5eb13b1ac6a8487be63e181a2b73053658f6b6374a01d183be1d4258ddaf0b18a4268a8a1e7d0c7ecfa414ad075d915beff5750d8ecef48b446b9c0d1da6"
    },
    {
      "version": 1,
      "llmqType": 1,
      "quorumHash": "0000000009931a8a6dcdf21a869739356e7715eb155c1a18a58c8bf13382ac33",
      "signersCount": 50,
      "signers": "ffffffffffff03",
      "validMembersCount": 50,
      "validMembers": "ffffffffffff03",
      "quorumPublicKey": "0694b46d8581423f2f68196dcc2d06be0b6b365a4100b54e351ab42f5828d09fd03941f8a1255363753a53d32b43f63b",
      "quorumVvecHash": "e0f2853af9fffc937af96264316982728fbbe483a36bff161c606f764ad9d8b9",
      "quorumSig": "16898292e519f01681c1a57606c54b7366275fa01a4912f8623eae73517ae1d3fd1607b7e8edcee43ce23141deba29fb00398d60f319adca9d460b972653715a4c5025a92141f065d92a0494cf211aa7485d6e4819514012efb107e8e2b9ba2e",
      "membersSig": "884a01e0ed65b745076198183883535d7bf636c7ebf9e13deb662ec4f4b202041fa826c978c9973380d614d11fd4071e0cf97abb3a7dd3a24f2eda0d8d7b179ab1a5837a78c53673567565aa3aaa72122d0e0bb8b6f2df092ca3da626c2b2800"
    },
    {
      "version": 1,
      "llmqType": 1,
      "quorumHash": "0000000006097e9d08a4ca9bedbe4a97bb9bf3fe8d09372d18d2398f185cff5d",
      "signersCount": 50,
      "signers": "ffffffffffff03",
      "validMembersCount": 50,
      "validMembers": "ffffffffffff03",
      "quorumPublicKey": "10d0488558afd929508cd2d11bda7564333a904aa23c8b4a1ed57d86b217e3181497469e7220e9421e14f645a00940fc",
      "quorumVvecHash": "fbe6b3ae8d002bd648788b3173753c9cec3d4634b7df55f19b34d632b438aa70",
      "quorumSig": "17d3c06ae24312c9cda1b0f5db10b16e1d1a356f6bb050827d066c5026ecd3cd26fbd2479d781c88a2755aa78f9e16a50882bf18c75e1ab96ff1514b1f283d4fb3b10b4dcd13f8f267ec449250e7d195bc27351a74c8c456a6fcf7d847535f05",
      "membersSig": "0afd25e67d72d59c2dfbc671ae4e8163bfa2e75cda50b0c86800be5e1dd393abf8a717b147392688855f505d237154f8195b2bb30605d0ca18407e4552b7573cb08a6cb53eaf2a71894fb937af1f7783dbf5e6cb80b0cb903ea4f76266c039e7"
    }
  ],
  "merkleRootMNList": "47228e73ce927c2ff0cd26fe8e410995c5829c1971ab98f0c86527ba27f16dd2"
}
```

*See also: none*

# Quorum

*Added in Dash Core 0.14.0*

The [`quorum` RPC](core-api-ref-remote-procedure-calls-evo#quorum) provides a set of commands for quorums (LLMQs).

## Quorum List

The `quorum list` RPC displays a list of on-chain quorums.

*Parameter #1---quorum count*

Name | Type | Presence | Description
--- | --- | --- | ---
`count` | number | Optional<br>(0 or 1) | Number of quorums to list. Will list active quorums if `count` is not specified.

*Result---a list of quorums*

Name | Type | Presence | Description
--- | --- | --- | ---
`result` | object | Required<br>(exactly 1) | Quorum list
→<br>Quorum | array | Required<br>(1 or more) | Array of quorum details
→ →<br>Quorum Hash | string (hex) | Optional<br>(0 or more) | A quorum hash

*Example from Dash Core 0.14.0*

``` bash
dash-cli -testnet quorum list
```

Result:
``` json
{
  "llmq_50_60": [
    "00000000023cc6dde69bed898c83fe2328ef38b1ea9da14a599efa14caef0b7d",
    "000000002b968fb3b2fc2ff18d6e89611e366b4d38a6d0437e99bd7c37f2fd83",
    "000000000301054c038b07b5b51493d5efc3f078e3aede6eb603c47943d1cc78",
    "000000000e901278c00c896754a06f8d45d0268c6aff6e72ffb3007d07c10e73",
    "000000001bc592f2a8676203835bc6ad442abeadb9c22b8d6a2999db07354b01",
    "000000000896c37ef8a32318ee871589394f1578473b8825275b610690e47db0",
    "00000000133b192b2319a0716ad18e5788981fff51856f61205af5d6a634ba41",
    "0000000004946f3f9f82a298985f73080d62627d51f6f4ba77f3cd8c6788b3d0",
    "0000000005cb014d3df9bac0ba379f1d5b8b75f0e6d7c408d43ac1db330ec641",
    "0000000006c1653c7ee747f140dd7daa1da23a541e67a0fc0dc88db3482ec4d5"
  ],
  "llmq_400_60": [
    "0000000007697fd69a799bfa26576a177e817bc0e45b9fcfbf48b362b05aeff2"
  ],
  "llmq_400_85": [
  ]
}
```

## Quorum Info

The `quorum info` RPC returns information about a specific quorum.

*Parameter #1---LLMQ Type*

Name | Type | Presence | Description
--- | --- | --- | ---
`llmqType` | number | Required<br>(exactly 1) | [Type of quorums](https://github.com/dashpay/dips/blob/master/dip-0006.md#current-llmq-types) to list:<br>`1` - LLMQ_50_60<br>`2` - LLMQ_400_60<br>`3` - LLMQ_400_85

*Parameter #2---quorum hash*

Name | Type | Presence | Description
--- | --- | --- | ---
`quorumHash` | string (hex) | Required<br>(exactly 1) | The block hash of the quorum

*Parameter #3---secret key share*

Name | Type | Presence | Description
--- | --- | --- | ---
`includeSkShare` | bool | Optional<br>(0 or 1) | Include the secret key share (default: `false`)

*Result---information about a quorum*

Name | Type | Presence | Description
--- | --- | --- | ---
`result` | object | Required<br>(exactly 1) | Quorum list
→<br>`height` | number | Required<br>(exactly 1) | Block height of the quorum
→<br>`type` | string | Required<br>(exactly 1) | Type of LLMQ
→<br>`quorumHash` | string (hex) | Required<br>(exactly 1) | The hash of the quorum
→<br>`minedBlock` | string (hex) | Required<br>(exactly 1) | The hash of the block that established the quorum
→<br>`members` | array | Required<br>(exactly 1) | An array containing quorum member details
→ →<br>Member | object | Required<br>(1 or more) | An object describing a particular member
→ → →<br>`proTxHash` | string (hex) | Required<br>(exactly 1) | The masternode's Provider Registration transaction hash
→ → →<br>`pubKeyOperator` | string (hex) | Required<br>(exactly 1) | *Added in Dash Core 0.15.0*<br><br>The masternode's Operator public key
→ → →<br>`valid` | bool | Required<br>(exactly 1) | Indicates if the member is valid
→ → →<br>`pubKeyShare` | string | Optional<br>(0 or 1) | Member public key share
→<br>`quorumPublicKey` | string | Required<br>(exactly 1) | Quorum public key
→<br>`secretKeyShare` | string | Optional<br>(exactly 1) | Quorum secret key share

*Example from Dash Core 0.15.0*

``` bash
dash-cli -testnet quorum info 1 \
  000004bfc56646880bfeb80a0b89ad955e557ead7b0f09bcc61e56c8473eaea9 true
```

Result (truncated):
``` json
{
  "height": 264072,
  "type": "llmq_50_60",
  "quorumHash": "000004bfc56646880bfeb80a0b89ad955e557ead7b0f09bcc61e56c8473eaea9",
  "minedBlock": "000006113a77b35a0ed606b08ecb8e37f1ac7e2d773c365bd07064a72ae9a61d",
  "members": [
    {
      "proTxHash": "6c91363d97b286e921afb5cf7672c88a2f1614d36d32058c34bef8b44e026007",
      "pubKeyOperator": "81749ba8363e5c03e9d6318b0491e38305cf59d9d57cea2295a86ecfa696622571f266c28bacc78666e8b9b0fb2b3121",
      "valid": true
    },
    {
      "proTxHash": "274ae6ab38ea0f3b8fe726b3e52d998443ba0d77e85d88c20d179d4fecd0b96e",
      "pubKeyOperator": "0db6da5d8ee9fb8925f0818df7553062bf35ec9d62114144bc395980c29fcd06b738beca63faf265d7480106fc6cceea",
      "valid": true
    },
    {"Truncated data":"..."},
    {
      "proTxHash": "3ecdbedf3d9a13822f437a1f0c5ea44f290ab90f7c3bb42c1b5fd785b5f9596a",
      "pubKeyOperator": "0634f8b926631cb2b14c81720c6130b3f6f5429da1c9dc9c33918b2474b7ffff239caa9b59c7b1a782565052232d052a",
      "valid": true
    }
  ],
  "quorumPublicKey": "0644ff153b9b92c6a59e2adf4ef0b9836f7f6af05fe432ffdcb69bc9e300a2a70af4a8d9fc61323f6b81074d740033d2",
  "secretKeyShare": "3da0d8f532309660f7f44aa0ed42c1569773b39c70f5771ce5604be77e50759e"
}
```

## Quorum DKGStatus

The `quorum list` RPC displays the status of the current DKG process.

*Parameter #1---detail level*

Name | Type | Presence | Description
--- | --- | --- | ---
`detail_level` | number | Optional<br>(0 or 1) | Detail level of output (default: 0):<br>`0` - Only show counts (_default_)<br>`1` - Show member indexes<br>`2` - Show member's ProTxHashes<br><br>_Note: Works only when Spork 17 is enabled and only displays details related to the node running the command._

*Result (if detail level was 0 or omitted)---JSON DKG details*

Name | Type | Presence | Description
--- | --- | --- | ---
`result` | array | Required<br>(exactly 1) | An array of objects each containing a provider transaction, or JSON `null` if an error occurred
→<br>`proTxHash` | string (hex) | Required<br>(exactly 1) | The hash of the initial provider registration transaction as hex in RPC byte order
→<br>`time` | string (hex) | Required<br>(exactly 1) | The Unix epoch time
→<br>`timeStr` | string (hex) | Required<br>(exactly 1) | The UTC time as a string
→<br>`session` | object | Required<br>(exactly 1) | Object containing DKG Session information
→ →<br>LLMQ Type | object | Required<br>(exactly 1) | Object
→ → →<br>`llmqType` | number | Required<br>(exactly 1) | [Type of quorum](https://github.com/dashpay/dips/blob/master/dip-0006.md#current-llmq-types):<br>`1` - LLMQ_50_60<br>`2` - LLMQ_400_60<br>`3` - LLMQ_400_85
→ → →<br>`quorumHash` | string (hex) | Required<br>(exactly 1) | The block hash of the quorum
→ → →<br>`quorumHeight` | number | Required<br>(exactly 1) | The block height of the quorum
→ → →<br>`phase` | number | Required<br>(exactly 1) | The active DKG phase<br>`1` - Initialized<br>`2` - Contributing<br>`3` - Complaining<br>`4` - Justifying<br>`5` - Committing<br>`6` - Finalizing
→ → →<br>`sentContributions` | bool | Required<br>(exactly 1) | True when contributions have been sent
→ → →<br>`sentComplaint` | bool | Required<br>(exactly 1) | True when complaints have been sent
→ → →<br>`sentJustification` | bool | Required<br>(exactly 1) | True when justifications have been sent
→ → →<br>`sentPrematureCommitment` | bool | Required<br>(exactly 1) | True when premature commitments have been sent
→ → →<br>`aborted` | bool | Required<br>(exactly 1) | True if the DKG session has been aborted
→ → →<br>`badMembers` | number | Required<br>(exactly 1) | Number of bad members
→ → →<br>`weComplain` | number | Required<br>(exactly 1) | Number of complaints sent
→ → →<br>`receivedContributions` | number | Required<br>(exactly 1) | Number of contributions received
→ → →<br>`receivedComplaints` | number | Required<br>(exactly 1) | Number of complaints received
→ → →<br>`receivedJustifications` | number | Required<br>(exactly 1) | Number of justifications received
→ → →<br>`receivedPrematureCommitments` | number | Required<br>(exactly 1) | Number of premature commitments received
→<br>`minableCommitments` | object | Required<br>(exactly 1) | Object containing minable commitments
→<br>`quorumConnections` | object | Required<br>(exactly 1) | **Added in Dash Core 0.16.0**<br><br>Object containing quorum connection information
→ →<br>Connection | object | Required<br>(exactly 1) | **Added in Dash Core 0.16.0**<br><br>An object describing a quorum connection
→ → →<br>`proTxHash` | string (hex) | Required<br>(exactly 1) | **Added in Dash Core 0.16.0**<br><br>The hash of the quorum member's provider registration transaction as hex in RPC byte order
→ → →<br>`connected` | boolean | Required<br>(exactly 1) | **Added in Dash Core 0.16.0**<br><br>Whether or not the connection is active
→ → →<br>`address` | string | Optional<br>(exactly 1) | **Added in Dash Core 0.16.0**<br><br>Address
→ → →<br>`outbound` | boolean | Required<br>(exactly 1) | **Added in Dash Core 0.16.0**<br><br>Whether or not this is an outbound connection

*Result (if detail level was 1)---JSON DKG details including member index*

Note: detail level 1 includes all level 0 fields and expands the following fields.

Name | Type | Presence | Description
--- | --- | --- | ---
→ → →<br>`badMembers` | array | Required<br>(exactly 1) | Array containing the member index for each bad member
→ → →<br>`weComplain` | array | Required<br>(exactly 1) | Array containing the member index for each complaint sent
→ → →<br>`receivedContributions` | array | Required<br>(exactly 1) | Array containing the member index for each contribution received
→ → →<br>`receivedComplaints` | array | Required<br>(exactly 1) | Array containing the member index for each complaint received
→ → →<br>`receivedJustifications` | array | Required<br>(exactly 1) | Array containing the member index for each justification received
→ → →<br>`receivedPrematureCommitments` | array | Required<br>(exactly 1) | Array containing the member index for each commitment received

*Result (if detail level was 2)---JSON DKG details including member index and ProTx hash*

Note: detail level 2 includes all level 0 fields, adds the `allMembers` field, and expands several fields.

Name | Type | Presence | Description
--- | --- | --- | ---
→ → →<br>`badMembers` | array | Required<br>(exactly 1) | An array of objects with each object containing the member index and ProTx hash for a bad member
→ → → →<br>Member | object | Required<br>(0 or more) | An object describing quorum member details
→ → → → →<br>`memberIndex` | number | Required<br>(exactly 1) | The quorum member's index
→ → → → →<br>`proTxHash` | string (hex) | Required<br>(exactly 1) | The hash of the quorum member's provider registration transaction as hex in RPC byte order
→ → →<br>`weComplain` | object | Required<br>(exactly 1) | An array of objects with each object containing the member index and ProTx hash for a member being complained about
→ → → →<br>Member | object | Required<br>(0 or more) | An object describing quorum member details
→ → → → →<br>`memberIndex` | number | Required<br>(exactly 1) | The quorum member's index
→ → → → →<br>`proTxHash` | string (hex) | Required<br>(exactly 1) | The hash of the quorum member's provider registration transaction as hex in RPC byte order
→ → →<br>`receivedContributions` | object | Required<br>(exactly 1) | An array of objects with each object containing the member index and ProTx hash for a member a contribution was received from
→ → → →<br>Member | object | Required<br>(0 or more) | An object describing quorum member details
→ → → → →<br>`memberIndex` | number | Required<br>(exactly 1) | The quorum member's index
→ → → → →<br>`proTxHash` | string (hex) | Required<br>(exactly 1) | The hash of the quorum member's provider registration transaction as hex in RPC byte order
→ → →<br>`receivedComplaints` | object | Required<br>(exactly 1) | An array of objects with each object containing the member index and ProTx hash for a member a complaint was received from
→ → → →<br>Member | object | Required<br>(0 or more) | An object describing quorum member details
→ → → → →<br>`memberIndex` | number | Required<br>(exactly 1) | The quorum member's index
→ → → → →<br>`proTxHash` | string (hex) | Required<br>(exactly 1) | The hash of the quorum member's provider registration transaction as hex in RPC byte order
→ → →<br>`receivedJustifications` | object | Required<br>(exactly 1) | An array of objects with each object containing the member index and ProTx hash for a member a justification was received from
→ → → →<br>Member | object | Required<br>(0 or more) | An object describing quorum member details
→ → → → →<br>`memberIndex` | number | Required<br>(exactly 1) | The quorum member's index
→ → → → →<br>`proTxHash` | string (hex) | Required<br>(exactly 1) | The hash of the quorum member's provider registration transaction as hex in RPC byte order
→ → →<br>`receivedPrematureCommitments` | object | Required<br>(exactly 1) | An array of objects with each object containing the member index and ProTx hash for a member a premature commitment was received from
→ → → →<br>Member | object | Required<br>(0 or more) | An object describing quorum member details
→ → → → →<br>`memberIndex` | number | Required<br>(exactly 1) | The quorum member's index
→ → → → →<br>`proTxHash` | string (hex) | Required<br>(exactly 1) | The hash of the quorum member's provider registration transaction as hex in RPC byte order
→ → →<br>`allMembers` | array | Required<br>(exactly 1) | Array containing the provider registration transaction hash for all quorum members

*Example from Dash Core 0.14.0*

``` bash
dash-cli -testnet quorum dkgstatus
```

Result:
``` json
{
  "proTxHash": "04d06d16b3eca2f104ef9749d0c1c17d183eb1b4fe3a16808fd70464f03bcd63",
  "time": 1555172494,
  "timeStr": "2019-04-13 16:21:34",
  "session": {
    "llmq_50_60": {
      "llmqType": 1,
      "quorumHash": "000000000122768294b19a5f6750094f6e9caa135c0826372d0538d4ceb910bc",
      "quorumHeight": 79368,
      "phase": 6,
      "sentContributions": true,
      "sentComplaint": true,
      "sentJustification": false,
      "sentPrematureCommitment": true,
      "aborted": false,
      "badMembers": 2,
      "weComplain": 0,
      "receivedContributions": 48,
      "receivedComplaints": 44,
      "receivedJustifications": 0,
      "receivedPrematureCommitments": 44
    }
  },
  "minableCommitments": {
    "llmq_50_60": {
      "version": 1,
      "llmqType": 1,
      "quorumHash": "000000000122768294b19a5f6750094f6e9caa135c0826372d0538d4ceb910bc",
      "signersCount": 0,
      "validMembersCount": 0,
      "quorumPublicKey": "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
    }
  }
}
```

*Example from Dash Core 0.14.0 (detail_level: 1)*

``` bash
dash-cli -testnet quorum dkgstatus 1
```

Result:
``` json
{
  "proTxHash": "04d06d16b3eca2f104ef9749d0c1c17d183eb1b4fe3a16808fd70464f03bcd63",
  "time": 1555172494,
  "timeStr": "2019-04-13 16:21:34",
  "session": {
    "llmq_50_60": {
      "llmqType": 1,
      "quorumHash": "000000000122768294b19a5f6750094f6e9caa135c0826372d0538d4ceb910bc",
      "quorumHeight": 79368,
      "phase": 6,
      "sentContributions": true,
      "sentComplaint": true,
      "sentJustification": false,
      "sentPrematureCommitment": true,
      "aborted": false,
      "badMembers": [
        35,
        42
      ],
      "weComplain": [
      ],
      "receivedContributions": [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24,
        25,
        26,
        27,
        28,
        29,
        30,
        31,
        32,
        33,
        34,
        36,
        37,
        38,
        39,
        40,
        41,
        43,
        44,
        45,
        46,
        47,
        48,
        49
      ],
      "receivedComplaints": [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        24,
        25,
        26,
        27,
        28,
        29,
        30,
        31,
        33,
        34,
        36,
        37,
        38,
        39,
        40,
        41,
        43,
        44,
        45,
        46,
        47,
        48,
        49
      ],
      "receivedJustifications": [
      ],
      "receivedPrematureCommitments": [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        24,
        25,
        26,
        27,
        28,
        29,
        30,
        31,
        33,
        34,
        36,
        37,
        38,
        39,
        40,
        41,
        43,
        44,
        45,
        46,
        47,
        48,
        49
      ]
    }
  },
  "minableCommitments": {
    "llmq_50_60": {
      "version": 1,
      "llmqType": 1,
      "quorumHash": "000000000122768294b19a5f6750094f6e9caa135c0826372d0538d4ceb910bc",
      "signersCount": 0,
      "validMembersCount": 0,
      "quorumPublicKey": "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
    }
  }
}
```

*Example from Dash Core 0.14.0 (detail_level: 2)*

``` bash
dash-cli -testnet quorum dkgstatus 2
```

Result:
``` json
{
  "proTxHash": "04d06d16b3eca2f104ef9749d0c1c17d183eb1b4fe3a16808fd70464f03bcd63",
  "time": 1555172494,
  "timeStr": "2019-04-13 16:21:34",
  "session": {
    "llmq_50_60": {
      "llmqType": 1,
      "quorumHash": "000000000122768294b19a5f6750094f6e9caa135c0826372d0538d4ceb910bc",
      "quorumHeight": 79368,
      "phase": 6,
      "sentContributions": true,
      "sentComplaint": true,
      "sentJustification": false,
      "sentPrematureCommitment": true,
      "aborted": false,
      "badMembers": [
        {
          "memberIndex": 35,
          "proTxHash": "c24aea30305d539887223fd923df775644b1d86db0aac8c654026e823b549cd7"
        },
        {
          "memberIndex": 42,
          "proTxHash": "f0567069d4f2a2e536e46173a097b318daf03edef989f6875ca06f5c4d49abc9"
        }
      ],
      "weComplain": [
      ],
      "receivedContributions": [
        {
          "memberIndex": 0,
          "proTxHash": "a6670caf2842a4ae5cb4bb78b3c10343456922b500693f6da043af541d58d9cb"
        },
        {
          "memberIndex": 1,
          "proTxHash": "77c0615fb5eb946f7f731a44eb36dc37ee77bf959e7205937d88186cacfbdc7e"
        },
        {
          "memberIndex": 2,
          "proTxHash": "8070c631ce9ac8850d2e95d4ed7be70171ead22ccd7f4bc9c3aee0a227f323c9"
        },
        {
          "memberIndex": 3,
          "proTxHash": "596be0851532a66037744afa694e4de6485f326f4638e704db93cc726866cda3"
        },
        {
          "memberIndex": 4,
          "proTxHash": "51c11d287dfa85aef3eebb5420834c8e443e01d15c0b0a8e397d67e2e51aa239"
        },
        {
          "memberIndex": 5,
          "proTxHash": "9f4f9f83ecbcd5739d7f1479ee14b508f2414d044a717acba0960566c4e6091d"
        },
        {
          "memberIndex": 6,
          "proTxHash": "21c0923badd20f953360c586edfcbb1a830be83206e30b3f65765f7794f2a640"
        },
        {
          "memberIndex": 7,
          "proTxHash": "cc36055f36345b85a2b8176e79feff0ff822c490691c7f8e8d3348b4b1a1d8ac"
        },
        {
          "memberIndex": 8,
          "proTxHash": "4636ed7acbacbc76aba60aa7a1011688fe9ad5fd701d0bf8fc42a502ea3e6543"
        },
        {
          "memberIndex": 9,
          "proTxHash": "32e5ad5cf9a06eb13e0f65cb7ecde1a93ef24995d07355fac2ff05ebd5b9ddbf"
        },
        {
          "memberIndex": 10,
          "proTxHash": "0022afbe93054ca11ce9b67892661af4558597bacff0ab82bff05a2b4a89ca2d"
        },
        {
          "memberIndex": 11,
          "proTxHash": "2523dc6e034911b9004862e87b4d23a32ed6198aec177915df7893f51cd645bd"
        },
        {
          "memberIndex": 12,
          "proTxHash": "abe5d16432915b201cf6f11299a1abd62e5f69a2c4e8717694d1e42d96dbd580"
        },
        {
          "memberIndex": 13,
          "proTxHash": "f443dd87ec7981e8630ae957f295d9d226d4bd3895f59dbd80b30137a92b3735"
        },
        {
          "memberIndex": 14,
          "proTxHash": "6a5be5c068a0be432b7db0772b25094a59ce1f433dd2df0d410511ac641c3768"
        },
        {
          "memberIndex": 15,
          "proTxHash": "84435c41688c8021a25a644e6b94c9f5159aff5658ee2e12f5cea5c714c21aa3"
        },
        {
          "memberIndex": 16,
          "proTxHash": "2db238aa40837319ca13e27aae4333d1248475546be6cfad985a3785c0ac9bd6"
        },
        {
          "memberIndex": 17,
          "proTxHash": "cefb7c69f75d9fbba21f648c6205bebf9b16325956404c70af03144c1135c7d7"
        },
        {
          "memberIndex": 18,
          "proTxHash": "cc7041c869c7c1c0bae7c137f0cda708ad492bc89c4b8f7a40a353d90335febf"
        },
        {
          "memberIndex": 19,
          "proTxHash": "24e642275f5d5f17f67db502d905153cfd83ffbd3d49c90196ec01200917fb31"
        },
        {
          "memberIndex": 20,
          "proTxHash": "bc5c77926b0ccfcb742123a1edf2c27147888f694701df399982a862309921c8"
        },
        {
          "memberIndex": 21,
          "proTxHash": "04d06d16b3eca2f104ef9749d0c1c17d183eb1b4fe3a16808fd70464f03bcd63"
        },
        {
          "memberIndex": 22,
          "proTxHash": "11eabc1e72394af02bbe86815975d054816fe69006fdc64c6d7a06b585e5c311"
        },
        {
          "memberIndex": 23,
          "proTxHash": "71cf5017c4c5f69db5c17a8cfb4c28ffc14ad1715dba2a83f0c30e534291f828"
        },
        {
          "memberIndex": 24,
          "proTxHash": "d567ac9cc7437848210365a0225271ec26a6a6c7d852544a6e9cbd40756075b3"
        },
        {
          "memberIndex": 25,
          "proTxHash": "16ef804605595f67a0e078f7ffbdd93ac55bcd22d9094cb8b61ef527c48f4c44"
        },
        {
          "memberIndex": 26,
          "proTxHash": "f51b426420ac4c518ad07c2bb03e434389337b4e2977d39233114d5e8ef21f69"
        },
        {
          "memberIndex": 27,
          "proTxHash": "2460848868c210d23c68460050f83f47a7ad00db2c47ad6f223a9b1eb04c8d54"
        },
        {
          "memberIndex": 28,
          "proTxHash": "49d94e4c584929320cfe159faf4f6e398f1b2d1fdaa413c01345ce23870d2ca9"
        },
        {
          "memberIndex": 29,
          "proTxHash": "e8b039ce3f1016b7caf781d1b0efbc11191860ec3b131fc49591402a260ba638"
        },
        {
          "memberIndex": 30,
          "proTxHash": "5ab82a5348b5d4c126b0c172665d364352be37c96ce442e710d4a844a6f80bf9"
        },
        {
          "memberIndex": 31,
          "proTxHash": "05b83104eea971582c803ded305109ecb734b582da93b8e301c6f00d6be6c496"
        },
        {
          "memberIndex": 32,
          "proTxHash": "c98c6303af03f7f3b2673ceece962134088e5dcc3c69a0977069c6201b26dc9b"
        },
        {
          "memberIndex": 33,
          "proTxHash": "f933d592d677f3409274646ddea2ffaaca77dfd4ceab7c54037a04e05fc7ee8b"
        },
        {
          "memberIndex": 34,
          "proTxHash": "5d40e68f65e7263d91e114b644ff7f8c9c376db63550d5ef9bc4228870c4f053"
        },
        {
          "memberIndex": 36,
          "proTxHash": "a36edfac56f7f1b0f58aa793115fbd53d792315857033fb32a862507a3f060ff"
        },
        {
          "memberIndex": 37,
          "proTxHash": "c9d43a69bd9effdaed579edc901c5d848711481047c9cc76bad8232d8f329dcd"
        },
        {
          "memberIndex": 38,
          "proTxHash": "d82152084615c73d79f3eb8b0ec6a61e6d0f94c4cdcf26f773f0e42b72176f6f"
        },
        {
          "memberIndex": 39,
          "proTxHash": "869f7f2054a6ed4241967afb74c3b1a07701d2772b368eb0bbfd2e3365adf6f3"
        },
        {
          "memberIndex": 40,
          "proTxHash": "5f1a70a350d21f673d93fae45a50c0362947366e46c96bade51b7933f0cada3e"
        },
        {
          "memberIndex": 41,
          "proTxHash": "024608d03beb6a6065f14a29a837c68ae449ac1e17056819366ca0b72b6dd81f"
        },
        {
          "memberIndex": 43,
          "proTxHash": "254bcd3b28d696ce9d468cd521e6be3f7eb01da32d8bf9fdf34868baaf09d9e7"
        },
        {
          "memberIndex": 44,
          "proTxHash": "0ae626ed4ee06c1f042b2eaa9669302a2e60a0df8137843b39de53f2c3e265aa"
        },
        {
          "memberIndex": 45,
          "proTxHash": "cfa6f7b58c78f827c15e8f1b6a5a2a3a92140101719006d8226a363e2c0c8e5c"
        },
        {
          "memberIndex": 46,
          "proTxHash": "03811a53a20289799f56227f576915492d2cede48522cd1b3f67c6c89cdacf83"
        },
        {
          "memberIndex": 47,
          "proTxHash": "f989866b2fadb674a1ca63746ff8bb97232d6843c95f9e805b8bc2a5ae8e768d"
        },
        {
          "memberIndex": 48,
          "proTxHash": "9de76b8291d00026ab0af86306023c7b90f8e9229dc04916fe1335bf5e11f15d"
        },
        {
          "memberIndex": 49,
          "proTxHash": "e441bbb2f056d471ae9fad83b4dd0fa691a0574eb4a373a0e59d6108614ee07e"
        }
      ],
      "receivedComplaints": [
        {
          "memberIndex": 0,
          "proTxHash": "a6670caf2842a4ae5cb4bb78b3c10343456922b500693f6da043af541d58d9cb"
        },
        {
          "memberIndex": 1,
          "proTxHash": "77c0615fb5eb946f7f731a44eb36dc37ee77bf959e7205937d88186cacfbdc7e"
        },
        {
          "memberIndex": 2,
          "proTxHash": "8070c631ce9ac8850d2e95d4ed7be70171ead22ccd7f4bc9c3aee0a227f323c9"
        },
        {
          "memberIndex": 3,
          "proTxHash": "596be0851532a66037744afa694e4de6485f326f4638e704db93cc726866cda3"
        },
        {
          "memberIndex": 4,
          "proTxHash": "51c11d287dfa85aef3eebb5420834c8e443e01d15c0b0a8e397d67e2e51aa239"
        },
        {
          "memberIndex": 5,
          "proTxHash": "9f4f9f83ecbcd5739d7f1479ee14b508f2414d044a717acba0960566c4e6091d"
        },
        {
          "memberIndex": 6,
          "proTxHash": "21c0923badd20f953360c586edfcbb1a830be83206e30b3f65765f7794f2a640"
        },
        {
          "memberIndex": 7,
          "proTxHash": "cc36055f36345b85a2b8176e79feff0ff822c490691c7f8e8d3348b4b1a1d8ac"
        },
        {
          "memberIndex": 8,
          "proTxHash": "4636ed7acbacbc76aba60aa7a1011688fe9ad5fd701d0bf8fc42a502ea3e6543"
        },
        {
          "memberIndex": 9,
          "proTxHash": "32e5ad5cf9a06eb13e0f65cb7ecde1a93ef24995d07355fac2ff05ebd5b9ddbf"
        },
        {
          "memberIndex": 10,
          "proTxHash": "0022afbe93054ca11ce9b67892661af4558597bacff0ab82bff05a2b4a89ca2d"
        },
        {
          "memberIndex": 11,
          "proTxHash": "2523dc6e034911b9004862e87b4d23a32ed6198aec177915df7893f51cd645bd"
        },
        {
          "memberIndex": 12,
          "proTxHash": "abe5d16432915b201cf6f11299a1abd62e5f69a2c4e8717694d1e42d96dbd580"
        },
        {
          "memberIndex": 14,
          "proTxHash": "6a5be5c068a0be432b7db0772b25094a59ce1f433dd2df0d410511ac641c3768"
        },
        {
          "memberIndex": 15,
          "proTxHash": "84435c41688c8021a25a644e6b94c9f5159aff5658ee2e12f5cea5c714c21aa3"
        },
        {
          "memberIndex": 16,
          "proTxHash": "2db238aa40837319ca13e27aae4333d1248475546be6cfad985a3785c0ac9bd6"
        },
        {
          "memberIndex": 17,
          "proTxHash": "cefb7c69f75d9fbba21f648c6205bebf9b16325956404c70af03144c1135c7d7"
        },
        {
          "memberIndex": 18,
          "proTxHash": "cc7041c869c7c1c0bae7c137f0cda708ad492bc89c4b8f7a40a353d90335febf"
        },
        {
          "memberIndex": 19,
          "proTxHash": "24e642275f5d5f17f67db502d905153cfd83ffbd3d49c90196ec01200917fb31"
        },
        {
          "memberIndex": 20,
          "proTxHash": "bc5c77926b0ccfcb742123a1edf2c27147888f694701df399982a862309921c8"
        },
        {
          "memberIndex": 21,
          "proTxHash": "04d06d16b3eca2f104ef9749d0c1c17d183eb1b4fe3a16808fd70464f03bcd63"
        },
        {
          "memberIndex": 24,
          "proTxHash": "d567ac9cc7437848210365a0225271ec26a6a6c7d852544a6e9cbd40756075b3"
        },
        {
          "memberIndex": 25,
          "proTxHash": "16ef804605595f67a0e078f7ffbdd93ac55bcd22d9094cb8b61ef527c48f4c44"
        },
        {
          "memberIndex": 26,
          "proTxHash": "f51b426420ac4c518ad07c2bb03e434389337b4e2977d39233114d5e8ef21f69"
        },
        {
          "memberIndex": 27,
          "proTxHash": "2460848868c210d23c68460050f83f47a7ad00db2c47ad6f223a9b1eb04c8d54"
        },
        {
          "memberIndex": 28,
          "proTxHash": "49d94e4c584929320cfe159faf4f6e398f1b2d1fdaa413c01345ce23870d2ca9"
        },
        {
          "memberIndex": 29,
          "proTxHash": "e8b039ce3f1016b7caf781d1b0efbc11191860ec3b131fc49591402a260ba638"
        },
        {
          "memberIndex": 30,
          "proTxHash": "5ab82a5348b5d4c126b0c172665d364352be37c96ce442e710d4a844a6f80bf9"
        },
        {
          "memberIndex": 31,
          "proTxHash": "05b83104eea971582c803ded305109ecb734b582da93b8e301c6f00d6be6c496"
        },
        {
          "memberIndex": 33,
          "proTxHash": "f933d592d677f3409274646ddea2ffaaca77dfd4ceab7c54037a04e05fc7ee8b"
        },
        {
          "memberIndex": 34,
          "proTxHash": "5d40e68f65e7263d91e114b644ff7f8c9c376db63550d5ef9bc4228870c4f053"
        },
        {
          "memberIndex": 36,
          "proTxHash": "a36edfac56f7f1b0f58aa793115fbd53d792315857033fb32a862507a3f060ff"
        },
        {
          "memberIndex": 37,
          "proTxHash": "c9d43a69bd9effdaed579edc901c5d848711481047c9cc76bad8232d8f329dcd"
        },
        {
          "memberIndex": 38,
          "proTxHash": "d82152084615c73d79f3eb8b0ec6a61e6d0f94c4cdcf26f773f0e42b72176f6f"
        },
        {
          "memberIndex": 39,
          "proTxHash": "869f7f2054a6ed4241967afb74c3b1a07701d2772b368eb0bbfd2e3365adf6f3"
        },
        {
          "memberIndex": 40,
          "proTxHash": "5f1a70a350d21f673d93fae45a50c0362947366e46c96bade51b7933f0cada3e"
        },
        {
          "memberIndex": 41,
          "proTxHash": "024608d03beb6a6065f14a29a837c68ae449ac1e17056819366ca0b72b6dd81f"
        },
        {
          "memberIndex": 43,
          "proTxHash": "254bcd3b28d696ce9d468cd521e6be3f7eb01da32d8bf9fdf34868baaf09d9e7"
        },
        {
          "memberIndex": 44,
          "proTxHash": "0ae626ed4ee06c1f042b2eaa9669302a2e60a0df8137843b39de53f2c3e265aa"
        },
        {
          "memberIndex": 45,
          "proTxHash": "cfa6f7b58c78f827c15e8f1b6a5a2a3a92140101719006d8226a363e2c0c8e5c"
        },
        {
          "memberIndex": 46,
          "proTxHash": "03811a53a20289799f56227f576915492d2cede48522cd1b3f67c6c89cdacf83"
        },
        {
          "memberIndex": 47,
          "proTxHash": "f989866b2fadb674a1ca63746ff8bb97232d6843c95f9e805b8bc2a5ae8e768d"
        },
        {
          "memberIndex": 48,
          "proTxHash": "9de76b8291d00026ab0af86306023c7b90f8e9229dc04916fe1335bf5e11f15d"
        },
        {
          "memberIndex": 49,
          "proTxHash": "e441bbb2f056d471ae9fad83b4dd0fa691a0574eb4a373a0e59d6108614ee07e"
        }
      ],
      "receivedJustifications": [
      ],
      "receivedPrematureCommitments": [
        {
          "memberIndex": 0,
          "proTxHash": "a6670caf2842a4ae5cb4bb78b3c10343456922b500693f6da043af541d58d9cb"
        },
        {
          "memberIndex": 1,
          "proTxHash": "77c0615fb5eb946f7f731a44eb36dc37ee77bf959e7205937d88186cacfbdc7e"
        },
        {
          "memberIndex": 2,
          "proTxHash": "8070c631ce9ac8850d2e95d4ed7be70171ead22ccd7f4bc9c3aee0a227f323c9"
        },
        {
          "memberIndex": 3,
          "proTxHash": "596be0851532a66037744afa694e4de6485f326f4638e704db93cc726866cda3"
        },
        {
          "memberIndex": 4,
          "proTxHash": "51c11d287dfa85aef3eebb5420834c8e443e01d15c0b0a8e397d67e2e51aa239"
        },
        {
          "memberIndex": 5,
          "proTxHash": "9f4f9f83ecbcd5739d7f1479ee14b508f2414d044a717acba0960566c4e6091d"
        },
        {
          "memberIndex": 6,
          "proTxHash": "21c0923badd20f953360c586edfcbb1a830be83206e30b3f65765f7794f2a640"
        },
        {
          "memberIndex": 7,
          "proTxHash": "cc36055f36345b85a2b8176e79feff0ff822c490691c7f8e8d3348b4b1a1d8ac"
        },
        {
          "memberIndex": 8,
          "proTxHash": "4636ed7acbacbc76aba60aa7a1011688fe9ad5fd701d0bf8fc42a502ea3e6543"
        },
        {
          "memberIndex": 9,
          "proTxHash": "32e5ad5cf9a06eb13e0f65cb7ecde1a93ef24995d07355fac2ff05ebd5b9ddbf"
        },
        {
          "memberIndex": 10,
          "proTxHash": "0022afbe93054ca11ce9b67892661af4558597bacff0ab82bff05a2b4a89ca2d"
        },
        {
          "memberIndex": 11,
          "proTxHash": "2523dc6e034911b9004862e87b4d23a32ed6198aec177915df7893f51cd645bd"
        },
        {
          "memberIndex": 12,
          "proTxHash": "abe5d16432915b201cf6f11299a1abd62e5f69a2c4e8717694d1e42d96dbd580"
        },
        {
          "memberIndex": 14,
          "proTxHash": "6a5be5c068a0be432b7db0772b25094a59ce1f433dd2df0d410511ac641c3768"
        },
        {
          "memberIndex": 15,
          "proTxHash": "84435c41688c8021a25a644e6b94c9f5159aff5658ee2e12f5cea5c714c21aa3"
        },
        {
          "memberIndex": 16,
          "proTxHash": "2db238aa40837319ca13e27aae4333d1248475546be6cfad985a3785c0ac9bd6"
        },
        {
          "memberIndex": 17,
          "proTxHash": "cefb7c69f75d9fbba21f648c6205bebf9b16325956404c70af03144c1135c7d7"
        },
        {
          "memberIndex": 18,
          "proTxHash": "cc7041c869c7c1c0bae7c137f0cda708ad492bc89c4b8f7a40a353d90335febf"
        },
        {
          "memberIndex": 19,
          "proTxHash": "24e642275f5d5f17f67db502d905153cfd83ffbd3d49c90196ec01200917fb31"
        },
        {
          "memberIndex": 20,
          "proTxHash": "bc5c77926b0ccfcb742123a1edf2c27147888f694701df399982a862309921c8"
        },
        {
          "memberIndex": 21,
          "proTxHash": "04d06d16b3eca2f104ef9749d0c1c17d183eb1b4fe3a16808fd70464f03bcd63"
        },
        {
          "memberIndex": 24,
          "proTxHash": "d567ac9cc7437848210365a0225271ec26a6a6c7d852544a6e9cbd40756075b3"
        },
        {
          "memberIndex": 25,
          "proTxHash": "16ef804605595f67a0e078f7ffbdd93ac55bcd22d9094cb8b61ef527c48f4c44"
        },
        {
          "memberIndex": 26,
          "proTxHash": "f51b426420ac4c518ad07c2bb03e434389337b4e2977d39233114d5e8ef21f69"
        },
        {
          "memberIndex": 27,
          "proTxHash": "2460848868c210d23c68460050f83f47a7ad00db2c47ad6f223a9b1eb04c8d54"
        },
        {
          "memberIndex": 28,
          "proTxHash": "49d94e4c584929320cfe159faf4f6e398f1b2d1fdaa413c01345ce23870d2ca9"
        },
        {
          "memberIndex": 29,
          "proTxHash": "e8b039ce3f1016b7caf781d1b0efbc11191860ec3b131fc49591402a260ba638"
        },
        {
          "memberIndex": 30,
          "proTxHash": "5ab82a5348b5d4c126b0c172665d364352be37c96ce442e710d4a844a6f80bf9"
        },
        {
          "memberIndex": 31,
          "proTxHash": "05b83104eea971582c803ded305109ecb734b582da93b8e301c6f00d6be6c496"
        },
        {
          "memberIndex": 33,
          "proTxHash": "f933d592d677f3409274646ddea2ffaaca77dfd4ceab7c54037a04e05fc7ee8b"
        },
        {
          "memberIndex": 34,
          "proTxHash": "5d40e68f65e7263d91e114b644ff7f8c9c376db63550d5ef9bc4228870c4f053"
        },
        {
          "memberIndex": 36,
          "proTxHash": "a36edfac56f7f1b0f58aa793115fbd53d792315857033fb32a862507a3f060ff"
        },
        {
          "memberIndex": 37,
          "proTxHash": "c9d43a69bd9effdaed579edc901c5d848711481047c9cc76bad8232d8f329dcd"
        },
        {
          "memberIndex": 38,
          "proTxHash": "d82152084615c73d79f3eb8b0ec6a61e6d0f94c4cdcf26f773f0e42b72176f6f"
        },
        {
          "memberIndex": 39,
          "proTxHash": "869f7f2054a6ed4241967afb74c3b1a07701d2772b368eb0bbfd2e3365adf6f3"
        },
        {
          "memberIndex": 40,
          "proTxHash": "5f1a70a350d21f673d93fae45a50c0362947366e46c96bade51b7933f0cada3e"
        },
        {
          "memberIndex": 41,
          "proTxHash": "024608d03beb6a6065f14a29a837c68ae449ac1e17056819366ca0b72b6dd81f"
        },
        {
          "memberIndex": 43,
          "proTxHash": "254bcd3b28d696ce9d468cd521e6be3f7eb01da32d8bf9fdf34868baaf09d9e7"
        },
        {
          "memberIndex": 44,
          "proTxHash": "0ae626ed4ee06c1f042b2eaa9669302a2e60a0df8137843b39de53f2c3e265aa"
        },
        {
          "memberIndex": 45,
          "proTxHash": "cfa6f7b58c78f827c15e8f1b6a5a2a3a92140101719006d8226a363e2c0c8e5c"
        },
        {
          "memberIndex": 46,
          "proTxHash": "03811a53a20289799f56227f576915492d2cede48522cd1b3f67c6c89cdacf83"
        },
        {
          "memberIndex": 47,
          "proTxHash": "f989866b2fadb674a1ca63746ff8bb97232d6843c95f9e805b8bc2a5ae8e768d"
        },
        {
          "memberIndex": 48,
          "proTxHash": "9de76b8291d00026ab0af86306023c7b90f8e9229dc04916fe1335bf5e11f15d"
        },
        {
          "memberIndex": 49,
          "proTxHash": "e441bbb2f056d471ae9fad83b4dd0fa691a0574eb4a373a0e59d6108614ee07e"
        }
      ],
      "allMembers": [
        "a6670caf2842a4ae5cb4bb78b3c10343456922b500693f6da043af541d58d9cb",
        "77c0615fb5eb946f7f731a44eb36dc37ee77bf959e7205937d88186cacfbdc7e",
        "8070c631ce9ac8850d2e95d4ed7be70171ead22ccd7f4bc9c3aee0a227f323c9",
        "596be0851532a66037744afa694e4de6485f326f4638e704db93cc726866cda3",
        "51c11d287dfa85aef3eebb5420834c8e443e01d15c0b0a8e397d67e2e51aa239",
        "9f4f9f83ecbcd5739d7f1479ee14b508f2414d044a717acba0960566c4e6091d",
        "21c0923badd20f953360c586edfcbb1a830be83206e30b3f65765f7794f2a640",
        "cc36055f36345b85a2b8176e79feff0ff822c490691c7f8e8d3348b4b1a1d8ac",
        "4636ed7acbacbc76aba60aa7a1011688fe9ad5fd701d0bf8fc42a502ea3e6543",
        "32e5ad5cf9a06eb13e0f65cb7ecde1a93ef24995d07355fac2ff05ebd5b9ddbf",
        "0022afbe93054ca11ce9b67892661af4558597bacff0ab82bff05a2b4a89ca2d",
        "2523dc6e034911b9004862e87b4d23a32ed6198aec177915df7893f51cd645bd",
        "abe5d16432915b201cf6f11299a1abd62e5f69a2c4e8717694d1e42d96dbd580",
        "f443dd87ec7981e8630ae957f295d9d226d4bd3895f59dbd80b30137a92b3735",
        "6a5be5c068a0be432b7db0772b25094a59ce1f433dd2df0d410511ac641c3768",
        "84435c41688c8021a25a644e6b94c9f5159aff5658ee2e12f5cea5c714c21aa3",
        "2db238aa40837319ca13e27aae4333d1248475546be6cfad985a3785c0ac9bd6",
        "cefb7c69f75d9fbba21f648c6205bebf9b16325956404c70af03144c1135c7d7",
        "cc7041c869c7c1c0bae7c137f0cda708ad492bc89c4b8f7a40a353d90335febf",
        "24e642275f5d5f17f67db502d905153cfd83ffbd3d49c90196ec01200917fb31",
        "bc5c77926b0ccfcb742123a1edf2c27147888f694701df399982a862309921c8",
        "04d06d16b3eca2f104ef9749d0c1c17d183eb1b4fe3a16808fd70464f03bcd63",
        "11eabc1e72394af02bbe86815975d054816fe69006fdc64c6d7a06b585e5c311",
        "71cf5017c4c5f69db5c17a8cfb4c28ffc14ad1715dba2a83f0c30e534291f828",
        "d567ac9cc7437848210365a0225271ec26a6a6c7d852544a6e9cbd40756075b3",
        "16ef804605595f67a0e078f7ffbdd93ac55bcd22d9094cb8b61ef527c48f4c44",
        "f51b426420ac4c518ad07c2bb03e434389337b4e2977d39233114d5e8ef21f69",
        "2460848868c210d23c68460050f83f47a7ad00db2c47ad6f223a9b1eb04c8d54",
        "49d94e4c584929320cfe159faf4f6e398f1b2d1fdaa413c01345ce23870d2ca9",
        "e8b039ce3f1016b7caf781d1b0efbc11191860ec3b131fc49591402a260ba638",
        "5ab82a5348b5d4c126b0c172665d364352be37c96ce442e710d4a844a6f80bf9",
        "05b83104eea971582c803ded305109ecb734b582da93b8e301c6f00d6be6c496",
        "c98c6303af03f7f3b2673ceece962134088e5dcc3c69a0977069c6201b26dc9b",
        "f933d592d677f3409274646ddea2ffaaca77dfd4ceab7c54037a04e05fc7ee8b",
        "5d40e68f65e7263d91e114b644ff7f8c9c376db63550d5ef9bc4228870c4f053",
        "c24aea30305d539887223fd923df775644b1d86db0aac8c654026e823b549cd7",
        "a36edfac56f7f1b0f58aa793115fbd53d792315857033fb32a862507a3f060ff",
        "c9d43a69bd9effdaed579edc901c5d848711481047c9cc76bad8232d8f329dcd",
        "d82152084615c73d79f3eb8b0ec6a61e6d0f94c4cdcf26f773f0e42b72176f6f",
        "869f7f2054a6ed4241967afb74c3b1a07701d2772b368eb0bbfd2e3365adf6f3",
        "5f1a70a350d21f673d93fae45a50c0362947366e46c96bade51b7933f0cada3e",
        "024608d03beb6a6065f14a29a837c68ae449ac1e17056819366ca0b72b6dd81f",
        "f0567069d4f2a2e536e46173a097b318daf03edef989f6875ca06f5c4d49abc9",
        "254bcd3b28d696ce9d468cd521e6be3f7eb01da32d8bf9fdf34868baaf09d9e7",
        "0ae626ed4ee06c1f042b2eaa9669302a2e60a0df8137843b39de53f2c3e265aa",
        "cfa6f7b58c78f827c15e8f1b6a5a2a3a92140101719006d8226a363e2c0c8e5c",
        "03811a53a20289799f56227f576915492d2cede48522cd1b3f67c6c89cdacf83",
        "f989866b2fadb674a1ca63746ff8bb97232d6843c95f9e805b8bc2a5ae8e768d",
        "9de76b8291d00026ab0af86306023c7b90f8e9229dc04916fe1335bf5e11f15d",
        "e441bbb2f056d471ae9fad83b4dd0fa691a0574eb4a373a0e59d6108614ee07e"
      ]
    }
  },
  "minableCommitments": {
    "llmq_50_60": {
      "version": 1,
      "llmqType": 1,
      "quorumHash": "000000000122768294b19a5f6750094f6e9caa135c0826372d0538d4ceb910bc",
      "signersCount": 0,
      "validMembersCount": 0,
      "quorumPublicKey": "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
    }
  }
}
```

## Quorum Sign

The `quorum sign` RPC requests threshold-signing for a message.
[block:callout]
{
  "type": "warning",
  "body": "Note: Used for RegTest testing only.",
  "title": "Regtest Network Only"
}
[/block]
*Parameter #1---LLMQ Type*

Name | Type | Presence | Description
--- | --- | --- | ---
`llmqType` | number | Required<br>(exactly 1) | [Type of quorum](https://github.com/dashpay/dips/blob/master/dip-0006.md#current-llmq-types):<br>`1` - LLMQ_50_60<br>`2` - LLMQ_400_60<br>`3` - LLMQ_400_85

*Parameter #2---id*

Name | Type | Presence | Description
--- | --- | --- | ---
`id` | string (hex) | Required<br>(exactly 1) | Signing request ID

*Parameter #3---message hash*

Name | Type | Presence | Description
--- | --- | --- | ---
`msgHash` | string (hex) | Required<br>(exactly 1) | Hash of the message to be signed

*Parameter #4---quorum hash*

Name | Type | Presence | Description
--- | --- | --- | ---
`quorumHash` | string (hex) | Optional<br>(0 or 1) | **Added in Dash Core 0.16.0**<br><br>The quorum identifier. Used by [Dash Platform](https://dashplatform.readme.io/docs/introduction-what-is-dash-platform) to direct layer 2 signing requests to a specific quorum.

*Result---status*

Name | Type | Presence | Description
--- | --- | --- | ---
result | bool | Required<br>(exactly 1) | True or false depending on success

*Example from Dash Core 0.14.0*

``` bash
dash-cli -testnet quorum sign 1 \
  "abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234" \
  "51c11d287dfa85aef3eebb5420834c8e443e01d15c0b0a8e397d67e2e51aa239"
```

Result:
``` json
false
```

## Quorum GetRecSig

The `quorum getrecsig` RPC gets the recovered signature for a previous threshold-signing message request.

*Parameter #1---LLMQ Type*

Name | Type | Presence | Description
--- | --- | --- | ---
`llmqType` | number | Required<br>(exactly 1) | [Type of quorum](https://github.com/dashpay/dips/blob/master/dip-0006.md#current-llmq-types):<br>`1` - LLMQ_50_60<br>`2` - LLMQ_400_60<br>`3` - LLMQ_400_85

*Parameter #2---id*

Name | Type | Presence | Description
--- | --- | --- | ---
`id` | string (hex) | Required<br>(exactly 1) | Signing request ID

*Parameter #3---message hash*

Name | Type | Presence | Description
--- | --- | --- | ---
`msgHash` | string (hex) | Required<br>(exactly 1) | Hash of the message to be signed

*Result---recovered signature*

Name | Type | Presence | Description
--- | --- | --- | ---
result | bool | Required<br>(exactly 1) | Recovered signature details
→<br>`llmqType` | number | Required<br>(exactly 1) | [Type of quorum](https://github.com/dashpay/dips/blob/master/dip-0006.md#current-llmq-types):<br>`1` - LLMQ_50_60<br>`2` - LLMQ_400_60<br>`3` - LLMQ_400_85
→<br>`quorumHash` | string (hex) | Required<br>(exactly 1) | The block hash of the quorum  
→<br>`id` | string (hex) | Required<br>(exactly 1) | The signing session ID
→<br>`msgHash` | string (hex) | Required<br>(exactly 1) | The message hash
→<br>`sig` | string (hex) | Required<br>(exactly 1) | The recovered signature
→<br>`hash` | string (hex) | Required<br>(exactly 1) | The hash of the recovered signature

*Example from Dash Core 0.14.0*

``` bash
dash-cli -testnet quorum getrecsig 1 \
  "e980ebf295b42f24b03321ffb255818753b2b211e8c46b61c0b6fde91242d12f" \
  "907087d4720850e639b7b5cc41d7a6d020e5a50debb3bc3974f0cb3d7d378ea4"
```

Result:
``` json
{
  "llmqType": 1,
  "quorumHash": "00000000008344da08e4d262773ea545472fbf625f78b3ebfe5fc067c33b1d22",
  "id": "e980ebf295b42f24b03321ffb255818753b2b211e8c46b61c0b6fde91242d12f",
  "msgHash": "907087d4720850e639b7b5cc41d7a6d020e5a50debb3bc3974f0cb3d7d378ea4",
  "sig": "1365171c408d686af2ca8f5fae91cdf9cf0b5eec60b0b161b9288a1c68e2cd68f225495a787415c924c5953a6282d131178aa6baf4c2673d19549fc627740cf71d295f8a38b9970525a7f248d54a548e16da285b5c1f3ec0740ad40edbcc8615",
  "hash": "d9b7f7904746fbb3eeaeec36fadc79b351f6a854cd22ee9e607592aee972fcb2"
}
```

## Quorum HasRecSig

The `quorum hasrecsig` RPC checks for a recovered signature for a previous threshold-signing message request.

[block:callout]
{
  "type": "warning",
  "body": "Note: Used for RegTest testing only.",
  "title": "Regtest Network Only"
}
[/block]
*Parameter #1---LLMQ Type*

Name | Type | Presence | Description
--- | --- | --- | ---
`llmqType` | number | Required<br>(exactly 1) | [Type of quorum](https://github.com/dashpay/dips/blob/master/dip-0006.md#current-llmq-types):<br>`1` - LLMQ_50_60<br>`2` - LLMQ_400_60<br>`3` - LLMQ_400_85

*Parameter #2---id*

Name | Type | Presence | Description
--- | --- | --- | ---
`id` | string (hex) | Required<br>(exactly 1) | Signing request ID

*Parameter #3---message hash*

Name | Type | Presence | Description
--- | --- | --- | ---
`msgHash` | string (hex) | Required<br>(exactly 1) | Hash of the message to be signed

*Result---status*

Name | Type | Presence | Description
--- | --- | --- | ---
result | bool | Required<br>(exactly 1) | True or false depending on success

*Example from Dash Core 0.14.0*

``` bash
dash-cli -testnet quorum hasrecsig 1 \
  "e980ebf295b42f24b03321ffb255818753b2b211e8c46b61c0b6fde91242d12f" \
  "907087d4720850e639b7b5cc41d7a6d020e5a50debb3bc3974f0cb3d7d378ea4"
```

Result:
``` json
true
```

## Quorum IsConflicting

The `quorum isconflicting` RPC checks if there is a conflict for a threshold-signing message request.

[block:callout]
{
  "type": "warning",
  "body": "Note: Used for RegTest testing only.",
  "title": "Regtest Network Only"
}
[/block]
*Parameter #1---LLMQ Type*

Name | Type | Presence | Description
--- | --- | --- | ---
`llmqType` | number | Required<br>(exactly 1) | [Type of quorum](https://github.com/dashpay/dips/blob/master/dip-0006.md#current-llmq-types):<br>`1` - LLMQ_50_60<br>`2` - LLMQ_400_60<br>`3` - LLMQ_400_85

*Parameter #2---id*

Name | Type | Presence | Description
--- | --- | --- | ---
`id` | string (hex) | Required<br>(exactly 1) | Signing request ID

*Parameter #3---message hash*

Name | Type | Presence | Description
--- | --- | --- | ---
`msgHash` | string (hex) | Required<br>(exactly 1) | Hash of the message to be signed

*Result---status*

Name | Type | Presence | Description
--- | --- | --- | ---
result | bool | Required<br>(exactly 1) | True or false depending on success

*Example from Dash Core 0.14.0*

``` bash
dash-cli -testnet quorum isconflicting 1 \
  "e980ebf295b42f24b03321ffb255818753b2b211e8c46b61c0b6fde91242d12f" \
  "907087d4720850e639b7b5cc41d7a6d020e5a50debb3bc3974f0cb3d7d378ea4"
```

Result:
``` json
false
```

## Quorum MemberOf

The [`quorum` RPC](core-api-ref-remote-procedure-calls-evo#quorum) checks which quorums the given masternode is a member of.

*Parameter #1---proTxHash*

Name | Type | Presence | Description
--- | --- | --- | ---
proTxHash | string | Required<br>(exactly 1) | ProTxHash of the masternode.

*Parameter #2---scanQuorumsCount*

Name | Type | Presence | Description
--- | --- | --- | ---
scanQuorumsCount | number | Optional | Number of quorums to scan for. If not specified, the active quorum count for each specific quorum type is used.

*Result---list of quorums the masternode is a member of*

Name | Type | Presence | Description
--- | --- | --- | ---
`result` | Array of objects | Required<br>(exactly 1) | Array containing info for quorum's the masternode belongs to
→<br>Quorum | object | Required<br>(0 or more) | An object describing quorum details
→ →<br>`height` | number | Required<br>(exactly 1) | Block height of the quorum
→ →<br>`type` | string | Required<br>(exactly 1) | [Type of quorum](https://github.com/dashpay/dips/blob/master/dip-0006.md#current-llmq-types)
→ →<br>`quorumHash` | string (hex) | Required<br>(exactly 1) | The hash of the quorum
→ →<br>`minedBlock` | string (hex) | Required<br>(exactly 1) | The hash of the block that established the quorum
→ →<br>`quorumPublicKey` | string (hex) | Required<br>(exactly 1) | Quorum public key
→ →<br>`isValidMember` | bool | Required<br>(exactly 1) | Indicates if the member is valid
→ →<br>`memberIndex` | number | Required<br>(exactly 1) | Index of the member within the quorum

*Example from Dash Core 0.15.0*

``` bash
dash-cli -testnet quorum memberof 1 \
  39c07d2c9c6d0ead56f52726b63c15e295cb5c3ecf7fe1fefcfb23b2e3cfed1f 1
```

Result:
``` json
[
  {
    "height": 72000,
    "type": "llmq_400_60",
    "quorumHash": "0000000007697fd69a799bfa26576a177e817bc0e45b9fcfbf48b362b05aeff2",
    "minedBlock": "00000000014d910dca80944b52aa3f522d5604254043b8354d641912aace4343",
    "quorumPublicKey": "03a3fbbe99d80a9be8fc59fd4fe43dfbeba9119b688e97493664716cdf15ae47fad70fea7cb93f20fba10d689f9e3c02",
    "isValidMember": true,
    "memberIndex": 80
  }
]
```

*See also: none*

## Quorum SelectQuorum

The `quorum selectquorum` RPC returns information about the quorum that would/should sign a request.

*Parameter #1---LLMQ Type*

Name | Type | Presence | Description
--- | --- | --- | ---
`llmqType` | number | Required<br>(exactly 1) | [Type of quorums](https://github.com/dashpay/dips/blob/master/dip-0006.md#current-llmq-types) to list:<br>`1` - LLMQ_50_60<br>`2` - LLMQ_400_60<br>`3` - LLMQ_400_85

*Parameter #2---request id*

Name | Type | Presence | Description
--- | --- | --- | ---
`id` | string (hex) | Required<br>(exactly 1) | The request ID

*Result---quorum hash and list of quorum members*

Name | Type | Presence | Description
--- | --- | --- | ---
`result` | Array of objects | Required<br>(exactly 1) | Array containing info for quorum's the masternode belongs to
→<br>`quorumHash` | string (hex) | Required<br>(exactly 1) | The hash of the quorum
→→<br>`recoveryMembers` | array | Required<br>(exactly 1) | Array containing ProRegTx hashes
→→→<br>ProRegTx Hash | string (hex) | Required<br>(exactly 1) | The hash of the provider transaction as hex in RPC byte order

*Example from Dash Core 0.16.0*

``` bash
dash-cli -testnet quorum selectquorum 1 \
  b95205c3bba72e9edfbe7380ec91fe5a97e16a189e28f39b03c6822757ad1a34
```

Result:
``` json
{
  "quorumHash": "00000ba8932486c66ed0742fd6b0f4e65afc75ab1e7886c6ef84580dfb7da34f",
  "recoveryMembers": [
    "0130c115522681b87082db1f45c38423d1a018a8e1559c2491103931e891c220",
    "dcd5dd71c4bd50c76d428f72b4a5731bd819720fbc656fff717548e2fe8cbd09",
    "a25c2f4549da0135411122ee9c2d37e8375577dc97431a282a5c374b4c71463a",
    "a1aaa653e5183d6a4525abfd0a76fc7d6a68393a1c4259117028dfce4fd215e1",
    "4c9eb7849590cca2aa18bf9aeeb1e4196c833740de2b111a7690eb62319b0735",
    "f38b8c5cb6c9e712aeeb150b9591cbdc70e99f9f26c1516955dd506b20dd9876",
    "afe12673c32de351e9f5a29178cd55656f03e64357be872536eb50b059032fe0",
    "651d56765c77b8c16b829a4a68f6d39cab40c913d0d365d7b7fd254ccc6cb2f1",
    "f88d0e5349d0bf7e4426a7461d7931d09f54c13edb6d83306c2521d19eb0b14b",
    "bdba1f169ab1e73c4dc96f4133b337c36907976e26a4612ffa5ae18869eba96c",
    "94044c070f9ce6bdd05c2b655ad2383c8402a74c10e0a9a3099d759b33cb7630",
    "515f77efd5983a765dc5740b0e0d3fae6e867917ca384467b24e31dda68c7369",
    "d1ebecfb816f5b4b5f34c91c0aab9c1b643c8567473e6ee35e02e01c9f2304c0",
    "2755d546b114aaec98589cf5b946e408a8996e4837234d2eee97e1da8c71e9ce",
    "b04b5240a8fc5ae62865dfa2e2558894f4b53d82fe88771e5345407b560d59bc",
    "53750150229202353bfbc3a2c866b993dd33a4c749d8f18ddcb1f5caf7e901ef",
    "7a5d1e05d4772feede8b9e71e17e013f99e77c622f13897b8a96339d6d06e1fc",
    "24f6fae5b5afd001d1046425f38e6ef523140afafc83013468bd31feb343f307",
    "18f2e176adf88043c41b406d0c97a2dd529d5daaca8b8ac49f72e6da30334926",
    "73191708ab5b21cc7ede9b12bc1e79de97ad5c4b9717a4fbf5de0ed1f3a5836a",
    "b57da176c0b6deae786afd318a8e00e351bed0f47ceac28f5b6d3d502f1c68d7",
    "161b2dcf8243162d11065eefd0948cb79d96dfa8ae869e34763a2bbd7d1d5d55",
    "fac81f18b3a968f5f881324d8eb38983f3f892c4999c2f46809c4de620b784d2",
    "42267d2c50a68350c880a488ec25ba0eac4e7cd436eb97c686fe0a6d035d25d3",
    "0be00b051c77fd4b6dac46a63b939f73726dc61dd80616e4573a9465f1aafa93"
  ]
}

```

*See also: none*