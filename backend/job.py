import threading
from typing import Callable, List

from kivy.clock import Clock

from .enums import JobStatus


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
        self.name = fun.__name__

    def _run_job(self):
        self.thread = threading.Thread(target=self._run_fun)
        self.thread.start()

    def _run_fun(self):
        try:
            self.result = self.fun(**self.args)
            self.status = JobStatus.DONE

        except Exception as err:
            self.status = JobStatus.FAILED
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
        self.event = None
        self.jobs = []
        self.fallback = None
        self.callback = None

    def add_concurent_jobs(
        self,
        funs: List[Callable],
        args: dict,
        callback: Callable,
        fallback: Callable = None,
        check_interval: float = 0.1,
    ):
        self.callback = callback
        self.fallback = fallback or do_nothing

        for fun in funs:
            self.jobs.append(Job(fun=fun, args=args))

        self.event = Clock.schedule_interval(self.check, check_interval)

    @property
    def n_jobs(self):
        return len(self.jobs)

    def check(self, dt: float) -> None:
        """Periodically checks if any of the Jobs fun is completed.

        JobManager will run all of functions in search of this one which return proper results.
        If all Jobs failed fallback function will be runned.

        Args:
            dt - float representing check time interval.
        """
        jobs_to_delete = []

        for job in self.jobs:
            if job.status == JobStatus.DONE:
                self.callback(job.result)
                self.kill_all_jobs()
                break

            elif job.status == JobStatus.FAILED:
                jobs_to_delete.append(job)

            else:
                # Work in Progress
                pass

        if jobs_to_delete:
            self.cleanup(jobs_to_delete)

    def cleanup(self, jobs_to_delete: List[Job]) -> None:
        if self.n_jobs == len(jobs_to_delete):

            results = {}
            for job in jobs_to_delete:
                results[job.name] = job.result

            self.fallback(results)
            self.kill_all_jobs()

        else:
            self.jobs = [job for job in self.jobs if job not in jobs_to_delete]

    def kill_all_jobs(self):
        self.event.cancel()
        self.jobs = []
        self.fallback = None
        self.callback = None
        Clock.unschedule(self.event)


def do_nothing(args):
    pass
