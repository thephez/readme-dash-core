# [Addressindex RPCs](core-api-ref-remote-procedure-calls-address-index)

These RPCs are all Dash-specific and not found in Bitcoin Core

* [GetAddressBalance](/docs/core-api-ref-remote-procedure-calls-address-index#section-get-address-balance): returns the balance for address(es).
* [GetAddressDeltas](/docs/core-api-ref-remote-procedure-calls-address-index#section-get-address-deltas): returns all changes for an address.
* [GetAddressMempool](/docs/core-api-ref-remote-procedure-calls-address-index#section-get-address-mempool): returns all mempool deltas for an address.
* [GetAddressTxids](/docs/core-api-ref-remote-procedure-calls-address-index#section-get-address-txids): returns the txids for an address(es).
* [GetAddressUtxos](/docs/core-api-ref-remote-procedure-calls-address-index#section-get-address-utxos): returns all unspent outputs for an address.

# [Block Chain RPCs](core-api-ref-remote-procedure-calls-blockchain)

* [GetBestBlockHash](/docs/core-api-ref-remote-procedure-calls-blockchain#section-get-best-block-hash): returns the header hash of the most recent block on the best block chain.
* [GetBestChainLock](/docs/core-api-ref-remote-procedure-calls-blockchain#section-get-best-chain-lock): returns the block hash of the best chainlock. **New in Dash Core 0.15.0**
* [GetBlock](/docs/core-api-ref-remote-procedure-calls-blockchain#section-get-block): gets a block with a particular header hash from the local block database either as a JSON object or as a serialized block. **Updated in Dash Core 0.15.0**
* [GetBlockChainInfo](/docs/core-api-ref-remote-procedure-calls-blockchain#section-get-block-chain-info): provides information about the current state of the block chain. **Updated in Dash Core 0.15.0**
* [GetBlockCount](/docs/core-api-ref-remote-procedure-calls-blockchain#section-get-block-count): returns the number of blocks in the local best block chain.
* [GetBlockHash](/docs/core-api-ref-remote-procedure-calls-blockchain#section-get-block-hash): returns the header hash of a block at the given height in the local best block chain.
* [GetBlockHashes](/docs/core-api-ref-remote-procedure-calls-blockchain#section-get-block-hashes): returns array of hashes of blocks within the timestamp range provided (requires `timestampindex` to be enabled). New in Dash Core 0.12.1
* [GetBlockHeader](/docs/core-api-ref-remote-procedure-calls-blockchain#section-get-block-header): gets a block header with a particular header hash from the local block database either as a JSON object or as a serialized block header.
* [GetBlockHeaders](/docs/core-api-ref-remote-procedure-calls-blockchain#section-get-block-headers): returns an array of items with information about the requested number of blockheaders starting from the requested hash. New in Dash Core 0.12.1
* [GetBlockStats](/docs/core-api-ref-remote-procedure-calls-blockchain#section-get-block-stats): computes per block statistics for a given window. **New in Dash Core 0.15.0**
* [GetChainTips](/docs/core-api-ref-remote-procedure-calls-blockchain#section-get-chain-tips): returns information about the highest-height block (tip) of each local block chain. *Updated in Dash Core 0.12.3*
* [GetChainTxStats](/docs/core-api-ref-remote-procedure-calls-blockchain#section-get-chain-tx-stats): compute statistics about the total number and rate of transactions in the chain. **New in Dash Core 0.15.0**
* [GetDifficulty](/docs/core-api-ref-remote-procedure-calls-blockchain#section-get-difficulty): returns the proof-of-work difficulty as a multiple of the minimum difficulty.
* [GetMemPoolAncestors](/docs/core-api-ref-remote-procedure-calls-blockchain#section-get-mem-pool-ancestors): returns all in-mempool ancestors for a transaction in the mempool. **Updated in Dash Core 0.14.0**
* [GetMemPoolDescendants](/docs/core-api-ref-remote-procedure-calls-blockchain#section-get-mem-pool-descendants): returns all in-mempool descendants for a transaction in the mempool. **Updated in Dash Core 0.14.0**
* [GetMemPoolEntry](core-api-ref-remote-procedure-calls-blockchain#section-get-mem-pool-entry): returns mempool data for given transaction (must be in mempool). **Updated in Dash Core 0.14.0**
* [GetMemPoolInfo](/docs/core-api-ref-remote-procedure-calls-blockchain#section-get-mem-pool-info): returns information about the node's current transaction memory pool. **Updated in Dash Core 0.15.0**
* [GetRawMemPool](/docs/core-api-ref-remote-procedure-calls-blockchain#section-get-raw-mem-pool): returns all transaction identifiers (TXIDs) in the memory pool as a JSON array, or detailed information about each transaction in the memory pool as a JSON object. **Updated in Dash Core 0.15.0**
* [GetMerkleBlocks](/docs/core-api-ref-remote-procedure-calls-blockchain#section-get-merkle-blocks): returns an array of hex-encoded merkleblocks for <count> blocks starting from <hash> which match <filter>. **New in Dash Core 0.15.0**
* [GetSpecialTxes](/docs/core-api-ref-remote-procedure-calls-blockchain#section-get-special-txes): returns an array of special transactions found in the specified block **New in Dash Core 0.13.1**
* [GetSpentInfo](/docs/core-api-ref-remote-procedure-calls-blockchain#section-get-spent-info): returns the txid and index where an output is spent (requires `spentindex` to be enabled). New in Dash Core 0.12.1
* [GetTxOut](/docs/core-api-ref-remote-procedure-calls-blockchain#section-get-tx-out): returns details about an unspent transaction output (UTXO). **Updated in Dash Core 0.15.0**
* [GetTxOutProof](/docs/core-api-ref-remote-procedure-calls-blockchain#section-get-tx-out-proof): returns a hex-encoded proof that one or more specified transactions were included in a block.
* [GetTxOutSetInfo](/docs/core-api-ref-remote-procedure-calls-blockchain#section-get-tx-out-set-info): returns statistics about the confirmed unspent transaction output (UTXO) set. Note that this call may take some time and that it only counts outputs from confirmed transactions---it does not count outputs from the memory pool. **Updated in Dash Core 0.15.0**
* [PreciousBlock](/docs/core-api-ref-remote-procedure-calls-blockchain#section-precious-block): treats a block as if it were received before others with the same work. *New in Dash Core 0.12.3*
* [PruneBlockChain](/docs/core-api-ref-remote-procedure-calls-blockchain#section-prune-block-chain): prunes the blockchain up to a specified height or timestamp. *New in Dash Core 0.12.3*
* [VerifyChain](/docs/core-api-ref-remote-procedure-calls-blockchain#section-verify-chain): verifies each entry in the local block chain database.
* [VerifyTxOutProof](/docs/core-api-ref-remote-procedure-calls-blockchain#section-verify-tx-out-proof): verifies that a proof points to one or more transactions in a block, returning the transactions the proof commits to and throwing an RPC error if the block is not in our best block chain.

# [Control RPCs](core-api-ref-remote-procedure-calls-control)

* [Debug](/docs/core-api-ref-remote-procedure-calls-control#section-debug): changes the debug category from the console. **Updated in Dash Core 0.14.0**
* [GetInfo](/docs/core-api-ref-remote-procedure-calls-control#section-get-info): prints various information about the node and the network. **Updated in Dash Core 0.15.0** **_Deprecated_**
* [GetMemoryInfo](/docs/core-api-ref-remote-procedure-calls-control#section-get-memory-info): returns information about memory usage. **Updated in Dash Core 0.15.0**
* [Help](/docs/core-api-ref-remote-procedure-calls-control#section-help): lists all available public RPC commands, or gets help for the specified RPC.  Commands which are unavailable will not be listed, such as wallet RPCs if wallet support is disabled.
* [Logging](/docs/core-api-ref-remote-procedure-calls-control#section-logging): gets and sets the logging configuration **New in Dash Core 0.15.0**
* [Stop](/docs/core-api-ref-remote-procedure-calls-control#section-stop): safely shuts down the Dash Core server.
* [Uptime](/docs/core-api-ref-remote-procedure-calls-control#section-uptime): returns the total uptime of the server. **New in Dash Core 0.15.0**

# [Dash RPCs](core-api-ref-remote-procedure-calls-dash)

* [GetGovernanceInfo](/docs/core-api-ref-remote-procedure-calls-dash#section-get-governance-info): returns an object containing governance parameters. **Updated in Dash Core 0.14.0**
* [GetPoolInfo](/docs/core-api-ref-remote-procedure-calls-dash#section-get-pool-info): returns an object containing mixing pool related information. **_Deprecated in 0.15.0_**
* [GetPrivateSendInfo](/docs/core-api-ref-remote-procedure-calls-dash#section-get-private-send-info): returns an object containing an information about PrivateSend settings and state. **New in Dash Core 0.15.0**
* [GetSuperblockBudget](/docs/core-api-ref-remote-procedure-calls-dash#section-get-superblock-budget): returns the absolute maximum sum of superblock payments allowed.
* [GObject](/docs/core-api-ref-remote-procedure-calls-dash#section-g-object): provides a set of commands for managing governance objects and displaying information about them. **Updated in Dash Core 0.15.0**
* [Masternode](/docs/core-api-ref-remote-procedure-calls-dash#section-masternode): provides a set of commands for managing masternodes and displaying information about them. **Updated in Dash Core 0.14.0**
* [MasternodeList](/docs/core-api-ref-remote-procedure-calls-dash#section-masternode-list): returns a list of masternodes in different modes. **Updated in Dash Core 0.14.0**
* [MnSync](/docs/core-api-ref-remote-procedure-calls-dash#section-mn-sync): returns the sync status, updates to the next step or resets it entirely. **Updated in Dash Core 0.14.0**
* [PrivateSend](/docs/core-api-ref-remote-procedure-calls-dash#section-private-send): controls the mixing process. *Updated in Dash Core 0.12.3*
* [Spork](/docs/core-api-ref-remote-procedure-calls-dash#section-spork): reads or updates spork settings on the network.
* [VoteRaw](/docs/core-api-ref-remote-procedure-calls-dash#section-vote-raw): compiles and relays a governance vote with provided external signature instead of signing vote internally

# [Evolution RPCs](core-api-ref-remote-procedure-calls-evo)

* [BLS](/docs/core-api-ref-remote-procedure-calls-evo#section-b-l-s): provides a set of commands to execute BLS-related actions. **Updated in Dash Core 0.14.0**
* [ProTx](/docs/core-api-ref-remote-procedure-calls-evo#section-pro-tx): provides a set of commands to execute ProTx related actions. **Updated in Dash Core 0.14.0**
* [Quorum](/docs/core-api-ref-remote-procedure-calls-evo#section-quorum): provides a set of commands for quorums (LLMQs). **New in Dash Core 0.14.0**

# [Generating RPCs](core-api-ref-remote-procedure-calls-generating)

* [Generate](/docs/core-api-ref-remote-procedure-calls-generating#section-generate): mines blocks immediately (before the RPC call returns). *Updated in Dash Core 0.12.3*
* [GenerateToAddress](/docs/core-api-ref-remote-procedure-calls-generating#section-generate-to-address): mines blocks immediately to a specified address. *New in Dash Core 0.12.3*

# [Mining RPCs](core-api-ref-remote-procedure-calls-mining)

* [GetBlockTemplate](/docs/core-api-ref-remote-procedure-calls-mining#section-get-block-template): gets a block template or proposal for use with mining software. *Updated in Dash Core 0.13.0*
* [GetMiningInfo](/docs/core-api-ref-remote-procedure-calls-mining#section-get-mining-info): returns various mining-related information.
* [GetNetworkHashPS](/docs/core-api-ref-remote-procedure-calls-mining#section-get-network-hash-p-s): returns the estimated network hashes per second based on the last n blocks.
* [PrioritiseTransaction](/docs/core-api-ref-remote-procedure-calls-mining#section-prioritise-transaction): adds virtual priority or fee to a transaction, allowing it to be accepted into blocks mined by this node (or miners which use this node) with a lower priority or fee. (It can also remove virtual priority or fee, requiring the transaction have a higher priority or fee to be accepted into a locally-mined block.) **Updated in Dash Core 0.14.0**
* [SubmitBlock](/docs/core-api-ref-remote-procedure-calls-mining#section-submit-block): accepts a block, verifies it is a valid addition to the block chain, and broadcasts it to the network. Extra parameters are ignored by Dash Core but may be used by mining pools or other programs.

# [Network RPCs](core-api-ref-remote-procedure-calls-network)

* [AddNode](/docs/core-api-ref-remote-procedure-calls-network#section-add-node): attempts to add or remove a node from the addnode list, or to try a connection to a node once.
* [ClearBanned](/docs/core-api-ref-remote-procedure-calls-network#section-clear-banned): clears list of banned nodes.
* [DisconnectNode](/docs/core-api-ref-remote-procedure-calls-network#section-disconnect-node): immediately disconnects from a specified node. **Updated in Dash Core 0.15.0**
* [GetAddedNodeInfo](/docs/core-api-ref-remote-procedure-calls-network#section-get-added-node-info): returns information about the given added node, or all added nodes (except onetry nodes). Only nodes which have been manually added using the [`addnode` RPC](core-api-ref-remote-procedure-calls-network#section-add-node) will have their information displayed. *Updated in Dash Core 0.12.3*
* [GetConnectionCount](/docs/core-api-ref-remote-procedure-calls-network#section-get-connection-count): returns the number of connections to other nodes.
* [GetNetTotals](/docs/core-api-ref-remote-procedure-calls-network#section-get-net-totals): returns information about network traffic, including bytes in, bytes out, and the current time.
* [GetNetworkInfo](/docs/core-api-ref-remote-procedure-calls-network#section-get-network-info): returns information about the node's connection to the network. **Updated in Dash Core 0.14.0**
* [GetPeerInfo](/docs/core-api-ref-remote-procedure-calls-network#section-get-peer-info): returns data about each connected network node. **Updated in Dash Core 0.15.0**
* [ListBanned](/docs/core-api-ref-remote-procedure-calls-network#section-list-banned): lists all banned IPs/Subnets.
* [Ping](/docs/core-api-ref-remote-procedure-calls-network#section-ping): sends a P2P ping message to all connected nodes to measure ping time. Results are provided by the [`getpeerinfo` RPC](core-api-ref-remote-procedure-calls-network#section-get-peer-info) pingtime and pingwait fields as decimal seconds. The P2P [`ping` message](core-ref-p2p-network-control-messages#section-ping) is handled in a queue with all other commands, so it measures processing backlog, not just network ping.
* [SetBan](/docs/core-api-ref-remote-procedure-calls-network#section-set-ban): attempts add or remove a IP/Subnet from the banned list.
* [SetNetworkActive](/docs/core-api-ref-remote-procedure-calls-network#section-set-network-active): disables/enables all P2P network activity.

# [Raw Transaction RPCs](core-api-ref-remote-procedure-calls-raw-transactions)

* [CombineRawTransaction](/docs/core-api-ref-remote-procedure-calls-raw-transactions#section-combine-raw-transaction): combine multiple partially signed transactions into one transaction. **New in Dash Core 0.15.0**
* [CreateRawTransaction](/docs/core-api-ref-remote-procedure-calls-raw-transactions#section-create-raw-transaction): creates an unsigned serialized transaction that spends a previous output to a new output with a P2PKH or P2SH address. The transaction is not stored in the wallet or transmitted to the network. *Updated in Dash Core 0.12.3*
* [DecodeRawTransaction](/docs/core-api-ref-remote-procedure-calls-raw-transactions#section-decode-raw-transaction): decodes a serialized transaction hex string into a JSON object describing the transaction. *Updated in Dash Core 0.13.0*
* [DecodeScript](/docs/core-api-ref-remote-procedure-calls-raw-transactions#section-decode-script): decodes a hex-encoded P2SH redeem script.
* [FundRawTransaction](/docs/core-api-ref-remote-procedure-calls-raw-transactions#section-fund-raw-transaction): adds inputs to a transaction until it has enough in value to meet its out value. **Updated in Dash Core 0.15.0**
* [GetRawTransaction](/docs/core-api-ref-remote-procedure-calls-raw-transactions#section-get-raw-transaction): gets a hex-encoded serialized transaction or a JSON object describing the transaction. By default, Dash Core only stores complete transaction data for UTXOs and your own transactions, so the RPC may fail on historic transactions unless you use the non-default `txindex=1` in your Dash Core startup settings. **Updated in Dash Core 0.15.0**
* [SendRawTransaction](/docs/core-api-ref-remote-procedure-calls-raw-transactions#section-send-raw-transaction): validates a transaction and broadcasts it to the peer-to-peer network. **Updated in Dash Core 0.15.0**
* [SignRawTransaction](/docs/core-api-ref-remote-procedure-calls-raw-transactions#section-sign-raw-transaction): signs a transaction in the serialized transaction format using private keys stored in the wallet or provided in the call.

# [Utility RPCs](core-api-ref-remote-procedure-calls-util)

* [CreateMultiSig](/docs/core-api-ref-remote-procedure-calls-util#section-create-multi-sig): creates a P2SH multi-signature address.
* [EstimateFee](/docs/core-api-ref-remote-procedure-calls-util#section-estimate-fee): estimates the transaction fee per kilobyte that needs to be paid for a transaction to begin confirmation within a certain number of blocks.
* [EstimateSmartFee](/docs/core-api-ref-remote-procedure-calls-util#section-estimate-smart-fee): estimates the transaction fee per kilobyte that needs to be paid for a transaction to begin confirmation within a certain number of blocks and returns the number of blocks for which the estimate is valid. **Updated in Dash Core 0.15.0**
* [SignMessageWithPrivKey](/docs/core-api-ref-remote-procedure-calls-util#section-sign-message-with-priv-key): signs a message with a given private key.  *New in Dash Core 0.12.3*
* [ValidateAddress](/docs/core-api-ref-remote-procedure-calls-util#section-validate-address): returns information about the given Dash address. *Updated in Dash Core 0.12.3*
* [VerifyMessage](/docs/core-api-ref-remote-procedure-calls-util#section-verify-message): verifies a signed message.

# [Wallet RPCs](core-api-ref-remote-procedure-calls-wallet)

**Note:** the wallet RPCs are only available if Dash Core was built with <<glossary:wallet support>>, which is the default.

* [AbandonTransaction](/docs/core-api-ref-remote-procedure-calls-wallet#section-abandon-transaction): marks an in-wallet transaction and all its in-wallet descendants as abandoned. This allows their inputs to be respent.
* [AbortRescan](/docs/core-api-ref-remote-procedure-calls-wallet#section-abort-rescan): stops current wallet rescan. **New in Dash Core 0.15.0**
* [AddMultiSigAddress](/docs/core-api-ref-remote-procedure-calls-wallet#section-add-multi-sig-address): adds a P2SH multisig address to the wallet.
* [BackupWallet](/docs/core-api-ref-remote-procedure-calls-wallet#section-backup-wallet): safely copies `wallet.dat` to the specified file, which can be a directory or a path with filename.
* [DumpHDInfo](/docs/core-api-ref-remote-procedure-calls-wallet#section-dump-h-d-info): returns an object containing sensitive private info about this HD wallet New in Dash Core 0.12.2
* [DumpPrivKey](/docs/core-api-ref-remote-procedure-calls-wallet#section-dump-priv-key): returns the wallet-import-format (WIP) private key corresponding to an address. (But does not remove it from the wallet.)
* [DumpWallet](/docs/core-api-ref-remote-procedure-calls-wallet#section-dump-wallet): creates or overwrites a file with all wallet keys in a human-readable format. *Updated in Dash Core 0.13.0*
* [EncryptWallet](/docs/core-api-ref-remote-procedure-calls-wallet#section-encrypt-wallet): encrypts the wallet with a passphrase.  This is only to enable encryption for the first time. After encryption is enabled, you will need to enter the passphrase to use private keys.
* [GetBalance](/docs/core-api-ref-remote-procedure-calls-wallet#section-get-balance): gets the balance in decimal dash across all accounts or for a particular account. *Updated in Dash Core 0.13.0*
* [GetNewAddress](/docs/core-api-ref-remote-procedure-calls-wallet#section-get-new-address): returns a new Dash address for receiving payments. If an account is specified, payments received with the address will be credited to that account.
* [GetRawChangeAddress](/docs/core-api-ref-remote-procedure-calls-wallet#section-get-raw-change-address): returns a new Dash address for receiving change. This is for use with raw transactions, not normal use.
* [GetReceivedByAddress](/docs/core-api-ref-remote-procedure-calls-wallet#section-get-received-by-address): returns the total amount received by the specified address in transactions with the specified number of confirmations. It does not count coinbase transactions. *Updated in Dash Core 0.13.0*
* [GetTransaction](/docs/core-api-ref-remote-procedure-calls-wallet#section-get-transaction): gets detailed information about an in-wallet transaction. **Updated in Dash Core 0.14.0**
* [GetUnconfirmedBalance](/docs/core-api-ref-remote-procedure-calls-wallet#section-get-unconfirmed-balance): returns the wallet's total unconfirmed balance.
* [GetWalletInfo](/docs/core-api-ref-remote-procedure-calls-wallet#section-get-wallet-info): provides information about the wallet.  *Updated in Dash Core 0.12.3*
* [ImportAddress](/docs/core-api-ref-remote-procedure-calls-wallet#section-import-address): adds an address or pubkey script to the wallet without the associated private key, allowing you to watch for transactions affecting that address or pubkey script without being able to spend any of its outputs.
* [ImportElectrumWallet](/docs/core-api-ref-remote-procedure-calls-wallet#section-import-electrum-wallet): imports keys from an Electrum wallet export file (.csv or .json) New in Dash Core 0.12.1
* [ImportMulti](/docs/core-api-ref-remote-procedure-calls-wallet#section-import-multi): imports addresses or scripts (with private keys, public keys, or P2SH redeem scripts) and optionally performs the minimum necessary rescan for all imports. *New in Dash Core 0.12.3*
* [ImportPrivKey](/docs/core-api-ref-remote-procedure-calls-wallet#section-import-priv-key): adds a private key to your wallet. The key should be formatted in the wallet import format created by the [`dumpprivkey` RPC](core-api-ref-remote-procedure-calls-wallet#section-dump-priv-key).
* [ImportPrunedFunds](/docs/core-api-ref-remote-procedure-calls-wallet#section-import-pruned-funds): imports funds without the need of a rescan. Meant for use with pruned wallets. *New in Dash Core 0.12.3*
* [ImportPubKey](/docs/core-api-ref-remote-procedure-calls-wallet#section-import-pub-key): imports a public key (in hex) that can be watched as if it were in your wallet but cannot be used to spend
* [ImportWallet](/docs/core-api-ref-remote-procedure-calls-wallet#section-import-wallet): imports private keys from a file in wallet dump file format (see the [`dumpwallet` RPC](core-api-ref-remote-procedure-calls-wallet#section-dump-wallet)). These keys will be added to the keys currently in the wallet.  This call may need to rescan all or parts of the block chain for transactions affecting the newly-added keys, which may take several minutes.
* [KeePass](/docs/core-api-ref-remote-procedure-calls-wallet#section-kee-pass): provides commands for configuring and managing KeePass authentication. New in Darkcoin Core 0.11.0
* [KeyPoolRefill](/docs/core-api-ref-remote-procedure-calls-wallet#section-key-pool-refill): fills the cache of unused pre-generated keys (the keypool).
* [ListAddressBalances](/docs/core-api-ref-remote-procedure-calls-wallet#section-list-address-balances): lists addresses of this wallet and their balances *New in Dash Core 0.12.3*
* [ListAddressGroupings](/docs/core-api-ref-remote-procedure-calls-wallet#section-list-address-groupings): lists groups of addresses that may have had their common ownership made public by common use as inputs in the same transaction or from being used as change from a previous transaction.
* [ListLockUnspent](/docs/core-api-ref-remote-procedure-calls-wallet#section-list-lock-unspent): returns a list of temporarily unspendable (locked) outputs.
* [ListReceivedByAddress](/docs/core-api-ref-remote-procedure-calls-wallet#section-list-received-by-address): lists the total number of dash received by each address. *Updated in Dash Core 0.13.0*
* [ListSinceBlock](/docs/core-api-ref-remote-procedure-calls-wallet#section-list-since-block): gets all transactions affecting the wallet which have occurred since a particular block, plus the header hash of a block at a particular depth. **Updated in Dash Core 0.15.0**
* [ListTransactions](/docs/core-api-ref-remote-procedure-calls-wallet#section-list-transactions): returns the most recent transactions that affect the wallet. **Updated in Dash Core 0.14.0**
* [ListUnspent](/docs/core-api-ref-remote-procedure-calls-wallet#section-list-unspent): returns an array of unspent transaction outputs belonging to this wallet. **Updated in Dash Core 0.15.0**
* [ListWallets](/docs/core-api-ref-remote-procedure-calls-wallet#section-list-wallets): returns a list of currently loaded wallets. **New in Dash Core 0.15.0**
* [LockUnspent](/docs/core-api-ref-remote-procedure-calls-wallet#section-lock-unspent): temporarily locks or unlocks specified transaction outputs. A locked transaction output will not be chosen by automatic coin selection when spending dash. Locks are stored in memory only, so nodes start with zero locked outputs and the locked output list is always cleared when a node stops or fails.
* [RemovePrunedFunds](/docs/core-api-ref-remote-procedure-calls-wallet#section-remove-pruned-funds): deletes the specified transaction from the wallet. Meant for use with pruned wallets and as a companion to importprunedfunds. *New in Dash Core 0.12.3*
* [SendMany](/docs/core-api-ref-remote-procedure-calls-wallet#section-send-many): creates and broadcasts a transaction which sends outputs to multiple addresses. **Updated in Dash Core 0.15.0**
* [SendToAddress](/docs/core-api-ref-remote-procedure-calls-wallet#section-send-to-address): spends an amount to a given address. **Updated in Dash Core 0.15.0**
* [SetPrivateSendAmount](/docs/core-api-ref-remote-procedure-calls-wallet#section-set-private-send-amount): sets the amount of DASH to be mixed with PrivateSend *New in Dash Core 0.13.0*
* [SetPrivateSendRounds](/docs/core-api-ref-remote-procedure-calls-wallet#section-set-private-send-rounds): sets the number of PrivateSend mixing rounds to use *New in Dash Core 0.13.0*
* [SetTxFee](/docs/core-api-ref-remote-procedure-calls-wallet#section-set-tx-fee): sets the transaction fee per kilobyte paid by transactions created by this wallet.
* [SignMessage](/docs/core-api-ref-remote-procedure-calls-wallet#section-sign-message): signs a message with the private key of an address.
* [WalletLock](/docs/core-api-ref-remote-procedure-calls-wallet#section-wallet-lock): removes the wallet encryption key from memory, locking the wallet. After calling this method, you will need to call `walletpassphrase` again before being able to call any methods which require the wallet to be unlocked.
* [WalletPassphrase](/docs/core-api-ref-remote-procedure-calls-wallet#section-wallet-passphrase): stores the wallet decryption key in memory for the indicated number of seconds. Issuing the `walletpassphrase` command while the wallet is already unlocked will set a new unlock time that overrides the old one.
* [WalletPassphraseChange](/docs/core-api-ref-remote-procedure-calls-wallet#section-wallet-passphrase-change): changes the wallet passphrase from 'old passphrase' to 'new passphrase'.

# [Wallet RPCs (Deprecated)](core-api-ref-remote-procedure-calls-wallet-deprecated)

**Note:** the wallet RPCs are only available if Dash Core was built with <<glossary:wallet support>>, which is the default.

* [GetAccount](/docs/core-api-ref-remote-procedure-calls-wallet-deprecated#section-get-account): returns the name of the account associated with the given address. **_Deprecated_**
* [GetAccountAddress](/docs/core-api-ref-remote-procedure-calls-wallet-deprecated#section-get-account-address): returns the current Dash address for receiving payments to this account. If the account doesn't exist, it creates both the account and a new address for receiving payment.  Once a payment has been received to an address, future calls to this RPC for the same account will return a different address. **_Deprecated_**
* [GetAddressesByAccount](/docs/core-api-ref-remote-procedure-calls-wallet-deprecated#section-get-addresses-by-account): returns a list of every address assigned to a particular account. **_Deprecated_**
* [GetReceivedByAccount](/docs/core-api-ref-remote-procedure-calls-wallet-deprecated#section-get-received-by-account): returns the total amount received by addresses in a particular account from transactions with the specified number of confirmations.  It does not count coinbase transactions. *Updated in Dash Core 0.13.0* **_Deprecated_**
* [ListAccounts](/docs/core-api-ref-remote-procedure-calls-wallet-deprecated#section-list-accounts): lists accounts and their balances. *Updated in Dash Core 0.13.0* **_Deprecated_**
* [ListReceivedByAccount](/docs/core-api-ref-remote-procedure-calls-wallet-deprecated#section-list-received-by-account): lists the total number of dash received by each account. *Updated in Dash Core 0.13.0* **_Deprecated_**
* [Move](/docs/core-api-ref-remote-procedure-calls-wallet-deprecated#section-move): moves a specified amount from one account in your wallet to another using an off-block-chain transaction. **_Deprecated_**
* [SendFrom](/docs/core-api-ref-remote-procedure-calls-wallet-deprecated#section-send-from): spends an amount from a local account to a dash address. *Updated in Dash Core 0.13.0* **_Deprecated_**
* [SetAccount](/docs/core-api-ref-remote-procedure-calls-wallet-deprecated#section-set-account): puts the specified address in the given account. **_Deprecated_**

# [Removed RPCs](core-api-ref-remote-procedure-calls-removed)

* [EstimatePriority](/docs/core-api-ref-remote-procedure-calls-removed#section-estimate-priority): was removed in Dash Core 0.14.0.
* [EstimateSmartPriority](/docs/core-api-ref-remote-procedure-calls-removed#section-estimate-smart-priority): was removed in Dash Core 0.14.0.
* [GetHashesPerSec](/docs/core-api-ref-remote-procedure-calls-removed#section-get-hashes-per-sec): was removed in Bitcoin Core 0.11.0 and is not part of Dash.
* [GetWork](/docs/core-api-ref-remote-procedure-calls-removed#section-get-work): was removed in Bitcoin Core 0.10.0. and is not part of Dash
* [GetGenerate](/docs/core-api-ref-remote-procedure-calls-removed#section-get-generate): was removed in Dash Core 0.12.3.
* [MasternodeBroadcast](/docs/core-api-ref-remote-procedure-calls-removed#section-masternode-broadcast): was removed in Dash Core 0.14.0.
* [SentinelPing](/docs/core-api-ref-remote-procedure-calls-removed#section-sentinel-ping): was removed in Dash Core 0.14.0.
* [SetGenerate](/docs/core-api-ref-remote-procedure-calls-removed#section-set-generate): was removed in Dash Core 0.12.3.
