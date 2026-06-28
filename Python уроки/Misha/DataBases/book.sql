
CREATE TABLE IF NOT EXISTS `book` (
	`book_id`	INTEGER PRIMARY KEY AUTO_INCREMENT,
	`title`	TEXT,
	`author`	TEXT,
	`price`	INTEGER,
	`amount` INTEGER
);
INSERT INTO `book` VALUES (1,'Мастер и Маргарита','Булгаков М.А.',670.99,3);
INSERT INTO `book` VALUES (2,'Белая гвардия','Булгаков М.А.',540.5,5);
INSERT INTO `book` VALUES (3,'Идиот','Достоевский Ф.М.',460,10);
INSERT INTO `book` VALUES (4,'Братья Карамазовы','Достоевский Ф.М.',799.01,2);
COMMIT;
