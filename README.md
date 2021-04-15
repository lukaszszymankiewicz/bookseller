This project will scan ISBN number from photo, check price on allegro and put it into auction if
user want to.

How to develop:

1) Create virtual enviroment with Python3
2) Install requirements.txt packages
3) Install requirements.dev.txt developes packages
4) Install external ZBar library:

```
sudo apt-get install libzbar0
```

TODO:
 - [ ] upgrade json extraction (actual version can explode in every second),
 - [ ] add whole app test (check if all method works abyhow, swithcing between screens etc),
 - [x] error screen - some basics but with try catch,
   - [ ] pretty error printing (now it shows raw Python error),
   - [ ] implement some basic fuckups (no Internet connection, 404, and so on),
 - [ ] add rudimental docstrings and documentation,
 - [ ] add async job to read barcode from camera,
 - [ ] add schema validation fo json extraction,
 - [ ] delete all TODOS
 - [ ] search for sold copies in Allegro Archive (add it as async job)
