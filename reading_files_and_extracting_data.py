import pandas as pd

if __name__ == '__main__':
    division_list = []
    cities_list = []
    df = pd.read_csv('REGION_CITY_MAPPING_DATA .csv')

    for index, row in df.iterrows():
        division_list.append(
            {
                'code': row['REGION_CODE'],
                'name': row['REGION_NAME'][:-4]
            }
        )

        cities_list.append(
            {
                'name': row['DISTRICT_OR_CITY_NAME'],
                'code': row['DISTRICT_OR_CITY_CODE'],
                'division_code': row['REGION_CODE']
            }
        )

    print(division_list)
    print(cities_list)