---
title: "Masternode Payment"
excerpt: ""
---
Since DIP3 (introduced in Dash Core 0.13.0), masternode reward payments are based on the deterministic masternode list information found on-chain in each block. This results in a transparent, deterministic process that operates using the [algorithm described in DIP3](https://github.com/dashpay/dips/blob/master/dip-0003.md#masternode-rewards).

On-chain masternode lists reduce the complexity of reward payments, make payments much more predictable, and also allow masternode payments to be enforced for all blocks (enforcement for superblocks was not possible in the previous system).