---
title: "Quick Reference"
excerpt: ""
---
#### Addressindex RPCs

These RPCs are all Dash-specific and not found in Bitcoin Core

* [GetAddressBalance](/docs/core-api-ref-remote-procedure-calls-address-index#section-getaddressbalance): returns the balance for address(es).
* [GetAddressDeltas](/docs/core-api-ref-remote-procedure-calls-address-index#section-getaddressdeltas): returns all changes for an address.
* [GetAddressMempool](/docs/core-api-ref-remote-procedure-calls-address-index#section-getaddressmempool): returns all mempool deltas for an address.
* [GetAddressTxids](/docs/core-api-ref-remote-procedure-calls-address-index#section-getaddresstxids): returns the txids for an address(es).
* [GetAddressUtxos](/docs/core-api-ref-remote-procedure-calls-address-index#section-getaddressutxos): returns all unspent outputs for an address.

#### Block Chain RPCs

* [GetBestBlockHash](/docs/core-api-ref-remote-procedure-calls-blockchain#section-getbestblockhash): returns the header hash of the most recent block on the best block chain.
* [GetBestChainLock](/docs/core-api-ref-remote-procedure-calls-blockchain#section-getbestchainlock): returns the block hash of the best chainlock. {{DASH_NEW0_14_1}}
* [GetBlock](/docs/core-api-ref-remote-procedure-calls-blockchain#section-getblock): gets a block with a particular header hash from the local block database either as a JSON object or as a serialized block. {{DASH_UPDATED0_14_1}}
* [GetBlockChainInfo](/docs/core-api-ref-remote-procedure-calls-blockchain#section-getblockchaininfo): provides information about the current state of the block chain. {{DASH_UPDATED0_14_1}}
* [GetBlockCount](/docs/core-api-ref-remote-procedure-calls-blockchain#section-getblockcount): returns the number of blocks in the local best block chain.
* [GetBlockHash](/docs/core-api-ref-remote-procedure-calls-blockchain#section-getblockhash): returns the header hash of a block at the given height in the local best block chain.
* [GetBlockHashes](/docs/core-api-ref-remote-procedure-calls-blockchain#section-getblockhashes): returns array of hashes of blocks within the timestamp range provided (requires `timestampindex` to be enabled). {{DASH_NEW0_12_1}}
* [GetBlockHeader](/docs/core-api-ref-remote-procedure-calls-blockchain#section-getblockheader): gets a block header with a particular header hash from the local block database either as a JSON object or as a serialized block header. {{NEW0_12_0}}
* [GetBlockHeaders](/docs/core-api-ref-remote-procedure-calls-blockchain#section-getblockheaders): returns an array of items with information about the requested number of blockheaders starting from the requested hash. {{DASH_NEW0_12_1}}
* [GetBlockStats](/docs/core-api-ref-remote-procedure-calls-blockchain#section-getblockstats): computes per block statistics for a given window. {{DASH_NEW0_14_1}}
* [GetChainTips](/docs/core-api-ref-remote-procedure-calls-blockchain#section-getchaintips): returns information about the highest-height block (tip) of each local block chain. {{DASH_UPDATED0_12_3}}
* [GetChainTxStats](/docs/core-api-ref-remote-procedure-calls-blockchain#section-getchaintxstats): compute statistics about the total number and rate of transactions in the chain. {{DASH_NEW0_14_1}}
* [GetDifficulty](/docs/core-api-ref-remote-procedure-calls-blockchain#section-getdifficulty): returns the proof-of-work difficulty as a multiple of the minimum difficulty.
* [GetMemPoolAncestors](/docs/core-api-ref-remote-procedure-calls-blockchain#section-getmempoolancestors): returns all in-mempool ancestors for a transaction in the mempool. {{DASH_UPDATED0_14_0}} {{NEW0_13_0}}
* [GetMemPoolDescendants](/docs/core-api-ref-remote-procedure-calls-blockchain#section-getmempooldescendants): returns all in-mempool descendants for a transaction in the mempool. {{DASH_UPDATED0_14_0}} {{NEW0_13_0}}
* [GetMemPoolEntry][rpc  getmempoolentry]: returns mempool data for given transaction (must be in mempool). {{DASH_UPDATED0_14_0}} {{NEW0_13_0}}
* [GetMemPoolInfo](/docs/core-api-ref-remote-procedure-calls-blockchain#section-getmempoolinfo): returns information about the node's current transaction memory pool. {{DASH_UPDATED0_14_1}}
* [GetRawMemPool](/docs/core-api-ref-remote-procedure-calls-blockchain#section-getrawmempool): returns all transaction identifiers (TXIDs) in the memory pool as a JSON array, or detailed information about each transaction in the memory pool as a JSON object. {{DASH_UPDATED0_14_1}}
* [GetMerkleBlocks](/docs/core-api-ref-remote-procedure-calls-blockchain#section-getmerkleblocks): returns an array of hex-encoded merkleblocks for <count> blocks<!--noref--> starting from <hash> which match <filter>. {{DASH_NEW0_14_1}}
* [GetSpecialTxes](/docs/core-api-ref-remote-procedure-calls-blockchain#section-getspecialtxes): returns an array of special transactions found in the specified block {{DASH_NEW0_13_1}}
* [GetSpentInfo](/docs/core-api-ref-remote-procedure-calls-blockchain#section-getspentinfo): returns the txid and index where an output is spent (requires `spentindex` to be enabled). {{DASH_NEW0_12_1}}
* [GetTxOut](/docs/core-api-ref-remote-procedure-calls-blockchain#section-gettxout): returns details about an unspent transaction output (UTXO). {{DASH_UPDATED0_14_1}}
* [GetTxOutProof](/docs/core-api-ref-remote-procedure-calls-blockchain#section-gettxoutproof): returns a hex-encoded proof that one or more specified transactions were included in a block. {{NEW0_11_0}}
* [GetTxOutSetInfo](/docs/core-api-ref-remote-procedure-calls-blockchain#section-gettxoutsetinfo): returns statistics about the confirmed unspent transaction output (UTXO) set. Note that this call may take some time and that it only counts outputs from confirmed transactions---it does not count outputs from the memory pool. {{DASH_UPDATED0_14_1}}
* [PreciousBlock](/docs/core-api-ref-remote-procedure-calls-blockchain#section-preciousblock): treats a block as if it were received before others with the same work. {{DASH_NEW0_12_3}} {{NEW0_14_0}}
* [PruneBlockChain](/docs/core-api-ref-remote-procedure-calls-blockchain#section-pruneblockchain): prunes the blockchain up to a specified height or timestamp. {{DASH_NEW0_12_3}} {{NEW0_14_0}}
* [VerifyChain](/docs/core-api-ref-remote-procedure-calls-blockchain#section-verifychain): verifies each entry in the local block chain database.
* [VerifyTxOutProof](/docs/core-api-ref-remote-procedure-calls-blockchain#section-verifytxoutproof): verifies that a proof points to one or more transactions in a block, returning the transactions the proof commits to and throwing an RPC error if the block is not in our best block chain. {{NEW0_11_0}}

#### Control RPCs

* [Debug](/docs/core-api-ref-remote-procedure-calls-control#section-debug): changes the debug category from the console. {{DASH_UPDATED0_14_0}}
* [GetInfo](/docs/core-api-ref-remote-procedure-calls-control#section-getinfo): prints various information about the node and the network. {{DASH_UPDATED0_14_1}} {{DEPRECATED}}
* [GetMemoryInfo](/docs/core-api-ref-remote-procedure-calls-control#section-getmemoryinfo): returns information about memory usage. {{DASH_UPDATED0_14_1}} {{NEW_14_0}}
* [Help](/docs/core-api-ref-remote-procedure-calls-control#section-help): lists all available public RPC commands, or gets help for the specified RPC.  Commands which are unavailable will not be listed, such as wallet RPCs if wallet support is disabled.
* [Logging](/docs/core-api-ref-remote-procedure-calls-control#section-logging): gets and sets the logging configuration {{DASH_NEW0_14_1}}
* [Stop](/docs/core-api-ref-remote-procedure-calls-control#section-stop): safely shuts down the Dash Core server.
* [Uptime](/docs/core-api-ref-remote-procedure-calls-control#section-uptime): returns the total uptime of the server. {{DASH_NEW0_14_1}}

#### Dash RPCs

* [GetGovernanceInfo](/docs/core-api-ref-remote-procedure-calls-dash#section-getgovernanceinfo): returns an object containing governance parameters. {{DASH_UPDATED0_14_0}}
* [GetPoolInfo](/docs/core-api-ref-remote-procedure-calls-dash#section-getpoolinfo): returns an object containing mixing pool related information. {{DEPRECATED}}
* [GetPrivateSendInfo][rpc getprivatesendinfo]: {{summary_getPrivateSend}} {{DASH_NEW0_14_1}}
* [GetSuperblockBudget](/docs/core-api-ref-remote-procedure-calls-dash#section-getsuperblockbudget): returns the absolute maximum sum of superblock payments allowed.
* [GObject](/docs/core-api-ref-remote-procedure-calls-dash#section-gobject): provides a set of commands for managing governance objects and displaying information about them. {{DASH_UPDATED0_14_1}}
* [Masternode](/docs/core-api-ref-remote-procedure-calls-dash#section-masternode): provides a set of commands for managing masternodes and displaying information about them. {{DASH_UPDATED0_14_0}}
* [MasternodeList](/docs/core-api-ref-remote-procedure-calls-dash#section-masternodelist): returns a list of masternodes in different modes. {{DASH_UPDATED0_14_0}}
* [MnSync](/docs/core-api-ref-remote-procedure-calls-dash#section-mnsync): returns the sync status, updates to the next step or resets it entirely. {{DASH_UPDATED0_14_0}}
* [PrivateSend](/docs/core-api-ref-remote-procedure-calls-dash#section-privatesend): controls the mixing process. {{DASH_UPDATED0_12_3}}
* [Spork](/docs/core-api-ref-remote-procedure-calls-dash#section-spork): reads or updates spork settings on the network.
* [VoteRaw](/docs/core-api-ref-remote-procedure-calls-dash#section-voteraw): compiles and relays a governance vote with provided external signature instead of signing vote internally

#### Evolution RPCs

* [BLS](/docs/core-api-ref-remote-procedure-calls-evolution#section-bls): provides a set of commands to execute BLS-related actions. {{DASH_UPDATED0_14_0}}
* [ProTx](/docs/core-api-ref-remote-procedure-calls-evolution#section-protx): provides a set of commands to execute ProTx related actions. {{DASH_UPDATED0_14_0}}
* [Quorum](/docs/core-api-ref-remote-procedure-calls-evolution#section-quorum): provides a set of commands for quorums (LLMQs). {{DASH_NEW0_14_0}}

#### Generating RPCs

* [Generate](/docs/core-api-ref-remote-procedure-calls-generating#section-generate): mines blocks immediately (before the RPC call returns). {{DASH_UPDATED0_12_3}} {{UPDATED0_13_0}}
* [GenerateToAddress](/docs/core-api-ref-remote-procedure-calls-generating#section-generatetoaddress): mines blocks immediately to a specified address. {{DASH_NEW0_12_3}} {{NEW0_13_0}}

#### Mining RPCs

* [GetBlockTemplate](/docs/core-api-ref-remote-procedure-calls-mining#section-getblocktemplate): gets a block template or proposal for use with mining software. {{DASH_UPDATED0_13_0}}
* [GetMiningInfo](/docs/core-api-ref-remote-procedure-calls-mining#section-getmininginfo): returns various mining-related information. {{UPDATED0_14_0}}
* [GetNetworkHashPS](/docs/core-api-ref-remote-procedure-calls-mining#section-getnetworkhashps): returns the estimated network hashes per second based on the last n blocks.
* [PrioritiseTransaction](/docs/core-api-ref-remote-procedure-calls-mining#section-prioritisetransaction): adds virtual priority or fee to a transaction, allowing it to be accepted into blocks mined by this node (or miners which use this node) with a lower priority or fee. (It can also remove virtual priority or fee, requiring the transaction have a higher priority or fee to be accepted into a locally-mined block.) {{UPDATED0_14_0}}
* [SubmitBlock](/docs/core-api-ref-remote-procedure-calls-mining#section-submitblock): accepts a block, verifies it is a valid addition to the block chain, and broadcasts it to the network. Extra parameters are ignored by Dash Core but may be used by mining pools or other programs.

#### Network RPCs

* [AddNode](/docs/core-api-ref-remote-procedure-calls-network#section-addnode): attempts to add or remove a node from the addnode list, or to try a connection to a node once. {{UPDATED0_14_0}}
* [ClearBanned](/docs/core-api-ref-remote-procedure-calls-network#section-clearbanned): clears list of banned nodes. {{NEW0_12_0}}
* [DisconnectNode](/docs/core-api-ref-remote-procedure-calls-network#section-disconnectnode): immediately disconnects from a specified node. {{DASH_UPDATED0_14_1}} {{UPDATED0_14_1}}
* [GetAddedNodeInfo](/docs/core-api-ref-remote-procedure-calls-network#section-getaddednodeinfo): returns information about the given added node, or all added nodes (except onetry nodes). Only nodes which have been manually added using the `addnode` RPC will have their information displayed. {{DASH_UPDATED0_12_3}} {{UPDATED0_14_0}}
* [GetConnectionCount](/docs/core-api-ref-remote-procedure-calls-network#section-getconnectioncount): returns the number of connections to other nodes.
* [GetNetTotals](/docs/core-api-ref-remote-procedure-calls-network#section-getnettotals): returns information about network traffic, including bytes in, bytes out, and the current time. {{UPDATED0_12_0}}
* [GetNetworkInfo](/docs/core-api-ref-remote-procedure-calls-network#section-getnetworkinfo): returns information about the node's connection to the network. {{DASH_UPDATED0_14_0}}
* [GetPeerInfo](/docs/core-api-ref-remote-procedure-calls-network#section-getpeerinfo): returns data about each connected network node. {{DASH_UPDATED0_14_1}}
* [ListBanned](/docs/core-api-ref-remote-procedure-calls-network#section-listbanned): lists all banned IPs/Subnets. {{NEW0_12_0}}
* [Ping](/docs/core-api-ref-remote-procedure-calls-network#section-ping): sends a P2P ping message to all connected nodes to measure ping time. Results are provided by the `getpeerinfo` RPC pingtime and pingwait fields as decimal seconds. The P2P `ping` message is handled in a queue with all other commands, so it measures processing backlog, not just network<!--noref--> ping.
* [SetBan](/docs/core-api-ref-remote-procedure-calls-network#section-setban): attempts add or remove a IP/Subnet from the banned list. {{NEW0_12_0}}
* [SetNetworkActive](/docs/core-api-ref-remote-procedure-calls-network#section-setnetworkactive): disables/enables all P2P network activity. {{NEW0_14_0}}

#### Raw Transaction RPCs

* [CombineRawTransaction](/docs/core-api-ref-remote-procedure-calls-raw-transaction#section-combinerawtransaction): combine multiple partially signed transactions into one transaction. {{DASH_NEW0_14_1}}
* [CreateRawTransaction](/docs/core-api-ref-remote-procedure-calls-raw-transaction#section-createrawtransaction): creates an unsigned serialized transaction that spends a previous output to a new output with a P2PKH or P2SH address. The transaction is not stored in the wallet or transmitted to the network. {{DASH_UPDATED0_12_3}} {{UPDATED0_14_1}}
* [DecodeRawTransaction](/docs/core-api-ref-remote-procedure-calls-raw-transaction#section-decoderawtransaction): decodes a serialized transaction hex string into a JSON object describing the transaction. {{UPDATED0_13_0}}
* [DecodeScript](/docs/core-api-ref-remote-procedure-calls-raw-transaction#section-decodescript): decodes a hex-encoded P2SH redeem script.
* [FundRawTransaction](/docs/core-api-ref-remote-procedure-calls-raw-transaction#section-fundrawtransaction): adds inputs to a transaction until it has enough in value to meet its out value. {{DASH_UPDATED0_14_1}}
* [GetRawTransaction](/docs/core-api-ref-remote-procedure-calls-raw-transaction#section-getrawtransaction): gets a hex-encoded serialized transaction or a JSON object describing the transaction. By default, Dash Core only stores complete transaction data for UTXOs and your own transactions, so the RPC may fail on historic transactions unless you use the non-default `txindex=1` in your Dash Core startup settings. {{DASH_UPDATED0_14_1}}
* [SendRawTransaction](/docs/core-api-ref-remote-procedure-calls-raw-transaction#section-sendrawtransaction): validates a transaction and broadcasts it to the peer-to-peer network. {{DASH_UPDATED0_14_1}}
* [SignRawTransaction](/docs/core-api-ref-remote-procedure-calls-raw-transaction#section-signrawtransaction): signs a transaction in the serialized transaction format using private keys stored in the wallet or provided in the call.

#### Utility RPCs

* [CreateMultiSig](/docs/core-api-ref-remote-procedure-calls-utility#section-createmultisig): creates a P2SH multi-signature address.
* [EstimateFee](/docs/core-api-ref-remote-procedure-calls-utility#section-estimatefee): estimates the transaction fee per kilobyte that needs to be paid for a transaction to begin confirmation within a certain number of blocks.
* [EstimateSmartFee](/docs/core-api-ref-remote-procedure-calls-utility#section-estimatesmartfee): estimates the transaction fee per kilobyte that needs to be paid for a transaction to begin confirmation within a certain number of blocks and returns the number of blocks for which the estimate is valid. {{DASH_UPDATED0_14_1}}
* [SignMessageWithPrivKey](/docs/core-api-ref-remote-procedure-calls-utility#section-signmessagewithprivkey): signs a message with a given private key.  {{DASH_NEW0_12_3}} {{NEW0_13_0}}
* [ValidateAddress](/docs/core-api-ref-remote-procedure-calls-utility#section-validateaddress): returns information about the given Dash address. {{DASH_UPDATED0_12_3}} {{UPDATED0_13_0}}
* [VerifyMessage](/docs/core-api-ref-remote-procedure-calls-utility#section-verifymessage): verifies a signed message.

#### Wallet RPCs

**Note:** the wallet RPCs are only available if Dash Core was built with <<glossary:wallet support>>, which is the default.

* [AbandonTransaction](/docs/core-api-ref-remote-procedure-calls-wallet#section-abandontransaction): marks an in-wallet transaction and all its in-wallet descendants as abandoned. This allows their inputs to be respent. {{NEW0_12_0}}
* [AbortRescan](/docs/core-api-ref-remote-procedure-calls-wallet#section-abortrescan): {{summary_abortrescan}} {{DASH_NEW0_14_1}}
* [AddMultiSigAddress](/docs/core-api-ref-remote-procedure-calls-wallet#section-addmultisigaddress): adds a P2SH multisig address to the wallet.
* [BackupWallet](/docs/core-api-ref-remote-procedure-calls-wallet#section-backupwallet): safely copies `wallet.dat`<!--noref--> to the specified file, which can be a directory or a path with filename.
* [DumpHDInfo](/docs/core-api-ref-remote-procedure-calls-wallet#section-dumphdinfo): returns an object containing sensitive private info about this HD wallet {{DASH_NEW0_12_2}}
* [DumpPrivKey](/docs/core-api-ref-remote-procedure-calls-wallet#section-dumpprivkey): returns the wallet-import-format (WIP) private key corresponding to an address. (But does not remove it from the wallet.)
* [DumpWallet](/docs/core-api-ref-remote-procedure-calls-wallet#section-dumpwallet): creates or overwrites a file with all wallet keys in a human-readable format. {{DASH_UPDATED0_13_0}}
* [EncryptWallet](/docs/core-api-ref-remote-procedure-calls-wallet#section-encryptwallet): encrypts the wallet with a passphrase.  This is only to enable encryption for the first time. After encryption is enabled, you will need to enter the passphrase to use private keys.
* [GetAccount](/docs/core-api-ref-remote-procedure-calls-wallet#section-getaccount): returns the name of the account associated with the given address. {{DEPRECATED}}
* [GetAccountAddress](/docs/core-api-ref-remote-procedure-calls-wallet#section-getaccountaddress): returns the current Dash address for receiving payments to this account. If the account doesn't exist, it creates both the account and a new address for receiving payment.  Once a payment has been received to an address, future calls to this RPC for the same account will return a different address. {{DEPRECATED}}
* [GetAddressesByAccount](/docs/core-api-ref-remote-procedure-calls-wallet#section-getaddressesbyaccount): returns a list of every address assigned to a particular account. {{DEPRECATED}}
* [GetBalance](/docs/core-api-ref-remote-procedure-calls-wallet#section-getbalance): gets the balance in decimal dash across all accounts or for a particular account. {{DASH_UPDATED0_13_0}}
* [GetNewAddress](/docs/core-api-ref-remote-procedure-calls-wallet#section-getnewaddress): returns a new Dash address for receiving payments. If an account is specified, payments received with the address will be credited to that account.
* [GetRawChangeAddress](/docs/core-api-ref-remote-procedure-calls-wallet#section-getrawchangeaddress): returns a new Dash address for receiving change. This is for use with raw transactions, not normal use.
* [GetReceivedByAccount](/docs/core-api-ref-remote-procedure-calls-wallet#section-getreceivedbyaccount): returns the total amount received by addresses in a particular account from transactions with the specified number of confirmations.  It does not count coinbase transactions. {{DASH_UPDATED0_13_0}} {{DEPRECATED}}
* [GetReceivedByAddress](/docs/core-api-ref-remote-procedure-calls-wallet#section-getreceivedbyaddress): returns the total amount received by the specified address in transactions with the specified number of confirmations. It does not count coinbase transactions. {{DASH_UPDATED0_13_0}}
* [GetTransaction](/docs/core-api-ref-remote-procedure-calls-wallet#section-gettransaction): gets detailed information about an in-wallet transaction. {{DASH_UPDATED0_14_0}}
* [GetUnconfirmedBalance](/docs/core-api-ref-remote-procedure-calls-wallet#section-getunconfirmedbalance): returns the wallet's total unconfirmed balance.
* [GetWalletInfo](/docs/core-api-ref-remote-procedure-calls-wallet#section-getwalletinfo): provides information about the wallet.  {{DASH_UPDATED0_12_3}}
* [ImportAddress](/docs/core-api-ref-remote-procedure-calls-wallet#section-importaddress): adds an address or pubkey script to the wallet without the associated private key, allowing you to watch for transactions affecting that address or pubkey script without being able to spend any of its outputs.
* [ImportElectrumWallet](/docs/core-api-ref-remote-procedure-calls-wallet#section-importelectrumwallet): imports keys from an Electrum wallet export file (.csv or .json) {{DASH_NEW0_12_1}}
* [ImportMulti](/docs/core-api-ref-remote-procedure-calls-wallet#section-importmulti): imports addresses or scripts (with private keys, public keys, or P2SH redeem scripts) and optionally performs the minimum necessary rescan for all imports. {{DASH_NEW0_12_3}} {{NEW0_14_0}}
* [ImportPrivKey](/docs/core-api-ref-remote-procedure-calls-wallet#section-importprivkey): adds a private key to your wallet. The key should be formatted in the wallet import format created by the `dumpprivkey` RPC.
* [ImportPrunedFunds](/docs/core-api-ref-remote-procedure-calls-wallet#section-importprunedfunds): imports funds without the need of a rescan. Meant for use with pruned wallets. {{DASH_NEW0_12_3}} {{NEW0_13_0}}
* [ImportPubKey](/docs/core-api-ref-remote-procedure-calls-wallet#section-importpubkey): imports a public key (in hex) that can be watched as if it were in your wallet but cannot be used to spend
* [ImportWallet](/docs/core-api-ref-remote-procedure-calls-wallet#section-importwallet): imports private keys from a file in wallet dump file format (see the `dumpwallet` RPC). These keys will be added to the keys currently in the wallet.  This call may need to rescan all or parts of the block chain for transactions affecting the newly-added keys, which may take several minutes.
* [KeePass](/docs/core-api-ref-remote-procedure-calls-wallet#section-keepass): provides commands for configuring and managing KeePass authentication {{DARKCOIN_NEW0_11_0}}
* [KeyPoolRefill](/docs/core-api-ref-remote-procedure-calls-wallet#section-keypoolrefill): fills the cache of unused pre-generated keys (the keypool).
* [ListAccounts](/docs/core-api-ref-remote-procedure-calls-wallet#section-listaccounts): lists accounts and their balances. {{DASH_UPDATED0_13_0}} {{DEPRECATED}}
* [ListAddressBalances](/docs/core-api-ref-remote-procedure-calls-wallet#section-listaddressbalances): lists addresses of this wallet and their balances {{DASH_NEW0_12_3}}
* [ListAddressGroupings](/docs/core-api-ref-remote-procedure-calls-wallet#section-listaddressgroupings): lists groups of addresses that may have had their common ownership made public by common use as inputs in the same transaction or from being used as change from a previous transaction.
* [ListLockUnspent](/docs/core-api-ref-remote-procedure-calls-wallet#section-listlockunspent): returns a list of temporarily unspendable (locked) outputs.
* [ListReceivedByAccount](/docs/core-api-ref-remote-procedure-calls-wallet#section-listreceivedbyaccount): lists the total number of dash received by each account. {{DASH_UPDATED0_13_0}} {{DEPRECATED}}
* [ListReceivedByAddress](/docs/core-api-ref-remote-procedure-calls-wallet#section-listreceivedbyaddress): lists the total number of dash received by each address. {{DASH_UPDATED0_13_0}}
* [ListSinceBlock](/docs/core-api-ref-remote-procedure-calls-wallet#section-listsinceblock): gets all transactions affecting the wallet which have occurred since a particular block, plus the header hash of a block at a particular depth. {{DASH_UPDATED0_14_1}}
* [ListTransactions](/docs/core-api-ref-remote-procedure-calls-wallet#section-listtransactions): returns the most recent transactions that affect the wallet. {{DASH_UPDATED0_14_0}}
* [ListUnspent](/docs/core-api-ref-remote-procedure-calls-wallet#section-listunspent): returns an array of unspent transaction outputs belonging to this wallet. {{DASH_UPDATED0_14_1}}
* [ListWallets](/docs/core-api-ref-remote-procedure-calls-wallet#section-listwallets): returns a list of currently loaded wallets. {{DASH_NEW0_14_1}}
* [LockUnspent](/docs/core-api-ref-remote-procedure-calls-wallet#section-lockunspent): temporarily locks or unlocks specified transaction outputs. A locked transaction output will not be chosen by automatic coin selection when spending dash. Locks are stored in memory only, so nodes start with zero locked outputs and the locked output list is always cleared when a node stops or fails.
* [Move](/docs/core-api-ref-remote-procedure-calls-wallet#section-move): moves a specified amount from one account in your wallet to another using an off-block-chain transaction. {{DEPRECATED}}
* [RemovePrunedFunds](/docs/core-api-ref-remote-procedure-calls-wallet#section-removeprunedfunds): deletes the specified transaction from the wallet. Meant for use with pruned wallets and as a companion to importprunedfunds. {{DASH_NEW0_12_3}} {{NEW0_13_0}}
* [SendFrom](/docs/core-api-ref-remote-procedure-calls-wallet#section-sendfrom): spends an amount from a local account to a dash address. {{DASH_UPDATED0_13_0}} {{DEPRECATED}}
* [SendMany](/docs/core-api-ref-remote-procedure-calls-wallet#section-sendmany): creates and broadcasts a transaction which sends outputs to multiple addresses. {{DASH_UPDATED0_14_1}}
* [SendToAddress](/docs/core-api-ref-remote-procedure-calls-wallet#section-sendtoaddress): spends an amount to a given address. {{DASH_UPDATED0_14_1}}
* [SetAccount](/docs/core-api-ref-remote-procedure-calls-wallet#section-setaccount): puts the specified address in the given account. {{DEPRECATED}}
* [SetPrivateSendAmount](/docs/core-api-ref-remote-procedure-calls-wallet#section-setprivatesendamount): sets the amount of DASH to be mixed with PrivateSend
* [SetPrivateSendRounds](/docs/core-api-ref-remote-procedure-calls-wallet#section-setprivatesendrounds): sets the number of PrivateSend mixing rounds to use
* [SetTxFee](/docs/core-api-ref-remote-procedure-calls-wallet#section-settxfee): sets the transaction fee per kilobyte paid by transactions created by this wallet.
* [SignMessage](/docs/core-api-ref-remote-procedure-calls-wallet#section-signmessage): signs a message with the private key of an address.
* [WalletLock](/docs/core-api-ref-remote-procedure-calls-wallet#section-walletlock): removes the wallet encryption key from memory, locking the wallet. After calling this method, you will need to call `walletpassphrase` again before being able to call any methods which require the wallet to be unlocked.
* [WalletPassphrase](/docs/core-api-ref-remote-procedure-calls-wallet#section-walletpassphrase): stores the wallet decryption key in memory for the indicated number of seconds. Issuing the `walletpassphrase` command while the wallet is already unlocked will set a new unlock time that overrides the old one.
* [WalletPassphraseChange](/docs/core-api-ref-remote-procedure-calls-wallet#section-walletpassphrasechange): changes the wallet passphrase from 'old passphrase' to 'new passphrase'.

#### Removed RPCs

* [EstimatePriority](/docs/core-api-ref-remote-procedure-calls-removed#section-estimatepriority): was removed in Dash Core 0.14.0.
* [EstimateSmartPriority](/docs/core-api-ref-remote-procedure-calls-removed#section-estimatesmartpriority): was removed in Dash Core 0.14.0.
* [GetHashesPerSec](/docs/core-api-ref-remote-procedure-calls-removed#section-gethashespersec): was removed in Bitcoin Core 0.11.0 and is not part of Dash.
* [GetWork](/docs/core-api-ref-remote-procedure-calls-removed#section-getwork): was removed in Bitcoin Core 0.10.0. and is not part of Dash
* [GetGenerate](/docs/core-api-ref-remote-procedure-calls-removed#section-getgenerate): was removed in Dash Core 0.12.3.
* [MasternodeBroadcast](/docs/core-api-ref-remote-procedure-calls-removed#section-masternodebroadcast): was removed in Dash Core 0.14.0.
* [SentinelPing](/docs/core-api-ref-remote-procedure-calls-removed#section-sentinelping): was removed in Dash Core 0.14.0.
* [SetGenerate](/docs/core-api-ref-remote-procedure-calls-removed#section-setgenerate): was removed in Dash Core 0.12.3.