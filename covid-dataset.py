import pandas as pd

url = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/live/us-counties.csv"
data = pd.read_csv(url)

# print(data.columns)
# state_Indiana = data[data['state'] == 'Indiana']
# print(state_Indiana)

# print(data.head())
# print(data.info())

# major_death = data[data['deaths']> 1000]
# print(major_death)


# major_cases = data[data['cases']> 5000]
# print(major_cases)

################ i want to find a data where there is very less difference between cases and deaths
# data['case_death_diff'] = data['cases'] - data['deaths']
# filtered_data = data[(data['cases'] > 0) & (data['deaths'] > 0)]


# critical_data = filtered_data[filtered_data['case_death_diff'] <100]
# print(critical_data)