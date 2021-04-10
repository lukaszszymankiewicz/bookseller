from time import sleep

from app.windows.utils.job import Job, JobManager, JobStatus


def test_job_runs_function_and_sets_done_flag():
    # GIVEN
    def mock_sum_function(a: int, b: int):
        return a + b

    args = {"a": 2, "b": 3}
    expected_results = sum(list(args.values()))  # I`m to lazy to set it simply to 5 XD

    # WHEN
    sum_job = Job(mock_sum_function, args)

    # THEN
    # make sure that job is done
    sleep(1.0)

    assert sum_job.result == expected_results
    assert sum_job.status == JobStatus.DONE


def test_job_runs_function_and_properly_catch_exception():
    # GIVEN
    expected_results_args = ("division by zero",)
    expected_results_class_name = "ZeroDivisionError"

    def mock_divide_function(a: int, b: int):
        return a / b

    args = {"a": 2, "b": 0}

    # WHEN
    failing_job = Job(mock_divide_function, args)

    # make sure that job is done
    sleep(1.0)

    # THEN
    assert failing_job.result.args == expected_results_args
    assert failing_job.result.__class__.__name__ == expected_results_class_name
    assert failing_job.thread.is_alive() is False


def test_job_runs_function_and_have_wip_status_while_running():
    # GIVEN
    def mock_sum_function(a: int, b: int):
        sleep(1.0)
        return a + b

    args = {"a": 2, "b": 3}

    # WHEN
    sum_job = Job(mock_sum_function, args)

    # THEN
    # still running
    assert sum_job.status == JobStatus.WIP

    # should be done
    sleep(1.1)
    assert sum_job.status == JobStatus.DONE


def test_job_manager_callback_properly():
    # GIVEN
    expected_result = 5
    manager = JobManager()

    def mock_sum_function(a: int, b: int) -> int:
        return a + b

    def callback_fun(args):
        globals()["test_result"] = args

    # WHEN
    manager.add_job(
        fun=mock_sum_function,
        args={"a": 2, "b": 3},
        callback=callback_fun,
    )

    # THEN
    sleep(0.1)
    manager.check(0.1)  # is there is ann issue in tests that Clock class isn`t working propelry?

    assert globals()["test_result"] == expected_result
    assert manager.job is None


def test_job_manager_fallback_properly():
    # GIVEN
    expected_result = 5
    manager = JobManager()
    expected_result = "ZeroDivisionError"

    def mock_divide_function(a: int, b: int) -> int:
        return a / b

    def callback_fun(args):
        globals()["test_result"] = args

    def fallback_fun(exception):
        globals()["test_result"] = exception.__class__.__name__

    # WHEN
    manager.add_job(
        fun=mock_divide_function,
        args={"a": 2, "b": 0},
        callback=callback_fun,
        fallback=fallback_fun,
    )

    # THEN
    sleep(0.1)
    manager.check(0.1)  # is there is ann issue in tests that Clock class isn`t working propelry?

    assert globals()["test_result"] == expected_result
    assert manager.job is None
