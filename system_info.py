
import psutil
import pytest
import json


def get_CPU_usage(number_of_seconds: int)-> float:
    return psutil.cpu_percent(5)

def get_virtual_memory_space() -> (float, float):
    memory_details = psutil.swap_memory()
    return memory_details.percent, memory_details.free

def get_top_running_process(process_count: int, time_of_seconds: int) -> [str]:
    array = []
    process_array = sorted(psutil.process_iter(), key = lambda pro: pro.cpu_percent(time_of_seconds))
    start = len(process_array) - process_count - 1
    top_cpu_process_array = process_array[start:]
    print(top_cpu_process_array)

def gather_all_information(performance_test_time: int):

    information = {
        "CPU_USAGE": get_CPU_usage(performance_test_time),
        "VIRTUAL_MEMORY_SPACE": get_virtual_memory_space(),
        "TOP_CPU_USAGES": get_top_running_process(performance_test_time),
    }

    return json.dumps(information)


@pytest.mark.parametrize("performance_test_time",[(0.2), (0.4)]) 
def test_performnace(performance_test_time: float):
    precent = get_CPU_usage(performance_test_time)
    assert precent < 60