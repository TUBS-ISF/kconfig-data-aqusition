# Requirements:
* Use Linux as OS (Recommended: Ubuntu 20.04 LTS)
* Use Python 3.8 or newer 

# Install required packages:
``` 
$ sudo apt update
$ sudo apt upgrade
$ sudo apt install python3.8 python3-pip
$ sudo apt install git
```

# Checkout repository:
```
$ git clone https://github.com/witschel/kconfig-base-data-acquisition
```

# Install required python packages:
``` 
$ pip3 install -r requirements.txt
```

# Supported and tested systems:
|System|Repository|SYSTEM_NAME|KCONFIG_FILE_NAME|START_DATE|END_DATE|
|---|---|---|---|---|---|
|BusyBox|https://github.com/mirror/busybox.git|busybox|Config.in|1999-10-05|2021-01-01|
|Soletta|https://github.com/solettaproject/soletta.git|soletta|Kconfig|2015-08-13|2018-07-10|
|Toybox|https://github.com/landley/toybox.git|toybox|Config.in|2006-10-30|2021-01-01|
|Fiasco|https://github.com/kernkonzept/fiasco.git|fiasco|Kconfig|1970-01-01|2021-01-01|
|uClibc-ng|https://github.com/wbx-github/uclibc-ng.git|uclibc-ng|Config.in|1970-01-01|2021-01-01|

# Get systems:
1. Go to systems directory
``` 
$ cd systems
```
2. Clone System repositories
```
$ git clone https://github.com/mirror/busybox.git
$ git clone https://github.com/solettaproject/soletta.git
$ git clone https://github.com/landley/toybox.git
$ git clone https://github.com/kernkonzept/fiasco.git
$ git clone https://github.com/wbx-github/uclibc-ng.git
```
3. Install all the required packages, which are needed to build the software (for each system)

# Analyze systems and convert kconfig models to .xml feature models (Repeat for each system):
1. Go to extractor directory
```
$ cd scripts/extractor
```
2. Run the following script with the required paramters (Depending on the system)
```
$ python3 extractor.py SYSTEM_NAME --config KCONFIG_FILE_NAME --start START_DATE --end END_DATE
```

# Hints:
* Make a script executable
``` 
$ sudo chmod +x ./NAME_OF_SCRIPT
```
* Run a script
``` 
$ ./NAME_OF_SCRIPT
```
