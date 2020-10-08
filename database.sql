CREATE DATABASE IF NOT EXISTS mydtb;
USE mydtb;
CREATE TABLE IF NOT EXISTS Worlds (
    world_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(32),
    descr TEXT,
    story TEXT
);

CREATE TABLE IF NOT EXISTS Countries (
    country_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(32),
    world_id INT UNSIGNED NOT NULL,
    FOREIGN KEY (world_id) REFERENCES Worlds (world_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Events (
    event_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(64),
    descr TEXT,
    story TEXT,
    event_type VARCHAR(32),
    start_date SMALLINT,
    start_month SMALLINT,
    start_year SMALLINT,
    end_date SMALLINT,
    end_month SMALLINT,
    end_year SMALLINT,
    world_id INT UNSIGNED NOT NULL,
    FOREIGN KEY (world_id) REFERENCES Worlds(world_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS CountryEvents (
    event_id INT UNSIGNED NOT NULL,
    country_id INT UNSIGNED NOT NULL,
    PRIMARY KEY (event_id, country_id),
    FOREIGN KEY (event_id) REFERENCES Events(event_id) ON DELETE CASCADE,
    FOREIGN KEY (country_id) REFERENCES Countries(country_id) ON DELETE CASCADE
);