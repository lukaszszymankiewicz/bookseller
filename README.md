This project will scan ISBN number from photo, check price on allegro and put it into auction if
user want to.

ISSUES:
 - [x] going back to main screen does not work (sic!)
 - [ ] inputting custom ISBN (not prepared) will sometimes block cool gif in the background,
 - [ ] problem message seems to be not initialised while quering for book.

DONE:
 - [x] number keyboard to input ISBN number in it,
 - [x] basic ISBN validation while typing,
 - [x] waiting screen made anyhow readable,
 - [x] result screen made anyhow readeble,
 - [x] consistency between screens,
 - [x] 403 issue on request module,
 - [x] clean up all methods using screen manager (add more descriptive function names and usages),
 - [x] refactor tests (all unit test work on old version of prototype),
 - [x] add more flexible status parameter to async request (job_done, job_wip, job succeded),
 - [x] implement one geneal use message (not query message and validation message!),
 - [x] add moeny currency at results screen,
 - [x] add settings screen,
 - [x] change name of "SearchWindow" to "InputNumberManuallyScreen".
 - [x] prettify kivy.kv file (move data to Python class),
 - [x] add welcome screen with three options available: scan by photo, input number manually and settings,
 - [x] Implement radio buttons in Settings tab! (actually Toggle box are better!)
 - [x] implement build-in check buttons,
 - [x] once again: fill all static values into kivy file:
   - [x] subclass all widgets

TODO:
 - [ ] add basic logo to main screen,
 - [ ] scan barcode from camera,
 - [ ] implement some basic message system (maybe by setting manage values in some basic class?),
 - [ ] maybe some of the basic label values should be inputted by some init method instead of
   hard-coding it kivy.kv? Think about it!,
 - [ ] add goback options in "input_number_manually_screen",
 - [ ] add config perserving closing app,
 - [ ] add whole app test (check if all method works abyhow, swithcing between screens etc),
 - [ ] add allegro login screen,
 - [ ] error screen - some basics but with try catch,
   - [ ] pretty error printing (now it shows raw Python error),
   - [ ] implement some basic fuckups (no Internet connection, 404, and so on),
 - [ ] taking ISBN number directly from photo (in real time!),
 - [ ] add rudimental docstrings,
 - [ ] upgrade json extraction (actual vesion can explode in every second).

 NICE TO HAVE:
 - [x] all widget in main.kv should have its own class (is it necessary?)
 - [x] change "wait_window" name to something more descriptable,
