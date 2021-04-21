from time import sleep

from backend.enums import JobStatus
from backend.job import Job, JobManager


def test_job_runs_function_and_sets_done_flag():
    # GIVEN
    expected_results = 5
    args = {"a": 2, "b": 3}

    def mock_sum_function(a: int, b: int):
        return a + b

    # WHEN
    sum_job = Job(mock_sum_function, args)

    # THEN
    # make sure that job is done
    sleep(1.0)

    assert sum_job.result == expected_results
    assert sum_job.status == JobStatus.DONE


def test_job_runs_function_and_properly_catch_exception():
    # GIVEN
    expected_results = "division by zero"
    args = {"a": 2, "b": 0}

    def mock_divide_function(a: int, b: int):
        return a / b

    # WHEN
    failing_job = Job(mock_divide_function, args)

    # make sure that job is done
    sleep(1.0)

    # THEN
    assert failing_job.result == expected_results
    assert failing_job.thread.is_alive() is False


def test_job_runs_function_and_have_wip_status_while_running():
    # GIVEN
    args = {"a": 2, "b": 3}

    def mock_sum_function(a: int, b: int):
        sleep(1.0)
        return a + b

    # WHEN
    sum_job = Job(mock_sum_function, args)

    # THEN
    # still running
    assert sum_job.status == JobStatus.WIP

    # should be done
    sleep(1.1)
    assert sum_job.status == JobStatus.DONE


def test_job_manager_for_single_job_callback_properly():
    # GIVEN
    expected_result = 5
    args = {"a": 2, "b": 3}
    manager = JobManager()

    def mock_sum_function(a: int, b: int) -> int:
        return a + b

    def callback_fun(args):
        globals()["place_result_here"] = args

    # WHEN
    manager.add_concurent_jobs(
        funs=[mock_sum_function],
        args=args,
        callback=callback_fun,
    )

    # THEN
    sleep(0.1)
    manager.check(0.1)  # is there is ann issue in tests that Clock class isn`t working propelry?

    assert globals()["place_result_here"] == expected_result

    # cleanup
    del globals()["place_result_here"]


def test_job_manager_for_two_jobs_runs_faster_function_callback_properly():
    # GIVEN
    expected_result = 5
    wrong_result = 0
    args = {"a": 2, "b": 3}
    manager = JobManager()

    def faster_function(a: int, b: int) -> int:
        return a + b

    def slower_function(a: int, b: int) -> int:
        sleep(0.2)
        return 0

    def callback_fun(args):
        globals()["place_result_here"] = args

    # WHEN
    manager.add_concurent_jobs(
        funs=[faster_function, slower_function],
        args=args,
        callback=callback_fun,
    )

    # THEN
    sleep(0.1)
    manager.check(0.1)

    assert globals()["place_result_here"] == expected_result
    assert globals()["place_result_here"] != wrong_result

    # cleanup
    del globals()["place_result_here"]


def test_job_manager_fallbacks_properly_for_single_function_and_defined_fallback():
    # GIVEN
    expected_result = 5
    args = {"a": 2, "b": 0}
    manager = JobManager()
    expected_result = {"mock_divide_function": "division by zero"}

    def mock_divide_function(a: int, b: int) -> int:
        return a / b

    def callback_fun(args):
        globals()["place_result_here"] = args

    def fallback_fun(message: str):
        globals()["place_result_here"] = message

    # WHEN
    manager.add_concurent_jobs(
        funs=[mock_divide_function],
        args=args,
        callback=callback_fun,
        fallback=fallback_fun,
    )

    # THEN
    sleep(0.1)
    manager.check(0.1)

    assert globals()["place_result_here"] == expected_result

    # cleanup
    del globals()["place_result_here"]


def test_job_manager_fallbacks_properly_for_two_function_and_defined_fallback():
    # GIVEN
    args = {"a": 2, "b": 0}
    expected_result = {
        "mock_divide_function": "division by zero",
        "mock_wrong_subsctriptable_function": "'int' object is not subscriptable",
    }
    manager = JobManager()

    def mock_divide_function(a: int, b: int) -> int:
        return a / b

    def mock_wrong_subsctriptable_function(a: int, b: int) -> int:
        return a[b]

    def callback_fun(args):
        globals()["place_result_here"] = args

    def fallback_fun(message: str):
        globals()["place_result_here"] = message

    # WHEN
    manager.add_concurent_jobs(
        funs=[mock_divide_function, mock_wrong_subsctriptable_function],
        args=args,
        callback=callback_fun,
        fallback=fallback_fun,
    )

    # THEN
    sleep(0.1)
    manager.check(0.1)

    assert globals()["place_result_here"] == expected_result

    # cleanup
    del globals()["place_result_here"]


def test_job_manager_fallbacks_properly_for_two_function_and_no_defined_fallback():
    # GIVEN
    args = {"a": 2, "b": 0}
    manager = JobManager()

    def mock_divide_function(a: int, b: int) -> int:
        return a / b

    def mock_wrong_subsctriptable_function(a: int, b: int) -> int:
        return a[b]

    def callback_fun(args):
        globals()["place_result_here"] = args

    # WHEN
    manager.add_concurent_jobs(
        funs=[mock_divide_function, mock_wrong_subsctriptable_function],
        args=args,
        callback=callback_fun,
    )

    # THEN
    sleep(0.1)
    manager.check(0.1)
    assert not globals().get("place_result_here")

    # cleanup (just in case)
    try:
        del globals()["place_result_here"]
    except KeyError:
        pass


def test_job_manager_callback_properly_even_if_proper_function_is_slowest():
    # GIVEN
    args = {"a": 2, "b": 0}
    expected_result = 2
    manager = JobManager()

    def function_that_will_success(a: int, b: int) -> int:
        sleep(0.2)
        return a + b

    def mock_divide_function(a: int, b: int) -> int:
        return a / b

    def mock_wrong_subsctriptable_function(a: int, b: int) -> int:
        return a[b]

    def fallback_fun(message: str):
        globals()["place_result_here"] = message

    def callback_fun(args):
        globals()["place_result_here"] = args

    # WHEN
    manager.add_concurent_jobs(
        funs=[mock_divide_function, mock_wrong_subsctriptable_function, function_that_will_success],
        args=args,
        callback=callback_fun,
        fallback=fallback_fun,
        check_interval=0.05,
    )

    # THEN
    sleep(0.1)
    manager.check(0.1)
    # mock_divide_function and mock_wrong_subsctriptable_function will fail
    assert not globals().get("place_result_here")

    sleep(0.3)
    manager.check(0.3)
    # function_that_will_success ends
    assert globals()["place_result_here"] == expected_result

    # cleanup
    del globals()["place_result_here"]


def test_job_manager_cancel_all_jobs_while_done():
    # GIVEN
    args = {"a": 2, "b": 0}
    manager = JobManager()

    def function_that_will_success(a: int, b: int) -> int:
        return a + b

    def fallback_fun(message: str):
        globals()["place_result_here"] = message

    def callback_fun(args):
        globals()["place_result_here"] = args

    # WHEN
    manager.add_concurent_jobs(
        funs=[function_that_will_success],
        args=args,
        callback=callback_fun,
        fallback=fallback_fun,
    )

    # THEN
    sleep(0.3)
    manager.check(0.1)
    manager.check(0.1)
    manager.check(0.1)

    assert manager.jobs == []

    # cleanup
    del globals()["place_result_here"]
