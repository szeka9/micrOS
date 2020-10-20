import sys
import os
import threading
import time
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QApplication, QPlainTextEdit
MYPATH = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(MYPATH, 'MicrOSDevEnv'))
import MicrOSDevEnv
import socketClient
sys.path.append(os.path.dirname(os.path.dirname(MYPATH)))
import devToolKit

DUMMY_EXEC = False


class App(QWidget):
    # HEX COLOR: https://www.hexcolortool.com/C0BBFE#1f0000
    TEXTCOLOR = "#1f0000"

    def __init__(self):
        super().__init__()
        self.title = 'micrOS devToolKit GUI dashboard'
        self.left = 10
        self.top = 10
        self.width = 700
        self.height = 400
        self.buttons_list = []
        self.pbar = None
        self.pbar_status = 0
        self.dropdown_objects_list = {}
        self.ui_state_machine = {'force': False}
        self.console = None
        self.device_conn_struct = []
        self.micropython_bin_pathes = []
        self.devtool_obj = MicrOSDevEnv.MicrOSDevTool(cmdgui=False, dummy_exec=DUMMY_EXEC)
        # Init UI elements
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setFixedWidth(self.width)
        self.setFixedHeight(self.height)
        self.setStyleSheet("background-color: grey; color: {};".format(App.TEXTCOLOR))
        self.venv_indicator()
        self.main_ui()

    def main_ui(self):
        self.__create_console()
        self.devtool_obj = MicrOSDevEnv.MicrOSDevTool(cmdgui=False, gui_console=self.console.append_output, dummy_exec=DUMMY_EXEC)

        self.progressbar()
        self.draw_logo()
        self.buttons()
        self.dropdown_board()
        self.dropdown_micropythonbin()
        self.dropdown_device()
        self.force_mode_radiobutton()

    def __create_console(self):
        dropdown_label = QLabel(self)
        dropdown_label.setText("Console".upper())
        dropdown_label.setStyleSheet("background-color : darkGray; color: {};".format(App.TEXTCOLOR))
        dropdown_label.setGeometry(250, 117, 420, 15)
        self.console = MyConsole(self)

    def __detect_virtualenv(self):
        def get_base_prefix_compat():
            """Get base/real prefix, or sys.prefix if there is none."""
            return getattr(sys, "base_prefix", None) or getattr(sys, "real_prefix", None) or sys.prefix

        def in_virtualenv():
            return get_base_prefix_compat() != sys.prefix
        return in_virtualenv()

    def venv_indicator(self):
        if self.__detect_virtualenv():
            label = QLabel(' [devEnv] virtualenv active', self)
            label.setGeometry(20, 5, self.width-50, 20)
            label.setStyleSheet("background-color : green; color: {};".format(App.TEXTCOLOR))
        else:
            label = QLabel(' [devEnv] virtualenv inactive', self)
            label.setGeometry(20, 5, self.width-50, 20)
            label.setStyleSheet("background-color : yellow; color: {};".format(App.TEXTCOLOR))
            label.setToolTip("Please create your dependency environment:\nvirtualenv -p python3 venv\
            \nsource venv/bin/activate\npip install -r micrOS/tools/requirements.txt")

    def buttons(self):
        height = 35
        width = 200
        yoffset = 3
        buttons = {'Deploy (USB)': ['Install "empty" device.\nDeploy micropython and micrOS Framework',
                                       20, 115, width, height, self.__on_click_usb_deploy, 'darkCyan'],
                   'Update (OTA)': ['OTA - Over The Air (wifi) update.\nUpload micrOS resources over webrepl',
                                  20, 115 + height + yoffset, width, height, self.__on_click_ota_update, 'darkCyan'],
                   'Update (USB)': ['Update micrOS over USB\nIt will redeploy micropython as well) ',
                                       20, 115 + (height+yoffset) * 2, width, height, self.__on_click_usb_update, 'darkCyan'],
                   'Search device': ['Search online micrOS devices\nOn local wifi network.',
                                      20, 115 + (height + yoffset) * 3, width, height, self.__on_click_serach_devices, 'darkCyan'],
                   'Simulator': ['Start micrOS on host.\nRuns with micropython dummy (module) interfaces',
                                      20, 115 + (height + yoffset) * 4, width, height, self.__on_click_simulator, 'darkCyan']
                   }

        for key, data_struct in buttons.items():
            tool_tip = data_struct[0]
            x = data_struct[1]
            y = data_struct[2]
            w = data_struct[3]
            h = data_struct[4]
            event_cbf = data_struct[5]
            bg = data_struct[6]

            button = QPushButton(key, self)
            button.setToolTip(tool_tip)
            button.setGeometry(x, y, w, h)
            button.setStyleSheet("QPushButton"
                                 "{"
                                 "background-color : darkCyan;"
                                 "}"
                                 "QPushButton::pressed"
                                 "{"
                                 "background-color : darkGreen;"
                                 "}")


            #"background-color: {}; border: 2px solid black;".format(bg))
            button.clicked.connect(event_cbf)

    @pyqtSlot()
    def __on_click_usb_deploy(self):
        print('__on_click_usb_deploy')
        self.console.append_output('__on_click_usb_deploy')
        self.progressbar_update()

        self.devtool_obj.selected_device_type = self.ui_state_machine['board']
        self.devtool_obj.selected_micropython_bin = self.ui_state_machine['micropython']
        self.devenv_usb_deployment_is_active = True
        # Create a Thread with a function without any arguments
        self.devtool_obj.deploy_micros(restore=False)

    @pyqtSlot()
    def __on_click_ota_update(self):
        print('__on_click_ota_update')
        self.console.append_output('__on_click_ota_update')
        self.progressbar_update()

        fuid = self.ui_state_machine['device']
        force = self.ui_state_machine['force']
        devip = None
        for conn_data in self.device_conn_struct:
            if fuid == conn_data[0]:
                devip = conn_data[1]
        if devip is None:
            self.console.append_output("[ERROR] Selecting device")
        self.console.append_output("Start OTA update on {}:{}".format(fuid, devip))
        self.devtool_obj.update_with_webrepl(device=(fuid, devip), force=force)

    @pyqtSlot()
    def __on_click_usb_update(self):
        print('__on_click_usb_update')
        self.console.append_output('__on_click_usb_update')
        self.progressbar_update()

        self.devtool_obj.selected_device_type = self.ui_state_machine['board']
        self.devtool_obj.selected_micropython_bin = self.ui_state_machine['micropython']
        self.devenv_usb_deployment_is_active = True
        self.devtool_obj.update_micros_via_usb(force=False)

    @pyqtSlot()
    def __on_click_serach_devices(self):
        self.console.append_output('[Search] Search devices')
        # Create a Thread with a function without any arguments
        th = threading.Thread(target=socketClient.ConnectionData().filter_MicrOS_devices, daemon=True)
        th.start()
        self.progressbar_update()

    @pyqtSlot()
    def __on_click_simulator(self):
        self.console.append_output('[Simulator] Start')
        self.progressbar_update()
        th = threading.Thread(target=devToolKit.simulate_micrOS, daemon=True)
        th.start()
        self.console.append_output('[Simulator] Started successfully')
        self.progressbar_update()

    def draw_logo(self):
        label = QLabel(self)
        label.setGeometry(20, 30, 80, 80)
        label.setScaledContents(True)
        logo_path = os.path.join(MYPATH, '../media/logo_mini.png')
        pixmap = QPixmap(logo_path)
        label.setPixmap(pixmap)
        label.setToolTip("micrOS: https://github.com/BxNxM/micrOS")

    def progressbar(self):
        # creating progress bar
        self.pbar = QProgressBar(self)

        # setting its geometry
        self.pbar.setGeometry(20, self.height-40, self.width-70, 30)

    def progressbar_update(self, value=None, reset=False):
        if reset:
            self.pbar_status = 0
        if value is not None and 0 <= value <= 100:
            self.pbar_status = value
        self.pbar_status = self.pbar_status + 1 if self.pbar_status < 100 else 0
        self.pbar.setValue(self.pbar_status)
        print(self.pbar_status)

    def draw(self):
        self.show()

    def dropdown_board(self):
        dropdown_label = QLabel(self)
        dropdown_label.setText("Select board".upper())
        dropdown_label.setGeometry(120, 30, 160, 30)

        # creating a combo box widget
        combo_box = QComboBox(self)

        # setting geometry of combo box
        combo_box.setGeometry(120, 60, 160, 30)

        # GET DEVICE TYPES
        geek_list = self.devtool_obj.dev_types_and_cmds.keys()
        self.ui_state_machine['board'] = list(geek_list)[0]

        # making it editable
        combo_box.setEditable(False)

        # adding list of items to combo box
        combo_box.addItems(geek_list)

        combo_box.setStyleSheet("QComboBox"
                                     "{"
                                     "border : 3px solid purple;"
                                     "}"
                                     "QComboBox::on"
                                     "{"
                                     "border : 4px solid;"
                                     "border-color : orange orange orange orange;"
                                
                                     "}")

        # getting view part of combo box
        view = combo_box.view()

        # making view box hidden
        view.setHidden(False)

        self.dropdown_objects_list['board'] = combo_box
        combo_box.activated.connect(self.__on_click_board_dropdown)

    def dropdown_micropythonbin(self):
        dropdown_label = QLabel(self)
        dropdown_label.setText("Select micropython".upper())
        dropdown_label.setGeometry(290, 30, 200, 30)

        # creating a combo box widget
        combo_box = QComboBox(self)

        # setting geometry of combo box
        combo_box.setGeometry(290, 60, 200, 30)

        # GET MICROPYTHON BINARIES
        geek_list = self.devtool_obj.get_micropython_binaries()
        self.micropython_bin_pathes = geek_list
        geek_list = [os.path.basename(path) for path in geek_list]
        self.ui_state_machine['micropython'] = geek_list[0]

        # making it editable
        combo_box.setEditable(False)

        # adding list of items to combo box
        combo_box.addItems(geek_list)

        combo_box.setStyleSheet("QComboBox"
                                "{"
                                "border : 3px solid green;"
                                "}"
                                "QComboBox::on"
                                "{"
                                "border : 4px solid;"
                                "border-color : orange orange orange orange;"

                                "}")

        # getting view part of combo box
        view = combo_box.view()

        # making view box hidden
        view.setHidden(False)

        self.dropdown_objects_list['micropython'] = combo_box
        combo_box.activated.connect(self.__on_click_micropython_dropdown)

    def dropdown_device(self):
        dropdown_label = QLabel(self)
        dropdown_label.setText("Select device".upper())
        dropdown_label.setGeometry(500, 35, 170, 20)

        # creating a combo box widget
        combo_box = QComboBox(self)

        # setting geometry of combo box
        combo_box.setGeometry(500, 60, 170, 30)

        # Get stored devices
        conn_data = socketClient.ConnectionData()
        conn_data.read_MicrOS_device_cache()
        self.device_conn_struct = []
        for uid in conn_data.MICROS_DEV_IP_DICT.keys():
            devip = conn_data.MICROS_DEV_IP_DICT[uid][0]
            fuid = conn_data.MICROS_DEV_IP_DICT[uid][2]
            tmp = (fuid, devip, uid)
            self.device_conn_struct.append(tmp)
            print("\t{}".format(tmp))

        # Get devices friendly unique identifier
        geek_list = [fuid[0] for fuid in self.device_conn_struct]
        self.ui_state_machine['device'] = geek_list[0]

        # making it editable
        combo_box.setEditable(False)

        # adding list of items to combo box
        combo_box.addItems(geek_list)

        combo_box.setStyleSheet("QComboBox"
                                "{"
                                "border : 3px solid blue;"
                                "}"
                                "QComboBox::on"
                                "{"
                                "border : 4px solid;"
                                "border-color : orange orange orange orange;"

                                "}")

        # getting view part of combo box
        view = combo_box.view()

        # making view box hidden
        view.setHidden(False)

        self.dropdown_objects_list['device'] = combo_box
        combo_box.activated.connect(self.__on_click_device_dropdown)

    def get_widget_values(self):
        self.__show_gui_state_on_console()
        return self.ui_state_machine

    def __on_click_board_dropdown(self, index):
        self.ui_state_machine['board'] = self.dropdown_objects_list['board'].itemText(index)
        self.get_widget_values()

    def __on_click_micropython_dropdown(self, index):
        micropython = self.dropdown_objects_list['micropython'].itemText(index)
        #self.ui_state_machine['micropython'] = micropython
        print(self.micropython_bin_pathes)
        self.ui_state_machine['micropython'] = [path for path in self.micropython_bin_pathes if micropython in path][0]
        self.get_widget_values()

    def __on_click_device_dropdown(self, index):
        self.ui_state_machine['device'] = self.dropdown_objects_list['device'].itemText(index)
        self.get_widget_values()

    def __show_gui_state_on_console(self):
        self.console.append_output("micrOS GUI Info")
        for key, value in self.ui_state_machine.items():
            self.console.append_output("  {}: {}".format(key, value))

    def force_mode_radiobutton(self):
        rbtn1 = QRadioButton('Force mode', self)
        rbtn1.move(20, self.height-60)
        rbtn1.toggled.connect(self.__on_click_force_mode)

    @pyqtSlot()
    def __on_click_force_mode(self):
        radioBtn = self.sender()
        if radioBtn.isChecked():
            self.ui_state_machine['force'] = True
        else:
            self.ui_state_machine['force'] = False
        self.__show_gui_state_on_console()


class MyConsole(QPlainTextEdit):
    console = None

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setReadOnly(True)
        self.setMaximumBlockCount(20000)  # limit console to 20000 lines
        self._cursor_output = self.textCursor()
        self.setGeometry(250, 132, 420, 175)
        MyConsole.console = self

    @pyqtSlot(str)
    def append_output(self, text, end='\n'):
        self._cursor_output.insertText("{}{}".format(text, end))
        self.scroll_to_last_line()

    def scroll_to_last_line(self):
        cursor = self.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.movePosition(QTextCursor.Up if cursor.atBlockStart() else
                            QTextCursor.StartOfLine)
        self.setTextCursor(cursor)


def main():
    app = QApplication(sys.argv)
    ex = App()
    ex.draw()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
