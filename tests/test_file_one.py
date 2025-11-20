import time
import random

import pytest

@pytest.mark.parametrize("seconds_to_sleep", [
    (1),
    (2),
    (3),
    (4),
    (5),
    (6),
    (7),
    (8),
    (9),
    (10),
    (11),
    (12),
    (13),
    (14),
    (15)
])
@pytest.mark.xdist
def test_run_loop_long(seconds_to_sleep: int):
    print("Starting test_run_loop")
    time.sleep(random.choice(range(seconds_to_sleep)))
    print("Finished test_run_loop")
    assert True

@pytest.mark.parametrize("seconds_to_sleep", [
    (5),
    (5),
    (5),
    (5),
    (5),
    (5),
    (5),
    (5),
    (5),
    (5),
])
@pytest.mark.xdist
def test_run_loop_short(seconds_to_sleep: int):
    print("Starting test_run_loop_short")
    time.sleep(random.choice(range(seconds_to_sleep)))
    print("Finished test_run_loop_short")
    assert True

@pytest.mark.xdist
def test_run_single():
    print("Starting test_run_single")
    time.sleep(random.choice(range(30)))
    print("Finished test_run_single")
    assert True

