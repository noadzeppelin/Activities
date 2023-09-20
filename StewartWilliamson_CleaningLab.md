# 8.2 Welcome to the SQL Data Cleaning Lab 
<br>
<br>
<br>

# Directions for Today's Self Guided SQL Cleaning Tour
 1. You will be tasked with cleaning a dataset using SQL statements and queries
 2. Follow the instructions of each section
 3. Please record all of your queries and Statements in a Markdown file for submission for Week 8 HW. 
 4. You will have all of 8.2 class to work through the assignment and whatever you have left at the end of class will become this week's SQL HW 


<br>

# TABLE set-up for Tonight's Lab 
1. Please open up DBrowser for SQLite. 
2. Open a New DATABASE and name the DATABASE "SQLCleaningLab"
3. Import the csv file called "SavvyCoders_SQL_CleaningLab.csv" from section 08 resources
4. Name the table `evCars'
5. In the pop up window: Make sure that your field separator is a comma and your quote character is a single quote. 
6. In the pop up window: Glance over the data and make sure it looks correct (data in row/column format)
7. Open up the advanced menu and select the option to "disable data type selection"
8. Press okay to import the table. 

<br>

 ### First look at our table `evCars` after importing the table
 
<p><br></p>
<img src = "images/SavvyCoders_SQL_CleaningLab_evCars.png" alt="tablediagram" width = "100%" height="100%" style="display: block; margin: 0 auto"/>
<p><br></p>


 
# Section 1

- If you look at the column `Accel` you can see that each value has the ' sec' suffix on the value. 
- This creates an issue becasue if you ever wanted to run a summary function like AVG() on the `Accel` values you would not be able to becasue the datatype would most likely be a string and not an acceptable type to run that function. 
- Our Job is to remove that suffix from the `Accel` column. We are also going to rename the column with the units in the column name to inform the person looking at the table what the column units are. 
<br>

### - 1.1 Review the column that you are looking to change
<br>

```SQL

SELECT Accel FROM evCars

```
<br>

### - 1.2 Selecting the correct string function

- We would like to remove ' sec'  from each value in the `Accel` column. 
- Choose the appropriate string function from the string function list. There may be more then one way to accomplish this task. 
- Please place your queries in a .md file for review. Whatever you do not finish is considered HW. 
<br>

```SQL

RTRIM(string, character)

```
<br>

### - 1.3 Visualizing the changes before making them 

- Use a select statement to visualize the original column and the changes that are made by the string function side by side in the result set. 
- Also take note of how many rows are returned in this select statement. (you can use the rowid on the far left of the result set---> scroll to the bottom number)
- You will use this number to confirm you are changing the correct amount of rows in the next step. 
<br>

```SQL
SELECT Accel, RTRIM(Accel, '  sec') 
FROM evCars

```
<br>

### - 1.4 UPDATE the records 

- Write the update statement to set `Accel` to equal the return value of the string function that you chose to use in 1.2.

<br>

```SQL

UPDATE evCars 
SET Accel = RTRIM(Accel, ' sec')

```
<br>

### - 1.5 Check your work
- It is good practice to check over the rows that you changed. Write a select statement to look at the column again. (you can reuse the code you wrote above)
<br>

```SQL

SELECT columnname FROM tablename;

```
<br>

### - 1.6 Rename the column
 - Rename the `Accel` column to `accelSec`
 <br>

```SQL
ALTER TABLE evCars
 RENAME Accel TO AccelSec
```

<br>


# Table Update
<p><br></p>
<img src = "images/SavvyCoders_SQL_section1tableupdate.png" alt="tablediagram" width = "100%" height="100%">
<p><br></p>

# Section 2

- We are going to go through basically the same process in Section 1 but for each of the following columns:
    ```SQL
    SELECT TopSpeed, Range, efficiency, FastCharge
    FROM evCars
    LIMIT 10
    ```

- I will outline `Topspeed` in section 2. After this section you will be instructed to do `Range`, `efficiency`, and `FastCharge`. 
- Rememeber please place your answers and queries in a .md file for review. 
<br>


### - 2.1 Review the column that you are looking to change 
- Write a query to look at all the records in the `Topspeed` column.  
<br>

```SQL

SELECT TopSpeed
FROM CleaningLab;

```
<br>

### - 2.2 Selecting the correct String Function

- We would like to remove 'km/h' from each value in the column `TopSpeed`. 
- Choose the appropriate string function from the string function list. There may be more then one way to accomplish this task.  

```SQL

SELECT rtrim(TopSpeed,5)
FROM CleaningLab;

```

### - 2.3 Visualizing the Changes before making them 

- Use a select statement to visualize the original column, `TopSpeed` and the changes that are made by the string function side by side in the result set. 
- Take note of how many rows are returned in this SELECT statement. You will use this number to confirm you are changing the correct amount of rows later. 

```SQL
SELECT TopSpeed, rtrim(TopSpeed)
FROM CleaningLab;

```

### - 2.4 UPDATE the records

- Write the update statement to set `TopSpeed` to equal the return value of the string function you chose in 2.2
<br>

```SQL

UPDATE CleaningLab
SET TopSpeed = RTRIM(TopSpeed, ' km/h')

```

### - 2.5 Check your work 
- Write a select statement to look at the column again. (you can reuse the code you wrote above in 2.1)
<br>

```SQL

SELECT TopSpeed FROM CleaningLab;

```

### - 2.6 Convert the units to MPH
- Let's convert the `TopSpeed` from km/h to MPH
- Write a select statement to multiply the speed by 0.621371. Return  original `Topspeed` and calculated `TopspeedMPH`. Round the answer to 1 decimal place . 

```SQL
SELECT TopSpeedkmh, round(TopSpeedkmh * 0.621371, 1) as 'TopSpeedMph'
FROM CleaningLab;

```
- Write and executing the above query to see the original and the converted value side by side
- Turn this query into an UPDATE statement

```SQL

UPDATE CleaningLab 
SET TopSpeedkmh = ROUND(TopSpeedkmh * 0.621371, 1) 

```
- use your query from 2.5 to check the column to make sure the changes are what yoiu expected. 

### - 2.7 Rename the column
 <br>

```SQL
ALTER TABLE CleaningLab
RENAME TopSpeedkmh TO TopSpeedmph;

```
<br>

### - 2.8  Select All of the records to get a look at the whole table with your recent changes. 
```SQL
SELECT * 
FROM CleaningLab

```

<br>

# Table Update
<p><br></p>
<img src = "images/SavvyCoders_SQL_Section2end.png" alt="tablediagram" width = "100%" height="100%">
<p><br></p>



# Section 3 

- We are going to go through basically the same process in Section 2 but `Range`. We will continue with `efficiency`, and `FastCharge` in the following sections. 
- For these sections there will be less help spelled out for you. 
- Rememeber please place your answers and queries in a .md file for review. 
### - 3.1 Review the column that you are looking to change 
```SQL
SELECT Range 
FROM CleaningLab;
```
### - 3.2 Selecting the correct String Function
- We would like to remove 'km' from each value in the column `Range`. 
- Choose the appropriate string function from the string function list. There may be more then one way to accomplish this task. 
```SQL
SELECT RTRIM(Range, ' km') 
FROM CleaningLab;

```

### - 3.3 Visualizing the Changes before making them 

- Use a select statement to visualize the original column, `Range` and the changes that are made by the string function side by side in the result set. 
- Take note of how many rows are returned in this SELECT statement. You will use this number to confirm you are changing the correct amount of rows later. 
```SQL
SELECT Range, RTRIM(Range, ' km') 
FROM CleaningLab;
```

### - 3.4 UPDATE the records

- Write the update statement to set `Range` to equal the return value of the string function you chose in 3.2
 ```SQL
UPDATE CleaningLab
SET RANGE = RTRIM(Range, ' km');
```
<br>

### - 3.5 Check your work 
- Write a select statement to look at the column again. (you can reuse the code you wrote above)
```SQL
SELECT Range 
FROM CleaningLab;
```
<br>

### - 3.6 Convert the units to MPH
- Let's convert the `Range` from km to miles. 
- Write a select statement to multiply the distance by 0.621371. Return original `Range` and calculated `RangeMiles`. Round the answer to 1 decimal place.
- After writing and executing the above query to see the original and the converted values, review them side by side and if satisfied then move to the next step
- Turn this query into an UPDATE statement. 
- Use your query from 3.5 to check the column 
<br>

```SQL
SELECT Range, ROUND(RANGE * 0.621371,0) AS 'Range in Miles'
FROM CleaningLab;

UPDATE CleaningLab
SET Range = ROUND(RANGE * 0.621371,0);
```

### - 3.7 Rename the column
 - Rename the `Range` column to `rangeMiles`
 <br>

 ```SQL
ALTER TABLE CleaningLab
RENAME RANGE TO RANGEMiles;
```

### - 3.8  Select All of the records to get a look at the whole table with your recent changes. 
```SQL
SELECT *
FROM CleaningLab;
```
<br>

# Table Update
<p><br></p>
<img src = "images/SavvyCoders_SQL_Section3end.png" alt="tablediagram" width = "100%" height="100%">
<p><br></p>


# SECTION 4 

- We are going to go through basically the same process as section 1-3 but we are going to work on `efficiency` and `FastCharge` at the same time. 
- Rememeber please place your answers and queries in a .md file for review. 
### - 4.1 Write a select statement to review both of the columns that you are looking to change 

```SQL
SELECT Efficiency, FastCharge
FROM CleaningLab;
```
### - 4.2 Selecting the correct String Function that we need to remove for each column.
- We would like to remove ' Wh/km' from each value in the column `efficiency`. 
- We would like to remove ' km/h from `FastCharge`
- Choose the appropriate string function from the string function list. There may be more then one way to accomplish this task. 

```SQL
SELECT RTRIM(Efficiency, ' Wh/km'),  RTRIM(FastCharge, ' km/h')
FROM CleaningLab;
```

### - 4.3 Visualizing the Changes before making them 

- Use a select statement to visualize the original column `efficiency`, the string function removing ' Wh/km', original column  `Fastcharge`, and the string function removing ' km/h'
- Take note of how many rows are returned in this SELECT statement. You will use this number to confirm you are changing the correct amount of rows later. 

```SQL
SELECT Efficiency, RTRIM(Efficiency, ' Wh/km'), FastCharge, RTRIM(FastCharge, ' km/h')
FROM CleaningLab;
```

### - 4.4 UPDATE the records

- Write the update statement to set `Range` to equal the return value of the string function you chose in 4.2
- use this for help: 

```SQL
UPDATE CleaningLab
SET Efficiency = RTRIM(Efficiency, ' Wh/km'),
 FastCharge = RTRIM(FastCharge, ' km/h');
``` 
<br>

### - 4.5 Check your work 
- Write a select statement to look at all of the columns again. (you can reuse the code you wrote above in section4.3)
<br>

```SQL
SELECT Efficiency, FastCharge
FROM CleaningLab;
```

### - 4.6 Convert the `FastCharge` units to MPH
- Let's convert the `FastCharge` from km to miles. 
- Write a select statement to multiply the distance by 0.621371. Return original `FastCharge` and calculated `OneHourFastChargeMiles`. Round the answer to 1 decimal place.
- After writing and executing the above query to see the original and the converted values, review them side by side and if satisfied then move to the next step
- Turn this query into an UPDATE statement. 
- Use your query from 4.5 to check the column 
<br>

```SQL
SELECT FastCharge, ROUND(FastCharge * 0.621371) 'OneHourFastChargeMiles'
FROM CleaningLab;

UPDATE CleaningLab
SET FastCharge = ROUND(FastCharge * 0.621371);
```

### - 4.7 Rename the column
 - Write two seperate ALTER TABLE statements for these. 
 - Rename the `FastCharge` column to `OneHourFastChargeMiles`
 - Rename the `efficiency` column to `efficiencyWHperKM`
 <br>

```SQL
ALTER TABLE CleaningLab
RENAME FastCharge TO OneHourFastChargeMiles;

ALTER TABLE CleaningLab
RENAME Efficiency TO efficiencyWHperKM;
```

### - 4.8 Select All of the records to get a look at the whole table with your recent changes. 
```SQL
SELECT *
FROM CleaningLab;
```

<br>

# Table Update
<p><br></p>
<img src = "images/SavvyCoders_SQL_Section4end.png" alt="tablediagram" width = "100%" height="100%">
<p><br></p>


# SECTION 5 
<br>

### - 5.1 Working with `RapidCharge`
- Write a query that selects `RapidCharge` and counts all the records based on that attribute. (HINT: Remember GROUP BY from SQL Lesson 7.2)
- Take note of the counts for each unique attriute. You should use this to make sure that you are changing the correct number of rows with your update statement. 

```SQL
SELECT RapidCharge, Count(*)
FROM CleaningLab
GROUP BY RapidCharge;
```
### - 5.2 making data cleaning choices 
- This attribute or column designates if the car had Rapid charging capability. 
- we are going to simplify the records 
    - this can be done in a few different ways
        1. you can make the values a boolean: either True or False

<br>

### - 5.3 Please fill in the blank on your .md answer sheet
- For the purpose of this exercise, if the car's `RapidCharge` value equals 'Rapid charging possible' then I want you to change the value to 'TRUE' 
- If the `RapidCharge` value equals 'Rapid charing not possible' then I want you to change the value to 'No'. 
<br>

```SQL
SELECT REPLACE(RapidCharge, 'Rapid charging possible', 'TRUE'), replace(RapidCharge, 'Rapid charging not possible', 'FALSE') 
FROM CleaningLab;
```
### - 5.2 Writing the update Statements  
- use this syntax reminder to help guide your update statement writing
- you are going to write two update statements, one for each of the conditions described above. 
<br>


```SQL
UPDATE CleaningLab
SET RapidCharge = 'TRUE' 
WHERE RapidCharge = 'Rapid charging possible';

UPDATE CleaningLab
SET RapidCharge = 'FALSE' 
WHERE RapidCharge = 'Rapid charging not possible';

```
<br>

# Table Update
<p><br></p>
<img src = "images/SavvyCoders_SQL_Section5end.png" alt="tablediagram" width = "100%" height="100%">
<p><br></p>

# SECTION 6 
### -6.1 Visualize the `Powertrain` records
- Write a query that selects `PowerTrain` and counts all the records. (HINT: Remember GROUP BY from SQL Lesson 7.2)
- Take note of the counts for each unique attriute. You should use this to make sure that you are changing the correct number of rows with your update statement. 
<br>

```SQL
SELECT Powertrain , Count(*)
FROM CleaningLab
GROUP BY Powertrain;
```

### - 6.2 Please fill in the blank on your .md answer sheet
- look at the three DISTINCT values from the query you wrote in 6.1 and fill in the blanks.
- If the PowerTrain equals 'All Wheel Drive' then I want you to change the value to 'AWD'
- If the PowerTrain equals 'Rear Wheel Drive' then I want you to change the value to 'RWD'
- If the PowerTrain equals 'Front Wheel Drive' then I want you to change the value to 'FWD'
<br>

### - 6.3 Write three update statements for the three different conditions 

```SQL
UPDATE CleaningLab
SET PowerTrain = 'AWD' 
WHERE PowerTrain = 'All Wheel Drive';

UPDATE CleaningLab
SET PowerTrain = 'RWD' 
WHERE PowerTrain = 'Rear Wheel Drive';

UPDATE CleaningLab
SET PowerTrain = 'FWD' 
WHERE PowerTrain = 'Front Wheel Drive';
```
### - 6.4 Write a query to Select all of the records to view your changes. 

```SQL
SELECT *
FROM CleaningLab;

```
<br>

# Table Update
<p><br></p>

<img src = "images/SavvyCoders_SQL_Section6end.png" alt="tablediagram" width = "100%" height="100%">
<p><br></p>

# SECTION 7 

### - 7.1 Convert the `PriceEuro` to `PriceUSD` 
- Let's convert the `PriceEuro` into US Dollar  
- Write a select statement to multiply the `PriceEuro` by 1.09 and Return `PriceEuro` and calculated column. Round the calculated column to 2 decimal places. 
- After writing and executing the above query to see the original and the converted values, review them side by side and if satisfied then move to the next step

```SQL
SELECT PriceEuro, ROUND((PriceEuro * 1.09),2) as 'PriceUSD'
FROM CleaningLab;
```

### - 7.2 Write the Update Statements 
- Turn this query into an UPDATE statement. Remember to round the calculation to two decimal points. 
- Write a select query from to check the PriceEuro column 

```SQL
SELECT PriceEuro
FROM CleaningLab;
```
### - 7.3 Rename the Column
- Rename `PriceEuro to PriceUSD`
<br>

```SQL
ALTER TABLE CleaningLab
RENAME PriceEuro TO PriceUSD;
```

# Table Update
<p><br></p>
<img src = "images/SavvyCoders_SQL_Section7end.png" alt="tablediagram" width = "100%" height="100%">
<p><br></p>

# Finish Line 
    1. Push this markdown containing your queries to your homework repo 
    2. Save and push the db file with the cleaned data to your homework repo as well 
    3. Place Jira ticket titled with your name and "SQL Cleaning Lab" and include the link to your repo. 

# Some Additional SQL Topics not covered in this course
- CASE Statements 
- UNION and UNION ALL 
- CTE
- SUBQUERY
- ETL or EXTRACT, TRANSFROM, AND LOAD 