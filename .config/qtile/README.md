# Qtile config 
~~A default config is located in `/usr/lib/python3.9/site-packages/libqtile/resources/default_config.py` from which this is based off of.~~
This was true when using Fedora which had an older version of qtile in its repos that did not generate a default config automatically. 
## Version
~~This configuration is for qtile version 0.14.2, the latest available in Fedora repos as of 1/11/2021.~~
## Autostart
The `autostart.sh` file is used to set the wallpaper on boot. When creating a shell
script it must be made into an executable file. This can be done by:
```bash
$ chmod +x path/to/file
```
in our case,
```bash
$ chmod +x ~/.config/qtile/autostart.sh
```
