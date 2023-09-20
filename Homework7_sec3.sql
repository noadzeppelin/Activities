-- SELECT weekday, round(AVG(chargeTimeHrs),2) AS 'avg_charge_times'
-- FROM evCharge
-- GROUP BY weekday
-- ORDER BY 'avg_charge_times' DESC
-- LIMIT 1;

-- SELECT userId, sum(kwhTotal) as 'totalPower'
-- FROM evCharge
-- GROUP BY userId
-- ORDER BY 2 DESC
-- LIMIT 15;

-- SELECT dimFacility.typeFacility, COUNT(factCharge.stationId)
-- FROM dimFacility
-- INNER JOIN factCharge 
-- ON dimFacility.FacilityKey = factCharge.facilityID
-- GROUP BY 1
-- ORDER BY 2 DESC;

 
SELECT userId, MIN(chargeTimeHrs) AS 'minTime', MAX(chargeTimeHrs) AS 'maxTime'
FROM evCharging
GROUP BY userId
HAVING chargeTimeHrs > 1
ORDER BY 2 DESC, 3 DESC;
