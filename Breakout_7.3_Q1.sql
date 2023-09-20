-- 1. Using factCharge and dimDay, find out which day of the week has the highest average charging time? Return `dayOfWeek` and `avgChargeTime`. Please round `avgChargeTime` to two decimal places and order the result set from highest to lowest `avgChargeTime`.

SELECT dimDay.dayOfWeek as 'dayofWeek',
ROUND(avg(factCharge.chargeTimeHrs),2) as 'avgTotalHrs'
FROM factCharge 
INNER JOIN dimDay 
ON factCharge.dayID = dimDay.dateKey
GROUP BY 1
ORDER BY 2 DESC;