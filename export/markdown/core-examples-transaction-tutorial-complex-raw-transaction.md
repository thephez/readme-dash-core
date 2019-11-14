In this example, we'll create a <<glossary:transaction>> with two <<glossary:inputs>> and two <<glossary:outputs>>.  We'll sign each of the inputs separately, as might happen if the two inputs belonged to different people who agreed to create a transaction together (such as a CoinJoin transaction).

# 1. List unspent outputs
[block:code]
{
  "codes": [
    {
      "code": "> dash-cli -regtest listunspent",
      "language": "shell",
      "name": null
    }
  ]
}
[/block]
``` json
[
  {
    "txid": "fa0f4105b0a2b2706d65581c5e6411d3970253c7f231944fa2f978b4a3d9010d",
    "vout": 0,
    "address": "yfV9Wirf5RkYHgNDttjpBz8Wdi8BavLHcP",
    "account": "",
    "scriptPubKey": "76a914d240140859744755d73e5967081c3bedceffc5db88ac",
    "amount": 499.99990000,
    "confirmations": 1,
    "ps_rounds": -2,
    "spendable": true,
    "solvable": true
  },
  {
    "txid": "f84ca4ad33ec7889d3c6ac670152137a3ee1603c4096230a10562976f700d130",
    "vout": 0,
    "address": "yRdk89fwSW1mUBxQo5fCmEfTva7b4wh2H5",
    "account": "",
    "scriptPubKey": "76a9143a4e8960f26c1fa82d937046959b656e4dd7966688ac",
    "amount": 10.00000000,
    "confirmations": 2,
    "ps_rounds": -2,
    "spendable": true,
    "solvable": true
  },
  {
    "txid": "f84ca4ad33ec7889d3c6ac670152137a3ee1603c4096230a10562976f700d130",
    "vout": 1,
    "address": "yavnyFMebbfX4F2VC25P18FW6LS66h2wqJ",
    "scriptPubKey": "76a914a0411dbed3eab4341d5c41496d61b4fa1b22037e88ac",
    "amount": 490.00000000,
    "confirmations": 2,
    "ps_rounds": -2,
    "spendable": true,
    "solvable": true
  },
  {
    "txid": "ea6d596da55a137846f8b08bfd414b4667ce456f9e3b3182e6f05810e8613d84",
    "vout": 0,
    "address": "yWtgzKSckhedxtJ8NXhShWGjfBivkvBGgG",
    "scriptPubKey": "21023fff9c9dc9088c0aeba90d75413705091111311d761054de23\
                      acdd217450869aac",
    "amount": 500.00000000,
    "confirmations": 101,
    "ps_rounds": -2,
    "spendable": true,
    "solvable": true
  }
]
```

# 2. Select UTXOs

For our two inputs, we select two UTXOs by placing the txid and output index numbers (vouts) in shell variables.  We also save the addresses corresponding to the public keys (hashed or unhashed) used in those transactions. We need the addresses so we can get the corresponding private keys from our wallet.

``` bash
> UTXO1_TXID=ea6d596da55a137846f8b08bfd414b4667ce456f9e3b3182e6f05810e8613d84
> UTXO1_VOUT=0
> UTXO1_ADDRESS=yWtgzKSckhedxtJ8NXhShWGjfBivkvBGgG

> UTXO2_TXID=f84ca4ad33ec7889d3c6ac670152137a3ee1603c4096230a10562976f700d130
> UTXO2_VOUT=0
> UTXO2_ADDRESS=yRdk89fwSW1mUBxQo5fCmEfTva7b4wh2H5
```

# 3. Get private keys
[block:callout]
{
  "type": "danger",
  "body": "**Warning:** Users should never manually manage private keys on mainnet. As dangerous as raw transactions are (see warnings above), making a mistake with a private key can be much worse---as in the case of a HD wallet [cross-generational key compromise](core-guide-wallets-wallet-files#section-hardened-keys). \n**These examples are to help you learn, not for you to emulate on mainnet.**",
  "title": "Private Key Warning"
}
[/block]
Use the [`dumpprivkey` RPC](core-api-ref-remote-procedure-calls-wallet#section-dumpprivkey) to get the <<glossary:private keys>> corresponding to the <<glossary:public keys>> used in the two UTXOs our inputs we will be spending.  We need the private keys so we can sign each of the inputs separately.

``` bash
> dash-cli -regtest dumpprivkey $UTXO1_ADDRESS
cNL522MEQUnQxsZJo4ryPH8sPd2uVZaFKjKnZivo9DyVjpAGU7qP

> dash-cli -regtest dumpprivkey $UTXO2_ADDRESS
cPtZ9nagmjQ5bRKMuqoDz8xni6hRPfZ1zp3TSrqH3j3RyUThTYGN

> UTXO1_PRIVATE_KEY=cNL522MEQUnQxsZJo4ryPH8sPd2uVZaFKjKnZivo9DyVjpAGU7qP

> UTXO2_PRIVATE_KEY=cPtZ9nagmjQ5bRKMuqoDz8xni6hRPfZ1zp3TSrqH3j3RyUThTYGN
```

# 4. Get new addresses

For our two outputs, get two new <<glossary:addresses>>.

``` bash
> dash-cli -regtest getnewaddress
yhshGrdbh3rWt9EPaSi7xSGRFMvFdzTZ8n
> dash-cli -regtest getnewaddress
yesLaP5XFTaLZiWAo2zK8mFfUCtV8rRhKw

> NEW_ADDRESS1=yhshGrdbh3rWt9EPaSi7xSGRFMvFdzTZ8n
> NEW_ADDRESS2=yesLaP5XFTaLZiWAo2zK8mFfUCtV8rRhKw
```

# 5. Create raw transaction

Create the <<glossary:raw transaction>> using the [`createrawtransaction` RPC](core-api-ref-remote-procedure-calls-raw-transactions#section-createrawtransaction) much the same as before, except now we have two inputs and two outputs.

``` bash
## Outputs - inputs = transaction fee, so always double-check your math!
> dash-cli -regtest createrawtransaction '''
    [
      {
        "txid": "'$UTXO1_TXID'",
        "vout": '$UTXO1_VOUT'
      },
      {
        "txid": "'$UTXO2_TXID'",
        "vout": '$UTXO2_VOUT'
      }
    ]
    ''' '''
    {
      "'$NEW_ADDRESS1'": 499.9999,
      "'$NEW_ADDRESS2'": 10
    }'''
0100000002843d61e81058f0e682313b9e6f45ce67464b41fd8bb0f84678135a\
a56d596dea0000000000ffffffff30d100f7762956100a2396403c60e13e7a13\
520167acc6d38978ec33ada44cf80000000000ffffffff02f04c3ba40b000000\
1976a914ec73fe6129b249617bb5f20c8760708055fb6fdb88ac00ca9a3b0000\
00001976a914cb7a56b046479f8c247875d672d3e1aed18c33f488ac00000000

> RAW_TX=0100000002843d61e81058f0e682313b9e6f45ce67464b41fd8bb0f[...]
```

# 6. Sign raw transaction

Signing the raw transaction with `signrawtransaction` gets more complicated as we now have three arguments:

1. The unsigned raw transaction.

2. An empty array. We don't do anything with this argument in this operation, but some valid JSON must be provided to get access to the later positional arguments.

3. The private key we want to use to sign one of the inputs.

## 6a. First input

The result is a raw transaction with only one input signed; the fact that the transaction isn't fully signed is indicated by value of the `complete` JSON field.  We save the incomplete, partly-signed raw transaction hex to a shell variable.

``` bash
> dash-cli -regtest signrawtransaction $RAW_TX '[]' '''
    [
      "'$UTXO1_PRIVATE_KEY'"
    ]'''
```
``` json
{
  "hex": "0100000002843d61e81058f0e682313b9e6f45ce67464b41fd8bb0\
  f84678135aa56d596dea00000000494830450221009f7f356c0cc2d3337b5f\
  76dfc6de9f9be7c8c5ac2074cbeeba4815b90329602002207790f23361480e\
  2a5a2d1fa6e293ccd5cd01279ad301176f091b84d6dd8e8f6501ffffffff30\
  d100f7762956100a2396403c60e13e7a13520167acc6d38978ec33ada44cf8\
  0000000000ffffffff02f04c3ba40b0000001976a914ec73fe6129b249617b\
  b5f20c8760708055fb6fdb88ac00ca9a3b000000001976a914cb7a56b04647\
  9f8c247875d672d3e1aed18c33f488ac00000000",
  "complete": false,
  "errors": [
    {
      "txid": "f84ca4ad33ec7889d3c6ac670152137a3ee1603c4096230a1\
                0562976f700d130",
      "vout": 0,
      "scriptSig": "",
      "sequence": 4294967295,
      "error": "Operation not valid with the current stack size"
    }
  ]
}
```
``` bash

> PARTLY_SIGNED_RAW_TX=0100000002843d61e81058f0e682313b9e6f45ce6[...]
```

## 6b. Second input

To sign the second input, we repeat the process we used to sign the first input using the second private key. Now that both inputs are signed, the `complete` result is *true*.

``` bash
> dash-cli -regtest signrawtransaction $PARTLY_SIGNED_RAW_TX '[]' '''
    [
      "'$UTXO2_PRIVATE_KEY'"
    ]'''
```
``` json
{
  "hex": "0100000002843d61e81058f0e682313b9e6f45ce67464b41fd8bb0\
  f84678135aa56d596dea00000000494830450221009f7f356c0cc2d3337b5f\
  76dfc6de9f9be7c8c5ac2074cbeeba4815b90329602002207790f23361480e\
  2a5a2d1fa6e293ccd5cd01279ad301176f091b84d6dd8e8f6501ffffffff30\
  d100f7762956100a2396403c60e13e7a13520167acc6d38978ec33ada44cf8\
  000000006a47304402207867e88e3fe2c926df29376d77eba81daf9f4a5573\
  44d4f02e9c7dcee96a51e4022076274c2365dc069e7ef797c95c75ab6e01ca\
  3757342f3e6f21a3d9d01086efb7012102ff9005f79aa4c22ac48fa93d9b7f\
  40f321db1c13cd70cf08bdab3e23c8d19620ffffffff02f04c3ba40b000000\
  1976a914ec73fe6129b249617bb5f20c8760708055fb6fdb88ac00ca9a3b00\
  0000001976a914cb7a56b046479f8c247875d672d3e1aed18c33f488ac0000\
  0000",
  "complete": true
}
```

Clean up the shell variables used. Unlike previous subsections, we're not going to send this transaction to the connected node with `sendrawtransaction`. This will allow us to illustrate in the [Offline Signing subsection](core-examples-transaction-tutorial-offline-signing) below how to spend a transaction which is not yet in the block chain or memory pool.

``` bash
> unset PARTLY_SIGNED_RAW_TX RAW_TX NEW_ADDRESS1 [...]
```