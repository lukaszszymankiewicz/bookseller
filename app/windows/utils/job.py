import threading
from typing import Callable

from kivy.clock import Clock


class JobStatus:
    WIP = "WIP"
    DONE = "DONE"
    PROBLEM = "PROBLEM"


class Job:
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

        except Exception as e:
            self.result = e
            self.status = JobStatus.PROBLEM


class JobManager:
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
        fallback: Callable,
        check_interval: float = 0.1,
    ):
        self.reaction[JobStatus.DONE] = callback
        self.reaction[JobStatus.PROBLEM] = fallback

        self.job = Job(fun=fun, args=args)
        self.event = Clock.schedule_interval(self.check, check_interval)

        if not check_interval:
            check_interval = self.default_check_interval

    def check(self, dt: float) -> None:
        if self.job.status == JobStatus.DONE:
            self.reaction[JobStatus.DONE](self.job.result)
            self.delete_job()

        elif self.job.status == JobStatus.PROBLEM:
            self.reaction[JobStatus.PROBLEM](self.job.result)
            self.delete_job()

        else:
            pass

    def delete_job(self):
        self.event.cancel()
