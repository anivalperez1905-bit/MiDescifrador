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
android.apptheme = @android:style/Theme.Holo.Light
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
android.allowBackups = True
android.wakelock = False
