-- 1. Using factCharge and dimDay, find out which day of the week has the highest average charging time? Return `dayOfWeek` and `avgChargeTime`. Please round `avgChargeTime` to two decimal places and order the result set from highest to lowest `avgChargeTime`.

-- SELECT dimDay.dayOfWeek as 'dayofWeek',
-- ROUND(sum(factCharge.chargeTimeHrs),2) as 'sumTotalHrs'
-- FROM factCharge 
-- INNER JOIN dimDay 
-- ON factCharge.dayID = dimDay.dateKey
-- GROUP BY 1
-- ORDER BY 2 DESC;

-- 2. Using dimUser and factCharge, which app platform had the most amount of charging sessions. Return `appPlatform` and `numCharges`. Order the result set from highest to lowest number of charges. 

SELECT u.appPlatform as 'appPlatform',
count(*) as 'numCharges'
FROM factCharge f
INNER Join dimUser u
ON f.userId = u.userId
GROUP BY u.appPlatform
ORDER BY 2 DESC;