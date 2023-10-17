[app]

# Title of your application
title = MattDiario

# Package name
package.name = online.mattebernini.mattdiario

# Package domain (needed for Android/iOS packaging)
package.domain = online.mattebernini
icon.filename = matt_diario.png

# Source code where the main.py resides
source.dir = .

# Application version
version = 1.0

# Build the app with Python for Android
source.include_exts = py,kv,ini,png,jpg,jpeg,atlas

# Application requirements
requirements = sqlite3,kivy,requests,python-dotenv

# iOS SDK (auto detected)
ios.sdk = 10.3

# Android NDK version to use (8c is recommended)
android.ndk = 21.1.6352462

# Android API to use for the compilation
android.api = 29

# Minimum API required
android.minapi = 21

# Android NDK toolchain version to be used
android.toolchain = clang

# Android NDK toolchain version to be used (in case of 4)
android.toolchain_version = 4.9

# Android App permissions
android.permissions = INTERNET

# Supported orientations (landscape, portrait, or all)
orientation = portrait

[buildozer]

# Log level (0 = error only, 1 = warning, 2 = info, 3 = debug)
log_level = 2

# Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# Build order (comma-delimited: all, python2, python3, ... for Android)
# p4a.branch = develop
# p4a.source_dir = /home/kivy/Desktop/myapp

# Path to build artifact storage, absolute or relative to spec file
# build_dir = ./.buildozer

# Parallel build (0 = sequential, 1 = parallel build)
# buildozer.use_p4a = True

# Recursion limit of the multiprocessing
# multiprocess.recursionlimit = 1000

# Local path to distribute prebuilt python-for-android python recipes
# p4a.local_recipes = /home/user/python-for-android/recipes

# Path to a local python3.8 build
# p4a.python3 = /usr/bin/python3

# Path to a local python2.7 build
# p4a.python2 = /usr/bin/python

# Allow progress bars
# android.allow_p4a_progress_bars = True

# Allow requests to be made to the internet while building
# allow_online = False
