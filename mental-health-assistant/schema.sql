CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL
);

CREATE TABLE entries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    date TEXT NOT NULL,
    text TEXT NOT NULL,
    sentiment TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id)
);
