---
title: "Retrieving A MerkleBlock"
excerpt: ""
---
For the [`merkleblock` message](core-ref-p2p-network-data-messages#section-merkleblock) documentation on the reference page, an actual merkle block was retrieved from the network and manually processed.  This section walks through each step of the process, demonstrating basic network communication and merkle block processing.

``` python

#!/usr/bin/env python

from time import sleep
from hashlib import sha256
import struct
import sys

network_string = "f9beb4d9".decode("hex")  # Mainnet

def send(msg,payload):
    ## Command is ASCII text, null padded to 12 bytes
    command = msg + ( ( 12 - len(msg) ) * "\00" )

    ## Payload length is a uint32_t
    payload_raw = payload.decode("hex")
    payload_len = struct.pack("I", len(payload_raw))

    ## Checksum is first 4 bytes of SHA256(SHA256(<payload>))
    checksum = sha256(sha256(payload_raw).digest()).digest()[:4]

    sys.stdout.write(
        network_string
        + command
        + payload_len
        + checksum
        + payload_raw
    )
    sys.stdout.flush()
```

To connect to the P2P network, the trivial Python function above was developed to compute message headers and send payloads decoded from hex.

``` python
## Create a version message
send("version",
      "71110100" # ........................ Protocol Version: 70001
    + "0000000000000000" # ................ Services: Headers Only (SPV)
    + "c6925e5400000000" # ................ Time: 1415484102
    + "00000000000000000000000000000000"
    + "0000ffff7f000001208d" # ............ Receiver IP Address/Port
    + "00000000000000000000000000000000"
    + "0000ffff7f000001208d" # ............ Sender IP Address/Port
    + "0000000000000000" # ................ Nonce (not used here)
    + "1b" # .............................. Bytes in version string
    + "2f426974636f696e2e6f726720457861"
    + "6d706c653a302e392e332f" # .......... Version string
    + "93050500" # ........................ Starting block height: 329107
    + "00" # .............................. Relay transactions: false
)
```

Peers on the network will not accept any requests until you send them a [`version` message](core-ref-p2p-network-control-messages#section-version). The receiving node will reply with their [`version` message](core-ref-p2p-network-control-messages#section-version) and a [`verack` message](core-ref-p2p-network-control-messages#section-verack).

``` python
sleep(1)
send("verack", "")
```

We're not going to validate their [`version` message](core-ref-p2p-network-control-messages#section-version) with this simple script, but we will sleep a short bit and send back our own [`verack` message](core-ref-p2p-network-control-messages#section-verack) as if we had accepted their [`version` message](core-ref-p2p-network-control-messages#section-version).

``` python
send("filterload",
      "02"  # ........ Filter bytes: 2
    + "b50f" # ....... Filter: 1010 1101 1111 0000
    + "0b000000" # ... nHashFuncs: 11
    + "00000000" # ... nTweak: 0/none
    + "00" # ......... nFlags: BLOOM_UPDATE_NONE
)
```

We set a bloom filter with the [`filterload` message](core-ref-p2p-network-control-messages#section-filterload). This filter is described in the two preceding sections.

``` python
send("getdata",
      "01" # ................................. Number of inventories: 1
    + "03000000" # ........................... Inventory type: filtered block
    + "a4deb66c0d726b0aefb03ed51be407fb"
    + "ad7331c6e8f9eef231b7000000000000" # ... Block header hash
)
```

We request a merkle block for transactions matching our filter, completing our script.

To run the script, we simply pipe it to the Unix [`netcat` command](https://en.wikipedia.org/wiki/Netcat) or one of its many clones, one of which is available for practically any platform. For example, with the original netcat and using hexdump (`hd`) to display the output:

``` bash
## Connect to the Bitcoin Core peer running on localhost
python get-merkle.py | nc localhost 8333 | hd
```

Part of the response is shown in the [Parsing a MerkleBlock](core-examples-p2p-network-parsing-a-merkleblock) section.