import pytest
from pomodoro import PomodoroTimer

@pytest.fixture
def pomodoro_timer():
    return PomodoroTimer(BASE_PATH="images")

def test_init(pomodoro_timer):
    assert pomodoro_timer.state == "work"
    assert pomodoro_timer.remaining_time == 25 * 60
    assert pomodoro_timer.is_running == False
    assert pomodoro_timer.display_time == True
    assert pomodoro_timer.display_color == False

def test_start_timer(pomodoro_timer):
    pomodoro_timer.start_timer(None)
    assert pomodoro_timer.is_running == True

def test_stop_timer(pomodoro_timer):
    pomodoro_timer.stop_timer(None)
    assert pomodoro_timer.is_running == False