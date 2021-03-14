import threading
from typing import Callable, Tuple

from .enums import JobStatus


class Job:
    def __init__(self, fun: Callable, args: Tuple):
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
        self.result = self.fun(self.args)
        self.status = JobStatus.DONE
