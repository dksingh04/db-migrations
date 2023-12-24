-- Create new users and todos table
-- depends:
-- transactional: false
CREATE TABLE `users_yoyo` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `email` varchar(100) NOT NULL,
  `username` varchar(50) DEFAULT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `hashed_password` varchar(200) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `username` (`username`),
  KEY `ix_users_alembic_id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `todos_yoyo` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `description` varchar(400) DEFAULT NULL,
  `priority` int DEFAULT NULL,
  `complete` tinyint(1) DEFAULT NULL,
  `owner_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `owner_id` (`owner_id`),
  KEY `ix_todos_alembic_id` (`id`),
  CONSTRAINT `todos_alembic_ibfk_1` FOREIGN KEY (`owner_id`) REFERENCES `users_yoyo` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


