This project will scan ISBN number from photo, check price on allegro and put it into auction if
user want to.

How to develop:

1) Create virtual enviroment with Python3
2) Install requirements.txt packages
3) Install requirements.dev.txt developes packages
4) Install external ZBar library:

   """sudo apt-get install libzbar0"""

ISSUES:
 - [x] going back to main screen does not work (sic!)
 - [x] problem message seems to be not initialised while quering for book.
 - [x] inputting custom ISBN (not prepared) will sometimes block cool gif in the background,

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
 - [x] add basic logo to main screen,
 - [x] add goback options in "input_number_manually_screen",
 - [x] add config perserving closing app,
   - [x] think about some options schema validation (it colud be ovekill though),
 - [x] add switching between screens to Manage class direclty (it could trigger some Python code, so
   this is rather necessary),

TODO:
 - [x] kewl loading screen (delete single job screen and add more user-fiendly waiting screen
   direcly on results).
 - [x] upgrade json extraction (actual version can explode in every second),
 - [ ] add whole app test (check if all method works abyhow, swithcing between screens etc),
 - [x] error screen - some basics but with try catch,
   - [ ] pretty error printing (now it shows raw Python error),
   - [ ] implement some basic fuckups (no Internet connection, 404, and so on),
 - [ ] add rudimental docstrings,
 - [x] scan barcode from camera,
 - [x] implement some basic message system (maybe by setting manage values in some basic class?),

 NICE TO HAVE:
 - [x] all widget in main.kv should have its own class (is it necessary?)
 - [x] change "wait_window" name to something more descriptable,
