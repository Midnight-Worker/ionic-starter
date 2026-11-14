SQLite mit Ionic und JavaScript

1. Bibliothek einbinden

In deiner index.html:

<script src="lib/sqljs/sql-wasm.js"></script>
<script defer src="main.js"></script>

Die Dateien sql-wasm.js und sql-wasm.wasm liegen beide in lib/sqljs/.

2. Datenbank öffnen

In main.js:

const SQL = await initSqlJs({
    locateFile: file => "lib/sqljs/" + file
});

const db = new SQL.Database();

Damit erzeugst du eine neue SQLite-Datenbank im Arbeitsspeicher.

3. Tabelle erstellen

db.run(`
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
    )
`);

4. Datensatz einfügen (INSERT)

db.run(
    "INSERT INTO users (name) VALUES (?)",
    ["Max"]
);

Das ? ist ein Platzhalter für den übergebenen Wert.

5. Datensätze auslesen (SELECT)

const result = db.exec("SELECT * FROM users");

console.log(result[0]?.values ?? []);

Beispielausgabe:

[
    [1, "Max"]
]

Alternativ mit Spaltennamen:

const stmt = db.prepare("SELECT * FROM users");

while (stmt.step()) {
    console.log(stmt.getAsObject());
}

stmt.free();

6. Datensatz ändern (UPDATE)

db.run(
    "UPDATE users SET name = ? WHERE id = ?",
    ["Anna", 1]
);

7. Datensatz löschen (DELETE)

db.run("DELETE FROM users WHERE id = ?", [1]);

8. Datenbank als Datei exportieren

const bytes = db.export();

bytes enthält die vollständige SQLite-Datenbank als Uint8Array.

Achtung: Ohne zusätzliche Speicherung gehen die Daten beim Neuladen der Webseite verloren.

9. Dauerhaft mit IndexedDB speichern

Einmalig IndexedDB öffnen:

const request = indexedDB.open("app", 1);

request.onupgradeneeded = () => {
    request.result.createObjectStore("files");
};

const storage = await new Promise((resolve, reject) => {
    request.onsuccess = () => resolve(request.result);
    request.onerror = () => reject(request.error);
});

Datenbank speichern:

async function saveDB() {
    const tx = storage.transaction("files", "readwrite");
    tx.objectStore("files").put(db.export(), "database");

    await new Promise((resolve, reject) => {
        tx.oncomplete = resolve;
        tx.onerror = () => reject(tx.error);
        tx.onabort = () => reject(tx.error);
    });
}

Gespeicherte Datenbank beim Start laden:

async function loadDB() {
    const tx = storage.transaction("files", "readonly");
    const req = tx.objectStore("files").get("database");

    const bytes = await new Promise((resolve, reject) => {
        req.onsuccess = () => resolve(req.result);
        req.onerror = () => reject(req.error);
    });

    return bytes
        ? new SQL.Database(bytes)
        : new SQL.Database();
}

Zum Verwenden muss db veränderbar sein (let db). Rufe loadDB() beim Start auf und verwende die zurückgegebene Datenbank. Rufe nach jeder Änderung await saveDB() auf.

10. SQL-Cheatsheet

Aufgabe

SQL

Tabelle erstellen

CREATE TABLE

Daten einfügen

INSERT INTO

Daten lesen

SELECT

Daten ändern

UPDATE

Daten löschen

DELETE

Datensätze zählen

SELECT COUNT(*)

Daten sortieren

ORDER BY

Daten filtern

WHERE

Merksatz:

db.run() – SQL ausführen

db.exec() – Daten abfragen

db.prepare() – vorbereitete Abfrage

db.export() – SQLite-Datei exportieren

IndexedDB – Datenbank dauerhaft speichern

sql.js arbeitet im Arbeitsspeicher. IndexedDB übernimmt die dauerhafte Speicherung im Browser oder in der Android-WebView.
