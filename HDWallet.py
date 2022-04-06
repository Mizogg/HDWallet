'''

Made by Mizogg Using HDWallet BIP44HDWallet BIP49HDWallet BIP84HDWallet . Python-based library for the implementation of a hierarchical deterministic wallet generator for over 140+ multiple cryptocurrencies. It allows the handling of multiple coins, multiple accounts, external and internal chains per account and millions of addresses per the chain.
https://pypi.org/project/hdwallet/     Requirements pip install hdwallet

'''
from hdwallet import BIP44HDWallet
from hdwallet import BIP49HDWallet
from hdwallet import BIP84HDWallet
from hdwallet.cryptocurrencies import EthereumMainnet
from hdwallet.cryptocurrencies import BitcoinMainnet
from hdwallet.derivations import BIP44Derivation
from hdwallet.derivations import Derivation
from hdwallet.utils import generate_mnemonic
from hdwallet import HDWallet
from typing import Optional
from hdwallet.symbols import ETH as SYMBOL
from hdwallet.symbols import BTC as SYMBOL1

filename ='eth.txt' #eth address list to look for database file needed
with open(filename) as f:
    line_count = 0
    for line in f:
        line != "\n"
        line_count += 1
eth_list = [line.split()[0].lower() for line in open(filename,'r')]
eth_list = set(eth_list)

filename ='btc.txt' #btc address list to look for database file needed
with open(filename) as f:
    line_count = 0
    for line in f:
        line != "\n"
        line_count += 1        
with open(filename) as file:
    add = file.read().split()
add = set(add)

def save_data():
    with open("winner.txt", "a") as f:
        f.write(f"""\nMnemonic_words for Bitcoin&ETH HDWallet:  {MNEMONIC}
        Privatekey HEX : {target_wallet['privatekey']}
        Privatekey DEC : {target_wallet['privatedec']}
        Derivation Path ETH :  {target_wallet['path']} Public Address ETH:  {target_wallet['address']}
        Derivation Path BTC1  :  {target_wallet['path44']} Public 1 Address:  {target_wallet['p2pkh']}
        Privatekey WIF BTC 1 Address : {target_wallet['wif44']}
        Root XPrivate Key BTC 1 Address: {target_wallet['root44']}
        Derivation Path BTC3  :  {target_wallet['path49']} Public 3 Address:  {target_wallet['p2pkh49']}
        Privatekey WIF BTC 3 Address : {target_wallet['wif49']}
        Root XPrivate Key BTC 3 Address: {target_wallet['root49']}
        Derivation Path ETH :  {target_wallet['path84']} Public bc1 Address:  {target_wallet['p2pkh84']}
        Privatekey WIF BTC bc1 Address : {target_wallet['wif84']}
        Root XPrivate Key BTC bc1 Address: {target_wallet['root84']}

        """)
    
def data_all():
    for address_index in range(divs):
        bip44_derivation: BIP44Derivation = BIP44Derivation(
            cryptocurrency=EthereumMainnet, account=0, change=False, address=address_index
        )
        bip44_hdwallet.from_path(path=bip44_derivation)
        hdwallet.from_path(path=f"m/44'/0'/0'/0/{address_index}")
        bip49_hdwallet.from_path(path=f"m/49'/0'/0'/0/{address_index}")
        bip84_hdwallet.from_path(path=f"m/84'/0'/0'/0/{address_index}")
        data.append({
                'path': bip44_hdwallet.path(), # ETH BIP 44 PATH
                'path44': hdwallet.path(), # BTC BIP 44 PATH
                'path49': bip49_hdwallet.path(), # BTC BIP 49 PATH
                'path84': bip84_hdwallet.path(), # BTC BIP 84 PATH
                
                'address': bip44_hdwallet.address(), # ETH Address
                
                'privatekey': bip44_hdwallet.private_key(),
                'privatedec': int(bip44_hdwallet.private_key(), 16),
                'root44':hdwallet.root_xprivate_key(),
                'root49':bip49_hdwallet.root_xprivate_key(),
                'root84':bip84_hdwallet.root_xprivate_key(),
                
                'wif44': hdwallet.wif(),
                'wif49': bip49_hdwallet.wif(),
                'wif84': bip84_hdwallet.wif(),
                
                'p2pkh': hdwallet.p2pkh_address(), # Public Key Hash (P2PKH) address.
                #'p2sh': hdwallet.p2sh_address(), # Script Hash (P2SH) address.
                #'p2wpkh': hdwallet.p2wpkh_address(), # Witness Public Key Hash (P2WPKH) address
                #'p2wpkhinp2sh': hdwallet.p2wpkh_in_p2sh_address(), # Get P2WPKH nested in P2SH address.
                #'p2wsh': hdwallet.p2wsh_address(), #  Pay to Witness Script Hash (P2WSH)
                #'p2wshinp2sh': hdwallet.p2wsh_in_p2sh_address(), # P2WSH nested in P2SH address
                'p2pkh49': bip49_hdwallet.address(), # P2WPKH nested in P2SH address BIP49 .
                'p2pkh84': bip84_hdwallet.address(), # Pay to Witness Public Key Hash (P2WPKH) address BIP84 .
            })
        hdwallet.clean_derivation()
        bip44_hdwallet.clean_derivation()
        bip49_hdwallet.clean_derivation()
        bip84_hdwallet.clean_derivation()

data = []
count=0
total= 0
    
print('Mnemonic 12/15/18/21/24 Words to Bitcoin&ETH HDWallet Tool')
R = int(input('Enter Ammount Mnemonic Words 12/15/18/21/24 : '))
if R == 12:
    s1 = 128
elif R == 15:
    s1 = 160
elif R == 18:
    s1 = 192
elif R == 21:
    s1 = 224
elif R == 24:
    s1 = 256
else:
    print("WRONG NUMBER!!! Starting with 24 Words")
    s1 = 256
Lang = int(input(' Choose language 1.english, 2.french, 3.italian, 4.spanish, 5.chinese_simplified, 6.chinese_traditional, 7.japanese or 8.korean '))
if Lang == 1:
    Lang1 = "english"
elif Lang == 2:
    Lang1 = "french"
elif Lang == 3:
    Lang1 = "italian"
elif Lang == 4:
    Lang1 = "spanish"
elif Lang == 5:
    Lang1 = "chinese_simplified"
elif Lang == 6:
    Lang1 = "chinese_traditional"
elif Lang == 7:
    Lang1 = "japanese"
elif Lang == 8:
    Lang1 = "korean"
else:
    print("WRONG NUMBER!!! Starting with english")
    Lang1 = "english"
divs = int(input("How Many Derivation Paths? m/44'/60'/0'/0/0/ to m/44'/60'/0'/0/???? -> "))
display = int(input('1=Full Display (Slower) 2=Slient Mode (Faster) : '))
while True:
    data=[]
    count += 1
    total += divs
    MNEMONIC: str = generate_mnemonic(language=Lang1, strength=s1)
    PASSPHRASE: Optional[str] = None
    bip44_hdwallet: BIP44HDWallet = BIP44HDWallet(cryptocurrency=EthereumMainnet)
    bip44_hdwallet.from_mnemonic(
        mnemonic=MNEMONIC, language=Lang1, passphrase=PASSPHRASE
    )
    hdwallet: HDWallet = HDWallet(symbol=SYMBOL1, use_default_path=False)
    hdwallet.from_mnemonic(
        mnemonic=MNEMONIC, language=Lang1, passphrase=PASSPHRASE
    )
    bip49_hdwallet: BIP49HDWallet = BIP49HDWallet(symbol=SYMBOL1, account=0, change=False, address=0)
    bip49_hdwallet.from_mnemonic(
        mnemonic=MNEMONIC, language=Lang1, passphrase=PASSPHRASE
    )
    bip84_hdwallet: BIP84HDWallet = BIP84HDWallet(symbol=SYMBOL1, account=0, change=False, address=0)
    bip84_hdwallet.from_mnemonic(
        mnemonic=MNEMONIC, language=Lang1, passphrase=PASSPHRASE
    )
    data_all()
    for target_wallet in data:
        address = target_wallet['address'].lower()
        p2pkh = target_wallet['p2pkh']
        p2pkh49 = target_wallet['p2pkh49']
        p2pkh84 = target_wallet['p2pkh84']
        if address in eth_list or p2pkh in add or p2pkh49 in add or p2pkh84 in add:
            print('\nMatch Found')
            print('\nmnemonic_words for Bitcoin&ETH HDWallet : ', MNEMONIC)
            print('Privatekey : ', target_wallet['privatekey'])
            print('Privatekey DEC : ', target_wallet['privatedec'])
            print('Derivation Path : ', target_wallet['path'], ' : ETH Address  : ', target_wallet['address'])
            print('Derivation Path : ', target_wallet['path44'], '  : BTC 1 Address : ', target_wallet['p2pkh'])
            print('Privatekey WIF BTC 1 Address : ', target_wallet['wif44'])
            print('Root XPrivate Key BTC 1 Address: ', target_wallet['root44'])
            print('Derivation Path : ', target_wallet['path49'], '  : BTC 3 Address : ', target_wallet['p2pkh49'])
            print('Privatekey WIF BTC 3 Address : ', target_wallet['wif49'])
            print('Root XPrivate Key BTC 3 Address: ', target_wallet['root49'])
            print('Derivation Path : ', target_wallet['path84'], '  : BTC bc1 Address : ', target_wallet['p2pkh84'])
            print('Privatekey WIF BTC bc1 Address : ', target_wallet['wif84'])
            print('Root XPrivate Key BTC bc1 Address: ', target_wallet['root84'])
            save_data()
    else:
        if display == 1:
            print(' [' + str(count) + '] ------------------------')
            print('Total Checked [' + str(total) + '] ')
            print('\nmnemonic_words  : ', MNEMONIC)
            for target_wallet in data:
                print('Privatekey : ', target_wallet['privatekey'])
                print('Privatekey DEC : ', target_wallet['privatedec'])
                print('Derivation Path : ', target_wallet['path'], ' : ETH Address  : ', target_wallet['address'])
                print('Derivation Path : ', target_wallet['path44'], '  : BTC 1 Address : ', target_wallet['p2pkh'])
                #print('Privatekey WIF BTC 1 Address : ', target_wallet['wif44'])
                #print('Root XPrivate Key BTC 1 Address: ', target_wallet['root44'])
                print('Derivation Path : ', target_wallet['path49'], '  : BTC 3 Address : ', target_wallet['p2pkh49'])
                #print('Privatekey WIF BTC 3 Address : ', target_wallet['wif49'])
                #print('Root XPrivate Key BTC 3 Address: ', target_wallet['root49'])
                print('Derivation Path : ', target_wallet['path84'], '  : BTC bc1 Address : ', target_wallet['p2pkh84'])
                #print('Privatekey WIF BTC bc1 Address : ', target_wallet['wif84'])
                #print('Root XPrivate Key BTC bc1 Address: ', target_wallet['root84'])
                                
                #print('Derivation Path : ', target_wallet['path2'], ' : BTC Address : ', target_wallet['p2sh'])
                #print('Derivation Path : ', target_wallet['path2'], ' : BTC Address : ', target_wallet['p2wpkh'])
                #print('Derivation Path : ', target_wallet['path2'], ' : BTC Address : ', target_wallet['p2wpkhinp2sh'])
                #print('Derivation Path : ', target_wallet['path2'], ' : BTC Address : ', target_wallet['p2wsh'])
                #print('Derivation Path : ', target_wallet['path2'], ' : BTC Address : ', target_wallet['p2wshinp2sh'])
                #save_data()


        if display == 2:
            print('Scan Number [' + str(count) + '] ------', 'Total Checked [' + str(total) + '] ', end='\r')