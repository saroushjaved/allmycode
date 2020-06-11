# Sample COVID Analysis with Pandas
# Level : Beginner 


import pandas as pd

 
df = pd.read_csv(r'/home/soroush/Downloads/owid-covid-data.csv')

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# Start by Looking for the colums in the data set

##print(df.columns)

# This gives the following output
##Index(['iso_code', 'continent', 'location', 'date', 'total_cases', 'new_cases',
##       'total_deaths', 'new_deaths', 'total_cases_per_million',
##       'new_cases_per_million', 'total_deaths_per_million',
##       'new_deaths_per_million', 'total_tests', 'new_tests',
##       'total_tests_per_thousand', 'new_tests_per_thousand',
##       'new_tests_smoothed', 'new_tests_smoothed_per_thousand', 'tests_units',
##       'stringency_index', 'population', 'population_density', 'median_age',
##       'aged_65_older', 'aged_70_older', 'gdp_per_capita', 'extreme_poverty',
##       'cvd_death_rate', 'diabetes_prevalence', 'female_smokers',
##       'male_smokers', 'handwashing_facilities', 'hospital_beds_per_thousand'],
##      dtype='object') 


# So There are multiple copies of same countries and we can now remove them

# df.drop_duplicates(subset="iso_code", keep ="first", inplace = True )

# The Above Function has Dropped the duplicates of countries from your data

# Now Lets make a copy with only the data we need

##copy_df = df.iloc[100:200, 1:12]
##print(copy_df)

# So from above we can see that the latest date avaliabel to us is 2020-06-08
# So now lets only have rows that have our latest date


copy_date_latest= df[df['date'].str.contains("2020-06-08")]

#print(copy_date_latest.iloc[1:100, 1:12])

# The Above thing is called masking data. The data is masked and only has the for which for
# Conditional provided at end turns out to eb true

# Now making a final copy of list with only out needed data

copy_final = copy_date_latest.iloc[1:1000, [2,4,6]]
copy_final.reset_index(drop = True, inplace = True)
print(copy_final)


#Saving the file

copy_final.to_csv(r'/home/soroush/Downloads/covid-data.csv')

conties =  census_df[census_df['SUMLEV'] == 50]
    answer = conties[((conties['REGION']==1)|(conties['REGION']==2))&(conties['CTYNAME']=='Washington County')&(conties['POPESTIMATE2015']>conties['POPESTIMATE2014'])][['STNAME','CTYNAME']]
    return answer
