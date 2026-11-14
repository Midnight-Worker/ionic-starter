# Ionic Framework – Cheatsheet

Ionic ist eine Bibliothek für mobile Benutzeroberflächen mit HTML, CSS und JavaScript.

Wir verwenden **Ionic Web Components** direkt, ohne React, Angular oder Vue.

## 1. Ionic einbinden

```html
<link rel="stylesheet" href="lib/ionic/css/ionic.bundle.css">

<script type="module"
    src="lib/ionic/dist/ionic/ionic.esm.js">
</script>
```

Alternativ über ein CDN:

```html
<script type="module"
    src="https://cdn.jsdelivr.net/npm/@ionic/core@8/dist/ionic/ionic.esm.js">
</script>

<link rel="stylesheet"
    href="https://cdn.jsdelivr.net/npm/@ionic/core@8/css/ionic.bundle.css">
```

## 2. Grundgerüst einer Ionic-App

```html
<ion-app>

    <ion-header>
        <ion-toolbar color="primary">
            <ion-title>Meine App</ion-title>
        </ion-toolbar>
    </ion-header>

    <ion-content class="ion-padding">
        <h2>Hallo Ionic!</h2>
    </ion-content>

    <ion-footer>
        <ion-toolbar>
            <ion-title>Footer</ion-title>
        </ion-toolbar>
    </ion-footer>

</ion-app>
```

|Element|Funktion|
|---|---|
|`ion-app`|Wurzelelement der Anwendung|
|`ion-header`|Oberer Bereich|
|`ion-toolbar`|Werkzeugleiste|
|`ion-title`|Seitentitel|
|`ion-content`|Scrollbarer Inhaltsbereich|
|`ion-footer`|Unterer Bereich|

## 3. Buttons

```html
<ion-button>Standard</ion-button>

<ion-button color="danger">Löschen</ion-button>

<ion-button fill="outline">Outline</ion-button>

<ion-button fill="clear">Ohne Hintergrund</ion-button>

<ion-button expand="block">Volle Breite</ion-button>

<ion-button size="small">Klein</ion-button>

<ion-button disabled>Deaktiviert</ion-button>
```

JavaScript-Ereignis:

```javascript
document.querySelector("#button")
    .addEventListener("click", () => {
        console.log("Geklickt!");
    });
```

## 4. Eingabefelder

### Text

```html
<ion-input
    id="name"
    label="Name"
    label-placement="stacked"
    placeholder="Name eingeben">
</ion-input>
```

### Zahlen

```html
<ion-input
    id="age"
    type="number"
    label="Alter">
</ion-input>
```

### Passwort

```html
<ion-input
    id="password"
    type="password"
    label="Passwort">
</ion-input>
```

Wert auslesen:

```javascript
const name = document.querySelector("#name").value;
```

Live-Eingabe:

```javascript
document.querySelector("#name")
    .addEventListener("ionInput", event => {
        console.log(event.detail.value);
    });
```

## 5. Toggle, Checkbox und Radio

### Schalter

```html
<ion-toggle id="power">Einschalten</ion-toggle>
```

```javascript
const power = document.querySelector("#power");

power.addEventListener("ionChange", event => {
    console.log(event.detail.checked);
});
```

### Checkbox

```html
<ion-checkbox id="done">Erledigt</ion-checkbox>
```

```javascript
const checked = document.querySelector("#done").checked;
```

### Radio-Buttons

```html
<ion-radio-group value="red">
    <ion-radio value="red">Rot</ion-radio>
    <ion-radio value="blue">Blau</ion-radio>
</ion-radio-group>
```

## 6. Slider

```html
<ion-range
    id="brightness"
    min="0"
    max="255"
    step="1"
    value="128">
</ion-range>
```

```javascript
document.querySelector("#brightness")
    .addEventListener("ionInput", event => {
        console.log(event.detail.value);
    });
```

Wichtige Eigenschaften:

|Eigenschaft|Bedeutung|
|---|---|
|`min`|Minimalwert|
|`max`|Maximalwert|
|`step`|Schrittweite|
|`value`|Aktueller Wert|
|`disabled`|Deaktivieren|
|`dual-knobs`|Zwei Reglergriffe|

## 7. Auswahlmenü

```html
<ion-select id="language" label="Sprache" value="de">

    <ion-select-option value="de">
        Deutsch
    </ion-select-option>

    <ion-select-option value="en">
        Englisch
    </ion-select-option>

</ion-select>
```

```javascript
const select = document.querySelector("#language");

select.addEventListener("ionChange", event => {
    console.log(event.detail.value);
});
```

## 8. Listen

```html
<ion-list>

    <ion-item>
        <ion-label>Python</ion-label>
    </ion-item>

    <ion-item>
        <ion-label>JavaScript</ion-label>
    </ion-item>

    <ion-item>
        <ion-label>C++</ion-label>
    </ion-item>

</ion-list>
```

### Dynamisch Einträge hinzufügen

```javascript
const list = document.querySelector("ion-list");

const item = document.createElement("ion-item");
const label = document.createElement("ion-label");

label.textContent = "Neue Aufgabe";

item.appendChild(label);
list.appendChild(item);
```

## 9. Karten

```html
<ion-card>

    <ion-card-header>
        <ion-card-title>Projekt</ion-card-title>
        <ion-card-subtitle>Beschreibung</ion-card-subtitle>
    </ion-card-header>

    <ion-card-content>
        Meine erste Android-App.
    </ion-card-content>

</ion-card>
```

## 10. Weitere Komponenten

|Element|Verwendung|
|---|---|
|`ion-badge`|Kleine Statusanzeige|
|`ion-chip`|Schlagwort oder Filter|
|`ion-avatar`|Profilbild|
|`ion-thumbnail`|Vorschaubild|
|`ion-icon`|Symbol|
|`ion-searchbar`|Suchfeld|
|`ion-progress-bar`|Fortschrittsbalken|
|`ion-spinner`|Ladeanimation|
|`ion-datetime`|Datum und Uhrzeit|
|`ion-reorder-group`|Sortierbare Liste|
|`ion-accordion`|Aufklappbarer Bereich|
|`ion-grid`|Rasterlayout|
|`ion-row`|Rasterzeile|
|`ion-col`|Rasterspalte|

## 11. Mehrere Seiten mit Tabs

```html
<ion-tabs id="tabs">

    <ion-tab tab="home">
        <ion-content class="ion-padding">
            <h2>Startseite</h2>
        </ion-content>
    </ion-tab>

    <ion-tab tab="settings">
        <ion-content class="ion-padding">
            <h2>Einstellungen</h2>
        </ion-content>
    </ion-tab>

    <ion-tab-bar slot="bottom">

        <ion-tab-button tab="home">
            <ion-label>Start</ion-label>
        </ion-tab-button>

        <ion-tab-button tab="settings">
            <ion-label>Optionen</ion-label>
        </ion-tab-button>

    </ion-tab-bar>

</ion-tabs>
```

Per JavaScript navigieren:

```javascript
document.querySelector("#tabs").select("settings");
```

### Echtes Routing mit URLs

Für umfangreichere Anwendungen gibt es:

- `ion-router`
    
- `ion-route`
    
- `ion-router-outlet`
    
- `ion-nav`
    

Damit lassen sich Seiten mit eigenen URLs und Vorwärts-/Zurück-Navigation aufbauen.

## 12. Dialoge

### Alert

```html
<ion-alert
    id="alert"
    header="Hinweis"
    message="Hallo Ionic!"
    buttons='["OK"]'>
</ion-alert>
```

Anzeigen:

```javascript
document.querySelector("#alert").present();
```

### Toast

```html
<ion-toast
    id="toast"
    message="Gespeichert!"
    duration="2000">
</ion-toast>
```

Anzeigen:

```javascript
document.querySelector("#toast").present();
```

### Modal

```html
<ion-modal id="modal">
    <ion-header>
        <ion-toolbar>
            <ion-title>Dialog</ion-title>
        </ion-toolbar>
    </ion-header>

    <ion-content class="ion-padding">
        <p>Inhalt des Dialogs</p>
        <ion-button id="close">Schließen</ion-button>
    </ion-content>
</ion-modal>
```

```javascript
const modal = document.querySelector("#modal");

modal.present();

document.querySelector("#close").onclick = () => {
    modal.dismiss();
};
```

## 13. Farben

Ionic kennt vordefinierte Farben:

```html
<ion-button color="primary">Primary</ion-button>
<ion-button color="secondary">Secondary</ion-button>
<ion-button color="tertiary">Tertiary</ion-button>
<ion-button color="success">Success</ion-button>
<ion-button color="warning">Warning</ion-button>
<ion-button color="danger">Danger</ion-button>
<ion-button color="medium">Medium</ion-button>
<ion-button color="dark">Dark</ion-button>
<ion-button color="light">Light</ion-button>
```

### Mit CSS gestalten

```css
ion-content {
    --background: #101820;
    --color: white;
}

ion-button {
    --background: #3366ff;
    --border-radius: 8px;
}
```

Ionic verwendet viele CSS-Variablen, die mit `--` beginnen.

## 14. Dark Mode

Passende Ionic-Palette einbinden:

```html
<link rel="stylesheet"
    href="lib/ionic/css/palettes/dark.class.css">
```

Dark Mode einschalten:

```javascript
document.documentElement.classList.add("ion-palette-dark");
```

Ausschalten:

```javascript
document.documentElement.classList.remove("ion-palette-dark");
```

Umschalten:

```javascript
document.documentElement.classList.toggle("ion-palette-dark");
```

## 15. JavaScript-Ereignisse

|Element|Ereignis|Wert|
|---|---|---|
|`ion-button`|`click`|—|
|`ion-input`|`ionInput`|`event.detail.value`|
|`ion-input`|`ionChange`|`event.detail.value`|
|`ion-toggle`|`ionChange`|`event.detail.checked`|
|`ion-checkbox`|`ionChange`|`event.detail.checked`|
|`ion-range`|`ionInput`|`event.detail.value`|
|`ion-select`|`ionChange`|`event.detail.value`|

Ein typisches Beispiel:

```javascript
const slider = document.querySelector("#brightness");

slider.addEventListener("ionInput", event => {
    console.log(event.detail.value);
});
```

**Merke:** `ionInput` reagiert während der Eingabe. `ionChange` meldet eine übernommene Änderung, abhängig vom Element.

## 16. Daten und Serverkommunikation

Ionic verwendet ganz normales JavaScript.

### REST-API

```javascript
const response = await fetch("/api/tasks");
const tasks = await response.json();
```

### Daten senden

```javascript
await fetch("/api/tasks", {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        title: "Neue Aufgabe"
    })
});
```

### WebSocket

```javascript
const socket = new WebSocket("wss://example.com/live");

socket.onmessage = event => {
    console.log(event.data);
};

socket.onopen = () => {
    socket.send("Hallo Server!");
};
```

### Lokale Daten

Für einfache Werte:

```javascript
localStorage.setItem("name", "Midnight Worker");

const name = localStorage.getItem("name");
```

Für größere Datenmengen:

- IndexedDB
    
- SQLite mit sql.js
    
- Native SQLite über ein Capacitor-Plugin
    

## 17. Ionic mit Capacitor verwenden

Ionic ist die Benutzeroberfläche, Capacitor verpackt sie als Android-App.

Ein bestehendes Capacitor-Projekt aktualisieren:

```bash
npx cap sync android
```

Android-Projekt öffnen:

```bash
npx cap open android
```

Android-App starten:

```bash
npx cap run android
```

Eine Debug-APK bauen:

```bash
cd android
./gradlew assembleDebug
```

## 18. Die wichtigsten Merksätze

**Ionic = HTML-Komponenten für mobile Benutzeroberflächen.**

**JavaScript = Programmlogik und Ereignisse.**

**CSS = Gestaltung und Anpassung.**

**Capacitor = Android-Integration und native Gerätefunktionen.**

**SQLite / IndexedDB = lokale Speicherung.**

**REST / WebSockets = Kommunikation mit Servern.**

Du benötigst für Ionic keine zusätzliche Programmiersprache. HTML, CSS und JavaScript reichen aus.

---

Offizielle Dokumentation: [https://ionicframework.com/docs/components](https://ionicframework.com/docs/components)

JavaScript-Einstieg: [https://ionicframework.com/docs/javascript/quickstart](https://ionicframework.com/docs/javascript/quickstart)

Capacitor: [https://capacitorjs.com/docs](https://capacitorjs.com/docs)