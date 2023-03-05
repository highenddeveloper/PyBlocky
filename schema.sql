DROP TABLE IF EXISTS blocks;

CREATE TABLE blocks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    header TEXT NOT NULL,
    hash TEXT NOT NULL
);

