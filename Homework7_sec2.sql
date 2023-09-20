-- SELECT *
-- FROM evRegistry
-- WHERE City IS NULL;
-- 
-- SELECT Make, Model, ElectricVehicleType
-- FROM evRegistry
-- WHERE VIN LIKE '%3E1EA1J';

-- SELECT ModelYear, Make, Model, ElectricVehicleType, ElectricRange
-- FROM evRegistry
-- WHERE Make = 'TESLA' OR Make = 'CHEVROLET'
-- ORDER BY Make, ModelYear DESC;

-- SELECT DISTINCT stationId, COUNT(stationId) AS 'Counts'
-- FROM evCharge
-- GROUP BY stationId
-- ORDER BY 2 DESC
-- LIMIT 5;

SELECT userId, MIN(chargeTimeHrs) AS 'minTime', MAX(chargeTimeHrs) AS 'maxTime'
FROM evCharge
WHERE chargeTimeHrs > .5
GROUP BY userId
ORDER BY 2, 3 DESC;