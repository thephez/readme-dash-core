---
title: "Instantsend"
excerpt: ""
---
Dash Core's InstantSend feature provides a way to lock transaction inputs and enable secure, instantaneous transactions. The network automatically attempts to upgrade any qualifying transaction to InstantSend without a need for the sending wallet to explicitly request it.

* To qualify for InstantSend, transaction inputs must either:
  * Be locked by InstantSend
  * Be in a block that has a ChainLock
  * Have at least the number confirmations (block depth) indicated by the table below

| **Network** | **Confirmations Required** |
| --- | --- |
| Mainnet | 6 Blocks |
| Testnet / Regtest / Devnet | 2 Blocks |

The introduction of Long-Living Masternode Quorums in Dash Core 0.14 provided a foundation to scale InstantSend. The transaction input locking process (and resulting network traffic) now occurs only within the quorum. This minimizes network congestion since only the `islock` message produced by the locking process is relayed to the entire Dash network. This message contains all the information necessary to verify a successful transaction lock.

Sporks 2 (`SPORK_2_INSTANTSEND_ENABLED`) and 20 (`SPORK_20_INSTANTSEND_LLMQ_BASED`) are used to manage InstantSend. Spork 2 enables or disables the entire InstantSend feature. Spork 20 was used to support the transition to LLMQ-based InstantSend and is currently retained for backward compatibility. It will be deprecated in a future release.

Note: A transaction will __not__ be included in the block template (from `getblocktemplate`) unless it:

 1. Has been locked, or 2. Has been in the mempool for >=10 minutes (`WAIT_FOR_ISLOCK_TIMEOUT`)

A miner may still include any transaction, but blocks containing only locked transactions (or ones older than the timeout) should achieve a ChainLock faster. This is desirable to miners since it prevents any reorgs that might orphan their block.

*InstantSend Data Flow*

| **InstantSend Client** | **Direction**  | **Peers**   | **Description** |
| --- | :---: | --- | --- |
| `tx` message                | → |                         | Client sends InstantSend transaction
| **LLMQ Signing Sessions**   |   |                         | Quorums internally process locking |
|                             |   |                         | Quorum(s) responsible for the transaction's inputs lock the inputs via LLMQ signing sessions
|                             |   |                         | Once all inputs are locked, the quorum responsible for the overall transaction creates the transaction lock (`islock`) via an LLMQ signing session
| **LLMQ Results**             |   |                         | Quorum results broadcast to the network |
|                             | ← | `inv` message (islock)  | Quorum responds with lock inventory
| `getdata` message (islock)  | → |                         | Client requests lock message
|                             | ← | `islock` message        | Quorum responds with lock message

Once a transaction lock is approved, the `instantlock` field of various RPCs is set to `true` (e.g. the `getmempoolentry` RPC).