-- Add new column
-- depends: 20231220_01_Q0xdg-create-new-users-and-todos-table
-- transactional: false
ALTER TABLE `yoyomigration`.todos_yoyo ADD completion_time TIMESTAMP;

