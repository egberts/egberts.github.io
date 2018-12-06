Title: Firefox Sync
Date: 2017-05-20T16:59
Tags: firefox, sync
Category: research
Summary: Firefox Sync is a built-in web browser add-in application and an
application network protocol.

Firefox Sync can synchronize between your own Firefox web browsers over
different devices for the following:

* Bookmarks
* Opened tabs
* Passwords
* History of browsed web pages
* Add-Ons (not available on mobile devices)
* Preferences (not available on mobile devices)

Application Program
===================

Setup by GUI
------------

Setup by command line
---------------------

On the UNIX platform, Firefox stores its preference data settings in the
`$HOME/.mozilla/firefox` directory. Check for your specific profile
subdirectory in the `$HOME/.mozilla/firefox/profiles.ini` file.

Add the following lines to the `user.js` file.

`Notice: Any and all changes toward ``preferences.js`` will be blown`

away by the next Firefox upgrade.

[jtable]
Column, Description
prefs.js:user_pref("services.sync.username", johndoe@example.com"), The Sync account name (maintained by Firefox Account Manager)
prefs.js:user_pref("services.sync.declinedEngines", "tabs,addons,passwords,history");
A list of things to keep track of. Valid options are tabs, addons, passwords, history.
prefs.js:user_pref("services.sync.account", "johndoe@example.com");
prefs.js:user_pref("services.sync.client.name", "johndoe' Firefox on johndoe-macbook");
[/jtable]

To set up the

Firefox Sync Network Protocol
=============================

Firefox Sync Server
-------------------

To host a private server of Firefox Sync, see
\[<https://mozilla-services.readthedocs.io/en/latest/howtos/run-sync-1.5.html%7CHowTo>
Firefox Sync server\]
