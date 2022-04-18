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
from lxml import html
import requests, random

colour_cyan = '\033[36m'
colour_reset = '\033[0;0;39m'
colour_red = '\033[31m'
colour_green='\033[0;32m'
colour_yellow='\033[0;33m'
colour_purple='\033[0;35m'
colour_blue='\033[0;34m'
colour_list = (colour_cyan, colour_reset, colour_red, colour_green, colour_yellow, colour_purple, colour_blue)


def xBal(addr):
    urlblock = "https://ethereum.atomicwallet.io/address/" + addr
    respone_block = requests.get(urlblock)
    byte_string = respone_block.content
    source_code = html.fromstring(byte_string)
    xpatch_txid = '/html/body/main/div/div[2]/div[1]/table/tbody/tr[4]/td[2]'
    treetxid = source_code.xpath(xpatch_txid)
    xVol = str(treetxid[0].text_content())
    return xVol

def xBal2(addr2):
    urlblock = "https://bitcoin.atomicwallet.io/address/" + addr2
    respone_block = requests.get(urlblock)
    byte_string = respone_block.content
    source_code = html.fromstring(byte_string)
    xpatch_txid = '/html/body/main/div/div[2]/div[1]/table/tbody/tr[4]/td[2]'
    treetxid = source_code.xpath(xpatch_txid)
    xVol = str(treetxid[0].text_content())
    return xVol

def xBal3(addr3):
    urlblock = "https://bitcoin.atomicwallet.io/address/" + addr3
    respone_block = requests.get(urlblock)
    byte_string = respone_block.content
    source_code = html.fromstring(byte_string)
    xpatch_txid = '/html/body/main/div/div[2]/div[1]/table/tbody/tr[4]/td[2]'
    treetxid = source_code.xpath(xpatch_txid)
    xVol = str(treetxid[0].text_content())
    return xVol

def xBal4(addr4):
    urlblock = "https://bitcoin.atomicwallet.io/address/" + addr4
    respone_block = requests.get(urlblock)
    byte_string = respone_block.content
    source_code = html.fromstring(byte_string)
    xpatch_txid = '/html/body/main/div/div[2]/div[1]/table/tbody/tr[4]/td[2]'
    treetxid = source_code.xpath(xpatch_txid)
    xVol = str(treetxid[0].text_content())
    return xVol
    
def save_data():
    with open("winner.txt", "a", encoding="utf-8") as f:
        f.write(f"""\nMnemonic_words for Bitcoin&ETH HDWallet:  {MNEMONIC}
        Privatekey HEX : {target_wallet['privatekey']}
        Privatekey DEC : {target_wallet['privatedec']}
        Derivation Path ETH :  {target_wallet['path']} Public Address ETH:  {target_wallet['address']}
        |==============================================|======================|
        |  {target_wallet['address']} |{get_balanceeth(ethaddr)}              |
        |==============================================|======================|
        Derivation Path BTC1  :  {target_wallet['path44']} Public 1 Address:  {target_wallet['p2pkh']}
        |==============================================|======================|
        | {target_wallet['path44']} |{get_balance(p2pkh)}                     |
        |==============================================|======================|
        Privatekey WIF BTC 1 Address : {target_wallet['wif44']}
        Root XPrivate Key BTC 1 Address: {target_wallet['root44']}
        Derivation Path BTC3  :  {target_wallet['path49']} Public 3 Address:  {target_wallet['p2pkh49']}
        |==============================================|======================|
        | {target_wallet['path49']} |{get_balance(p2pkh49)}                   |
        |==============================================|======================|
        Privatekey WIF BTC 3 Address : {target_wallet['wif49']}
        Root XPrivate Key BTC 3 Address: {target_wallet['root49']}
        Derivation Path ETH :  {target_wallet['path84']} Public bc1 Address:  {target_wallet['p2pkh84']}
        |==============================================|======================|
        | {target_wallet['path84']} |{get_balance(p2pkh84)}                   |
        |==============================================|======================|
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
    
print('Mnemonic ' + colour_yellow + '12/' + colour_red + '15/' + colour_blue + '18/' + colour_green + '21/' + colour_cyan + '24 : ' + colour_reset + 'Words to Bitcoin&ETH HDWallet Tool')
R = int(input('Enter Ammount Mnemonic Words ' + colour_yellow + '12/' + colour_red + '15/' + colour_blue + '18/' + colour_green + '21/' + colour_cyan + '24 : ' + colour_reset))
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
    print(colour_red + "WRONG NUMBER!!! Starting with 24 Words" + colour_reset)
    s1 = 256
Lang = int(input(' Choose language ' + colour_purple + '1.english, ' + colour_green + '2.french, ' + colour_blue + '3.italian, ' + colour_yellow + '4.spanish, ' + colour_cyan + '5.chinese_simplified, ' + colour_red + '6.chinese_traditional, ' + colour_reset + '7.japanese or ' + colour_purple + '8.korean ' + colour_reset))
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
divs = 1 # int(input("How Many Derivation Paths? m/44'/60'/0'/0/0/ to m/44'/60'/0'/0/???? -> "))

while True:
    data=[]
    count += 1
    total += 4
    random_colour = random.choice(colour_list)
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
        ethaddr = target_wallet['address']
        p2pkh = target_wallet['p2pkh']
        p2pkh49 = target_wallet['p2pkh49']
        p2pkh84 = target_wallet['p2pkh84']
        bal = xBal(ethaddr)
        bal2 = xBal2(p2pkh)
        bal3 = xBal3(p2pkh49)
        bal4 = xBal4(p2pkh84)

        if int(bal) > 0 or int(bal2) > 0 or int(bal3) > 0 or int(bal4) > 0:
            print('\nMatch Found')
            print(f''' 
     |==============================================|======================|
     | Bitcoin (BTC) & Ethereum (ETH) Address       |       Balance        |
     |==============================================|======================|
     | ''', ethaddr, ''' |  ''' + colour_green + '''''', bal, '''''' + colour_reset + '''                 |
     |==============================================|======================|
     |==============================================|======================|
     | ''', p2pkh, '''         |  ''' + colour_green + '''''', bal2, '''''' + colour_reset + '''                 |
     |==============================================|======================|
     |==============================================|======================|
     | ''', p2pkh49, '''         |  ''' + colour_green + '''''', bal3, '''''' + colour_reset + '''                 |
     |==============================================|======================|
     |==============================================|======================|
     | ''', p2pkh84, ''' |  ''' + colour_green + '''''', bal3, '''''' + colour_reset + '''                 |
     |==============================================|======================|''')
            print('\nmnemonic_words for Bitcoin&ETH HDWallet : ' + colour_green +  MNEMONIC + colour_reset)
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
            print(random_colour + ' [' + str(count) + '] ------------------------' + colour_reset)
            print(random_colour + 'Total Checked [' + str(total) + '] ' + colour_reset)
            print('\nmnemonic_words  : ' + colour_red + MNEMONIC + colour_reset)
            for target_wallet in data:
                ethaddr = target_wallet['address']
                p2pkh = target_wallet['p2pkh']
                p2pkh49 = target_wallet['p2pkh49']
                p2pkh84 = target_wallet['p2pkh84']
                print('Privatekey : ', target_wallet['privatekey'])
                print('Privatekey DEC : ', target_wallet['privatedec'])
                print(f''' 
     |==============================================|======================|
     | Bitcoin (BTC) & Ethereum (ETH) Address       |       Balance        |
     |==============================================|======================| 
     | ''', ethaddr, ''' |  ''' + colour_red + '''''', bal, '''''' + colour_reset + '''                 |
     |==============================================|======================|
     |==============================================|======================|
     | ''', p2pkh, '''         |  ''' + colour_red + '''''', bal2, '''''' + colour_reset + '''                 |
     |==============================================|======================|
     |==============================================|======================|
     | ''', p2pkh49, '''         |  ''' + colour_red + '''''', bal3, '''''' + colour_reset + '''                 |
     |==============================================|======================|
     |==============================================|======================|
     | ''', p2pkh84, ''' |  ''' + colour_red + '''''', bal4, '''''' + colour_reset + '''                 |
     |==============================================|======================|''')
                #save_data()
if __name__ == '__main__':
    p1: Process = Process(target=xBal, args=("p1",))
    p2: Process = Process(target=xBal2, args=("p2",))
    p3: Process = Process(target=xBal3, args=("p3",))
    p4: Process = Process(target=xBal4, args=("p4",))
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()