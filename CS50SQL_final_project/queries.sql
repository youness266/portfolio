-- In this SQL file, write (and comment!) the typical SQL queries users will run on your database

-- Find all Hotels given a Country and a City
SELECT * FROM "hotels"
WHERE "country" = 'Morocco' 
AND 
"city" = 'Fes'
ORDER BY "rating" DESC;

-- Find available Rooms given a hotel name
SELECT * FROM "available_rooms"
JOIN "hotels" ON "hotels"."name" = "available_rooms"."hotel_name"
WHERE "hotel_id" = (
    SELECT "hotels"."id" FROM "hotels"
    WHERE "name" = 'Barcelo'
);

-- Make a Reservation on a certain month
INSERT INTO "reservations" ("guest_id","room_id","hotel_id","reservation_date","check_in","check_out","amount")
VALUES (
    (SELECT "id" FROM "guests"
    WHERE "name" = 'Albert' AND "id_card" = 'ABC123'),
    12,
    4,
    DATE('now'),
    '2026-11-01',
    '2026-12-01',
    2000
);


--Adding employees
INSERT INTO "staff" ("name","hotel_id","role")
VALUES ("Fred",1,"manager");

--Changing Hotel's name
UPDATE "hotels" SET "name" = 'Zalagh'
WHERE "id" = 3;

--Firing an employee
DELETE FROM "staff"
WHERE "id" = 13;

--adding guests
INSERT INTO "guests" ("name","id_card")
VALUES ("William.a.jr","DEF456");
