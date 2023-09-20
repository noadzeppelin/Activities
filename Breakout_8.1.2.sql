--Find the average Charge Time Hrs per year by Car Make. Answer should include Year, ChargeTimeHrs, and carMake
SELECT DISTINCT dimCar.carMake, substr(factCharge.dateCreated,0,5) as 'Year', round(avg(factCharge.chargeTimeHrs), 2)   
FROM factCharge 
INNER JOIN dimUser 
ON factCharge.userID = dimUser.userId
LEFT JOIN dimcar 
ON dimUser.carID = dimCar.carID
GROUP BY 1
HAVING carMake IS NOT NULL
ORDER BY 3 DESC;



--The EVCHarging Company you work for is expanding operations abroad. Add a Column to dimUser called "Country" with all values equal to "USA". Drop DistanceHome from the table. Select and display the final results of your table