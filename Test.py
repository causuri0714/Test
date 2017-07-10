'''###########################################################################################
Author : Chaitanya Ausuri
Date : 06/30/2017
Assignment - PREDICT 420 DL SEC 55 - GrEx1
###########################################################################################'''
import pandas as pd             

#### SECTION 1 Create a single summary data set of ratings data #######
#### Creating dataframe 2014 using the xlsx file for 2014 ##########

xls_file=pd.ExcelFile('C:\\Users\\causuri\\Documents\\Predict420\\sfo cust sat 2014 data file_WEIGHTED_flysfo.xlsx')
df_2014 = xls_file.parse('Sheet 1')

# Below statements bring in all the needed ratings data
df_2014_1=df_2014[['RESPNUM','Q9BOARDING','Q9AIRTRAIN','Q9RENTAL','Q9FOOD','Q9RESTROOM','Q9ALL','Q10SAFE','Q12PRECHECKRATE',
                    'Q13GETRATE','Q14FIND','Q14PASSTHRU', 'Q16LIVE' ]]
df_2014_2 = df_2014.filter(regex="Q7")
df_2014 = df_2014_1.join(df_2014_2)
df_2014['YEAR']=2014  # Classifying this data as belonging to 2014.
df_2014 = df_2014.fillna(0)
df_2014=df_2014.set_index('RESPNUM') #setting respnum as an index

df_2014 = df_2014.rename(columns={'RESPNUM': 'RESP_NO', 'Q9BOARDING':'CLN_BOARD_RTNG','Q9AIRTRAIN':'CLN_AIRTRN_RTNG','Q9RENTAL':'CLN_RENT_RTNG','Q9FOOD':'CLN_RESTRNT_RTNG','Q9RESTROOM':'CLN_BATH_RTNG',
                                'Q9ALL':'CLN_OVERALL_RTNG','Q10SAFE':'SAFE_RTNG','Q12PRECHECKRATE':'TSA_PRECHK_RTNG','Q13GETRATE':'ARPT_GET_RTNG','Q14FIND':'ARPT_HELP_RTNG','Q14PASSTHRU':'SEC_PSSTHRGH_RTNG', 
                                'Q16LIVE':'RESP_LOC','Q7ART':'ARPT_ART_RTNG','Q7FOOD':'ARPT_FOOD_RTNG','Q7STORE':'ARPT_STORES_RTNG','Q7SIGN':'ARPT_DIRECTN_RTNG','Q7WALKWAYS':'ARPT_WALKS_RTNG',
                                'Q7SCREENS':'ARPT_DISPL_RTNG','Q7INFODOWN':'ARPT_INFO_DWNSTRS_RTNG','Q7INFOUP':'ARPT_INFO_UPSTRS_RTNG','Q7WIFI':'ARPT_WIFI_RTNG','Q7ROADS':'ARPT_ROADS_RTNG','Q7PARK':'ARPT_PRKNG_RTNG',
                                'Q7AIRTRAIN':'ARPT_AIRTRN_RTNG','Q7LTPARKING':'ARPT_LNGTRM_PARK_RTNG','Q7RENTAL':'ARPT_RNTLS_RTNG','Q7ALL':'ARPT_OVERALL_RTNG'})

#### Creating dataframe 2015 using the csv file for 2015 ##########

df_2015 = pd.read_csv('C:\\Users\\causuri\\Documents\\Predict420\\sfo cust sat 2015_data file_final_WEIGHTED_flysfo.csv', sep=',')
df_2015_1=df_2015[['RESPNUM','Q9BOARDING','Q9AIRTRAIN','Q9RENTAL','Q9FOOD','Q9RESTROOM','Q9ALL','Q10SAFE','Q12PRECHEKCRATE','Q13GETRATE',
                'Q14FIND','Q14PASSTHRU', 'Q16LIVE','Q8COM1','Q8COM2','Q8COM3' ]]
df_2015_1['Q8COM1'].fillna(0,inplace=True)
df_2015_1['Q8COM2'].fillna(0,inplace=True)
df_2015_1['Q8COM3'].fillna(0,inplace=True)
df_2015_2 = df_2015.filter(regex="Q7")
df_2015 = df_2015_1.join(df_2015_2)
df_2015['YEAR']=2015
df_2015=df_2015.set_index('RESPNUM')

#### dataframe 2016 using xlsx file for 2016 ##########

xls_file=pd.ExcelFile('C:\\Users\\causuri\\Documents\\Predict420\\2016 SFO Customer Survey Data.xlsx')
df_2016 = xls_file.parse('Data')
df_2016_1=df_2016[['*RESPNUM','Q9BOARDING','Q9AIRTRAIN','Q9RENTAL','Q9FOOD','Q9RESTROOM','Q9ALL','Q10SAFE','Q12PRECHECKRATE','Q13GETRATE',
                'Q14FIND','Q14PASSTHRU', 'Q16LIVE','Q8COM','Q8COM2','Q8COM3','Q8COM4','Q8COM5' ]]
df_2016_1['Q8COM'].fillna(0,inplace=True)
df_2016_1['Q8COM2'].fillna(0,inplace=True)
df_2016_1['Q8COM3'].fillna(0,inplace=True)
df_2016_1['Q8COM4'].fillna(0,inplace=True)
df_2016_1['Q8COM5'].fillna(0,inplace=True)
df_2016_1['Q12PRECHECKRATE'].fillna(0,inplace=True)
df_2016_2 = df_2016.filter(regex="Q7")
df_2016 = df_2016_1.join(df_2016_2)
df_2016['YEAR']=2016
df_2016 = df_2016.rename(columns={'*RESPNUM': 'RESPNUM'})
df_2016=df_2016.set_index('RESPNUM')

#### End pulling dataframes .######

df_combined = pd.concat([df_2014, df_2015, df_2016], join='outer') # concatenating 2014, 2015 AND 2016 dataframes

df_combined.to_csv('C:\\Users\\causuri\\Documents\\Predict420\\Combined_SFO_RATINGS.csv', sep=',')

###### SECTION 2 - Identify the top three (3) comments made in survey years 2015 and 2016 #####

top3_2015 = pd.melt(df_2015, value_vars=['Q8COM1','Q8COM2','Q8COM3'], value_name = 'CODE')
top3_2015['CODE'] = top3_2015['CODE'].astype(int) 
top3_2015 = top3_2015.loc[top3_2015['CODE'] != 0]
top3_2015 = top3_2015['variable'].value_counts().nlargest(3)  # Top 3 Comments in 2015

top3_2016 = pd.melt(df_2016, value_vars=['Q8COM','Q8COM2','Q8COM3','Q8COM4','Q8COM5'], value_name = 'CODE')
top3_2016['CODE'] = top3_2016['CODE'].astype(int) 
top3_2016 = top3_2016.loc[top3_2016['CODE'] != 0]
top3_2016 = top3_2016['variable'].value_counts().nlargest(3)  # Top 3 Comments in 2016

### Section 3  ###########
#summarize the distribution of the SFO Airport "as a whole" ratings by respondent residence location 

df_summary = pd.crosstab(df_combined["Q7ALL"], df_combined["Q16LIVE"], margins=True)

#### Section 4 ###########

# Sample respondent's data by year
df_RESP = pd.read_csv('C:\\Users\\causuri\\Documents\\Predict420\\select_resps.csv',sep=',')
df_RESP=df_RESP.rename(columns={'year':'YEAR'})

# 2015 respondents data
df_2015_SURV = pd.read_csv('C:\\Users\\causuri\\Documents\\Predict420\\sfo cust sat 2015_data file_final_WEIGHTED_flysfo.csv', sep=',')
df_2015_SURV['YEAR']=2015

# Join the Sample respondents and 2015 respondents by Year. Below results in 2015 respondents data
merged_2015 = pd.merge(df_RESP, df_2015_SURV, on =['RESPNUM', 'YEAR'])

df_merged_2015 = merged_2015.filter(['RESPNUM','YEAR','INTDATE','DESTGEO','DESTMARK','Q2PURP1','Q2PURP2','Q2PURP3','Q2PURP4','Q2PURP5','Q2PURP6','Q3PARK','Q4BAGS','Q4STORE','Q4FOOD','Q4WIFI','Q5TIMESFLOWN','Q5FIRSTTIME','Q6LONGUSE','Q16LIVE','Q18Age',
                                    'Q19Gender','Q20INCOME','Q21FLY','LANG','Q22SJC','Q22OAK'], axis=1)
                                    
#Convert date number column to a valid date formal                                    
df_merged_2015['INTDATE'] = '05/' + df_merged_2015['INTDATE'].astype(str) + '/2015'
df_merged_2015['INTDATE'] = pd.to_datetime(df_merged_2015['INTDATE'],format="%m/%d/%Y")

# Fill in NAs with 0 only to be filtered out for frequency counts.
df_merged_2015['Q3PARK'].fillna(0,inplace=True)
df_merged_2015['Q5TIMESFLOWN'].fillna(0,inplace=True)
df_merged_2015['Q6LONGUSE'].fillna(0,inplace=True)

df_merged_2015.to_csv('C:\\Users\\causuri\\Documents\\Predict420\\df_merged_2015.csv', sep=',') # Save to a file

#equencies of the codes for Parking, Times Flown, How Long Using SFO
merged_melted_2015 = pd.melt(df_merged_2015, value_vars=['Q3PARK', 'Q5TIMESFLOWN','Q6LONGUSE'], value_name = 'CODE')
merged_melted_2015['CODE'] = merged_melted_2015['CODE'].astype(int) 
merged_melted_2015 = merged_melted_2015.loc[merged_melted_2015['CODE'] != 0]
merged_melted_2015 = merged_melted_2015['variable'].value_counts()  

### for 2016

df_2016_SURV=pd.ExcelFile('C:\\Users\\causuri\\Documents\\Predict420\\2016 SFO Customer Survey Data.xlsx')
df_2016_SURV = df_2016_SURV.parse('Data')
df_2016_SURV=df_2016_SURV.rename(columns={'*RESPNUM':'RESPNUM'})
df_2016_SURV['YEAR']=2016

merged_2016 = pd.merge(df_RESP, df_2016_SURV, on =['RESPNUM', 'YEAR'])

df_merged_2016 = merged_2016.filter(['RESPNUM','YEAR','INTDATE','DESTGEO','DESTMARK','Q2PURP1','Q2PURP2','Q2PURP3','Q2PURP4','Q2PURP5','Q2PURP6','Q3PARK','Q4BAGS','Q4STORE','Q4FOOD','Q4WIFI','Q5TIMESFLOWN','Q5FIRSTTIME','Q6LONGUSE','Q16LIVE','Q18Age',
                                    'Q19Gender','Q20INCOME','Q21FLY','LANG','Q22SJC','Q22OAK'], axis=1)

df_merged_2016['Q3PARK'].fillna(0,inplace=True)
df_merged_2016['Q5TIMESFLOWN'].fillna(0,inplace=True)
df_merged_2016['Q6LONGUSE'].fillna(0,inplace=True)
df_merged_2016.to_csv('C:\\Users\\causuri\\Documents\\Predict420\\df_merged_2016.csv', sep=',') # Save to a file

#frequencies of the codes for Parking, Times Flown, How Long Using SFO
merged_melted_2016 = pd.melt(df_merged_2016, value_vars=['Q3PARK', 'Q5TIMESFLOWN','Q6LONGUSE'], value_name = 'CODE')
merged_melted_2016['CODE'] = merged_melted_2016['CODE'].astype(int) 
merged_melted_2016 = merged_melted_2016.loc[merged_melted_2016['CODE'] != 0]
merged_melted_2016 = merged_melted_2016['variable'].value_counts()      
                     
#### sec 4 end                                                                        

#### sec 5 start - Saving the data sets by pickling

#Section 1 datasets save

df_2014.to_pickle('C:\\Users\\causuri\\Documents\\Predict420\\df_2014')
df_2015.to_pickle('C:\\Users\\causuri\\Documents\\Predict420\\df_2015')
df_2016.to_pickle('C:\\Users\\causuri\\Documents\\Predict420\\df_2016')
df_combined.to_pickle('C:\\Users\\causuri\\Documents\\Predict420\\df_combined')
top3_2015.to_pickle('C:\\Users\\causuri\\Documents\\Predict420\\top3_2015')
top3_2016.to_pickle('C:\\Users\\causuri\\Documents\\Predict420\\top3_2016')
df_summary.to_pickle('C:\\Users\\causuri\\Documents\\Predict420\\df_summary')
df_RESP.to_pickle('C:\\Users\\causuri\\Documents\\Predict420\\df_RESP')
df_2015_SURV.to_pickle('C:\\Users\\causuri\\Documents\\Predict420\\df_2015_SURV')
merged_2015.to_pickle('C:\\Users\\causuri\\Documents\\Predict420\\merged_2015')
df_merged_2015.to_pickle('C:\\Users\\causuri\\Documents\\Predict420\\df_merged_2015')
merged_melted_2015.to_pickle('C:\\Users\\causuri\\Documents\\Predict420\\merged_melted_2015')
df_2016_SURV.to_pickle('C:\\Users\\causuri\\Documents\\Predict420\\df_2016_SURV')
merged_2016.to_pickle('C:\\Users\\causuri\\Documents\\Predict420\\merged_2016')
df_merged_2016.to_pickle('C:\\Users\\causuri\\Documents\\Predict420\\df_merged_2016')
merged_melted_2016.to_pickle('C:\\Users\\causuri\\Documents\\Predict420\\merged_melted_2016')

### example un-pickling

df_unpickle_2015 = pd.read_pickle('C:\\Users\\causuri\\Documents\\Predict420\\merged_melted_2015')
df_unpickle_2016 = pd.read_pickle('C:\\Users\\causuri\\Documents\\Predict420\\merged_melted_2016')

#### sec 5 end