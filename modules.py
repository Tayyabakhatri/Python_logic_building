import sys

print(sys.builtin_module_names)
(
    "_abc",
    "_ast",
    "_bisect",
    "_blake2",
    "_codecs",
    "_codecs_cn",
    "_codecs_hk",
    "_codecs_iso2022",
    "_codecs_jp",
    "_codecs_kr",
    "_codecs_tw",
    "_collections",
    "_contextvars",
    "_csv",
    "_datetime",
    "_functools",
    "_heapq",
    "_hmac",
    "_imp",
    "_interpchannels",
    "_interpqueues",
    "_interpreters",
    "_io",
    "_json",
    "_locale",
    "_lsprof",
    "_md5",
    "_multibytecodec",
    "_opcode",
    "_operator",
    "_pickle",
    "_random",
    "_sha1",
    "_sha2",
    "_sha3",
    "_signal",
    "_sre",
    "_stat",
    "_statistics",
    "_string",
    "_struct",
    "_suggestions",
    "_symtable",
    "_sysconfig",
    "_thread",
    "_tokenize",
    "_tracemalloc",
    "_types",
    "_typing",
    "_warnings",
    "_weakref",
    "_winapi",
    "array",
    "atexit",
    "binascii",
    "builtins",
    "cmath",
    "errno",
    "faulthandler",
    "gc",
    "itertools",
    "marshal",
    "math",
    "mmap",
    "msvcrt",
    "nt",
    "sys",
    "time",
    "winreg",
    "xxsubtype",
    "zlib",
)


import pkgutil
import sys

modules = pkgutil.iter_modules()
for module in modules:
    print(module.name)
# (currency_convertor
# data_engineering
# even_odd
# functions
# modules
# my_string
# _asyncio
# _bz2
# _ctypes
# _ctypes_test
# _decimal
# _elementtree
# _hashlib
# _lzma
# _multiprocessing
# _overlapped
# _queue
# _remote_debugging
# _socket
# _sqlite3
# _ssl
# _testbuffer
# _testcapi
# _testclinic
# _testclinic_limited
# _testconsole
# _testimportmultiple
# _testinternalcapi
# _testlimitedcapi
# _testmultiphase
# _testsinglephase
# _tkinter
# _uuid
# _wmi
# _zoneinfo
# _zstd
# pyexpat
# select
# unicodedata
# winsound
# __future__
# __hello__
# __phello__
# _aix_support
# _android_support
# _apple_support
# _ast_unparse
# _collections_abc
# _colorize
# _compat_pickle
# _ios_support
# _markupbase
# _opcode_metadata
# _osx_support
# _py_abc
# _py_warnings
# _pydatetime
# _pydecimal
# _pyio
# _pylong
# _pyrepl
# _sitebuiltins
# _strptime
# _threading_local
# _weakrefset
# abc
# annotationlib
# antigravity
# argparse
# ast
# asyncio
# base64
# bdb
# bisect
# bz2
# cProfile
# calendar
# cmd
# code
# codecs
# codeop
# collections
# colorsys
# compileall
# compression
# concurrent
# configparser
# contextlib
# contextvars
# copy
# copyreg
# csv
# ctypes
# curses
# dataclasses
# datetime
# dbm
# decimal
# difflib
# dis
# doctest
# email
# encodings
# ensurepip
# enum
# filecmp
# fileinput
# fnmatch
# fractions
# ftplib
# functools
# genericpath
# getopt
# getpass
# gettext
# glob
# graphlib
# gzip
# hashlib
# heapq
# hmac
# html
# http
# idlelib
# imaplib
# importlib
# inspect
# io
# ipaddress
# json
# keyword
# linecache
# locale
# logging
# lzma
# mailbox
# mimetypes
# modulefinder
# multiprocessing
# netrc
# ntpath
# nturl2path
# numbers
# opcode
# operator
# optparse
# os
# pathlib
# pdb
# pickle
# pickletools
# pkgutil
# platform
# plistlib
# poplib
# posixpath
# pprint
# profile
# pstats
# pty
# py_compile
# pyclbr
# pydoc
# pydoc_data
# queue
# quopri
# random
# re
# reprlib
# rlcompleter
# runpy
# sched
# secrets
# selectors
# shelve
# shlex
# shutil
# signal
# site
# smtplib
# socket
# socketserver
# sqlite3
# sre_compile
# sre_constants
# sre_parse
# ssl
# stat
# statistics
# string
# stringprep
# struct
# subprocess
# symtable
# sysconfig
# tabnanny
# tarfile
# tempfile
# test
# textwrap
# this
# threading
# timeit
# tkinter
# token
# tokenize
# tomllib
# trace
# traceback
# tracemalloc
# tty
# turtle
# turtledemo
# types
# typing
# unittest
# urllib
# uuid
# venv
# warnings
# wave
# weakref
# webbrowser
# wsgiref
# xml
# xmlrpc
# zipapp
# zipfile
# zipimport
# zoneinfo
# click
# colorama
# joblib
# nltk
# pip
# regex
# tqdm)