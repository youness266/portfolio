-- In this SQL file, write (and comment!) the schema of your database, including the CREATE TABLE, CREATE INDEX, CREATE VIEW, etc. statements that compose it

-- Creating the tables 
CREATE TABLE "hotels" (
    "id" INTEGER,
    "name" TEXT NOT NULL UNIQUE,
    "city" TEXT NOT NULL,
    "country" TEXT NOT NULL,
    "rating" NUMERIC,
    PRIMARY KEY ("id")
);

CREATE TABLE "rooms" (
    "id" INTEGER,
    "hotel_id" INTEGER,
    "number" INTEGER,
    "reserved" INTEGER NOT NULL DEFAULT 0 CHECK ("reserved" IN (0, 1)),
    PRIMARY KEY ("id"),
    FOREIGN KEY ("hotel_id") REFERENCES "hotels"("id") ON DELETE CASCADE,
    UNIQUE ("hotel_id","number")
);

CREATE TABLE "staff" (
    "id" INTEGER,
    "name" TEXT NOT NULL,
    "hotel_id" INTEGER,
    "role" TEXT NOT NULL,
    PRIMARY KEY ("id"),
    FOREIGN KEY ("hotel_id") REFERENCES "hotels"("id") ON DELETE CASCADE
);

CREATE TABLE "reservations" (
    "id" INTEGER,
    "guest_id" INTEGER,
    "room_id" INTEGER,
    "hotel_id" INTEGER,
    "reservation_date" DATE NOT NULL,
    "check_in" DATE NOT NULL,
    "check_out" DATE NOT NULL,
    "amount" REAL NOT NULL,
    PRIMARY KEY ("id"),
    FOREIGN KEY ("guest_id") REFERENCES "guests"("id") ON DELETE CASCADE,
    FOREIGN KEY ("room_id") REFERENCES "rooms"("id") ON DELETE CASCADE,
    FOREIGN KEY ("hotel_id") REFERENCES "hotels"("id") ON DELETE CASCADE
);

CREATE TABLE "guests" (
    "id" INTEGER,
    "name" TEXT NOT NULL,
    "card_id" TEXT NOT NULL,
    PRIMARY KEY ("id")
);

-- Creating Views
CREATE VIEW "available_rooms" AS 
SELECT "rooms"."number" AS "room Number","hotels"."name" AS "Hotel",
"hotels"."city" AS "City" , "hotels"."country" AS "Country",
"hotels"."rating" AS "Rating"
FROM "rooms"
JOIN "hotels" ON "hotels"."id" = "rooms"."hotel_id"
WHERE "rooms"."reserved" = 0;

-- Creating Indexes
CREATE INDEX "hotels_location" ON "hotels"("country","city");
CREATE INDEX "rooms_reserved" ON "rooms"("reserved");
