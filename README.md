# ![LOGO](./media/logo_mini.png?raw=true) micrOS

### micropython based smart edge IoT platform

`#telnet #wifi #esp32 #ota #GPIO #RTC/NTP #AP/STA #IRQ #thread #cron`

![MICROSVISUALIZATION](./media/micrOS_welcome.png?raw=true)

📲 💻 Communication over WiFi: Generic communication API <br/>
&nbsp;&nbsp; ✉️ Expose upython module functions - telnet TCP/IP <br/>
⚙️ 📝 Device initialization from user config <br/>
🧩  Codeless end user experience via phone client <br/>
🚪 No external server or service required for client-device communication <br/>
&nbsp;&nbsp; ⚠️ 🛡 Works on Local Network (WiFi-WLAN) <br/>
🛠 Easy to customize, create your own Load Modules: <br/>
&nbsp;&nbsp; 1. Write **LM_**`<your_app>`**.py** <br/>
&nbsp;&nbsp; 2. Copy (OTA/USB) python script to your device (drap&drop)<br/>
&nbsp;&nbsp; 3. Call any function your **`<your_app>`** module <br/>
🦾 Built-in scheduling (IRQs):<br/>
&nbsp;&nbsp; - Time stamp based <br/>
&nbsp;&nbsp; - Geolocation based utc + sunset, sunrise rest features <br/>
&nbsp;&nbsp; - Simple periodic <br/>
&nbsp;&nbsp; - Thread (beta) <br/>

🚀🎈Lightweight and high performance core system that leaves you space 😎

## ◉ Shortcuts:
1. micrOS Client Application [link](https://github.com/BxNxM/micrOS#micrOS-Client-Application)
2. micrOS Installer [link](https://github.com/BxNxM/micrOS/#installing-micros-with-devtoolkit-esp32)
3. micrOS Tutorials [link](https://github.com/BxNxM/micrOS#micros-video-tutorials)
4. micrOS System and features [link](https://github.com/BxNxM/micrOS#micros-system-message-function-visualization)
5. micrOS Node configuration [link](https://github.com/BxNxM/micrOS#micros-node-configuration-parameters-with-description)

Thingiverse 3D print projects: [link](https://www.thingiverse.com/micros_framework/designs)</br>
Youtube: [link](https://www.youtube.com/channel/UChRlJw7OYAoKroC-Mi75joA)</br>
Facebook page: [link](https://www.facebook.com/Micros-Framework-103501302140755/)

----------------------------------------
----------------------------------------

## micrOS Client Application

### AppStore
&nbsp;&nbsp;&nbsp;[![AppStoreURL](./media/store/AppStoreBadge.svg)](https://apps.apple.com/hu/app/micros-client/id1562342296)

### PlayStore
&nbsp;&nbsp;&nbsp;[![PlayStore](./media/store/GooglePlayBadge.png)](https://play.google.com/store/apps/details?id=com.BMT.micrOSClient)

----------------------------------------
----------------------------------------

## Installing micrOS with DevToolKit #ESP32
**From macOS / Windows / Linux to any esp32 boards**

End-to-End solution for deployment, update, monitor and develop micrOS boards.

I would suggest to use micrOS GUI as a primary interface for micrOS development kit, but you can use cli as well if you prefer.

> Note: The main purpose of the USB deployment scripts to install micropython on the board and put all micrOS resources (precompiled) from `micrOs/toolkit/workspace/precompiled` to the board.

<br/>

### 1. Install python3.8

Link for python 3.8 [download](https://www.python.org/downloads/release/python-383/)

> Note: Allow extend system path with that python version (installation parameter) </br>
> On **Windows**: RUN AS ADMINISTARTOR

----------------------------------------

### 2. Install Git

#### 2.1. On macOS:

&nbsp;Open command line, press: `commnd+space` + type: `terminal` + press: `enter`

&nbsp;**`xcode-select --install; git --version`**
	
#### 2.2. On Windows:

&nbsp;Install git: **[download from here](https://git-scm.com/download/win)**

----------------------------------------

### ONLY ON WINDOWNS: Special dependencies

*You will need **C++ compiler** to able to install all python pip dependencies (defined in the tool/requirements.txt and setup.py)*

&nbsp;**[C++ compiler download](https://support.microsoft.com/en-us/topic/the-latest-supported-visual-c-downloads-2647da03-1eea-4433-9aff-95f26a218cc0?fbclid=IwAR3_sC43aIkQ7TaCIyO3LnJAH5YEM22GavxngTS-X08Z2p1rJq12_vrX6FU)**

----------------------------------------

### 3. Install and RUN **devToolKit** GUI

Download and install micrOS devToolKit python package:

> NOTE: There are multiple ways to start python pip install, it depends on your OS and python deployment. </br>
> Select One command from below:

**``` pip install git+https://github.com/BxNxM/micrOS.git```**

OR

```python3 -m pip install git+https://github.com/BxNxM/micrOS.git```

OR

```python -m pip install git+https://github.com/BxNxM/micrOS.git```

then, you can use the following cmdline paramater to start the devToolKit app:

**`devToolKit.py`**

It will open a graphical user interface for micrOS device management, like usb deploy, update, OTA operations, test executions, etc...

![MICROSVISUALIZATION](./media/micrOSToolkit.gif?raw=true)

- Example

```
1. Select BOARD TYPE
2. Select MICROPYTHON VERSION
3. Click on [Deploy (USB)] button
```

It will install your board via USB with default settings. **Continue with micrOS Client app...**

> Note: At the first USB deployment, devToolKit will ask to install **SerialUSB driver** and it will open the driver installer as well, please follow the steps and install the necessary driver.


```
╔╗ ╔╗                  ╔═══╗╔╗ ╔╗╔═╗ ╔╗       ╔═══╗
║║ ║║                  ║╔══╝║║ ║║║║╚╗║║       ╚╗╔╗║
║╚═╝║╔══╗ ╔╗╔╗╔══╗     ║╚══╗║║ ║║║╔╗╚╝║    ╔═╗ ║║║║
║╔═╗║╚ ╗║ ║╚╝║║╔╗║     ║╔══╝║║ ║║║║╚╗║║    ╚═╝ ║║║║
║║ ║║║╚╝╚╗╚╗╔╝║║═╣    ╔╝╚╗  ║╚═╝║║║ ║║║    ╔═╗╔╝╚╝║
╚╝ ╚╝╚═══╝ ╚╝ ╚══╝    ╚══╝  ╚═══╝╚╝ ╚═╝    ╚═╝╚═══╝
```

----------------------------------------
----------------------------------------

## micrOS Video Tutorials

### 1.1 Prepare micrOS devToolKit for deployment [macOS]

[![micrOSAppBasics](./media/thumbnails/install_on_mac.jpg)](https://www.youtube.com/watch?v=heqZMTUAWcg&t)

### 1.2 Prepare micrOS devToolKit for deployment [Windows]

[![micrOSAppBasics](./media/thumbnails/install_on_windows.jpg)](https://www.youtube.com/watch?v=8e_YCjFVZng)

### 2. Basic setup with micrOS Client App

[![micrOSAppBasics](./media/thumbnails/first_configuration.jpg)](https://www.youtube.com/watch?v=xVNwHnBs1Tw)

	
### 3. How to OTA update device
### 4. Widgets and Load Modules via micrOS Client  

How to get available module list
Overview of micrOS Client UI

### 5. Configuration via micrOS Client

Idea behind: network, time, boothook, irqs, cron
Set some stuff in config ...

### 6. Get familier with micrOS shell

micrOS terminal
built-in commands, Load Modules

### 7. How to customize or contribute to micrOS

Create custom Load Modules (LMs)

----------------------------------------

## micrOS System, message-function visualization

![MICROSVISUALIZATION](./media/micrOS.gif?raw=true)

>Note: micrOS development kit contains command line interface for socket communication. Example: `./devToolKit.py --connect`

```
[i]         FUID        IP               UID
[0] Device: __device_on_AP__ - 192.168.4.1 - __devuid__
[1] Device: __simulator__ - 127.0.0.1 - __localhost__
[2] Device: BedLamp - 192.168.1.90 - micrf008d1d2ac30OS
[3] Device: ImpiGamePro - 192.168.1.159 - micr240ac45861c8OS
Choose a device index: 2
Device IP was set: 192.168.1.90
BedLamp $  hello
hello:BedLamp:micrf008d1d2ac30OS
BedLamp $  neopixel neopixel 100 10 10
NEOPIXEL SET TO R100G10B10
BedLamp $  neopixel help
 neopixel r=<0-255> g b smooth=True force=True,
 toggle state=None smooth=True,
 load_n_init ledcnt=24,
 segment r, g, b, s=<0-n>,
 set_transition r=<0-255> g b sec,
 run_transition,
 pinmap,
```


----------------------------------------

## micrOS Framework Features💡

- **micrOS loader** - starts micrOS or WEBREPL(update / recovery modes)
	- **OTA update** - push update over wifi (webrepl automation) / monitor update and auto restart node
- **Config handling(*)** - user config - node_config.json
	- Accessable over socket interface or Phone client
- **[L]oad [M]odule** aka **application** handling
	- Lot of built-in functions
	- Create your own module with 2 easy steps
		- Create a file in `micrOS` folder like: `LM_<your_app_name>.py`
- **Boot phase** handling - preload Load Module(s) - pinout initialization from node_config
- **Network handling** - based on node_config 
	- STA / AP
	- NTP setup
	- Static IP configuration
- **Socket interpreter** - wireless communication interface with the nodes
	- **System commands**: `help, version, reboot, webrepl, etc.`
		- webrepl <--> micrOS interface switch  
	- **Config(*)** SET/GET/DUMP
		- `conf` and `noconf` 
	- **LM** - Load Module function execution (application modules)
- **Scheduling / External events** - Interrupt callback - based on node_config 
	- Time based
		- simple LM task pool execution
			- `Timer(0)` 
		- cron [time stump:LM task] pool execution
			- `Timer(1)` 
	- Event based
		-  Set trigger event up/down/both with LM callback function
- [BETA!] **Background Job** aka **BgJob**
		- Capable of execute [L]oad [M]odules in a background thread
		- WARNING, limitation: not use with IRQs and in micrOS config
		- Invoke with single execution `&` or loop execution `&&`
		- Example:
			- In loop: `system heartbeat &&`
			- Single call: `system heartbeat &`
		- Stop thread: `bgjob stop`
		- Show thread ouput and status: `bgjob show` 
- **[L]ogical [P]inout** handling - lookuptables for each board
	- Predefined pinout modules for esp32, tinyPico
	- Create your pinout based on `LP_esp32.py`, naming convencion: `LP_<name>.py`
	- To activate your custom pinout set `cstmpmap` config parameter to `<name>`


DevToolKit CLI feature:

- Socket client python plugin - interactive - non interactive mode

## Built in pheriphery support

### Sensors / inputes

![micrOS project Pheriphery Support](./media/microsPheriphery_sensors.png)</br>

### Actuators / outputs

![micrOS project Pheriphery Support](./media/microsPheriphery_actuators.png)</br>

### Power supply

![micrOS project Pheriphery Support](./media/microsPheriphery_power.png)</br>

----------------------------------------

## Device Pinouts for wiring

### Logical pin association handling

[micrOS/source/LogicalPins.py](./micrOS/source/LogicalPins.py)

LogicalPin lookup tables:

- [tinypico](./micrOS/source/LP_tinypico.py)
- [esp32](./micrOS/source/LP_esp32.py)

> Note: Good idea to use costant variable for pin map declaration, check the files for more info, These files are also precompiled automatically into byte steams -> `.mpy`

![MicrOStinyPicopinout](./media/NodeMCUPinOutTinyPico.png?raw=true)

GENERAL CONTROLLER CONCEPT: [microPLC](./media/microPLC.png)


![MicrOSESP23pinout](./media/NodeMCUPinOutESP32.png?raw=true)


----------------------------------------

# System Architecture 

![MICROSARCHITECTURE](./media/MicrOSArchitecture.png?raw=true)

> Secure Core (OTA static modules): `boot.py`, `micrOSloader.mpy`, `Network.mpy`

## Networking - automatic network modes

![MICROSNWMODES](./media/micrOSNetworking.png?raw=true)

### RELESE NOTE

|  VERSION (TAG) |    RELEASE INFO    |  MICROS CORE MEMORY USAGE  |  SUPPORTED DEVICE(S) | APP PROFILES | Load Modules  |     NOTE       |
| :----------: | :----------------: | :------------------------:   |  :-----------------: | :------------: | :------------:| -------------- |
|  **v0.1.0-0** | [release_Info-0.1.0-0](./release_info/micrOS_ReleaseInfo/release_0.1.0-0_note.md)| 13 - 28 % (1216-2544byte) | esp8266 | [App Profiles](./release_info/node_config_profiles) | [LM manual](./release_info/micrOS_ReleaseInfo/release_sfuncman_0.1.0-0.json)| Stable Core with applications - first release
|  **v0.4.0-0** | [release_Info-0.4.0-0](./release_info/micrOS_ReleaseInfo/release_0.4.0-0_note_esp8266.md)| 26 - 53 % (2512-5072byte) | esp8266 | [App Profiles](./release_info/node_config_profiles) | [LM manual](./release_info/micrOS_ReleaseInfo/release_sfuncman_0.4.0-0.json)| micrOS multi device support with finalized core and so more. OTA update feature.
|  **v0.4.0-0** | [release_Info-0.4.0-0](./release_info/micrOS_ReleaseInfo/release_0.4.0-0_note_esp32.md)| 23 - 28 % (17250-20976byte) | esp32 | [App Profiles](./release_info/node_config_profiles) | [LM manual](./release_info/micrOS_ReleaseInfo/release_sfuncman_0.4.0-0.json)| micrOS multi device support with finalized core and advanced task scheduler based on time, and and so more. OTA update feature.
|  **v1.0.0-0** | [release_Info-1.0.0-0](./release_info/micrOS_ReleaseInfo/release_1.0.0-0_note_esp32.md)| 15 - 23 % (10394-15488byte) | esp32 | [App Profiles](./release_info/node_config_profiles) | [LM manual](./release_info/micrOS_ReleaseInfo/release_sfuncman_1.0.0-0.json)| Release of v1 micrOS, timer and event based irqs, cron task scheduling, realtime communication, multiple device support. OTA, etc. 
|  **v1.2.2-0** | [release_Info-1.2.2-0](./release_info/micrOS_ReleaseInfo/release_1.2.2-0_note_esp32.md)|  10-25 % | esp32 | [App Profiles](./release_info/node_config_profiles) | [LM manual](./release_info/micrOS_ReleaseInfo/release_sfuncman_1.2.2-0.json)| Public Release of v1 micrOS, timer and event based irqs, cron task scheduling, realtime communication, multiple device support. OTA update, thread from socket shell (beta) etc.
|  **v light-1.3.0-0** | None |  % | esp8266 | [lightweight branch](https://github.com/BxNxM/micrOS/tree/lightweight)| remove esp8266 due to memory limitation - BUT still supported with limited functionalities on **`lightweight`** branch. Hint: Change branch on github and download zip file, then start micrOSDevToolKit dashboard GUI
|  **v 1.3.0-0** | None |  % | esp32, tinyPico | None | Refactor, IRQ callback scheduling (4 input), thread invocation over socket cli, cron - timed task scheduler, etc... :)



----------------------------------------

## micrOS **node configuration**, parameters with description

|        Config keys   |   Default value and type    | Reboot required |       Description       |
| -------------------- | :-------------------------: | :-------------: | ----------------------- |
| **devfid**           |    `node01`  `<str>`        |       Yes        | Device friendly "unique" name - also used for AccessPoint nw mode (AP name)
| **boostmd**          |      `True`  `<bool>`       |      Yes        | boost mode - set up cpu frequency low or high 8MHz-16Mhz-24MHz (depends on boards)
| **staessid**         |   `your_wifi_name` `<str>`  |       Yes       | Wifi router name (for default connection mode)
| **stapwd**           | `your_wifi_passwd` `<str>`  |       Yes       | Wifi router password (for default connection mode)
| **appwd**            |   `ADmin123`  `<str>`       |       Yes       | Device system password.: Used in AP password (access point mode) + webrepl password
| **auth**             |     `False` `<bool>`        |       Yes       | Enables socket password authentication, password: `appwd`. Passwordless functions: `hello`, `version`, `exit`. **WARNING** OTA upade not supported in this mode.
| **utc**              |     `60`   `<int>`          |       Yes       | NTP-RTC - timezone setup (UTC in minute) - it is automatically calibrated in STA mode based on geolocation.
| **boothook**         |    `n/a` `<str>`            |      Yes        | Callback function(s) list for priority Load Module(s) execution in boot sequence [before network setup!]. Add LoadModule(s) here, separator `;`. Example: Set LED colors / Init custom module(s) / etc.
| **timirq**           |     `False`  `<bool>`       |       Yes       | Timer(0) interrupt enabler - background "subprocess" emulation, timer based infinite loop for the LoadModule execution
| **timirqcbf**        |      `n/a`   `<str>`        |      Yes        | if `timirq` enabled, calls the given Load Module(s), e.x.: `module function optional_parameter(s)`, task separator: `;`
| **timirqseq**        |    `1000`   `<int>`         |      Yes        | Timer interrupt period in ms, default: `3000` ms (for `timirq` infinite loop timer value)
| **cron**             |     `False`  `<bool>`       |       Yes       | Cron enabler, Timer(1) interrupt enabler - time based task scheduler.
| **cronseq**          |    `3000`   `<int>`         |       Yes        | Cron (Timer(1)) interrupt period in ms, default: `3000` ms (for `cron` infinite loop timer value) 
| **crontasks**        |     `n/a`  `<str>`          |       Yes        | Cron scheduler input, task format: `WD:H:M:S!module function` e.g.: `1:8:0:0!system heartbeat`, task separator in case of multiple tasks: `;`. [WD:0-6, H:0-23, M:0-59, S:0-59] in case of each use: `*` **Note**: If the value was `n/a` default, then reboot required.
| **irq1**           |     `False`  `<bool>`       |      Yes        | External event interrupt enabler - Triggers when desired signal state detected - button press happens / motion detection / etc
| **irq1_cbf**        |     `n/a`  `<str>`          |      Yes        | `irq1` enabled, calls the given Load Modules, e.x.: `module function optional_parameter(s)` when external trigger happens
| **irq1_trig**       |     `n/a`   `<str>`         |      Yes        | Sets trigger mode for external irq, signal phase detection, values `up` (default: `n/a`) or `down` or `both`.
| **irq2**           |     `False`  `<bool>`       |      Yes        | External event interrupt enabler - Triggers when desired signal state detected - button press happens / motion detection / etc
| **irq2_cbf**        |     `n/a`  `<str>`          |      Yes        | `irq2` enabled, calls the given Load Modules, e.x.: `module function optional_parameter(s)` when external trigger happens
| **irq2_trig**       |     `n/a`   `<str>`         |      Yes        | Sets trigger mode for external irq, signal phase detection, values `up` (default: `n/a`) or `down` or `both`.
| **irq3**           |     `False`  `<bool>`       |      Yes        | External event interrupt enabler - Triggers when desired signal state detected - button press happens / motion detection / etc
| **irq3_cbf**        |     `n/a`  `<str>`          |      Yes        | `irq3` enabled, calls the given Load Modules, e.x.: `module function optional_parameter(s)` when external trigger happens
| **irq3_trig**       |     `n/a`   `<str>`         |      Yes        | Sets trigger mode for external irq, signal phase detection, values `up` (default: `n/a`) or `down` or `both`.
| **irq4**           |     `False`  `<bool>`       |      Yes        | External event interrupt enabler - Triggers when desired signal state detected - button press happens / motion detection / etc
| **irq4_cbf**        |     `n/a`  `<str>`          |      Yes        | `irq4` enabled, calls the given Load Modules, e.x.: `module function optional_parameter(s)` when external trigger happens
| **irq4_trig**       |     `n/a`   `<str>`         |      Yes        | Sets trigger mode for external irq, signal phase detection, values `up` (default: `n/a`) or `down` or `both`.
| **cstmpmap**         |      `n/a`  `<str>`          |      Yes       | Custom pin mapping for custom function setups. (1) copy your pinmap aka [L]ogical[P]ins (python variables in module) to the board, file format: `LP_<pin_map_name>.py` or `.mpy`, (2) set `<pin_map_name>` as the parameter.
| **dbg**	            |     `True`    `<bool>`      |       Yes       | Debug mode - enable micrOS system printout, server info, etc. + progress LED (heartbeat)
| **soctout**          |   `100`      `<int>`        |      Yes        | Socket server connection timeout (because single process socket interface)
| **socport**          |    `9008`  `<int>`          |      Yes        | Socket server service port (should not be changed due to client and API inconpatibility)
| **irqmreq**          |      `6000`  `<int>`        |       No        | Controlls memory overload avoidance (byte). `timirq` requires this amount of memory for activation. `irqmreq`*0.7 is the memory limit for `extirq` enabling. **WARNING**: If the system gets memory overloaded with irq(s) micropython crashes and stucks in cycling reboot!!!
| **devip**            |      `n/a`  `<str>`         |    Yes(N/A)      | Device IP address, (first stored IP in STA mode will be the device static IP on the network), you are able to provide specific static IP here.
| **nwmd**             |     `n/a`  `<str>`          |      N/A        | Prefered network mode - `AP` or `STA`
| **hwuid**            |      `n/a`  `<str>`         |      N/A        | USED BY SYSTEM (state storage) - hardware address - dev uid
| **guimeta**          |      `n/a`  `str`           |      No        | USED BY micrOS Client (state storage) - stores - offloaded parameter type in config. Clinet widget meta data.

> Note: Default empty value: `n/a` in case of string parameter.
> Note: Cron is only available on devices with Timer(**1**): esp32
> 


----------------------------------------
----------------------------------------


## Developer Quick guide

#### Erase device & Deploy micropython & Install micrOS 

Go to micrOS repo, where the `devToolKit.py` located.

```
cd micrOs 
./devToolKit.py --make
```
> Note: Follow the steps :)


Search and Connect to the device

```
./devToolKit.py -s -c
```

----------------------------------------

**User commands**

```
./devToolKit.py -h

optional arguments:
  -h, --help            show this help message and exit

Base commands:
  -m, --make            Erase & Deploy & Precompile (MicrOS) & Install (MicrOS)
  -r, --update          Update/redeploy connected (usb) MicrOS. - node config will be restored
  -c, --connect         Connect via socketclinet
  -o, --OTA				 OTA update, over wifi (webrepl)
  -p CONNECT_PARAMETERS, --connect_parameters CONNECT_PARAMETERS
                        Parameters for connection in non-interactivve mode.
```

**Search devices**

```
./devToolKit.py --search_devices

or

./devToolKit.py -s
```

**List discovered devices with status updates**

```
./devToolKit.py -stat

or

./devToolKit.py --node_status
```

Output:

```
       [ UID ]                [ FUID ]		[ IP ]		[ STATUS ]	[ VERSION ]	[COMM SEC]
micr123c8456OS            RingLamp          10.0.1.75	ONLINE		1.0.1-0		0.319
micr123456OS            BigRGB            10.0.1.119	ONLINE		1.0.1-0		0.418
micr12345c860OS                CamLed            10.0.1.84	ONLINE		1.0.1-0		0.498
micr12c83456OS                airquality        10.0.1.50	ONLINE		1.0.1-0		0.495
micr5123456OS            tinyPico          10.0.1.189	ONLINE		<n/a>		n/a
micr212345670OS            nodepro           10.0.1.140	OFFLINE		<n/a>		n/a
micrf1234562a0OS            BedLamp           10.0.1.45	ONLINE		1.0.1-0		0.317
micr212345661xOS            CatGamePro       10.0.1.23	ONLINE		1.0.1-0		0.393
```

**Developer commands**

```
Development & Deployment & Connection:
  -e, --erase           Erase device
  -d, --deploy          Deploy micropython
  -i, --install         Install MicrOS on micropython
  -l, --list_devs_n_bins
                        List connected devices & micropython binaries.
  -cc, --cross_compile_micros
                        Cross Compile MicrOS system [py -> mpy]
  -v, --version         Get micrOS version - repo + connected device.
  -ls, --node_ls        List micrOS node filesystem content.
  -u, --connect_via_usb
                        Connect via serial port - usb

Toolkit development:
  --dummy               Skip subshell executions - for API logic test.
```

## Socket terminal example - non interactive

### Identify device

```
./devToolKit.py -c -p '--dev slim01 hello'
Load MicrOS device cache: /Users/bnm/Documents/NodeMcu/MicrOs/tools/device_conn_cache.json
Activate MicrOS device connection address
[i]         FUID        IP               UID
[0] Device: slim01 - 10.0.1.73 - 0x500x20x910x680xc0xf7
Device was found: slim01
hello:slim01:0x500x20x910x680xc0xf7
```

### Get help

```
./devToolKit.py -c -p '--dev node01 help'
Load MicrOS device cache: /Users/bnm/Documents/NodeMcu/MicrOs/tools/device_conn_cache.json
Activate MicrOS device connection address
[i]         FUID        IP               UID
[0] Device: node01 - 10.0.1.73 - 0x500x20x910x680xc0xf7
Device was found: node01
node01 $  help
[MICROS]   - commands (SocketServer built-in)
   hello   - default hello msg - identify device
   version - shows micrOS version
   exit    - exit from shell socket prompt
   reboot  - system safe reboot
   webrepl - start web repl for file transfers - update
[CONF] Configure mode (InterpreterShell built-in):
  conf       - Enter conf mode
    dump       - Dump all data
    key        - Get value
    key value  - Set value
  noconf     - Exit conf mode
[EXEC] Command mode (LMs):
   L298N_DCmotor
                help
   VL53L0X
          measure
          help
   adc
      measure
      action_fltr
      help
   air
      help
   bledns
         advert
         scan
         list
         make
         help
   bme280
         help
   co2
      help
   dht11
        help
   dht22
        help
   dimmer
         help
   distance_HCSR04
                  distance_mm
                  distance_cm
                  deinit
                  help
   esp32
        hall
        temp
        touch
        battery
        help
   i2c
      scan
      help
   intercon
           help
   light_sensor
               help
   motion_sensor
                get_PIR_state
                PIR_deinit
                help
   neopixel
           help
   oled_128x64i2c
                 help
   oled_widgets
               help
   ph_sensor
            measure
            help
   repair
         help
   rgb
      help
   rgbfader
           help
   servo
        help
   switch
         help
   system
         help
   test
       run
       help
   tinyrgb
          help
   tinyrgb
          setrgb
          getstate
          toggle
          wheel
          help
```
 
### Embedded config handler
 
```  
./devToolKit.py -c -p '--dev node01 conf <a> dump'
Load MicrOS device cache: /Users/bnm/Documents/NodeMcu/MicrOs/tools/device_conn_cache.json
Activate MicrOS device connection address
[i]         FUID        IP               UID
[0] Device: node01 - 10.0.1.73 - 0x500x20x910x680xc0xf7
Device was found: node01
[configure] node01
  gmttime   :        1
  irqmreq   :        6000
  pled      :        True
  crontasks :        *:19:2:0!rgbfader fade 0 107 6 120;*:19:4:0!rgbfader fade 0 92 2 120;*:19:6:0!rgbfader fade 128 0 7 120;*:19:8:0!rgbfader fade 107 7 0 120;*:19:10:0!rgbfader fade 0 31 9 120;*:19:12:0!rgbfader fade 310 1 2 120;*:19:14:0!rgbfader fade 11 1 0 120;*:23:0:0!rgbfader fade 0 0 0 3600;*:7:0:0!rgbfader fade 0 107 6 3600
  soctout   :        100
  devip     :        10.0.1.119
  version   :        1.0.1-0
  auth      :        False
  cronseq   :        3000
  guimeta   :        ...
  cron      :        True
  timirqcbf :        rgbfader transition
  devfid    :        BigRGB
  cstmpmap  :        n/a
  boostmd   :        True
  socport   :        9008
  dbg       :        True
  irqmembuf :        1000
  timirqseq :        1000
  extirq    :        False
  staessid  :        <your-wifi-name>; <your-wifi-name2>
  appwd     :        ADmin123
  stapwd    :        <your-wifi-pwd>; <your-wifi-pwd2>
  timirq    :        True
  hwuid     :        micr8caab594d4c4OS
  extirqcbf :        n/a
  nwmd      :        STA
  extirqtrig:        n/a
  boothook  :        rgbfader fader_cache_load_n_init
```

### Load Modules - User defined functions

```
./devToolKit.py -c -p '--dev node01 system info'
Load MicrOS device cache: /Users/bnm/Documents/NodeMcu/MicrOs/tools/device_conn_cache.json
Device was found: node01
CPU clock: 24 [MHz]
MemFree: 25 kB 80 byte
FSFREE: 88 %
Plaform: esp32
```

## SocketClient

### Config:

```json
{
    "<UINIGUE ID - MAC ADDRESS (UID)>": [
        "<MICROS DEVIDE IP (DEVIP)>",
        "<MICROS DEVIDE MAC>",
        "<MICROS FRIENDLY NAME (FUID)>"
    ]
}
```

> NOTE: MUST TO HAVE DATA FOR CONNECTION: 
```
<MICROS DEVIDE IP (DEVIP)>
```

> All the other data can be dummy value :) 

#### Interactive mode

```
./devToolKit.py -c 
or
./devToolKit.py -connect
Load MicrOS device cache: /Users/bnm/Documents/NodeMcu/MicrOs/tools/device_conn_cache.json
Activate MicrOS device connection address
[i]         FUID        IP               UID
[0] Device: node01 - 10.0.1.119 - 0x500x20x910x680xc0xf7
Choose a device index: 0
Device IP was set: 10.0.1.119
node01 $  help
[MICROS]   - commands (SocketServer built-in)
   hello   - default hello msg - identify device
   version - shows micrOS version
   exit    - exit from shell socket prompt
   reboot  - system safe reboot
   webrepl - start web repl for file transfers - update
[CONF] Configure mode (InterpreterShell built-in):
  conf       - Enter conf mode
    dump       - Dump all data
    key        - Get value
    key value  - Set value
  noconf     - Exit conf mode
[EXEC] Command mode (LMs):
   L298N_DCmotor
                help
   VL53L0X
          measure
          help
   adc
      measure
      action_fltr
      help
   air
      help
   ...
node01 $  exit
Bye!

```

## Project structure

### MicrOS resources library

```
micrOS/
├── BleHandler.py
├── Common.py
├── ConfigHandler.py
├── Hooks.py
├── InterConnect.py
├── InterpreterCore.py
├── InterpreterShell.py
├── InterruptHandler.py
├── LP_esp32.py
├── LP_esp8266.py
├── LP_tinypico.py
├── LogicalPins.py
├── Network.py
├── Scheduler.py
├── SocketServer.py
├── TinyPLed.py
├── boot.py
├── micrOS.py
├── micrOSloader.py
├── node_config.json
├── reset.py
```
> Note: Core MicrOS components

```
micrOS/
├── LM_L298N_DCmotor.py
├── LM_VL53L0X.py
├── LM_bledns.py
├── LM_bme280.py
├── LM_co2.py
├── LM_dht11.py
├── LM_dht22.py
├── LM_dimmer.py
├── LM_distance_HCSR04.py
├── LM_esp32.py
├── LM_i2c.py
├── LM_intercon.py
├── LM_light_sensor.py
├── LM_neopixel.py
├── LM_oled_128x64i2c.py
├── LM_oled_widgets.py
├── LM_ph_sensor.py
├── LM_repair.py
├── LM_rgb.py
├── LM_rgbfader.py
├── LM_servo.py
├── LM_switch.py
├── LM_system.py
├── LM_tinyrgb.py
```
> LM (Load Modules) - Application logic - accessable over socket server as a command

```
micrOS/
├── node_config.json
```
> Note: System description config

### MicrOS development tools library

```
├── devToolKit.py
├── tools
│   ├── MicrOSDevEnv
```
> Note: devToolKit wrapper resources for development, deployment, precompile, etc.

```
│   ├── nwscan.py
│   ├── socketClient.py
```
> Note: devToolKit wrapper socket based connection handling

```
├── user_data
│   ├── device_conn_cache.json
│   └── node_config_archive
```
> Note: User data dir: conatins node connection informations (devToolKit --search_devices) and deployed node config backups are here.


### MicrOS deployment resources

Precompiled components with the actual user configured config location

```
mpy-micrOS/
├── BleHandler.mpy
├── Common.mpy
├── ConfigHandler.mpy
├── Hooks.mpy
├── InterConnect.mpy
├── InterpreterCore.mpy
├── InterpreterShell.mpy
├── InterruptHandler.mpy
├── LM_L298N_DCmotor.mpy
├── LM_VL53L0X.py
├── LM_bledns.py
├── LM_bme280.mpy
├── LM_co2.mpy
├── LM_dht11.mpy
├── LM_dht22.mpy
├── LM_dimmer.mpy
├── LM_distance_HCSR04.py
├── LM_esp32.py
├── LM_i2c.py
├── LM_intercon.mpy
├── LM_light_sensor.mpy
├── LM_neopixel.mpy
├── LM_oled_128x64i2c.mpy
├── LM_oled_widgets.mpy
├── LM_ph_sensor.py
├── LM_repair.mpy
├── LM_rgb.mpy
├── LM_rgbfader.mpy
├── LM_servo.mpy
├── LM_switch.mpy
├── LM_system.mpy
├── LM_tinyrgb.mpy
├── LP_esp32.mpy
├── LP_esp8266.mpy
├── LP_tinypico.mpy
├── LogicalPins.mpy
├── Network.mpy
├── Scheduler.mpy
├── SocketServer.mpy
├── TinyPLed.mpy
├── boot.py
├── micrOS.mpy
├── micrOSloader.mpy
└── reset.mpy
44 files
```

> Note: These resources will be copy to the micropython base image, all `LM_`s are optional.

### Release info and Application Profiles

```
├── release_info
│   ├── micrOS_ReleaseInfo
│   │   ├── release_0.1.0-0_note.md
│   │   ├── release_0.4.0-0_note_esp32.md
│   │   ├── release_0.4.0-0_note_esp8266.md
│   │   ├── release_sfuncman_0.1.0-0.json
│   │   └── release_sfuncman_0.4.0-0.json
│   └── node_config_profiles
│       ├── README.md
│       ├── catgame_profile-node_config.json
│       ├── catgame_profile_command_examples.txt
│       ├── default_profile-node_config.json
│       ├── default_profile_command_examples.txt
│       ├── dimmer_profile-node_config.json
│       ├── dimmer_profile_command_examples.txt
│       ├── heartbeat_profile-node_config.json
│       ├── heartbeat_profile_command_examples.txt
│       ├── lamp_profile-node_config.json
│       ├── lamp_profile_command_examples.txt
│       ├── neopixel_profile-node_config.json
│       └── neopixel_profile_command_examples.txt
```

> Note:  Under node_config_profiles you can find **configuration temaples**, named **profiles** (devenv automatically able to inject these under deployment) - there are also **command examples** for each application.

> **MicrOS_Release_Info** folder(s) conatins system verification logs like:
> 
> - bootup log with different configurations
> - application execution log
> - memory measurements

### Other project resoures 

```
apps/
├── AirQualityBME280_app.py
├── AirQualityDHT22_CO2_app.py
├── AnanlogLED_app.py
├── CatGame_app.py
├── Dimmer_app.py
├── GetVersion_app.py
├── NeopixelTest_app.py
├── Template_app.py
```

----------------------------------------

## HINTS

- Save **screen** console buffer (**output**)
Press `ctrl + A :` and type `hardcopy -h <filename>`

- Create callgraph: [pycallgraph](http://pycallgraph.slowchop.com/en/master/)

- Convert PNG/JPG-s to GIF: `convert -delay 60 ./*.png mygif.gif`

- **micrOS core source code** lines:

```bash
Ferenc@Bans-MBP:micrOS$ core_files=($(ls -1 | grep '.py' | grep -v 'LM_')); all_line_codes=0; for coref in ${core_files[@]}; do content_lines_cnt=$(cat $coref | grep -v -e '^$' | wc -l); all_line_codes=$((all_line_codes+content_lines_cnt)); echo -e "$content_lines_cnt\t$coref"; done; echo -e "SUM OF CODE LINES: $all_line_codes"
     111	BgJob.py
     154	BleHandler.py	       -> beta code
      70	Common.py           -> Common functions/decorators for LMs
     212	ConfigHandler.py
     102	Debug.py				-> FSCO (TODO)
      54	Hooks.py
      42	InterConnect.py
     164	InterpreterCore.py
     199	InterpreterShell.py
     119	InterruptHandler.py
      43	LP_esp32.py
      55	LP_tinypico.py
      44	LogicalPins.py
     185	Network.py          -> FSCO (ForceCoreOTA update)
     130	Scheduler.py
     291	SocketServer.py
      24	TinyPLed.py
      19	boot.py             -> FSCO
      60	micrOS.py
     110	micrOSloader.py     -> FSCO
       5	reset.py            -> only used for webrepl manual reset
SUM OF CODE LINES: 2193
```

- **micrOS Load Module-s** (application-s) source code lines:


```
bnm@Bans-MacBook-Pro:micrOS$ core_files=($(ls -1 | grep '.py' | grep 'LM_')); all_line_codes=0; for coref in ${core_files[@]}; do content_lines_cnt=$(cat $coref | grep -v -e '^$' | wc -l); all_line_codes=$((all_line_codes+content_lines_cnt)); echo -e "$content_lines_cnt\t$coref"; done; echo -e "SUM OF CODE LINES: $all_line_codes"
      59	LM_L298N_DCmotor.py
      37	LM_L9110_DCmotor.py
     310	LM_VL53L0X.py
      27	LM_bledns.py
     273	LM_bme280.py
     194	LM_buzzer.py
      24	LM_catgame.py
     176	LM_cct.py
     103	LM_co2.py
      32	LM_dht11.py
      32	LM_dht22.py
      89	LM_dimmer.py
      57	LM_distance_HCSR04.py
      36	LM_ds18.py
      24	LM_esp32.py
      67	LM_genIO.py
      19	LM_i2c.py
      16	LM_intercon.py
      55	LM_light_sensor.py
     108	LM_neoeffects.py
     205	LM_neopixel.py
     161	LM_oled.py
     169	LM_oled_ui.py
      30	LM_pet_feeder.py
      50	LM_ph_sensor.py
     197	LM_rgb.py
     154	LM_roboarm.py
      40	LM_robustness.py
      89	LM_servo.py
     110	LM_stepper.py
     179	LM_switch.py
     140	LM_system.py
      60	LM_tinyrgb.py
SUM OF CODE LINES: 3322
```

GIT:
- Add git tag: `git tag -a vX.Y.Z-K -m "tag message"`

- Publish tags: `git push origin --tags`

- Pretty git view: `git log --pretty=oneline`

- File change list: `git diff --name-only fbb4875609a3c0ee088b6a118ebf9f8a500be0fd HEAD | grep 'mpy-MicrOS'`

- GitHub embed youtube link: `https://github.com/itskeshav/Add-youtube-link-in-Readme.md`

git push -u origin master
