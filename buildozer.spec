# buildozer.spec

[app]
title = Afghan Services Finder
package.name = afghan_service_finder
package.domain = org.example
source.dir = src
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = kivy
orientation = portrait
osx.kivy_version = 2.1.0
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1
android.archs = armeabi-v7a, arm64-v8a
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 21b
android.private_storage = 1
android.p4a = 0.1.0
android.gradle = 7.0.2
android.gradle_version = 7.0.2
android.gradle_dependencies = com.android.support:appcompat-v7:28.0.0

[global]
requirements = python3,kivy
python.version = 3.8
log_level = 2
```