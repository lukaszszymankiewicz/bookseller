This project will scan ISBN number from photo, check price on allegro and put it into auction if
user want to.

TODO:

[x] number keyboard to input ISBN number in it.
[x] basic ISBN validation while typing
[x] waiting screen made anyhow readable (query now indicated somehow)
[x] result screen made anyhow readeble
[x] consistency between screens (one color only)
[ ] 403 issue on request module (check GET headers)
[ ] add more flexible status parameter to async request (job_done, job_wip, job succeded). Think about RabbitMQ here (watch out! That could be overkill in this place!)
[ ] refactor tests (all unit test work on old version of prototype)
[ ] add welcome screen with three options available: scan by photo, input number manually and settings.
[ ] add settings screen (logging to allegro, new auction template, selling strategy and so on)
[ ] add choose-method screen
[x] error screen - some basics but with try catch.
  [ ] pretty error printing (now it shows raw Python error)
  [ ] implement some basic fuckups (no Internet connection, 404, and so on)
[ ] taking ISBN number directly from photo (in real time!)
