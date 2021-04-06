create table if not exists `Source` (
    `idSource` INT NOT NULL AUTO_INCREMENT,
    `nameSource` VARCHAR(45),
    PRIMARY KEY (`idSource`)
)

create table if not exists `Waifu` (
    `idWaifu` INT NOT NULL AUTO_INCREMENT,
    `nameWaifu` VARCHAR(45),
    `Source_idSource` INT NOT NULL,
    PRIMARY KEY (`idWaifu`),
    FOREIGN KEY (`Source_idSource`) REFERENCES `Source`(`idSource`)
)