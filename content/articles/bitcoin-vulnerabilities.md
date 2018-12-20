Title: Bitcoin Vulnerabilities
Date: 2018-08-20 09:43
Tags: bitcoin, vulnerabilities
Category: research
summary: Vulnerabilities Found in Bitcoin.

Some errors Satoshi with Bitcoin made are:

* Early version of bitcoind allows you to spend any coin by using `op_true op_return` as signature.
* It was initially possible to fork each version of the client on its own chain using "**op\_version**"
* Input value were not directly covered by signature, making it impossible for offline devices to check how much is spent and paid in fees.
* It is possible to put **op\_checksig** in an input script. Computing the signature hash fails and return 1 as an error code, but error code was checked so it is possible to produce a valid signature signing 1.
* Version fields are completely useless because they don't degrade gracefully.
* In case of hard fork, you can't make sense of the new data regardless of version, and in case of soft forks, they aren't useful.
* Places where addresses could be useful, for instance outputs, do not have one.
* Numerous opcodes were seriously flawed in early version, some of them exhibiting buffer overflow.
* It was possible to create several coinbases with the same **txid**, and in fact, Satoshi lost coins doing so. This breaks numerous assumption about the **txns** graph being a [DAG](wikipedia:Directed_acyclic_graph "wikilink") by design.
* Block size and/or tx count are not covered by pow. This creates DoS vector that lead to the introduction of the block size.  \[\[wikipedia:Bitcoin
* Unlimited|Bitcoin Unlimited\]\] suffered from attacks after neglecting these DoS * vectors.
* The script number format is little-endian, one complement. No more comments on that one.
* The original code had numerous problems checking signature encoding, at least one could lead to a chain split between 32 and 64 bits architectures.
* The [Merkle tree](wikipedia:Merkle_tree "wikilink") doesn't handle empty branches properly. This lead to a vulnerability where you could repeat transactions is a block and get a node to reject it.
* It is also possible to generate a valid 64 bytes transaction that looks like an intermediate node in the Merkle tree, making it possible to lie to **spv** by brute forcing 70bits or so, which isn't considered secure.
* Verifying signatures was O(n\*m) where n is the number of **checksig** ops and **m** the transaction size. This makes it possible to generate transaction that are absurdly expensive to validate.

References
==========

* <https://twitter.com/deadalnix/status/1007548856375095296?s=09>

