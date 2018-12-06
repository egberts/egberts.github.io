title: Bro Core Engine
date:  2018-05-16T14:20:12
tags: bro, debugging
category: research
summary: How to debug the Core Engine of Bro-IDS.

Debugging Bro Core Engine
=========================

This page covers how to debug the Core Engine of Bro. 
1. Viewing BroString Object 
2. Breakpoint an Analyzer function

Viewing BroString Object
========================

To view a BroString object, enter at GDB prompt:

```gdb
(gdb) print content_subtype_str->CheckString()
$14 = 0x2a51e60 "MIXED"
```

Breakpoint an Analyzer function
===============================

Setting a breakpoint on a C++ function is similar to setting a
breakpoint on a C function. However C++ is polymorphic, so you must tell
break which version of the function you want to break on (even if there
is only one). To do this, you tell it the list of argument types.

GDB also assist in auto-completing your desired function name via TAB
keys, provided the namespace(s) are correct.

To add a breakpoint to a function deep in the Analyzer part of Bro Core
Engine, add the analyzer::mime:: namespace to its full function name:

```gdb
(gdb) break analyzer::mime::MIME_Entity::ParseFieldParameters
```
