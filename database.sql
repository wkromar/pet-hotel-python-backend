database name = pet-hotel-group-project

CREATE TABLE "owners"(
    "id" SERIAL PRIMARY KEY,
    "name" VARCHAR(100) NOT NULL
);

CREATE TABLE "pets"(
    "id" SERIAL PRIMARY KEY,
    "owner_id" INT REFERENCES "owners",
    "pet_name" varchar,
    "breed" VARCHAR(100),
    "color" VARCHAR(100),
    "check_in" VARCHAR(100)
);

INSERT INTO "owners" ("name")
VALUES ('Kevin'), ('Mike'), ('Sean'), ('Woody');

INSERT INTO "pets" ("owner_id", "pet_name", "breed", "color", "check_in")
VALUES (1, 'Roux', 'Golden Lab mix', 'Golden', null), (2, 'Dave', 'Black Lab', 'Black', 'Feb 2'), (3, 'Carl', 'Pomeranian', 'White', null), (4, 'Bruce', 'Tabby', 'Brown Striped', 'Feb 22');

DROP TABLE "owners";
DROP TABLE "pets";