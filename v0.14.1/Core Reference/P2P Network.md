---
title: "P2P Network"
excerpt: ""
---
This section describes the Dash P2P network protocol (but it is not a specification). It does not describe the [BIP70 payment protocol][/en/glossary/payment-protocol], the [GetBlockTemplate mining protocol][section getblocktemplate], or any network protocol never implemented in an official version of Dash Core.

All peer-to-peer communication occurs entirely over TCP.
[block:callout]
{
  "type": "warning",
  "body": "Note: unless their description says otherwise, all multi-byte integers mentioned in this section are transmitted in little-endian order."
}
[/block]