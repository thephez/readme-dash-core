---
title: "Configuration File"
excerpt: ""
---
All three programs get settings from `dash.conf` in the `DashCore` application directory:

* Windows: `%APPDATA%\DashCore\`

* OSX: `$HOME/Library/Application Support/DashCore/`

* Linux: `$HOME/.dashcore/`

To use `dashd` and `dash-cli`, you will need to add a RPC password to your `dash.conf` file. Both programs will read from the same file if both run on the same system as the same user, so any long random password will work:

``` text
rpcpassword=change_this_to_a_long_random_password
```

You should also make the `dash.conf` file only readable to its owner.  On Linux, Mac OSX, and other Unix-like systems, this can be accomplished by running the following command in the Dash Core application directory:

``` text
chmod 0600 dash.conf
```

For development, it's safer and cheaper to use Dash's test network (testnet), regression test mode (regtest), or a develper network (devnet) described below.

Questions about Dash use are best sent to the [Dash forum](https://www.dash.org/forum/categories/dash-support.61/) and [Discord channels](http://www.dashchat.org).

In the following documentation, some strings have been shortened or wrapped: "[...]" indicates extra data was removed, and lines ending in a single backslash "\\" are continued below. If you hover your mouse over a paragraph, cross-reference links will be shown in blue.  If you hover over a cross-reference link, a brief definition of the term will be displayed in a tooltip.