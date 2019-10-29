---
title: "Solo Mining"
excerpt: ""
---
As illustrated below, solo miners typically use `dashd` to get new transactions from the network. Their mining software periodically polls `dashd` for new transactions using the `getblocktemplate` RPC, which provides the list of new transactions plus the public key to which the coinbase transaction should be sent.

![Solo Bitcoin Mining](https://dash-docs.github.io/img/dev/en-solo-mining-overview.svg)

The mining software constructs a block using the template (described below) and creates a block header. It then sends the 80-byte block header to its mining hardware (an ASIC) along with a target threshold (difficulty setting). The mining hardware iterates through every possible value for the block header nonce and generates the corresponding hash.

If none of the hashes are below the threshold, the mining hardware gets an updated block header with a new merkle root from the mining software;
this new block header is created by adding extra nonce data to the coinbase field of the coinbase transaction.

On the other hand, if a hash is found below the target threshold, the mining hardware returns the block header with the successful nonce to the mining software. The mining software combines the header with the block and sends the completed block to `dashd` to be broadcast to the network for addition to the block chain.