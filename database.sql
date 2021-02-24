database name = pet-hotel-group-project

CREATE TABLE "owners"(
    "id" SERIAL PRIMARY KEY,
    "name" VARCHAR(100) NOT NULL,
    "num_of_pets" int
)

CREATE TABLE "pets"(
    "id" SERIAL PRIMARY KEY,
    "owner_id" INT,
    "pet_name" varchar,
    "breed" VARCHAR(100),
    "color" VARCHAR(100),
    "check_in" BOOLEAN DEFAULT('false')
)