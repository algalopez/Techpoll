CREATE TABLE poll (
    `uuid` CHAR(36) PRIMARY KEY,
    `name` VARCHAR(255) NOT NULL UNIQUE,
    `description` TEXT
);

CREATE TABLE poll_question (
    `uuid` CHAR(36) PRIMARY KEY,
    `poll_uuid` CHAR(36) NOT NULL,
    `topic` VARCHAR(255) NOT NULL,
    `description` VARCHAR(255) NOT NULL,
    `enabled` BOOL NOT NULL DEFAULT 1
);

CREATE TABLE question_options (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `question_uuid` CHAR(36) NOT NULL,
    `options` JSON NOT NULL
);


CREATE TABLE poll_answer (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `user` VARCHAR(255) NOT NULL,
    `key` VARCHAR(255) NOT NULL,
    `datetime` datetime DEFAULT NOW(),
    `poll_uuid` CHAR(36) NOT NULL,
    `question_uuid` CHAR(36) NOT NULL,
    `value` VARCHAR(255)
);

