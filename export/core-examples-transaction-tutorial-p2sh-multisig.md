In this subsection, we will create a <<glossary:P2SH multisig>> address, spend <<glossary:duffs>> to it, and then spend those duffs from it to another <<glossary:address>>.

Creating a <<glossary:multisig>> address is easy. Multisig <<glossary:outputs>> have two parameters, the *minimum* number of signatures required (*m*) and the *number* of <<glossary:public keys>> to use to validate those signatures. This is called m-of-n, and in this case we'll be using 2-of-3.

``` bash
    > dash-cli -regtest getnewaddress
    yYtWtpW7akCc2a5En8NsXeTGENyYbNgv9q
    > dash-cli -regtest getnewaddress
    yarm2x9eDFd9dKCycyPigwwj1vfJcYFxsH
    > dash-cli -regtest getnewaddress
    yLknHbtnjJRVWQr78aTfCPfNB42jfNkDWK

    > NEW_ADDRESS1=yYtWtpW7akCc2a5En8NsXeTGENyYbNgv9q
    > NEW_ADDRESS2=yarm2x9eDFd9dKCycyPigwwj1vfJcYFxsH
    > NEW_ADDRESS3=yLknHbtnjJRVWQr78aTfCPfNB42jfNkDWK
```

Generate three new P2PKH addresses. A <<glossary:P2PKH address>> cannot be used with the multisig redeem script created below. (Hashing each public key is unnecessary anyway---all the public keys are protected by a hash when the <<glossary:redeem script>> is hashed.) However, Dash Core uses addresses as a way to reference the underlying full (unhashed) public keys it knows about, so we get the three new addresses above in order to use their public keys.

Recall from the Guide that the hashed public keys used in addresses obfuscate the full public key, so you cannot give an address to another person or device as part of creating a typical multisig output or P2SH multisig redeem script. You must give them a full public key.

``` bash
> dash-cli -regtest validateaddress $NEW_ADDRESS3
```
``` json
{
  "isvalid": true,
  "address": "yLknHbtnjJRVWQr78aTfCPfNB42jfNkDWK",
  "scriptPubKey": "76a91404caa000366b99780f8e606ccc818883ca7f48f888ac",
  "ismine": true,
  "iswatchonly": false,
  "isscript": false,
  "pubkey": "038007ef6fd812d73da054271b68a42dae06672cff2a30b2814935537e593\
              0ebf6",
  "iscompressed": true,
  "account": ""
}

```
``` bash

> NEW_ADDRESS3_PUBLIC_KEY=038007ef6fd812d73da054271b68a42dae0667[...]
```

Use the [`validateaddress` RPC](core-api-ref-remote-procedure-calls-utility#section-validateaddress) to display the full (unhashed) public key for one of the addresses.  This is the information which will actually be included in the multisig redeem script.  This is also the information you would give another person or device as part of creating a multisig output or P2SH multisig redeem script.

We save the address returned to a shell variable.

``` bash
> dash-cli -regtest createmultisig 2 '''
    [
      "'$NEW_ADDRESS1'",
      "'$NEW_ADDRESS2'",
      "'$NEW_ADDRESS3_PUBLIC_KEY'"
    ]'''
```
``` json
{
  "address": "8meEZF54K7GxhHhdLCCeNwFQjHENv4CK86",
  "redeemScript": "522103fa8866cccae3c975a72884443a351801a0ea9721cbe721558\
                  6ddd6fab5f39f262103b2259f42a241f4870e794521594f2af7aadf0\
                  e4c580a43582e58630e4618634621038007ef6fd812d73da054271b6\
                  8a42dae06672cff2a30b2814935537e5930ebf653ae"
}
```
``` bash

> P2SH_ADDRESS=8meEZF54K7GxhHhdLCCeNwFQjHENv4CK86
> P2SH_REDEEM_SCRIPT=522103fa8866cccae3c975a72884443a351801a0ea9[...]
```

Use the [`createmultisig` RPC](core-api-ref-remote-procedure-calls-utility#section-createmultisig) with two arguments, the number (*n*) of signatures required and a list of addresses or public keys.  Because P2PKH addresses can't be used in the multisig redeem script created by this RPC, the only addresses which can be provided are those belonging to a public key in the <<glossary:wallet>>.  In this case, we provide two addresses and one public key---all of which will be converted to public keys in the redeem script.

The P2SH address is returned along with the redeem script which must be provided when we spend duffs sent to the P2SH address.
[block:callout]
{
  "type": "danger",
  "body": "**Warning:** You must not lose the redeem script, especially if you don't have a record of which public keys you used to create the P2SH multisig address. You need the redeem script to spend any dash sent to the P2SH address. \n\nIf you lose the redeem script, you can recreate it by running the same command above, with the public keys listed in the same order. **However, if you lose both the redeem script and even one of the public keys, you will never be able to spend duffs sent to that P2SH address.**",
  "title": "Redeem Script"
}
[/block]

Neither the address nor the redeem script are stored in the wallet when you use `createmultisig`. To store them in the wallet, use the [`addmultisigaddress` RPC](core-api-ref-remote-procedure-calls-wallet#section-addmultisigaddress) instead.  If you add an address to the wallet, you should also make a new backup.

``` bash
> dash-cli -regtest sendtoaddress $P2SH_ADDRESS 10.00
ddb2a2eb2402a9ae61d7db93a9a48c0747859d899e704b10f5b72145779f9c52

> UTXO_TXID=ddb2a2eb2402a9ae61d7db93a9a48c0747859d899e704b10f5b7[...]
```

Paying the P2SH multisig address with Dash Core is as simple as paying a more common P2PKH address. Here we use the same command (but different variable) we used in the [Simple Spending subsection](core-examples-transaction-tutorial-simple-spending). As before, this command automatically selects an UTXO, creates a <<glossary:change output>> to a new one of our P2PKH addresses if necessary, and pays a <<glossary:transaction fee>> if necessary.

We save that <<glossary:TXID>> to a shell variable as the TXID of the UTXO we plan to spend next.

``` bash
> dash-cli -regtest getrawtransaction $UTXO_TXID 1
```
``` json
{
  "hex": "010000000130d100f7762956100a2396403c60e13e7a13520167acc6d38978ec\
          33ada44cf8010000006b48304502210084effe3132550e6ba43a7f4cc54ad30d\
          001c0dbc3ea66d638e5f3d6039a28c2b022044c8cd89cf455b8650fe259306eb\
          2a30b0112969717e469a722bca0263e0975d01210324c2226564b19f0948306b\
          b7160a735c28001bbd046cd46059df9f8434f41254feffffff0200ca9a3b0000\
          000017a9144f334f26e350c8903c92ff25b733670902cfad5a8700e0052d0b00\
          00001976a91479165c2155b8fec5c702ec7f251d0982f27b402988ac67000000",
  "txid": "ddb2a2eb2402a9ae61d7db93a9a48c0747859d899e704b10f5b72145779f9c52",
  "size": 224,
  "version": 1,
  "locktime": 103,
  "vin": [
    {
      "txid": "f84ca4ad33ec7889d3c6ac670152137a3ee1603c4096230a10562976f70\
                0d130",
      "vout": 1,
      "scriptSig": {
        "asm": "304502210084effe3132550e6ba43a7f4cc54ad30d001c0dbc3ea66d63\
                8e5f3d6039a28c2b022044c8cd89cf455b8650fe259306eb2a30b01129\
                69717e469a722bca0263e0975d[ALL] 0324c2226564b19f0948306bb7\
                160a735c28001bbd046cd46059df9f8434f41254",
        "hex": "48304502210084effe3132550e6ba43a7f4cc54ad30d001c0dbc3ea66d\
                638e5f3d6039a28c2b022044c8cd89cf455b8650fe259306eb2a30b011\
                2969717e469a722bca0263e0975d01210324c2226564b19f0948306bb7\
                160a735c28001bbd046cd46059df9f8434f41254"
      },
      "sequence": 4294967294
    }
  ],
  "vout": [
    {
      "value": 10.00000000,
      "valueSat": 1000000000,
      "n": 0,
      "scriptPubKey": {
        "asm": "OP_HASH160 4f334f26e350c8903c92ff25b733670902cfad5a OP_EQUAL",
        "hex": "a9144f334f26e350c8903c92ff25b733670902cfad5a87",
        "reqSigs": 1,
        "type": "scripthash",
        "addresses": [
          "8meEZF54K7GxhHhdLCCeNwFQjHENv4CK86"
        ]
      }
    },
    {
      "value": 480.00000000,
      "valueSat": 48000000000,
      "n": 1,
      "scriptPubKey": {
        "asm": "OP_DUP OP_HASH160 79165c2155b8fec5c702ec7f251d0982f27b4029\
                OP_EQUALVERIFY OP_CHECKSIG",
        "hex": "76a91479165c2155b8fec5c702ec7f251d0982f27b402988ac",
        "reqSigs": 1,
        "type": "pubkeyhash",
        "addresses": [
          "yXMhQ1L5q3PcnJgEhyAFztQPPRaEr8Mh8s"
        ]
      }
    }
  ]
}
```
``` bash

> UTXO_VOUT=0
> UTXO_OUTPUT_SCRIPT=a9144f334f26e350c8903c92ff25b733670902cfad5a87
```

We use the [`getrawtransaction` RPC](core-api-ref-remote-procedure-calls-raw-transaction#section-getrawtransaction) with the optional second argument (*true*) to get the decoded transaction we just created with `sendtoaddress`. We choose one of the <<glossary:outputs>> to be our UTXO and get its <<glossary:output index>> number (vout) and <<glossary:pubkey script>> (scriptPubKey).

``` bash
> dash-cli -regtest getnewaddress
yZSxAakpoWGG3vcsvpk9qNtsYREhump4Cr

> NEW_ADDRESS4=yZSxAakpoWGG3vcsvpk9qNtsYREhump4Cr
```

We generate a new P2PKH address to use in the output we're about to create.

``` bash
## Outputs - inputs = transaction fee, so always double-check your math!
> dash-cli -regtest createrawtransaction '''
    [
      {
        "txid": "'$UTXO_TXID'",
        "vout": '$UTXO_VOUT'
      }
   ]
   ''' '''
   {
     "'$NEW_ADDRESS4'": 9.998
   }'''

0100000001529c9f774521b7f5104b709e899d8547078ca4a993dbd761aea902\
24eba2b2dd0000000000ffffffff01c0bc973b000000001976a914900504f96c\
55d6ebe1c33581ba9430ca05b12a1488ac00000000

010000000175e1769813db8418fea17576694af1ff31cb2b512b7333e6eb42f0\
30d0d778720000000000ffffffff01c0bc973b000000001976a914b6f64f5bf3\
e38f25ead28817df7929c06fe847ee88ac00000000

> RAW_TX=0100000001529c9f774521b7f5104b709e899d8547078ca4a993dbd[...]
```

We generate the <<glossary:raw transaction>> the same way we did in the [Simple Raw Transaction subsection](core-examples-transaction-tutorial-simple-raw-transaction).

``` bash
> dash-cli -regtest dumpprivkey $NEW_ADDRESS1
cThhxbQUtBDzHZbZrW6XAR4XkXfaQf4Abo7BQaTK2zVp7sVrHdmv
> dash-cli -regtest dumpprivkey $NEW_ADDRESS3
cUbYymPeHhRszTn64Xg7dzYKez8YC83M39ZTPJDiBDu8dRD3EjzF

> NEW_ADDRESS1_PRIVATE_KEY=cThhxbQUtBDzHZbZrW6XAR4XkXfaQf4Abo7BQ[...]
> NEW_ADDRESS3_PRIVATE_KEY=cUbYymPeHhRszTn64Xg7dzYKez8YC83M39ZTP[...]
```

We get the <<glossary:private keys>> for two of the <<glossary:public keys>> we used to create the transaction, the same way we got private keys in the [Complex Raw Transaction subsection](https://dash-core.readme.io/docs/core-examples-transaction-tutorial-complex-raw-transaction). Recall that we created a 2-of-3 multisig pubkey script, so signatures from two private keys are needed.
[block:callout]
{
  "type": "danger",
  "body": "**Reminder:** Users should never manually manage private keys on mainnet. See the warning in the [complex raw transaction section](core-examples-transaction-tutorial-complex-raw-transaction).",
  "title": "Private Key Warning"
}
[/block]

``` bash
> dash-cli -regtest signrawtransaction $RAW_TX '''
    [
      {
        "txid": "'$UTXO_TXID'",
        "vout": '$UTXO_VOUT',
        "scriptPubKey": "'$UTXO_OUTPUT_SCRIPT'",
        "redeemScript": "'$P2SH_REDEEM_SCRIPT'"
      }
    ]
    ''' '''
    [
      "'$NEW_ADDRESS1_PRIVATE_KEY'"
    ]'''
```
``` json
{
  "hex": "0100000001529c9f774521b7f5104b709e899d8547078ca4a993dbd761aea902\
          24eba2b2dd00000000b40047304402201cc50eac6d2db04dabd8ccd68b3116c0\
          a8d37e7e41335e0d0ab441a5aa08cdcd02204011d184dca2489758c05e01556f\
          f2ff9c48c39ff434fdfb1d9e0284fbde7701014c69522103fa8866cccae3c975\
          a72884443a351801a0ea9721cbe7215586ddd6fab5f39f262103b2259f42a241\
          f4870e794521594f2af7aadf0e4c580a43582e58630e4618634621038007ef6f\
          d812d73da054271b68a42dae06672cff2a30b2814935537e5930ebf653aeffff\
          ffff01c0bc973b000000001976a914900504f96c55d6ebe1c33581ba9430ca05\
          b12a1488ac00000000",
  "complete": false,
  "errors": [
    {
      "txid": "ddb2a2eb2402a9ae61d7db93a9a48c0747859d899e704b10f5b72145779\
                f9c52",
      "vout": 0,
      "scriptSig": "0047304402201cc50eac6d2db04dabd8ccd68b3116c0a8d37e7e41\
                    335e0d0ab441a5aa08cdcd02204011d184dca2489758c05e01556f\
                    f2ff9c48c39ff434fdfb1d9e0284fbde7701014c69522103fa8866\
                    cccae3c975a72884443a351801a0ea9721cbe7215586ddd6fab5f3\
                    9f262103b2259f42a241f4870e794521594f2af7aadf0e4c580a43\
                    582e58630e4618634621038007ef6fd812d73da054271b68a42dae\
                    06672cff2a30b2814935537e5930ebf653ae",
      "sequence": 4294967295,
      "error": "Operation not valid with the current stack size"
    }
  ]
}
```
``` bash

> PARTLY_SIGNED_RAW_TX=010000000175e1769813db8418fea17576694af1f[...]
```

We make the first <<glossary:signature>>. The input argument (JSON object) takes the additional <<glossary:redeem script>> parameter so that it can append the redeem script to the <<glossary:signature script>> after the two signatures.

``` bash
> dash-cli -regtest signrawtransaction $PARTLY_SIGNED_RAW_TX '''
    [
      {
        "txid": "'$UTXO_TXID'",
        "vout": '$UTXO_VOUT',
        "scriptPubKey": "'$UTXO_OUTPUT_SCRIPT'",
        "redeemScript": "'$P2SH_REDEEM_SCRIPT'"
      }
    ]
    ''' '''
    [
      "'$NEW_ADDRESS3_PRIVATE_KEY'"
    ]'''
```
``` json
{
  "hex": "0100000001529c9f774521b7f5104b709e899d8547078ca4a993dbd761aea902\
          24eba2b2dd00000000fdfd000047304402201cc50eac6d2db04dabd8ccd68b31\
          16c0a8d37e7e41335e0d0ab441a5aa08cdcd02204011d184dca2489758c05e01\
          556ff2ff9c48c39ff434fdfb1d9e0284fbde770101483045022100e0e1f95f1a\
          b85814ee0920d5bd28c6831086e838af4bec344fd8654a0b58525f022075989f\
          d3a677e1522aa85d45c41720aec9e7c127acadb6c14338c3b1a768ab28014c69\
          522103fa8866cccae3c975a72884443a351801a0ea9721cbe7215586ddd6fab5\
          f39f262103b2259f42a241f4870e794521594f2af7aadf0e4c580a43582e5863\
          0e4618634621038007ef6fd812d73da054271b68a42dae06672cff2a30b28149\
          35537e5930ebf653aeffffffff01c0bc973b000000001976a914900504f96c55\
          d6ebe1c33581ba9430ca05b12a1488ac00000000",
  "complete": true
}
```
``` bash

> SIGNED_RAW_TX=0100000001529c9f774521b7f5104b709e899d8547078ca4[...]
```

The `signrawtransaction` call used here is nearly identical to the one used above.  The only difference is the private key used.  Now that the two required signatures have been provided, the transaction is marked as complete.

``` bash
> dash-cli -regtest sendrawtransaction $SIGNED_RAW_TX
483061b32894aacf6c4050291252a480c2a4c869eb85bd45082fb87d6b175ae8
```

We send the transaction spending the P2SH multisig output to the local <<glossary:node>>, which accepts it.