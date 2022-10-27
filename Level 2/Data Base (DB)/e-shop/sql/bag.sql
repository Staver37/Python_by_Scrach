CREATE TABLE "Bag"
(
id          INTEGER  PRIMARY KEY ,
client_id   numeric(21)  NOT NULL 

--CONSTRAINT fk_bag  FOREIGN  KEY (client_id)
--REFERENCES  Client(id)
);

ALTER TABLE "Bag"
ADD      CONSTRAINT fk_bag  FOREIGN  KEY (client_id)
REFERENCES  "Client"(id);

INSERT INTO "Bag"(id,client_id )values (2,1661148593640792000);

INSERT INTO "Bag"(id,client_id )values (3,166114859364079200);

DELETE FROM "Bag" WHERE id = 3;