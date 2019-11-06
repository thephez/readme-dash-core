#!/usr/bin/env bash
# Called by update-all-message-urls.sh

perl \
	-pe "s~ (\`block\` message[s]?)~ \[\1\](core-ref-p2p-network-data-messages#section-block)~g;" \
	-pe "s~ (\`blocktxn\` message[s]?)~ \[\1\](core-ref-p2p-network-data-messages#section-blocktxn)~g;" \
	-pe "s~ (\`cmpctblock\` message[s]?)~ \[\1\](core-ref-p2p-network-data-messages#section-cmpctblock)~g;" \
	-pe "s~ (\`getblocks\` message[s]?)~ \[\1\](core-ref-p2p-network-data-messages#section-getblocks)~g;" \
	-pe "s~ (\`getblocktxn\` message[s]?)~ \[\1\](core-ref-p2p-network-data-messages#section-getblocktxn)~g;" \
	-pe "s~ (\`getdata\` message[s]?)~ \[\1\](core-ref-p2p-network-data-messages#section-getdata)~g;" \
	-pe "s~ (\`getheaders\` message[s]?)~ \[\1\](core-ref-p2p-network-data-messages#section-getheaders)~g;" \
	-pe "s~ (\`getmnlistd\` message[s]?)~ \[\1\](core-ref-p2p-network-data-messages#section-getmnlistd)~g;" \
	-pe "s~ (\`headers\` message[s]?)~ \[\1\](core-ref-p2p-network-data-messages#section-headers)~g;" \
	-pe "s~ (\`inv\` message[s]?)~ \[\1\](core-ref-p2p-network-data-messages#section-inv)~g;" \
	-pe "s~ (\`mempool\` message[s]?)~ \[\1\](core-ref-p2p-network-data-messages#section-mempool)~g;" \
	-pe "s~ (\`merkleblock\` message[s]?)~ \[\1\](core-ref-p2p-network-data-messages#section-merkleblock)~g;" \
	-pe "s~ (\`mnlistdiff\` message[s]?)~ \[\1\](core-ref-p2p-network-data-messages#section-mnlistdiff)~g;" \
	-pe "s~ (\`notfound\` message[s]?)~ \[\1\](core-ref-p2p-network-data-messages#section-notfound)~g;" \
	-pe "s~ (\`tx\` message[s]?)~ \[\1\](core-ref-p2p-network-data-messages#section-tx)~g;" \
	-pe "s~ (\`addr\` message[s]?)~ \[\1\](core-ref-p2p-network-control-messages#section-addr)~g;" \
	-pe "s~ (\`filteradd\` message[s]?)~ \[\1\](core-ref-p2p-network-control-messages#section-filteradd)~g;" \
	-pe "s~ (\`filterclear\` message[s]?)~ \[\1\](core-ref-p2p-network-control-messages#section-filterclear)~g;" \
	-pe "s~ (\`filterload\` message[s]?)~ \[\1\](core-ref-p2p-network-control-messages#section-filterload)~g;" \
	-pe "s~ (\`getaddr\` message[s]?)~ \[\1\](core-ref-p2p-network-control-messages#section-getaddr)~g;" \
	-pe "s~ (\`getsporks\` message[s]?)~ \[\1\](core-ref-p2p-network-control-messages#section-getsporks)~g;" \
	-pe "s~ (\`ping\` message[s]?)~ \[\1\](core-ref-p2p-network-control-messages#section-ping)~g;" \
	-pe "s~ (\`pong\` message[s]?)~ \[\1\](core-ref-p2p-network-control-messages#section-pong)~g;" \
	-pe "s~ (\`reject\` message[s]?)~ \[\1\](core-ref-p2p-network-control-messages#section-reject)~g;" \
	-pe "s~ (\`sendcmpct\` message[s]?)~ \[\1\](core-ref-p2p-network-control-messages#section-sendcmpct)~g;" \
	-pe "s~ (\`senddsq\` message[s]?)~ \[\1\](core-ref-p2p-network-control-messages#section-senddsq)~g;" \
	-pe "s~ (\`sendheaders\` message[s]?)~ \[\1\](core-ref-p2p-network-control-messages#section-sendheaders)~g;" \
	-pe "s~ (\`spork\` message[s]?)~ \[\1\](core-ref-p2p-network-control-messages#section-spork)~g;" \
	-pe "s~ (\`verack\` message[s]?)~ \[\1\](core-ref-p2p-network-control-messages#section-verack)~g;" \
	-pe "s~ (\`version\` message[s]?)~ \[\1\](core-ref-p2p-network-control-messages#section-version)~g;" \
	-pe "s~ (\`govobj\` message[s]?)~ \[\1\](core-ref-p2p-network-governance-messages#section-govobj)~g;" \
	-pe "s~ (\`govobjvote\` message[s]?)~ \[\1\](core-ref-p2p-network-governance-messages#section-govobjvote)~g;" \
	-pe "s~ (\`govsync\` message[s]?)~ \[\1\](core-ref-p2p-network-governance-messages#section-govsync)~g;" \
	-pe "s~ (\`clsig\` message[s]?)~ \[\1\](core-ref-p2p-network-instantsend-messages#section-clsig)~g;" \
	-pe "s~ (\`islock\` message[s]?)~ \[\1\](core-ref-p2p-network-instantsend-messages#section-islock)~g;" \
	-pe "s~ (\`ssc\` message[s]?)~ \[\1\](core-ref-p2p-network-masternode-messages#section-ssc)~g;" \
	-pe "s~ (\`mnauth\` message[s]?)~ \[\1\](core-ref-p2p-network-masternode-messages#section-mnauth)~g;" \
	-pe "s~ (\`dsa\` message[s]?)~ \[\1\](core-ref-p2p-network-privatesend-messages#section-dsa)~g;" \
	-pe "s~ (\`dsc\` message[s]?)~ \[\1\](core-ref-p2p-network-privatesend-messages#section-dsc)~g;" \
	-pe "s~ (\`dsf\` message[s]?)~ \[\1\](core-ref-p2p-network-privatesend-messages#section-dsf)~g;" \
	-pe "s~ (\`dsi\` message[s]?)~ \[\1\](core-ref-p2p-network-privatesend-messages#section-dsi)~g;" \
	-pe "s~ (\`dsq\` message[s]?)~ \[\1\](core-ref-p2p-network-privatesend-messages#section-dsq)~g;" \
	-pe "s~ (\`dss\` message[s]?)~ \[\1\](core-ref-p2p-network-privatesend-messages#section-dss)~g;" \
	-pe "s~ (\`dssu\` message[s]?)~ \[\1\](core-ref-p2p-network-privatesend-messages#section-dssu)~g;" \
	-pe "s~ (\`dstx\` message[s]?)~ \[\1\](core-ref-p2p-network-privatesend-messages#section-dstx)~g;" \
	-pe "s~ (\`qcontrib\` message[s]?)~ \[\1\](core-ref-p2p-network-quorum-messages#section-qcontrib)~g;" \
	-pe "s~ (\`qcomplaint\` message[s]?)~ \[\1\](core-ref-p2p-network-quorum-messages#section-qcomplaint)~g;" \
	-pe "s~ (\`qjustify\` message[s]?)~ \[\1\](core-ref-p2p-network-quorum-messages#section-qjustify)~g;" \
	-pe "s~ (\`qpcommit\` message[s]?)~ \[\1\](core-ref-p2p-network-quorum-messages#section-qpcommit)~g;" \
	-pe "s~ (\`qfcommit\` message[s]?)~ \[\1\](core-ref-p2p-network-quorum-messages#section-qfcommit)~g;" \
	-pe "s~ (\`qbsigs\` message[s]?)~ \[\1\](core-ref-p2p-network-quorum-messages#section-qbsigs)~g;" \
	-pe "s~ (\`qgetsigs\` message[s]?)~ \[\1\](core-ref-p2p-network-quorum-messages#section-qgetsigs)~g;" \
	-pe "s~ (\`qsendrecsigs\` message[s]?)~ \[\1\](core-ref-p2p-network-quorum-messages#section-qsendrecsigs)~g;" \
	-pe "s~ (\`qsigrec\` message[s]?)~ \[\1\](core-ref-p2p-network-quorum-messages#section-qsigrec)~g;" \
	-pe "s~ (\`qsigsesann\` message[s]?)~ \[\1\](core-ref-p2p-network-quorum-messages#section-qsigsesann)~g;" \
	-pe "s~ (\`qsigsinv\` message[s]?)~ \[\1\](core-ref-p2p-network-quorum-messages#section-qsigsinv)~g;" \
	-pe "s~ (\`qwatch\` message[s]?)~ \[\1\](core-ref-p2p-network-quorum-messages#section-qwatch)~g;" \
