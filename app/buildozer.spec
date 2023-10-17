[app]

# (str) Title of your application
title = MattDiario

# (str) Package name
package.name = online.mattebernini.mattdiario
icon.filename = matt_diario.png

# (str) Package domain (needed for android/ios packaging)
package.domain = online.mattebernini

# (str) Source code where the main.py live
source.dir = .

# (str) Application version
version = 1.0

# (int) Build the app with the Python for android
source.include_exts = py,kv,ini,png,jpg,jpeg,atlas

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = sqlite3,kivy,requests,python-dotenv

# (str) Custom source folders for requirements
# Sets custom source directories for requirements. Can be system path, python
# path, or download path.
# requirements.source.kivy = ../../kivy

# (str) iOS SDK (auto detected) (clan)
ios.sdk = 10.3

# (str) Android NDK version to use (8c is recommended)
android.ndk = 21.1.6352462

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
# android.ndk_path = 

# (int) Android API to use for the compilation
android.api = 29

# (int) Minimum API required
android.minapi = 21

# (int) Android NDK version to be used
android.ndk = 21.1.6352462

# (int) Android NDK toolchain version to be used
android.toolchain = clang

# (str) Android NDK toolchain version to be used (in case of 4)
android.toolchain_version = 4.9

# (str) Android API to be used
android.api = 29

# (int) Minimum API required
android.minapi = 21

# (int) Android App permissions
# The list of permissions needed for the application. You can use the
# Android reference documentation to define permissions.
android.permissions = INTERNET

# (int) Minimum memory required (in MB)
#android.minmem = 60

# (int) Minimum storage required (in MB)
#android.minstorage = 0

# (str) How to integrate python source (with the recipe for example)
# source.path = $(source.dir)

# (str) Local path to the main.py file
source.main.filename = main.py

# (str) Application version code
# version.code = 1

# (str) Icon of the application
# icon.filename = icon.png

# (str) Supported orientations (landscape, portrait or all)
orientation = portrait

# (list) List of service to declare
# services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

# (bool) Wheter to try to compile before packaging
#android.p4a = True

[buildozer]

# (int) Log level (0 = error only, 1 = warning, 2 = info, 3 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to a custom distribution
# dist_name = mydist

# (str) Custom origin
# dist_origin = mycompany

# (str) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Build order (comma delimited: all, python2, python3, ... for android)
# p4a.branch = develop
# p4a.source_dir = /home/kivy/Desktop/myapp

# (str) Path to build artifact storage, absolute or relative to spec file
# build_dir = ./.buildozer

# (int) Configured log level (0, 1, 2, 3)
log_level = 2

# (int) Parallel build (0 = sequential, 1 = parallel build)
# buildozer.use_p4a = True

# (str) Recursion limit of the multiprocessing
# multiprocess.recursionlimit = 1000

# (str) Local path to distribute prebuilt python-for-android python recipes
# p4a.local_recipes = /home/user/python-for-android/recipes

# (str) Path to a local python3.8 build
# p4a.python3 = /usr/bin/python3

# (str) Path to a local python2.7 build
# p4a.python2 = /usr/bin/python

# (bool) Allow progress bars
# android.allow_p4a_progress_bars = True

# (bool) Allow requests to be made to the internet while building
# allow_online = False
