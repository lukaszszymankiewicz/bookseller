This project will scan ISBN number from photo, check price on allegro and put it into auction if
user want to.

ISSUES:
 - [ ] going back to main screen does not work (sic!)

DONE:
 - [x] number keyboard to input ISBN number in it,
 - [x] basic ISBN validation while typing,
 - [x] waiting screen made anyhow readable,
 - [x] result screen made anyhow readeble,
 - [x] consistency between screens,
 - [x] 403 issue on request module.
 - [x] clean up all methods using screen manager (add more descriptive function names and usages),
 - [x] refactor tests (all unit test work on old version of prototype),

TODO:
 - [ ] add whole app test (check if all method works abyhow, swithcing between screens etc)
 - [ ] change "wait_window" name to something more descriptable
 - [ ] add more flexible status parameter to async request (job_done, job_wip, job succeded). Think about RabbitMQ here (watch out! That could be overkill in this place!),
 - [ ] implement one geneal use message (not query message and validation message!),
 - [ ] add welcome screen with three options available: scan by photo, input number manually and settings,
 - [ ] add settings screen (logging to allegro, new auction template, selling strategy and so on),
 - [ ] add choose-method screen,
 - [ ] error screen - some basics but with try catch,
   - [ ] pretty error printing (now it shows raw Python error),
   - [ ] implement some basic fuckups (no Internet connection, 404, and so on),
 - [ ] taking ISBN number directly from photo (in real time!),
