SECONDS_IN_A_YEAR = 365 * 24 * 60 * 60

BIRTHS_PER_YEAR = SECONDS_IN_A_YEAR // 7
DEATHS_PER_YEAR = SECONDS_IN_A_YEAR // 13
IMMIGRANT_PER_YEAR = SECONDS_IN_A_YEAR // 45
DELTA_POPULATION = BIRTHS_PER_YEAR - DEATHS_PER_YEAR + IMMIGRANT_PER_YEAR

population_2018 = 7600000000000
population_2019 = population_2018 + DELTA_POPULATION
population_2020 = population_2019 + DELTA_POPULATION
population_2021 = population_2020 + DELTA_POPULATION
population_2022 = population_2021 + DELTA_POPULATION
population_2023 = population_2022 + DELTA_POPULATION

print('The population in 2018 is', population_2018)
print('The population in 2019 is', population_2019)
print('The population in 2020 is', population_2020)
print('The population in 2021 is', population_2021)
print('The population in 2022 is', population_2022)
print('The population in 2023 is', population_2023)
