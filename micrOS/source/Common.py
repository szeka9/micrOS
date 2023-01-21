"""
Module is responsible for collect the additional
feature definition dedicated to micrOS framework towards LoadModules

socket_stream decorator
- adds an extra msgobj to the wrapped function arg list
- msgobj provides socket msg interface for the open connection

Designed by Marcell Ban aka BxNxM
"""

from SocketServer import SocketServer
from machine import Pin, ADC
from sys import platform
from LogicalPins import physical_pin
try:
    from TaskManager import Task, Manager
except Exception as e:
    print("Import ERROR, TaskManager: {}".format(e))
    Task, Manager = None, None


def socket_stream(func):
    """
    Provide socket message object as [msgobj]
    (SocketServer singleton class)
    """
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs, msgobj=SocketServer().reply_message)
    return wrapper


def transition(from_val, to_val, step_ms, interval_sec):
    """
    Generator for color transitions:
    :param from_val: from value - start from
    :param to_val: to value - target value
    :param step_ms: step to reach to_val - timirq_seq
    :param interval_sec: full interval
    """
    if interval_sec > 0:
        step_cnt = round((interval_sec*1000)/step_ms)
        delta = abs((from_val-to_val)/step_cnt)
        direc = -1 if from_val > to_val else 1
        for cnt in range(0, step_cnt+1):
            yield round(from_val + (cnt * delta) * direc)
    else:
        yield round(to_val)


class SmartADC:
    """
    ADC.ATTN_0DB: 0dB attenuation, gives a maximum input voltage of 1.00v - this is the default configuration
    ADC.ATTN_2_5DB: 2.5dB attenuation, gives a maximum input voltage of approximately 1.34v
    ADC.ATTN_6DB: 6dB attenuation, gives a maximum input voltage of approximately 2.00v
    ADC.ATTN_11DB: 11dB attenuation, gives a maximum input voltage of approximately 3.6v
    """
    OBJS = {}

    def __init__(self, pin):
        self.adc = None
        self.adp_prop = ()
        if not isinstance(pin, int):
            pin = physical_pin(pin)
        if 'esp8266' in platform:
            self.adc = ADC(pin)  # 1V measure range
            self.adp_prop = (1023, 1.0)
        else:
            self.adc = ADC(Pin(pin))
            self.adc.atten(ADC.ATTN_11DB)  # 3.3V measure range
            self.adp_prop = (4095, 3.6)

    def get(self):
        raw = self.adc.read()
        percent = raw / self.adp_prop[0]
        volt = round(percent * self.adp_prop[1], 1)
        return {'raw': raw, 'percent': round(percent*100, 1), 'volt': volt}

    @staticmethod
    def get_singleton(pin):
        if pin in SmartADC.OBJS.keys():
            return SmartADC.OBJS[pin]
        SmartADC.OBJS[pin] = SmartADC(pin)
        return SmartADC.OBJS[pin]


def micro_task(tag, task=None):
    """
    Async task creation from Load Modules
    - Indirect interface
    tag:
        [1] tag=None: return task generator object
        [2] tag=taskID: return existing task object by tag
    task: coroutine to execute (built in overload protection and lcm)
    """
    # [0] Check dependencies
    if Task is None or Manager is None:
        # RETURN: None - cannot utilize async task functionality
        return None
    if task is None:
        # [1] Task is None -> Get task mode by tag
        # RETURN task obj (access obj.out + obj.done (automatic - with keyword arg))
        async_task = Task.TASKS.get(tag, None)
        return async_task
    elif Task.task_is_busy(tag):
        # [2] Shortcut: Check task state by tag
        # RETURN: None - if task is already running
        return None
    else:
        # [3] Create task (not running) + task coroutine was provided
        # RETURN task creation state - success (True) / fail (False)
        state = Manager().create_task(callback=task, tag=tag)
        return state
