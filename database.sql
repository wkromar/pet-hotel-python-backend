database name = pet-hotel-group-project

CREATE TABLE "owners"(
    "id" SERIAL PRIMARY KEY,
    "name" VARCHAR(100) NOT NULL
);

CREATE TABLE "pets"(
    "id" SERIAL PRIMARY KEY,
    "owner_id" INT REFERENCES "owners" ON DELETE CASCADE,
    "pet_name" varchar,
    "breed" VARCHAR(100),
    "color" VARCHAR(100),
    "check_in" DATE DEFAULT NOW()
);

INSERT INTO "owners" ("name")
VALUES ('Kevin'), ('Mike'), ('Sean'), ('Woody');

INSERT INTO "pets" ("owner_id", "pet_name", "breed", "color", "check_in")
VALUES (2, 'Dave', 'Black Lab', 'Black', '2/2/2021'), (4, 'Bruce', 'Tabby', 'Brown Striped', '2/22/2021');

INSERT INTO "pets" ("owner_id", "pet_name", "breed", "color")
VALUES (1, 'Roux', 'Golden Lab mix', 'Golden'), (3, 'Carl', 'Pomeranian', 'White');

DROP TABLE "owners";
DROP TABLE GROUP BY "owners".id, "pets".id;BLE "pets";


SELECT "owners".*, COUNT("pets".id) AS "pet_count" FROM "owners" LEFT JOIN "pets" ON "owners".id = "pets".ow