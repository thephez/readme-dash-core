---
title: "Quick Reference"
excerpt: "List of Dash Core HTTP REST APIs"
---
* [GET Block](/docs/core-api-ref-http-rest-requests#section-get-block) gets a block with a particular header hash from the local block database either as a JSON object or as a serialized block. _Updated in Bitcoin Core 0.13.0_
* [GET Block/NoTxDetails](/docs/core-api-ref-http-rest-requests#section-get-blocknotxdetails) gets a block with a particular header hash from the local block database either as a JSON object or as a serialized block.  The JSON object includes TXIDs for transactions within the block rather than the complete transactions [GET block](/docs/core-api-ref-http-rest-requests#section-get-block) returns. _Updated in Bitcoin Core 0.13.0_
* [GET ChainInfo](/docs/core-api-ref-http-rest-requests#section-get-chaininfo) returns information about the current state of the block chain. _Updated in Bitcoin Core 0.12.0_
* [GET GetUtxos](/docs/core-api-ref-http-rest-requests#section-get-getutxos) returns an UTXO set given a set of outpoints. _New in Bitcoin Core 0.11.0_
* [GET Headers](/docs/core-api-ref-http-rest-requests#section-get-headers) returns a specified amount of block headers in upward direction. _Updated in Bitcoin Core 0.13.0_
* [GET MemPool/Contents](/docs/core-api-ref-http-rest-requests#section-get-mempoolcontents) returns all transaction in the memory pool with detailed information. _New in Bitcoin Core 0.12.0_
* [GET MemPool/Info](/docs/core-api-ref-http-rest-requests#section-get-mempoolinfo) returns information about the node's current transaction memory pool. _New in Bitcoin Core 0.12.0_
* [GET Tx](/docs/core-api-ref-http-rest-requests#section-get-tx) gets a hex-encoded serialized transaction or a JSON object describing the transaction. By default, Dash Core only stores complete transaction data for UTXOs and your own transactions, so this method may fail on historic transactions unless you use the non-default `txindex=1` in your Dash Core startup settings. _Updated in Bitcoin Core 0.13.0_