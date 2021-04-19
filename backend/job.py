import threading
import traceback
from typing import Callable

from kivy.clock import Clock


class JobStatus:
    WIP = "WIP"
    DONE = "DONE"
    PROBLEM = "PROBLEM"


class Job:
    """
    Container for function run in secondary thread (so running function in Job won`t stop main
    thread).
    Exceptions are catched, so even if function failed information are passed along.
    """

    def __init__(self, fun: Callable, args: dict):
        self.fun = fun
        self.args = args

        self.thread = None
        self.result = None

        self.status = JobStatus.WIP
        self._run_job()

    def _run_job(self):
        self.thread = threading.Thread(target=self._run_fun)
        self.thread.start()

    def _run_fun(self):
        try:
            self.result = self.fun(**self.args)
            self.status = JobStatus.DONE

        except Exception as err:
            traceback.print_tb(err.__traceback__)
            self.status = JobStatus.PROBLEM
            self.result = err.args[0]


class JobManager:
    """
    Wraper for Job class. Will run Job function and periodically check if Job is done. Futhermore
    status about such Job is collected.

    Every Job inputted into Manager must have defined callback function (function which will be run
    if Job succeded) and fallback function (function which will be run in Job failed). As arguments
    to fallback/callback function are results of Job function used (so when everything went good
    result are passed along, if function failed Exception/messsage is passed along).

    If Job function does not return anything code will move over and do nothing.
    """

    def __init__(self):
        self.job = None
        self.event = None
        self.reaction = {JobStatus.DONE: None, JobStatus.PROBLEM: None}
        self.default_check_interval = 0.5

    def add_job(
        self,
        fun: Callable,
        args: dict,
        callback: Callable,
        fallback: Callable = None,
        check_interval: float = 0.1,
    ):
        if not check_interval:
            check_interval = self.default_check_interval

        self.reaction[JobStatus.DONE] = callback
        self.reaction[JobStatus.PROBLEM] = fallback

        self.job = Job(fun=fun, args=args)
        self.event = Clock.schedule_interval(self.check, check_interval)

    def check(self, dt: float) -> None:
        """Periodically checks if Job fun is completed and routes the results.

        Args:
            dt - float representing check time interval.
        """

        if self.job.status == JobStatus.DONE and self.job.result:
            self.reaction[JobStatus.DONE](self.job.result)
            self.kill_jobs()

        elif self.job.status == JobStatus.DONE and not self.job.result:
            self.kill_jobs()

        elif self.job.status == JobStatus.PROBLEM:
            if self.reaction[JobStatus.PROBLEM]:
                self.reaction[JobStatus.PROBLEM](self.job.result)
                self.kill_jobs()
            else:
                self.kill_jobs()

        else:
            pass

    def kill_jobs(self):
        self.event.cancel()
        Clock.unschedule(self.event)
