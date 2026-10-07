[app]

title = FenixDecryptor
package.name = fenixdecryptor
package.domain = org.fenix
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

requirements = python3,kivy,pycryptodome

android.api = 33
android.ndk = 25b
android.sdk = 24
android.build_tools_version = 34.0.0
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
android.allowBackups = True
android.wakelock = False
android.accept_all_licenses = True
android.ndk_api = 21
android.sdk_path = $HOME/.buildozer/android/platform/android-sdk
