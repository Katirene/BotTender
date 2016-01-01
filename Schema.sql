CREATE TABLE Spirits
(
id int PRIMARY KEY,
name text
);

CREATE TABLE Mixers
(
id int PRIMARY KEY,
name text
);

CREATE TABLE Garnishes
(
id int PRIMARY KEY,
name text
); 

CREATE TABLE Recipes
(
id int PRIMARY KEY,
Spirits.id int,
Mixers.id int,
Garnishes.id int
);

INSERT INTO Spirits.name
VALUES (rum, vodka, tequilla, bourbon, whiskey, raspberry vodka, scotch, brandy)

INSERT INTO Mixers.name
VALUES (orange juice, sugar water, cranberry juice, soda water, tonic, lime juice, lemon juice, coke, sevenUp)

INSERT INTO Garnishes.name
VALUES (twist of orange, twist of lime, dusting of cinnamon, sprig of mint, skewer of olives, top with a cherry, grapefruit slice,)


