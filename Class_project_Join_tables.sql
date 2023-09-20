SELECT EVIncentivesbyState.State, EVIncentivesbyState.TaxEVIncentiveAmount, EVRegMerged.TotalRegCount, EVRegMerged.EVRegistrationCount, gas_price_by_state.gasoline, EVRegMerged.StatePopulations, Income.MedianIncome
FROM EVIncentivesbyState
LEFT JOIN EVRegMerged
ON EVIncentivesbyState.State = EVRegMerged.Stateid
LEFT JOIN gas_price_by_state
ON EVIncentivesbyState.State = gas_price_by_state.name
LEFT JOIN Income
ON EVIncentivesbyState.State = Income.stateName
ORDER by gas_price_by_state.gasoline DESC;


-- SELECT EVIncentivesbyState.*, EVIncentivesbyState.*, EVRegMerged.*, EVRegMerged.*, gas_price_by_state.*, EVRegMerged.*, Income.*
-- FROM EVIncentivesbyState
-- LEFT JOIN EVRegMerged
-- ON EVIncentivesbyState.State = EVRegMerged.Stateid
-- LEFT JOIN gas_price_by_state
-- ON EVIncentivesbyState.State = gas_price_by_state.name
-- LEFT JOIN Income
-- ON EVIncentivesbyState.State = Income.stateName;

-- UPDATE Income
-- SET stateName = REPLACE(Income.stateName,' ','');
SELECT replace(EVIncentivesbyState.State,' ', '')
FROM EVIncentivesbyState;
-- 
-- UPDATE EVRegMerged
-- SET Stateid = REPLACE(EVRegMerged.Stateid, ' ', '')


-- UPDATE Income
-- SET MedianIncome= replace(Income.MedianIncome, ',', '')
-- WHERE Income.MedianIncome IS NOT NULL;




