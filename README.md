This project will scan ISBN number from photo, check price on allegro and put it into auction if
user want to.

DONE:
 - [x] number keyboard to input ISBN number in it,
 - [x] basic ISBN validation while typing,
 - [x] waiting screen made anyhow readable,
 - [x] result screen made anyhow readeble,
 - [x] consistency between screens,
 - [x] 403 issue on request module.

TODO:
 - [ ] clean up all methods using screen manager (add more descriptive function names and usages),
 - [ ] add more flexible status parameter to async request (job_done, job_wip, job succeded). Think about RabbitMQ here (watch out! That could be overkill in this place!),
 - [ ] implement one geneal use message (not query message and validation message!),
 - [ ] refactor tests (all unit test work on old version of prototype),
 - [ ] add welcome screen with three options available: scan by photo, input number manually and settings,
 - [ ] add settings screen (logging to allegro, new auction template, selling strategy and so on),
 - [ ] add choose-method screen,
 - [ ] error screen - some basics but with try catch,
   - [ ] pretty error printing (now it shows raw Python error),
   - [ ] implement some basic fuckups (no Internet connection, 404, and so on),
 - [ ] taking ISBN number directly from photo (in real time!),
