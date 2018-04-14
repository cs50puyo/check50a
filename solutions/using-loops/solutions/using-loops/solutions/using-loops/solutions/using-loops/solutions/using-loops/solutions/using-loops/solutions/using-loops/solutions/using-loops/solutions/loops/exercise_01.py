MILES_PER_KMS = 1 / 1.609
KMS_PER_MILES = 1 / 0.621

print('Miles\tKilometers\t|\tKilometers\tMiles')
for miles, kms in zip(range(1, 11), range(20, 66, 5)):
    miles_to_km = round(miles * KMS_PER_MILES, 3)
    kms_to_miles = round(kms * MILES_PER_KMS, 3)
    print(f'{miles}\t{miles_to_km}\t\t|\t{kms}\t{kms_to_miles}')
