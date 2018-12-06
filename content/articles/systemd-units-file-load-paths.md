title: Systemd Unit File Load Paths
date: 2018-10-14T10:14
category: research
tags: systemd

Unit File Load Path
===================

Unit files are loaded from a set of paths determined during compilation,
described in the two tables below. Unit files found in directories
listed earlier override files with the same name in directories lower in
the list.

When the variable $SYSTEMD\_UNIT\_PATH is set, the contents of this
variable overrides the unit load path. If $SYSTEMD\_UNIT\_PATH ends with
an empty component (":"), the usual unit load path will be appended to
the contents of the variable.

Table 1. Load path when running in system mode (--system).

```
    Path    Description
    /etc/systemd/system.control Persistent and transient configuration created using the dbus API
    /run/systemd/system.control
    /run/systemd/transient  Dynamic configuration for transient units
    /run/systemd/generator.early    Generated units with high priority (see early-dir in system.generator(7))
    /etc/systemd/system Local configuration
    /run/systemd/system Runtime units
    /run/systemd/generator  Generated units with medium priority (see normal-dir in system.generator(7))
    /usr/local/lib/systemd/system   Units of installed packages
    /usr/lib/systemd/system
    /run/systemd/generator.late Generated units with low priority (see late-dir in system.generator(7))
```

Table 2. Load path when running in user mode (--user).

```
    Path    Description
    $XDG_CONFIG_HOME/systemd/user.control or ~/.config/systemd/user.control
    Persistent and transient configuration created using the dbus API
    ($XDG_CONFIG_HOME is used if set, ~/.config otherwise)
    $XDG_RUNTIME_DIR/systemd/user.control
    /run/systemd/transient  Dynamic configuration for transient units
    /run/systemd/generator.early    Generated units with high priority (see
    early-dir in system.generator(7))
    $XDG_CONFIG_HOME/systemd/user or $HOME/.config/systemd/user User configuration
    ($XDG_CONFIG_HOME is used if set, ~/.config otherwise)
    /etc/systemd/user   Local configuration
    $XDG_RUNTIME_DIR/systemd/user   Runtime units (only used when $XDG_RUNTIME_DIR
    is set)
    /run/systemd/user   Runtime units
    $XDG_RUNTIME_DIR/systemd/generator  Generated units with medium priority (see
    normal-dir in system.generator(7))
    $XDG_DATA_HOME/systemd/user or $HOME/.local/share/systemd/user  Units of
    packages that have been installed in the home directory ($XDG_DATA_HOME is used
    if set, ~/.local/share otherwise)
    $dir/systemd/user for each $dir in $XDG_DATA_DIRS   Additional locations for
    installed user units, one for each entry in $XDG_DATA_DIRS
    /usr/local/lib/systemd/user Units of packages that have been installed
    system-wide
    /usr/lib/systemd/user
    $XDG_RUNTIME_DIR/systemd/generator.late Generated units with low priority (see late-dir in system.generator(7))
```

The set of load paths for the user manager instance may be augmented or
changed using various environment variables. And environment variables
may in turn be set using environment generators, see
systemd.environment-generator(7). In particular, $XDG\_DATA\_HOME and
$XDG\_DATA\_DIRS may be easily set using
systemd-environment-d-generator(8). Thus, directories listed here are
just the defaults. To see the actual list that would be used based on
compilation options and current environment use

```bash
systemd-analyze --user unit-paths
```

Moreover, additional units might be loaded into systemd ("linked") from
directories not on the unit load path. See the link command for
systemctl(1).
