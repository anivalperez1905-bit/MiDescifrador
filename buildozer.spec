[app]
title = Fenix App
package.name = fenixapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv
version = 0.1
requirements = python3,kivy,openssl
orientation = portrait
osx.kivy_version = 2.1.0
fullscreen = 0
android.archs = arm64-v8a
android.allow_backup = True
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1
