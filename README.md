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
 - [x] add async job to read barcode from camera,
 - [x] check intenet connection at start (or at request?)
 - [x] upgrade json extraction (actual version can explode in every second),
 - [ ] add whole app test (check if all method works anyhow, swithcing between screens etc),
 - [x] error screen - some basics but with try catch,
   - [x] pretty error printing (now it shows raw Python error),
   - [x] implement some basic fuckups (no Internet connection, 404, and so on),
 - [ ] add rudimental docstrings and documentation,
 - [ ] delete all TODOS
 - [ ] search for sold copies in Allegro Archive (add it as async job)
 - [ ] try...catch if camera exist
 - [ ] think about cleaning up project (app/windows/utils/..) should be named in some back-end
   convention
 - [ ] whink about moving all the functions directly into Python code. Right now tis is the only 
   thing that lays in kivy code that actualy does something. I belive that this is braking up whole
   MVC model convention.

NICE TO HAVE:
 - [ ] Camera should run only when needed.
