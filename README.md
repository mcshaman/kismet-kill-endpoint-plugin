<p align="center">
	<img src="https://github.com/mcshaman/kismet-kill-endpoint-plugin/blob/media/kill-logo.svg" alt="Kismet kill endpoint plugin" width="150" height="300">
</p>

# Kismet kill endpoint plugin
Used to kill Kismet service

## Install

Install plugin in same directory as Kismet e.g. ` /usr/bin` or `/usr/local/bin/`

```sh
$ pip3 install . --install-option="--install-scripts=/usr/bin"
```

Copy manifest to Kismet's plugins directory e.g. `/usr/lib/kismet/` or `/usr/local/lib/kismet/`:

```sh
$ mkdir /usr/lib/kismet/killendpoint/
$ cp ./manifest.conf /usr/lib/kismet/killendpoint/
```

Confirm installation by starting Kismet and look for the line `INFO: Plugin 'killendpoint' loaded...` or by hitting the list plugins endpoint e.g. `http://localhost:2501/plugins/all_plugins.json`
## Usage

```sh
http://localhost:2501/kill.cmd
```

## Uninstall

Find the install location of plugin package.

```sh
$ pip3 show kismet-kill-endpoint-plugin
```

Uninstall plugin package and dependencies.

```sh
$ pip3 uninstall -r requirements.txt
```

Delete the egg-info folder remaining in the install location of plugin package e.g. `/usr/local/lib/python3.7/dist-packages/`

```sh
$ rm -rf /usr/local/lib/python3.7/dist-packages/kismet_kill_endpoint_plugin-1.0.0.egg-info
```

Delete plugin script from the same directory as Kismet e.g. ` /usr/bin` or `/usr/local/bin/`

```sh
$ rm /usr/bin/kismet-kill-endpoint-plugin
```

Delete manifest from Kismet's plugins directory e.g. `/usr/lib/kismet/` or `/usr/local/lib/kismet/`.

```sh
$ rm -rf /usr/lib/kismet/killendpoint/
```