---
title: "Block Broadcasting"
excerpt: ""
---
When a miner discovers a new block, it broadcasts the new block to its peers using one of the following methods:

* **<<glossary:Unsolicited Block Push>>:**
  the miner sends a `block` message to each of its full node peers with the new block. The miner can reasonably bypass the standard relay method in this way because it knows none of its peers already have the just-discovered block.

* **<<glossary:Standard Block Relay>>:**
  the miner, acting as a standard relay node, sends an `inv` message to each of its peers (both full node and SPV) with an inventory referring to the new block. The most common responses are:

   * Each blocks-first (BF) peer that wants the block replies with a `getdata` message requesting the full block.

   * Each headers-first (HF) peer that wants the block replies with a `getheaders` message containing the header hash of the highest-height header on its best header chain, and likely also some headers further back on the best header chain to allow fork detection. That message is immediately followed by a `getdata` message requesting the full block. By requesting headers first, a headers-first peer can refuse orphan blocks as described in the subsection below.

   * Each Simplified Payment Verification (SPV) client that wants the block replies with a `getdata` message typically requesting a merkle block.

   The miner replies to each request accordingly by sending the block in a `block` message, one or more headers in a `headers` message, or the merkle block and transactions relative to the SPV client's bloom filter in a `merkleblock` message followed by zero or more `tx` messages.

By default, Dash Core broadcasts blocks using standard block relay, but it will accept blocks sent using either of the methods described above.

Full nodes validate the received block and then advertise it to their peers using the standard block relay method described above.  The condensed table below highlights the operation of the messages described above (Relay, BF, HF, and SPV refer to the relay node, a blocks-first node, a headers-first node, and an SPV client; *any* refers to a node using any block retrieval method.)

| **Message** | [`inv`][inv message]                                   | [`getdata`][getdata message]               | [`getheaders`][getheaders message]                                     | [`headers`][headers message]
| --- | --- | --- | --- | --- |
| **From→To** | Relay→_Any_                                            | BF→Relay                                   | HF→Relay                                                               | Relay→HF
| **Payload** | The inventory of the new block                         | The inventory of the new block             | One or more header hashes on the HF node's best header chain (BHC)     | Up to 2,000 headers connecting HF node's BHC to relay node's BHC
| **Message** | [`block`][block message]                               | [`merkleblock`][merkleblock message]       | [`tx`][tx message]                                                     |
| **From→To** | Relay→BF/HF                                            | Relay→SPV                                  | Relay→SPV                                                              |
| **Payload** | The new block in [serialized format][section serialized blocks] | The new block filtered into a merkle block | Serialized transactions from the new block that match the bloom filter |

# Orphan Blocks

Blocks-first nodes may download orphan blocks---blocks whose previous block header hash field refers to a block header this node hasn't seen yet. In other words, orphan blocks have no known parent (unlike stale blocks, which have known parents but which aren't part of the best block chain).

![Difference Between Orphan And Stale Blocks](https://dash-docs.github.io/img/dev/en-orphan-stale-definition.svg)

When a blocks-first node downloads an orphan block, it will not validate it. Instead, it will send a `getblocks` message to the node which sent the orphan block; the broadcasting node will respond with an `inv` message containing inventories of any blocks the downloading node is missing (up to 500); the downloading node will request those blocks with a `getdata` message; and the broadcasting node will send those blocks with a `block` message. The downloading node will validate those blocks, and once the parent of the former orphan block has been validated, it will validate the former orphan block.

Headers-first nodes avoid some of this complexity by always requesting block headers with the `getheaders` message before requesting a block with the `getdata` message. The broadcasting node will send a `headers` message containing all the block headers (up to 2,000) it thinks the downloading node needs to reach the tip of the best header chain; each of those headers will point to its parent, so when the downloading node receives the `block` message, the block shouldn't be an orphan block---all of its parents should be known (even if they haven't been validated yet). If, despite this, the block received in the `block` message is an orphan block, a headers-first node will discard it immediately.

However, orphan discarding does mean that headers-first nodes will ignore orphan blocks sent by miners in an unsolicited block push.