---
title: "Full Node"
excerpt: ""
---
The first and most secure model is the one followed by Dash Core, also known as a “thick” or “full chain” client. This security model assures the validity of the block chain by downloading and validating blocks from the genesis block all the way to the most recently discovered block. This is known as using the *height* of a particular block to verify the client’s view of the network.

For a client to be fooled, an adversary would need to give a complete alternative block chain history that is of greater difficulty than the current “true” chain, which is computationally expensive (if not impossible) due to the fact that the chain with the most cumulative proof of work is by definition the "true" chain. Due to the computational difficulty required to generate a new block at the tip of the chain, the ability to fool a full node becomes very expensive after 6 confirmations. This form of verification is highly resistant to sybil attacks---only a single honest network peer is required in order to receive and verify the complete state of the "true" block chain.

![Block Height Compared To Block Depth](https://dash-docs.github.io/img/dev/en-block-height-vs-depth.svg)