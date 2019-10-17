# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
data=pd.read_csv(path)
data.rename(columns={'Total':'Total_Medals'},inplace =True)
data.head(10)

#Code starts here



# --------------
try:
    data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'] , 'Summer', 'Winter')
    data['Better_Event'] =np.where(data['Total_Summer'] ==data['Total_Winter'],'Both',data['Better_Event']) 
    #print(data['Better_Event'])
    Total_Count=data['Better_Event'].value_counts()
    if(Total_Count[0]>Total_Count[1]):
        better_event='Summer'
        print(better_event)
        print(data)
    else:
        better_event='Winter'
        print(better_event)
except:
    print("code Failed")

else:
    print("code passed Successfully")


# --------------
#Code starts here
top_countries= data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
top_countries=top_countries[:-1]
#print(top_countries)


def top_ten(Col):
    country_list= list((data.nlargest(11,Col)['Country_Name']))
    country_list=country_list[1:]
    print(country_list)
    return country_list


top_10_summer=top_ten('Total_Summer')
top_10_winter =top_ten('Total_Winter')
top_10 =top_ten('Total_Medals')

common=list(set(top_10_summer) & set(top_10_winter) & set(top_10))
print("common",common)


# --------------
#Code starts here

summer_df =data[data['Country_Name'].isin(top_10_summer)]
winter_df =data[data['Country_Name'].isin(top_10_winter)]
top_df =data[data['Country_Name'].isin(top_10)]




# --------------
#Code starts here
summer_df['Golden_Ratio']=summer_df['Gold_Summer']/summer_df['Total_Summer'] 
summer_max_ratio=max(summer_df['Golden_Ratio']) 
summer_country_gold=summer_df.loc[summer_df['Golden_Ratio'].idxmax(),'Country_Name']

winter_df['Golden_Ratio']=winter_df['Gold_Winter']/winter_df['Total_Winter'] 
winter_max_ratio=max(winter_df['Golden_Ratio']) 
winter_country_gold=summer_df.loc[winter_df['Golden_Ratio'].idxmax(),'Country_Name']

top_df['Golden_Ratio']=top_df['Gold_Total']/top_df['Total_Medals'] 
top_max_ratio=max(top_df['Golden_Ratio']) 
top_country_gold=summer_df.loc[top_df['Golden_Ratio'].idxmax(),'Country_Name']


# --------------
#Code starts here
data_1=data[:-1]
data_1['Total_Points']=pd.Series(data_1['Gold_Total']*3+data_1['Silver_Total']*2+data_1['Bronze_Total'])
print(data_1['Total_Points'])
most_points = max(data_1['Total_Points'])
print(most_points)
best_country =  data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']
print(most_points)
print(best_country)


# --------------
#Code starts here
best = pd.DataFrame(data[data['Country_Name']==best_country])
best=best[['Gold_Total','Silver_Total','Bronze_Total']]

best.plot.bar()
plt.xlabel('United States')
plt.ylabel('Medals Tally')
# Rotate X-axes labels
plt.xticks(rotation=45)


