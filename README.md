# HDWallet Hierarchical Deterministic Wallet

Using HDWallet BIP44HDWallet BIP49HDWallet BIP84HDWallet  140+ multiple cryptocurrencies.

For more Information https://pypi.org/project/hdwallet/ and https://github.com/meherett/python-hdwallet

For more info see the BIP specs.

| BIP's                                                                    | Titles                                                     |
| :----------------------------------------------------------------------- | :--------------------------------------------------------- |
| [BIP44](https://github.com/bitcoin/bips/blob/master/bip-0044.mediawiki)  | Multi-Account Hierarchy for Deterministic Wallets          |
| [BIP49](https://github.com/bitcoin/bips/blob/master/bip-0049.mediawiki)  | Derivation scheme for P2WPKH-nested-in-P2SH based accounts |
| [BIP84](https://github.com/bitcoin/bips/blob/master/bip-0084.mediawiki)  | Derivation scheme for P2WPKH based accounts                |

## Installation

The easiest way to install `hdwallet` is via pip:

```
pip install hdwallet
```
To run use any terminal CMD. You will need 2 database files one for Bitcoin and one for ETH address that you wish to find `bct.txt & eth.txt`:
```
python HDWallet.py
```
```
Mnemonic 12/15/18/21/24 Words to Bitcoin&ETH HDWallet Tool
Enter Ammount Mnemonic Words 12/15/18/21/24 : 24
 Choose language 1.english, 2.french, 3.italian, 4.spanish, 5.chinese_simplified, 6.chinese_traditional, 7.japanese or 8.korean 1
How Many Derivation Paths? m/44'/60'/0'/0/0/ to m/44'/60'/0'/0/???? -> 10
1=Full Display (Slower) 2=Slient Mode (Faster) : 1
 [1] ------------------------
Total Checked [10]
mnemonic_words  :  mechanic narrow dutch roof twin marine elegant thank copy cup seven walnut cargo such visit slab earth virtual build pond confirm inner outdoor idea
Privatekey :  27eb97aa125584ff32ebf71be6a70ec97a054b42785d1ea11781a2cba2a1de69
Privatekey DEC :  18056456903790410194360872016295984982729604303718539849028684071465398689385
Derivation Path :  m/44'/60'/0'/0/0/44'/60'/0'/0/0  : ETH Address  :  0xC8C1039f367c3f3312991cC88537Dc4166Dd96Cb
Derivation Path :  m/44'/0'/0'/0/0   : BTC 1 Address :  1DqsZP2BpxVkrra72un77fHzbHTD3mk1n7
Derivation Path :  m/49'/0'/0'/0/0/49'/0'/0'/0/0   : BTC 3 Address :  33TSuqANmVbZ8yo8PyXXnZT5BWToqgQ4Bo
Derivation Path :  m/84'/0'/0'/0/0/84'/0'/0'/0/0   : BTC bc1 Address :  bc1qy6es0hluw9c9j90g2fza3lv5q3t40ukk0pggsp
Privatekey :  2260d359fc056d0a782404fbd4ced87b4993310c4c375392c7223b6e9252ba21
Privatekey DEC :  15549712864505137888835854022682805846400955349271592763168085062776649857569
Derivation Path :  m/44'/60'/0'/0/1  : ETH Address  :  0xbD047d3Ef35A53502C2a5C45cc52225e4Fe56b8c
Derivation Path :  m/44'/0'/0'/0/1   : BTC 1 Address :  1GHDGofakeRrvd76C1AHcAgZk1nPqG1qDS
Derivation Path :  m/49'/0'/0'/0/1   : BTC 3 Address :  3PG84SBdZ2dk8nBgusdg87T8VRu49CcUsi
Derivation Path :  m/84'/0'/0'/0/1   : BTC bc1 Address :  bc1q5kevkg22zqzfmnmljttjltdu9cts5kagg3xu97
Privatekey :  36c77a26e2addac93c7e450e1ac1c6de6fa179b4a4395b089a349afad97fed71
Privatekey DEC :  24777339450791662819125413676329567845958690923318929115213122167524558892401
Derivation Path :  m/44'/60'/0'/0/2  : ETH Address  :  0x5228B395036E5c759217476e34e571ddF402baA5
Derivation Path :  m/44'/0'/0'/0/2   : BTC 1 Address :  15J4h1v6k7sLUZfc5eLUTgyZBJ84UaWM9k
Derivation Path :  m/49'/0'/0'/0/2   : BTC 3 Address :  3D8sKn8rcCDmbBKxGCvyfpxqs1H7wSTRJh
Derivation Path :  m/84'/0'/0'/0/2   : BTC bc1 Address :  bc1qxfus0qsvx0y0elstek6cfge9vca3nvdux3qh43
Privatekey :  8acbc0c51af4f34209f95eef420c096b583301cbda73de55fd913cd22b88c910
Privatekey DEC :  62779173507887737093204484753290143331732618295975415205352376346154522691856
Derivation Path :  m/44'/60'/0'/0/3  : ETH Address  :  0x82D964ab302F687513493113da56a13c99fF56ef
Derivation Path :  m/44'/0'/0'/0/3   : BTC 1 Address :  16bRTxVL6qWRqfgQTKt3rKVBdYMXSqvB3d
Derivation Path :  m/49'/0'/0'/0/3   : BTC 3 Address :  394xcJCWuosyKDGGvc3gLigAV5J8wNr8tb
Derivation Path :  m/84'/0'/0'/0/3   : BTC bc1 Address :  bc1qzpz8a8ee2728kzanqs3aks6t2mh4n4n86rsvzk
Privatekey :  0cbca58b6fb04b4735fc9b135a1515dd30306b21a2fa0a9a05b520a45e562a01
Privatekey DEC :  5761063978519527634488682515993698053513580333388571531537563884652066122241
Derivation Path :  m/44'/60'/0'/0/4  : ETH Address  :  0x7575bcf32a6608d1A6d375040339D2adDD5fA010
Derivation Path :  m/44'/0'/0'/0/4   : BTC 1 Address :  1CFsLb3DLt64J9bcvBUiFiv4Sa3Jv5yUKm
Derivation Path :  m/49'/0'/0'/0/4   : BTC 3 Address :  3CfgXjvSfAKxUG3g6xaxKVkea15fHdHnps
Derivation Path :  m/84'/0'/0'/0/4   : BTC bc1 Address :  bc1q8tn38aqsag9sxnswt662hjrvkuy7x0kjk258ay
Privatekey :  758d49b76fe5f3c6e08af7cf6871b0ae8ae6f9b70529b2a67f844546411c9031
Privatekey DEC :  53170237493313736675306896670982330049549572390144429023077066981110645035057
Derivation Path :  m/44'/60'/0'/0/5  : ETH Address  :  0xFa791fE2deA685a835329799d424D55a4572b3F8
Derivation Path :  m/44'/0'/0'/0/5   : BTC 1 Address :  1BSkEntJGB7GzDhp48m4AeX17pCExu3PeP
Derivation Path :  m/49'/0'/0'/0/5   : BTC 3 Address :  39e3fEdnGCfyJp1ovzff4rfXDA27G7kJ4d
Derivation Path :  m/84'/0'/0'/0/5   : BTC bc1 Address :  bc1qx3vmt4hd4tksj7498dr5l4v7ms5twc4p56f4qp
Privatekey :  f8c285d3ed86d10148b47e638675bacd2b4998d8e882fe82850001593f60906b
Privatekey DEC :  112517278425044414176521665179318787472040225789959939228021803865433763254379
Derivation Path :  m/44'/60'/0'/0/6  : ETH Address  :  0x05E359E4527b1191DB7A24ee543c04678aad833C
Derivation Path :  m/44'/0'/0'/0/6   : BTC 1 Address :  1DNENSA5Tir6jg3VJxsBMvpH9A9LFRaMBA
Derivation Path :  m/49'/0'/0'/0/6   : BTC 3 Address :  3HQSyhHt5pFGz9WoWqRbkRgYXCAx7NkyuP
Derivation Path :  m/84'/0'/0'/0/6   : BTC bc1 Address :  bc1qv73fc0g446lt0mg2ejqvej57xm0fp7w8j0s2uc
Privatekey :  5f4aa925fd604e0fb8e5f0b199e7d4d903cf81f895f99da196b34d0133abfeed
Privatekey DEC :  43101634717538168967087054290132574160318683837909674665174079012620171214573
Derivation Path :  m/44'/60'/0'/0/7  : ETH Address  :  0xA709761839282C29c7388F5B64f2eA1C7A54A5A3
Derivation Path :  m/44'/0'/0'/0/7   : BTC 1 Address :  176LawVe9EWf9uSRQcuguYiXUHaqYwPeMw
Derivation Path :  m/49'/0'/0'/0/7   : BTC 3 Address :  32yKKgsCweuYW85h7Wm52MauiASMYU8Cf5
Derivation Path :  m/84'/0'/0'/0/7   : BTC bc1 Address :  bc1qwgwa3lvusf22zwmlt5ve77c69jst3jrm7k3gjh
Privatekey :  c003875befd3bdbe8fc53819c75624bb3df8f6d481e3cc873a9f5977c7a1930a
Privatekey DEC :  86850301683550188139135309206526534663962752533334344510468744391748684452618
Derivation Path :  m/44'/60'/0'/0/8  : ETH Address  :  0x2A1506Ae7060B75675810Fc20dD5ebf1B7DcEF5D
Derivation Path :  m/44'/0'/0'/0/8   : BTC 1 Address :  1E4GDZGFfJ1BQerBjrDHHBMqdeWxkuTook
Derivation Path :  m/49'/0'/0'/0/8   : BTC 3 Address :  3NZuYcszDV3Mx9PYLYJvjTwVEu654p7tT1
Derivation Path :  m/84'/0'/0'/0/8   : BTC bc1 Address :  bc1q9tw7pl77q9k86w9h92pq0g46tr4n2nn2mhj3r4
Privatekey :  d796fdcba8e9b9f8c07402c1813db19a4bee624ac65d0952d1e0e7efa4bdf424
Privatekey DEC :  97514041137602557079680212208250230152605698885460946727585070129092902122532
Derivation Path :  m/44'/60'/0'/0/9  : ETH Address  :  0xC7DB9f82C613E11D39d32E277A8438DE1c75191e
Derivation Path :  m/44'/0'/0'/0/9   : BTC 1 Address :  1LTRCRmqCUKdXWhQCEXH4Du51uszPgDXdm
Derivation Path :  m/49'/0'/0'/0/9   : BTC 3 Address :  3JDAuQJegQPkY5yeUzBEyYAbmipce32nSK
Derivation Path :  m/84'/0'/0'/0/9   : BTC bc1 Address :  bc1qkmcuee9zra7rw9vte6fmp3st8wuddunaam0ln8
```
