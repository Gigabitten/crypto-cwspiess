Very simple program, only hardly different from the one made in class.

First, just like the one in class, it sets up a connection to the running daemon. Then the
transaction ID of a transaction I made with a testnet faucet is used to get the information for that
transaction.

Unlike the example in class, instead of getting the decoded transaction directly, it gets a raw
transaction, prints it, decodes it, then prints the decoded version. I'm sure if I went and looked
at the opcodes I could decode a piece manually and see what's going on.