<p align="center">
	<img src="https://github.com/mcshaman/kismet-kill-endpoint-plugin/blob/media/kill-logo.svg" alt="Kismet kill endpoint plugin" width="150" height="300">
</p>

# Kismet kill endpoint plugin
Used to kill Kismet service

## Installation

``` bash
$ sudo python3 setup.py install --script-dir /usr/bin
```

## Usage

``` bash
http://{{domain}}/kill.cmd
```

## Uninstallation

Output list of file locations

``` bash
$ python setup.py install --record files.txt
```
``` bash
$ xargs rm -rf < files.txt
```