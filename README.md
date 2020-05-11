# Dogecoin

Amacımız trezor ile multi signature doge coin cüzdan oluşturmak. Bunun için de bizim electrum denilen cüzdanları
kullanmamız gerekiyor. Bu cüzdanlar SPV denilen serverlara ihtiyaç duyuyor ve serverlar da tutmak ve indexlemek için 
serverlara ihtiyaç duyuyor. Biz de tüm coinler için bu süreci başlattık. Ama dogecoin de takıldık çünkü dogecoin nin
electrum dan fork edildiği proje 6 yıl önce son güncellemesini almış yani terkedilmiş. Projenin çalışmama sebebi olarak 
online sunuculara sahip olmadığını yazmışlar fakat biz kendimiz de sunucu bulacağımız için bunu dert etmedik. 

İlk önce electrum-dogeyi host makineme kurdum ve çalıştırdım. Program çalıştıktan sonra aktif sunucu var mı diye baktım
fakat yoktu. Programın sadece sunucuya ihtiyaç duyduğunu varsayıyorum. Şimdilik bundan emin değilim. Programı çalıştırdıktan sonra bir SPV sunucusu ihtiyacımız kaldı. Onun için bir 
kaç seçenek vardı o andan itibaren asıl görev başladı. Bununla birlikte sanal makineye 6 yıl önce aynı kişiler
tarafından yapılmış electrum-server i indirdim. Tabiki de electrum-server aynı zamanda bir daemon a ihtiyaç duyuyor
bu ihtiyacı da Dogecoin core sayesinde sağlıyoruz.

Proje çok eski olduğu için bir yerde hata verdi ve ben çok uğraşmadan bıraktık. Sonra electrumx e baktık ve bunda deneyeceğimizi
düşündük. Biraz uğraştıktan sonra core ile sağlıklı bir şekilde çalışan bir server elde ettik(Electrumx). Fakat cüzdan ile
etkileşime girmesini sağlayamadık. Acaba electrumx ile ilgili bir problem mi var diye düşünüp Litecoin ile denemeye karar verdik.
Ama onun kurulum aşamasında ssl serfikaları isteyince vazgeçip bıraktık. Biraz da düşündükten sonra electrumx ile 
electrum-dogenin uyumsuz olabileceğine karar verdik ve en başta kolay vazgeçtiğimiz electrum-dogeye geri döndük. Buradaki
hata gerçekten de basitmiş. Eksikleri kendi github ıma forkladığım kodlarla tamamladım. Bir hata aldık ve bu hata txindex=1
olmalı hatasıydı yani bütün blockhanin blok zincirine ihtiyaç duyuyordu. Sonra geriye baktığımızda galiba electrumx de de 
txindex=1 olmalıydı diye düşündük. Host makinede bir dogecoind oluşturup txindex=1 yapıp beklemeye başladım yaklaşık 1 gün sürdü
Txindex olurken bir tane daha server keşfettik electrum-person-server. Bu daha cüzdan private key 
isteyip çalışma mantığı biraz daha farklı. Electrumun serverina bağlanma parametrelerini console ile vermemiz gerektiğini
söylüyordu özellikle eski tip cüzdanlarda. Biz de ona göre hareket ettik.

Sonuç olarak 3 farklı yola girdik. Birincisi electrum-personal-doge ile electrum cüzdan oluşturmaktı. Bu txindex istemediği için
ilk önce bunu yapmaya kara verdim. İlk önce indirdiğimde proje Bitcoin Core 1.20 zorunlu olarak istiyordu. Projeyi yapana bir issue oluşturdum. Eski sürümlerini kullanmayı önerdi. Ben de bir önceki sürümü indirmeye karar verdim. Programı çalıştırdım fakat cüzdanla bir etkileşime girmesini sağlayamadım. Console da çalışıyor
görünüyordu ama bir cevap yoktu. Diğer yollara baktıktan sonra dönmek üzere not alıp kapattım. 

İkinci olarak txindex bittikten sonra tekrar electrum-doge-server ile electrum-doge ye döndük .İkiside aynı proje içerisinde
yer alıyor. Bence en rahat bunların çalışması gerekiyor. Txindex ile çalışmaya başladı fakat indexleme hızı çok yavaş olduğu için
bunu da not edip kapattım.

Üçüncü olarak ise electrumx in bizim eski electrum-doge cüzdanı ile zaten çalışmayacağını tespit ettik ama orjinal bitcoin için yapılmış olan electrum wallet ile çalışır mı diye denemeye
karar verdik. Baya popüler kullanıldıkları için kurulum baya hızlı oldu ve çalıştırdım ikisini de. Electrumx in indexleme
hızı yüksek olduğu için de bunu denedikten sonra diğerlerine dönmeye karar verdim. Fakat burada electrumun orjinal wallet ını kullanacağımı ziçin uyumsuzluk olma olasılığı baya yüksek görünüyor.     




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

### Electrum-doge komutu

```bash
electrum-doge --oneserver --server 127.0.0.1:50101:s

```




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
