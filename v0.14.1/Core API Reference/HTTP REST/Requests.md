---
title: "Requests"
excerpt: ""
---
# GET Block/NoTxDetails

The `GET block/notxdetails` operation {{summary_restGetBlock-noTxDetails}}

*Request*

``` text
GET /block/notxdetails/<hash>.<format>
```

*Parameter #1---the header hash of the block to retrieve*

Name | Type | Presence | Description
--- | --- | --- | ---
Header Hash | path (hex) | Required<br>(exactly 1) | The hash of the header of the block to get, encoded as hex in RPC byte order

*Parameter #2---the output format*

Name | Type | Presence | Description
--- | --- | --- | ---
Format | suffix | Required<br>(exactly 1) | Set to `.json` for decoded block contents in JSON, or `.bin` or `hex` for a serialized block in binary or hex

*Response as JSON*

Name | Type | Presence | Description
--- | --- | --- | ---
Result | object | Required<br>(exactly 1) | An object containing the requested block
→<br>`hash` | string (hex) | Required<br>(exactly 1) | The hash of this block's block header encoded as hex in RPC byte order.  This is the same as the hash provided in parameter #1
→<br>`confirmations` | number (int) | Required<br>(exactly 1) | The number of confirmations the transactions in this block have, starting at 1 when this block is at the tip of the best block chain.  This score will be -1 if the the block is not part of the best block chain
→<br>`size` | number (int) | Required<br>(exactly 1) | The size of this block in serialized block format, counted in bytes
→<br>`height` | number (int) | Required<br>(exactly 1) | The height of this block on its block chain
→<br>`version` | number (int) | Required<br>(exactly 1) | This block's version number.  See [block version numbers][section block versions]
→<br>`versionHex` | number (int) | Required<br>(exactly 1) | *Added in Bitcoin Core 0.13.0*<br><br>This block's version number formatted in hexadecimal.  See [BIP9 assignments]
→<br>`merkleroot` | string (hex) | Required<br>(exactly 1) | The merkle root for this block, encoded as hex in RPC byte order
→<br>`tx` | array | Required<br>(exactly 1) | An array containing all transactions in this block.  The transactions appear in the array in the same order they appear in the serialized block
→ →<br>TXID | string (hex) | Required<br>(1 or more) | The TXID of a transaction in this block, encoded as hex in RPC byte order
→<br>`time` | number (int) | Required<br>(exactly 1) | The value of the *time* field in the block header, indicating approximately when the block was created
→<br>`mediantime` | number (int) | Required<br>(exactly 1) | *Added in Bitcoin Core 0.12.0*<br><br>The median time of the 11 blocks before the most recent block on the blockchain.  Used for validating transaction locktime under BIP113  
→<br>`nonce` | number (int) | Required<br>(exactly 1) | The nonce which was successful at turning this particular block into one that could be added to the best block chain
→<br>`bits` | string (hex) | Required<br>(exactly 1) | The value of the *nBits* field in the block header, indicating the target threshold this block's header had to pass
→<br>`difficulty` | number (real) | Required<br>(exactly 1) | The estimated amount of work done to find this block relative to the estimated amount of work done to find block 0
→<br>`chainwork` | string (hex) | Required<br>(exactly 1) | The estimated number of block header hashes miners had to check from the genesis block to this block, encoded as big-endian hex
→<br>`previousblockhash` | string (hex) | Required<br>(exactly 1) | The hash of the header of the previous block, encoded as hex in RPC byte order
→<br>`nextblockhash` | string (hex) | Optional<br>(0 or 1) | The hash of the next block on the best block chain, if known, encoded as hex in RPC byte order

*Examples from Dash Core 0.12.2*

Request a block in hex-encoded serialized block format:

``` bash
curl http://localhost:19998/rest/block/notxdetails/0000000000ccbf46cf6b78827ac1019f82598be839bce08bff00d188e75fb451.hex
```

Result (wrapped):

``` bash
0000002097e8135d73afa52145f6d0b4d0f957030cd598837ddc6750271fb109\
000000008478305a7abf2f7cb21a889fb68d53c3e51685349e18e1b104b5956c\
100bfea2c72d285a84030a1cd0041ed701010000000100000000000000000000\
00000000000000000000000000000000000000000000ffffffff13037a94000e\
2f5032506f6f6c2d74444153482fffffffff06a1f9ef04000000001976a91414\
e3832cd7192ffb358a31d842636c4db8dfb1ac88ac6c357f3c000000001976a9\
149262f2289e1f021dca954d8cf07a7ad72c2cc24d88ac31f49e010000000019\
76a914d93f7ffa324b77d361e89a3c9c8df46ccdb4b39288ac40230e43000000\
001976a914c4541983721b26ada79770bf22de4885e19f566188ac0200000000\
0000004341047559d13c3f81b1fadbd8dd03e4b5a1c73b05e2b980e00d467aa9\
440b29c7de23664dde6428d75cafed22ae4f0d302e26c5c5a5dd4d3e1b796d72\
81bdc9430f35ac00000000000000002a6a28c855abe6461b1003ea36feb88a3b\
d50c5696e5784d11f8cd5e892978685de1d6000000000100000000000000
```

Get the same block in JSON:

``` bash
curl http://localhost:19998/rest/block/notxdetails/0000000000ccbf46cf6b78827ac1019f82598be839bce08bff00d188e75fb451.json
```

Result (whitespace added):

``` json
{  
   "hash":"0000000000ccbf46cf6b78827ac1019f82598be839bce08bff00d188e75fb451",
   "confirmations":55,
   "size":414,
   "height":38010,
   "version":536870912,
   "merkleroot":"a2fe0b106c95b504b1e1189e348516e5c3538db69f881ab27c2fbf7a5a307884",
   "tx":[  
      "a2fe0b106c95b504b1e1189e348516e5c3538db69f881ab27c2fbf7a5a307884"
   ],
   "time":1512582599,
   "mediantime":1512582025,
   "nonce":3609068752,
   "bits":"1c0a0384",
   "difficulty":25.56450187425715,
   "chainwork":"00000000000000000000000000000000000000000000000000092fc476457b68",
   "previousblockhash":"0000000009b11f275067dc7d8398d50c0357f9d0b4d0f64521a5af735d13e897",
   "nextblockhash":"0000000000a9baff28a79db2a50e13af8f313138f4568339f58d73eda14a4d51"
}
```

*See also*

* [GET Block][rest get block]: {{summary_restGetBlock}}
* [GetBlock][rpc getblock] RPC: {{summary_getBlock}}
* [GetBlockHash][rpc getblockhash] RPC: {{summary_getBlockHash}}
* [GetBestBlockHash][rpc getbestblockhash] RPC: {{summary_getBestBlockHash}}