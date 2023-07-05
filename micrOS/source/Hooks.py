"""
This module loads before Network setup!

Module is responsible for collect the additional
feature definition dedicated to micrOS framework.

Boot phase execution based on config
- initialize / preload modules to memory

Profiling info
- free memory monitoring between seperated phases
- memory block usage

Designed by Marcell Ban aka BxNxM
"""

#################################################################
#                           IMPORTS                             #
#################################################################
from LogicalPins import detect_platform
from ConfigHandler import cfgget
from Debug import console_write
from TaskManager import exec_lm_pipe
from micropython import mem_info
from machine import freq

#################################################################
#                          FUNCTIONS                            #
#################################################################


def software_migration():
    # TODO: remove
    print("[MIG?] boot.py -> main.py")
    from os import listdir, remove
    if "boot.py" in listdir() and "main.py" in listdir():
        print("|- delete boot.py")
        remove("boot.py")


def bootup_hook():
    """
    Executes when system boots up.
    """
    # Execute LMs from boothook config parameter
    console_write("[BOOTHOOK] EXECUTION ...")
    bootasks = cfgget('boothook')
    if bootasks is not None and bootasks.lower() != 'n/a':
        console_write(f"|-[BOOTHOOK] TASKS: {bootasks}")
        if exec_lm_pipe(bootasks):
            console_write("|-[BOOTHOOK] DONE")
        else:
            console_write("|-[BOOTHOOK] ERROR")

    # Set boostmd (boost mode)
    if cfgget('boostmd') is True:
        console_write(f"[BOOT HOOKS] Set up CPU high Hz - boostmd: {cfgget('boostmd')}")
        if 'esp32' in detect_platform():
            freq(240_000_000)   # 240 Mhz
    else:
        console_write(f"[BOOT HOOKS] Set up CPU low Hz - boostmd: {cfgget('boostmd')}")
        if 'esp32' in detect_platform():
            freq(160_000_000)   # 160 Mhz

    # Scripts for file structure / config changes
    software_migration()


def profiling_info(label=""):
    """
    Runtime memory measurements
    """
    if cfgget('dbg'):
        console_write(f"{'~'*5} [PROFILING INFO] - {label} {'~'*5}")
        mem_info()
        console_write("~"*30)
