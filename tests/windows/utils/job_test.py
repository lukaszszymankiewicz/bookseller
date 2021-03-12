from time import sleep
from typing import List

from windows.utils.enums import JobStatus
from windows.utils.job import Job


def test_job_runs_function_and_sets_done_flag():
    # GIVEN
    def mock_sum_function(numbers: List[int]):
        return sum(numbers)

    args = [2, 3]
    expected_results = sum(args)

    # WHEN
    sum_job = Job(mock_sum_function, args)

    # make sure that job is done
    sleep(1.0)

    # THEN
    assert sum_job.result == expected_results
    assert sum_job.status == JobStatus.DONE
