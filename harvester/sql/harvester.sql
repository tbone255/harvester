# Harvester MySQL Stub

CREATE TABLE `plant` (
    `plant_id`          INTEGER      NOT NULL AUTO_INCREMENT,
    `type`              VARCHAR(32)  NOT NULL,
    `scientific_name`   VARCHAR(128) NOT NULL,
    `description`       VARCHAR(512) NOT NULL,
    `planter_id`        INTEGER,
    PRIMARY KEY (`plant_id`),
    FOREIGN KEY (`planter_id`) REFERENCES `planter` (`planter_id`)
) ENGINE=InnoDB;

CREATE TABLE `planter` (
    `planter_id`        INTEGER     NOT NULL AUTO_INCREMENT,
    `x_coordinate`      INTEGER     DEFAULT NULL,
    `y_coordinate`      INTEGER     DEFAULT NULL,
    `length`            INTEGER     NOT NULL,
    `width`             INTEGER     NOT NULL,
    PRIMARY KEY (`planter_id`)
) ENGINE=InnoDB;

CREATE TABLE `event` (
    `event_id`          INTEGER      NOT NULL AUTO_INCREMENT,
    `event_type`        VARCHAR(32)  NOT NULL,
    `description`       VARCHAR(128) NOT NULL,
    PRIMARY KEY (`event_id`)
) ENGINE=InnoDB;

CREATE TABLE `nutrition` (
    `nutrition_id`      INTEGER      NOT NULL AUTO_INCREMENT,
    `brand`             VARCHAR(32)  DEFAULT    NULL,
    `type`              VARCHAR(32)  NOT NULL,
    `description`       VARCHAR(128) NOT NULL,
    PRIMARY KEY (`nutrition_id`)
) ENGINE=InnoDB;

CREATE TABLE `event_log` (
    `event_log_id`      INTEGER     NOT NULL AUTO_INCREMENT,
    `event_id`          INTEGER     NOT NULL,
    `plant_id`          INTEGER,
    `planter_id`        INTEGER,
    `nutrition_id`      INTEGER     DEFAULT NULL,
    `timestamp`         DATETIME    DEFAULT NULL,
    `description`       VARCHAR(256),
    PRIMARY KEY (`event_log_id`),
    FOREIGN KEY (`event_id`) REFERENCES `event` (`event_id`),
    FOREIGN KEY (`plant_id`) REFERENCES `plant` (`plant_id`),
    FOREIGN KEY (`planter_id`) REFERENCES `planter` (`planter_id`)
) ENGINE=InnoDB;

