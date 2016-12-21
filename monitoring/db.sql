BEGIN;
--
-- Create model Counter
--
CREATE TABLE `dashboard_counter` (`counter_id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `timestamp` datetime(6) NOT NULL, `tag` varchar(200) NOT NULL, `value` integer UNSIGNED NOT NULL);
--
-- Create model Node
--
CREATE TABLE `dashboard_node` (`node_id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `node_ip` varchar(25) NOT NULL, `probing_frequency` integer UNSIGNED NOT NULL, `created` datetime(6) NOT NULL, `last_probed` datetime(6) NOT NULL, `last_status` varchar(200) NOT NULL, `active` bool NOT NULL, `error_msg` varchar(200) NOT NULL, `last_failure` datetime(6) NOT NULL, `owner_id` integer NOT NULL);
--
-- Create model Service
--
CREATE TABLE `dashboard_service` (`service_id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `name` varchar(200) NOT NULL, `created` datetime(6) NOT NULL, `active` bool NOT NULL, `owner_id` integer NOT NULL);
--
-- Add field service_id to node
--
ALTER TABLE `dashboard_node` ADD COLUMN `service_id_id` integer NOT NULL;
ALTER TABLE `dashboard_node` ALTER COLUMN `service_id_id` DROP DEFAULT;
--
-- Add field node_id to counter
--
ALTER TABLE `dashboard_counter` ADD COLUMN `node_id_id` integer NOT NULL;
ALTER TABLE `dashboard_counter` ALTER COLUMN `node_id_id` DROP DEFAULT;
ALTER TABLE `dashboard_node` ADD CONSTRAINT `dashboard_node_owner_id_ebc327ed_fk_auth_user_id` FOREIGN KEY (`owner_id`) REFERENCES `auth_user` (`id`);
ALTER TABLE `dashboard_service` ADD CONSTRAINT `dashboard_service_owner_id_22b754ff_fk_auth_user_id` FOREIGN KEY (`owner_id`) REFERENCES `auth_user` (`id`);
CREATE INDEX `dashboard_node_47f05606` ON `dashboard_node` (`service_id_id`);
ALTER TABLE `dashboard_node` ADD CONSTRAINT `dashboard_service_id_id_22bb96ae_fk_dashboard_service_service_id` FOREIGN KEY (`service_id_id`) REFERENCES `dashboard_service` (`service_id`);
CREATE INDEX `dashboard_counter_e2514c22` ON `dashboard_counter` (`node_id_id`);
ALTER TABLE `dashboard_counter` ADD CONSTRAINT `dashboard_counter_node_id_id_dc017437_fk_dashboard_node_node_id` FOREIGN KEY (`node_id_id`) REFERENCES `dashboard_node` (`node_id`);

COMMIT;
