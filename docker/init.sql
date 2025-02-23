CREATE TABLE IF NOT EXISTS games (
    id SERIAL PRIMARY KEY,
    steam_id INT UNIQUE NOT NULL,
    name TEXT NOT NULL,
    developer TEXT,
    genre TEXT,
    publisher TEXT,
    release_date DATE
);


CREATE TABLE IF NOT EXISTS reviews (
    id SERIAL PRIMARY KEY,
    game_id INT REFERENCES games(id) ON DELETE CASCADE,
    review_text TEXT NOT NULL,
    sentiment TEXT CHECK (sentiment IN ('positive', 'neutral', 'negative')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total_positive INT,
    total_negative INT
);