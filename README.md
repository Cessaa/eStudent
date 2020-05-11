# Dogecoin

Şimdi 3 task tamamladım. Hepsi programatik olarak çalışıyor.

1 - Sanal makine kullandığım ve txindex=0 olan tek task buydu. **Electrum-personel-server** ile **dogecoin core** sanal makinemde, **electrum-doge** ise host makinede çalıştı. Wallet private key ini config dosyasında tanımladım. Aşağıdaki kodda var zaten. Ama sonuç alamadığım tek task bu belki biraz daha araştımam gerekiyor böyle kaldı çünkü. ip adresi sorunu olabilir. Dediğim gibi ayrıntılı bakılabilir.

2- Bu ve 3. taskı kendi host makinemde çalıştırdım. Dogecoin core un config dosyası ve blok ağı genel bilgilerini aşağıda verdim. Blok sayısı genel blockhain uzunluğuna yaklaşık 1-2 gün içinde geldi. Şuan çalıştığında da blok eklenmişse onu ekliyor ve tam blok sayısına hakimiz. Bu taskta **electrum-doge-server** ile **electrum-doge** yi denedim. Çalışırken blok sayısına ulaşması gerekiyor galiba ama bu çok yavaş. Çalıştırdıktan 280 saniye sonra catch_up: blok sayısı 9000 oldu. Bu baya yavaş gibi geliyor bana nasıl tamamlarız bilemiyorum. Öte yandan senin verdiğin parametrelerle electrum-doge'yi çalıştırdım ama not connect diyor. Heralde catch_up sayısı bitmediği içindir. Bir de ona tamamlandıktan sonra bakmamız gerekebilir.

3- Bu ise bence en etkili şkilde çalışan task. **Electrum** , **electrumx-server** ve   **dogecoind** ile çalışma aşağıda mevcut.
Yine not connect diyor ama **BlockProcessor'un** bitmesini beklemedim. En sonunda istediğinden başlarız diye sona saklıyorum onu. Sanki bu ikinci taska göre çok daha hızlı biter.

Sonuç olarak abi hiçbiri ile cüzdan conneti sağlayamadım.    




# 1.TASK electrum-personel-server electrum-doge

## electrum-personel-server çıktısı

```bash
INFO:2020-05-11 13:13:22,162: Starting Electrum Personal Server
INFO:2020-05-11 13:13:22,165: Logging to /tmp/electrumpersonalserver.log
INFO:2020-05-11 13:13:22,391: Displaying first 3 addresses of each master public key:
INFO:2020-05-11 13:13:22,420: 
default_wallet =>
	D9vV4yxdjoHQG2oSWyxGeH7xCtQVL6Lhqy
	DC1eLjpyCDrWaNp9Yut5rHZjVTMTRmRUFj
	DAuPLyj684fsjNub2wrWekpEMW3GSvijYz
INFO:2020-05-11 13:13:22,421: Obtaining bitcoin addresses to monitor . . .
INFO:2020-05-11 13:13:43,345: Obtained list of addresses to monitor in 21.174005270004272sec
INFO:2020-05-11 13:13:43,345: Building history with 2000 addresses . . .
INFO:2020-05-11 13:13:43,501: Found 0 txes. History built in 0.014749526977539062sec
INFO:2020-05-11 13:13:43,507: Starting electrum server
INFO:2020-05-11 13:13:43,507: Listening for Electrum Wallet on ('127.0.0.1', 50002)


```



# 2.TASK  electrum-doge-server ile electrum-doge 

## Host makinedeki dogecoin.conf


```bash
regtest=0
upnp=0
usehd=0
daemon=1
server=1

txindex=1

datadir=/var/dogecoin_data
rpcuser=dogecoin
rpcpassword=paroladoge
rpcport=22666

```

## Host makinedeki dogecoin getinfo

```bash

  "version": 1140200,
  "protocolversion": 70015,
  "walletversion": 60000,
  "balance": 0.00000000,
  "blocks": 3224506,
  "timeoffset": -1,
  "connections": 8,
  "proxy": "",
  "difficulty": 3498968.445680608,
  "testnet": false,
  "keypoololdest": 1589039259,
  "keypoolsize": 100,
  "paytxfee": 0.00000000,
  "relayfee": 1.00000000,
  "errors": ""

```



### Electrum-doge-server çıktısı

```
INFO:electrum-doge:Starting Electrum server on localhost
INFO:electrum-doge:Database version 3
INFO:electrum-doge:Blockchain height 8043
INFO:electrum-doge:UTXO tree root hash: ec286b621747a3c85adc7c5ca3a4ddc94f77ff56d7e27ba132433f7206293ccb
INFO:electrum-doge:Coins in database: 399058258100000000
INFO:electrum-doge:catching up missing headers: 8029 8043
INFO:electrum-doge:TCP server started on 127.0.0.1:50101
INFO:electrum-doge:catch_up: block 9000 (220.953s 280.448s) 24ee71355f9bcaa2958ca5b6dd351a022ed82bb9a183f0316a56a4980dab702a


```
Çalıştırdıktan 280 saniye sonra catch_up: blok sayısı 9000 oldu. Bu baya yavaş gibi geliyor bana nasıl tamamlarız bilemiyorum.

Öte yandan senin verdiğin parametrelerle **electrum-doge**'yi çalıştırdım ama not connect diyor. Heralde catch_up sayısı bitmediği içindir. 

### Electrum-doge komutu

```bash
electrum-doge --oneserver --server 127.0.0.1:50101:s

```
Bu komut da tek server a ve istediğimiz server a bağlanmamızı sağlıyor client içinden de ayarlanıyor ama bizim electrum-doge eski olduğu için garanti olsun.




# 3.TASK  electrumx-server ile electrum



### Electrumx komutu

```
COIN=dogecoin DB_DIRECTORY=/electrumx-db/ DAEMON_URL="http://dogecoin:paroladoge@127.0.0.1:22666/"
SERVICES=rpc://:50001,tcp://:50002 /usr/bin/python3.7 /usr/local/bin/electrumx_server


```

### Electrumx çıktısı

```
.
.
.
INFO:Prefetcher:catching up to daemon height 3,224,516 (3,091,491 blocks behind)
INFO:SessionManager:RPC server listening on localhost:50001
INFO:BlockProcessor:our height: 133,035 daemon: 3,224,516 UTXOs 0MB hist 0MB
INFO:BlockProcessor:our height: 150,335 daemon: 3,224,517 UTXOs 174MB hist 79MB
INFO:BlockProcessor:our height: 164,635 daemon: 3,224,517 UTXOs 301MB hist 133MB

```
