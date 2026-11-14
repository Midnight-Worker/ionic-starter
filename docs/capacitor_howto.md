Capacitor – Android Anleitung

Capacitor verpackt eine HTML-/JavaScript-Anwendung als native Android-App.

Kein React, Angular, Vite oder SCSS erforderlich.

1. Voraussetzungen

Für Capacitor 8 benötigst du:

Node.js 22 oder neuer

npm

Android Studio mit Android SDK für lokale Android-Builds

Download: https://nodejs.org

Download: https://developer.android.com/studio

Prüfen:

node -v
npm -v

2. Projektstruktur

mein-projekt/
├── www/
│   ├── index.html
│   ├── style.css
│   ├── main.js
│   └── lib/
├── package.json
└── capacitor.config.json

In www liegen sämtliche HTML-, CSS-, JavaScript- und Bibliotheksdateien.

3. Capacitor installieren

Im Projektverzeichnis:

npm init -y
npm install @capacitor/core@8 @capacitor/android@8
npm install -D @capacitor/cli@8

Capacitor initialisieren:

npx cap init

Dabei App-Name und App-ID eingeben, beispielsweise:

App name: Midnight Worker
App ID: de.midnightworker.app

Die App-ID sollte dauerhaft eindeutig bleiben.

4. Konfiguration

In capacitor.config.json:

{
  "appId": "de.midnightworker.app",
  "appName": "Midnight Worker",
  "webDir": "www"
}

Wichtig: webDir zeigt direkt auf unseren fertigen www-Ordner. Wir benötigen keinen zusätzlichen Web-Build.

5. Android-Projekt erstellen

Nur einmal ausführen:

npx cap add android

Danach entsteht:

mein-projekt/
├── www/
├── android/
├── node_modules/
├── package.json
└── capacitor.config.json

6. Änderungen synchronisieren

Nach Änderungen an HTML, CSS oder JavaScript:

npx cap sync android

Damit kopiert Capacitor die Dateien aus www in das Android-Projekt und aktualisiert gegebenenfalls native Abhängigkeiten.

7. Android-App testen

Auf einem verbundenen Android-Gerät oder Emulator:

npx cap run android

Alternativ Android Studio öffnen:

npx cap open android

8. APK erstellen

Windows (PowerShell oder CMD)

cd android
gradlew.bat assembleDebug

Linux

cd android
./gradlew assembleDebug

Unter Windows mit Git Bash kannst du ebenfalls ./gradlew.bat assembleDebug verwenden.

Die fertige APK liegt hier:

android/app/build/outputs/apk/debug/app-debug.apk

Diese Debug-APK kann zum Testen auf einem Android-Gerät installiert werden.

Für die Veröffentlichung im Play Store brauchst du später einen signierten Release-Build.

9. APK nach Änderungen neu erstellen

Im Projektverzeichnis:

npx cap sync android

Danach unter Linux:

cd android
./gradlew assembleDebug

Oder unter Windows:

cd android
./gradlew.bat assembleDebug

10. GitHub Actions – automatischer Build

Mit unserem GitHub-Workflow genügt:

git add .
git commit -m "App aktualisiert"
git push origin main

GitHub Actions startet automatisch, sofern der Workflow push auf main enthält.

Nach erfolgreichem Build:

GitHub → Actions → Build auswählen → Artifacts → APK herunterladen

Auf deinem eigenen Rechner sind dafür weder Android Studio noch Gradle nötig.

11. Die wichtigsten Befehle

Befehl

Funktion

npm install

Abhängigkeiten installieren

npx cap init

Capacitor konfigurieren

npx cap add android

Android-Projekt erstellen

npx cap sync android

Webdateien synchronisieren

npx cap run android

App auf Gerät starten

npx cap open android

Android Studio öffnen

./gradlew assembleDebug

Debug-APK erstellen

12. Wichtige Hinweise

npx cap add android nur bei der erstmaligen Erstellung verwenden.

npx cap sync android nach Änderungen ausführen.

Lokale Bibliotheken aus www/lib werden mit in die APK kopiert.

Für den normalen HTML-/JavaScript-Code brauchst du keinen Bundler.

SQLite mit sql.js funktioniert innerhalb der Android-WebView.

sql.js speichert Änderungen nicht automatisch dauerhaft. Dafür beispielsweise IndexedDB verwenden.

Für ein stabiles Update einer installierten App sind dieselbe App-ID und derselbe Signaturschlüssel erforderlich.

Merksatz

Ionic erstellt die Benutzeroberfläche.

JavaScript steuert die Anwendung.

Capacitor verbindet die Web-App mit Android.

Gradle erstellt die APK.

GitHub Actions kann den gesamten Android-Build übernehmen.

Offizielle Dokumentation:

https://capacitorjs.com/docs

https://capacitorjs.com/docs/android
