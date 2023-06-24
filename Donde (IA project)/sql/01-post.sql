CREATE TABLE `post`
(
    `id`      INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `subject` VARCHAR(255) NOT NULL,
    `content` TEXT         NOT NULL,
    PRIMARY KEY (`id`)
) COLLATE='utf8_polish_ci'
;
