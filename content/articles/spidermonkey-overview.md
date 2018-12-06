Title: SpiderMonkey Overview
Date: 2018-09-24T10:35
Tags: javascript, js engine, browser, mozilla
Category: javascript
SpiderMonkey is a Mozilla Web Browser DOM component that comprises of
the following functional capabilities:

* JavaScript engine
* JavaScript just-in-time compiler (IonMonkey DOM network graphical support
* Threading support (SpiderMonkey Promise)

SpiderMonkey is compliant with ECMA 6 standard. Two engine components
have been created from SpiderMonkey:

1.  JavaScript/Emulators/SpiderMonkey/js - JavaScript console-based engine
2. JavaScript/Emulators/SpiderMonkey/xpcshell - JavaScript Browser-based engine

Difference between `js` and `xpcshell` is that `js` has no graphical
support (thus a smaller subset of JS API support).

Overviews
=========

High level overviews
--------------------

* http://hacks.mozilla.org/2010/03/a-quick-note-on-javascript-engine-components/
* https://developer.mozilla.org/en-US/docs/Mozilla/Projects/SpiderMonkey/Internals

Medium level documentation
--------------------------

`jsapi.h`:

* http://hg.mozilla.org/mozilla-central/file/tip/js/src/jsapi.h and the
* files in http://hg.mozilla.org/mozilla-central/file/tip/js/public

Frequently used coding recipes and mappings from JS idioms to
SpiderMonkey code:

* https://developer.mozilla.org/En/SpiderMonkey/JSAPI_Cookbook

Detailed documentation
----------------------

Build:

* https://developer.mozilla.org/en/SpiderMonkey/Build_Documentation

Testing:

* https://developer.mozilla.org/en/SpiderMonkey/Running_Automated_JavaScript_Tests

Shell:

* https://developer.mozilla.org/En/SpiderMonkey/Introduction_to_the_JavaScript_shell

Function reference:

* https://developer.mozilla.org/en/SpiderMonkey/JSAPI_Reference

API
---

Best C++ API is the official Mozilla JSAPI page:
https://developer.mozilla.org/en-US/docs/Mozilla/Projects/SpiderMonkey/JSAPI_reference

Bindings - C++
--------------

Bindings of SpiderMonkey to C++ have evolved over time:

1. http://spiderape.sourceforge.net/ is the first one
2. http://flusspferd.org/%7Cflusspferd> was the mainstream one
3. libjspp is another good binding that ended its support in 2012
4. https://github.com/rogerpoon/jspp%7Cjspp is the current one
