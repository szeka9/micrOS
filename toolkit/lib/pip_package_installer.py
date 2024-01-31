from sys import executable
import os
import subprocess
MYPATH = os.path.dirname(__file__)
USER_DATA_OPT_INST_DONE = os.path.join(MYPATH, '../user_data/.opt_install_done')
INTERPRETER = executable

try:
    from . import TerminalColors
except Exception as e:
    print("Import warning __name__:{}: {}".format(__name__, e))
    import TerminalColors

AVAILABLE_PACKAGES = []

def list_packages():
    global AVAILABLE_PACKAGES
    if len(AVAILABLE_PACKAGES) == 0:
        print("[PIP] load available package list")
        output = subprocess.check_output([INTERPRETER, '-m', 'pip', 'list'])
        AVAILABLE_PACKAGES  = [p.strip().split()[0].strip() for p in output.decode('utf-8').split('\n') if '.' in p]
    return AVAILABLE_PACKAGES


def install_package(name):
    try:
        state = subprocess.check_call([INTERPRETER, '-m', 'pip', 'install', name])
        if state:
            print(f"{TerminalColors.Colors.OK}[PIP] install {name} OK{TerminalColors.Colors.NC}")
        else:
            print(f"{TerminalColors.Colors.WARN}[PIP] install {name} NOK{TerminalColors.Colors.NC}")
    except subprocess.CalledProcessError as e:
        print(f"{TerminalColors.Colors.ERR}[PIP] error: {e}{TerminalColors.Colors.NC}")
        state = False
    return state


def install_optional_dependencies(requirements):
    print("[PIP] micrOS optional dependency installer")

    # SKIP in VENV
    if os.environ.get("VIRTUAL_ENV", None) is not None:
        print("[PIP][DISABLED] IN VENV (developer mode) - please use: magic.bash")
        return True

    # SKIP if it was already done
    if os.path.exists(USER_DATA_OPT_INST_DONE):
        print(f"[PIP] Already (attempted) to install optional dependencies: {USER_DATA_OPT_INST_DONE}")
        return True

    # INSTALL DEPs
    available_packages = list_packages()
    if isinstance(requirements, list):
        for dep in requirements:
            dep_name = dep.split('==')[0] if '==' in dep else dep
            if dep_name not in available_packages:
                install_package(dep)
            else:
                print(f"[PIP] SKIP install {dep} (available)")
        with open(USER_DATA_OPT_INST_DONE, 'w') as f:
            f.write('done')
        return True
    return False


if __name__ == "__main__":
    print(list_packages())
    install_optional_dependencies(['PyQt5'])