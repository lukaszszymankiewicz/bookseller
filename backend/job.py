import threading
from typing import Callable, List

from kivy.clock import Clock

from .enums import JobStatus


class Job:
    """
    Container for function run in secondary thread (so running function in Job won`t stop main
    thread). Exceptions are catched, so even if function failed information are passed along.
    """

    def __init__(self, fun: Callable, args: dict):
        """
        Initialize Job. Last step od initialization is starting inside function to run (so there
        isn`t way to put Job to run later).

        Args:
            fun - Python function to be run in Job,
            args - arguments for function.

        """
        self.fun = fun
        self.name = fun.__name__
        self.args = args
        self.result = None

        self.thread = None
        self.status = JobStatus.WIP

        self._run_job()

    def _run_job(self) -> None:
        """Creates separate thread and run function inside that thread."""

        self.thread = threading.Thread(target=self._run_fun)
        self.thread.start()

    def _run_fun(self):
        """
        Directly run function and catch its result (even if failed). Function state after run is
        perserved also.
        """

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

    JobManager has global callback and fallback function - that means that if one of the concuring
    job succeded callback fun is run with its result. But only if ALL Jobs failed global fallback
    function is run (so JobManager is optimistinc in founding result).
    """

    def __init__(self):
        """
        Initialize JobManager. Initialization does nothing more than set empty value to all
        paramters.

        Args:
            self.event - container for kivy Clock event (which will periodically check if Job/Jobs
                are completed),
            self.jobs - list of jobs to be performed,
            self.fallback - function to run if all Jobs failed (raises some Exception),
            self.callback - function to run id any of the Job/Jobs succeded.
        """
        self.event = None
        self.jobs = []
        self.fallback = None
        self.callback = None

    @property
    def n_jobs(self):
        return len(self.jobs)

    def add_concurent_jobs(
        self,
        funs: List[Callable],
        args: dict,
        callback: Callable,
        fallback: Callable = None,
        check_interval: float = 0.1,
    ):
        """
        Sets list of Jobs to be run. Each Jobs function is placed into separate thread (so multiple
        requests are done in parallel).

        Args:
            funs - list of functions to be run in parallel,
            args - arguments for functions (same arguments are used for ALL of functions!),
            callback - callback function to be run if ANY of the function succeded,
            fallback - fallback function to be run if ALL function fails (raises Exception),
            check_interval - float representation of time interval of how often functions state are
                check.
        """
        self.callback = callback
        self.fallback = fallback or do_nothing

        for fun in funs:
            self.jobs.append(Job(fun=fun, args=args))

        self.event = Clock.schedule_interval(self.check, check_interval)

    def check(self, dt: float) -> None:
        """
        Periodically checks if any of the Jobs fun is completed.

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
        """
        Iterates by failed jobs and deletes it from self.jobs list. If there is only one job left
        (and it also failed), fallback function is run.

        As a result list of jobs are refreshed (only such which are still Work In Progress status is
        left).

        Args:
            jobs_to_delte: List of Jobs instances to be deleted.
        """
        if self.n_jobs == len(jobs_to_delete):

            results = {}
            for job in jobs_to_delete:
                results[job.name] = job.result

            self.fallback(results)
            self.kill_all_jobs()

        else:
            self.jobs = [job for job in self.jobs if job not in jobs_to_delete]

    def kill_all_jobs(self):
        """
        Stops/kills all jobs and restart JobManager to state where it can handle another request.
        """
        self.event.cancel()
        self.jobs = []
        self.fallback = None
        self.callback = None
        Clock.unschedule(self.event)


def do_nothing(args):
    """Very important function."""
    pass
