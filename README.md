whale-watcher

<img width="595" alt="screen shot 2017-09-07 at 8 16 22 pm" src="https://user-images.githubusercontent.com/17755587/30194677-8359d170-9409-11e7-92c8-a5ccd6897ea0.png">

***python 2.7.10***

change permissions:
```bash
chmod a+x whale_watcher.py
```

help:
```bash
./whale_watcher.py -h
```
- runs help screen (shown)

fetch:
```bash
./whale_watcher.py -f
```
- prompts for ETH address then fetches most recent transaction history of account

cached:
```bash
./whale_watcher.py -c
```
- runs whale-watcher from local version (test.html in cwd) of previously run fetch session


todo:
- add additional non-contract addresses (i.e. exchanges)


license:

MIT
