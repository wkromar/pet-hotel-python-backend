## FILES TO CREATE
    [ ] - config.py
    [ ] - connect.py (is this just where our routes live?)
    [ ] - database.ini

## ROUTES NEEDED
    [ ] - GET
        [ ] - History - join owners & pets tables?
        [ ] - Owners
    [ ] - POST
        [ ] - Add pet
    [ ] - PUT
        [ ] - Check in/out pet
    [ ] - DELETE
        [ ] - Remove pet
        [ ] - Remove owner if no pets assigned

## Table structures
    db - python-pet-hotel
    OWNERS
        ID serial key
        NAME varchar
        NUM_OF_PETS int (? maybe doesn't need to be here ?)

    PETS
        ID serial key
        OWNER_ID reference int
        PET_NAME varchar
        BREED varchar
        COLOR varchar
        CHECK_IN boolean