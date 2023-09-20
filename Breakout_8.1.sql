
--1. Use LEFT JOIN and join `factcharge` and `dimFacility` together. Select all of the rows and order the output by `typeFacility`.
-- SELECT *
-- FROM factCharge
-- LEFT JOIN dimFacility
-- ON factCharge.facilityID = dimFacility.FacilityKey
-- ORDER BY typeFacility;

--2. Use INNER JOIN to join`factCharge` and `DimUser`, and add a second join in the query and LEFT JOIN `dimCar`. Select the distinct users, make, Model, and  the price in Euros multiplied by 1.09--> name this column `priceUSD`.

SELECT DISTINCT factCharge.userId, dimCar.carMake, dimCar.carModel, (1.09 * dimCar.priceEuro) as 'USD_price'
FROM factCharge 
INNER JOIN dimUser 
ON factCharge.userID = dimUser.userId
LEFT JOIN dimcar 
ON dimUser.carID = dimCar.carID
GROUP BY factCharge.userId
HAVING dimCar.carMake IS NOT NULL;
