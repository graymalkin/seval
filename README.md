# seval

`seval` provides a meta-circular Python interpreter for user interaction. It is
designed to safely evaluate python code without allowing calls to access the
underlying operating system.

This is done by evaluation of python expressions under a restricted environment.
Various python libraries are forbidden, and access to private fields is
prohibited.

```
>>> "".__repr__()
Exception: access to private fields is disallowed
```

## Purpose

`seval` has been designed to provide a programming interface over IRC to enable
writing macros and plugins for [piperbot](https://github.com/ellxc/piperbot).

## Caveat

`seval` has not been formally tested, and may have bugs. It has been implemented
to attempt to ensure safe sandboxed execution, but there could be bugs. Use at
your own risk.

## `repl.py`

There is a `repl` using a GNU Readline interface. You'll need a readline
implementation installed from pip. `anyreadline` is a metapackage which installs
a readline library appropriate for your operating system. The `gnureadline`
package is incompatible with Windows.

## Build, test, install

### Build
Building is simple using setuptools. It is advisable to work in a virtualenv.

```shellsession
$ virtualenv .
$ . bin/activate
# Install dependencies using pip
$ python3 ./setup.py build
```

### Test

Tests are in the `test/` directory. They're using the `unittest`
library and don't currently cover much of seval.

```shellsession
$ python3 ./setup.py test
```

### Install

Installation is also done with setuptools.

```shellsession
$ python3 ./setup.py test
```

This will put the following into a `bin/` directory

 - basic_repl.py
 - pt_repl.py
 - readline_repl.py
 

