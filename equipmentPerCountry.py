def findEquipmentsPerCountry (fileName):

#--------import files-----------#

    import pandas as pd
    file = pd.read_csv(fileName, sep=';')
    initialDf = pd.DataFrame(file)
    
#--------format dataframe-------#

    # make everything lower string
    initialDf = initialDf.astype(str).apply(lambda x: x.str.lower())
    
    # group by location
    grouped=initialDf.groupby(['location'])['equipments'].apply(','.join).reset_index()
    
    # tranform into equipments string into a list
    grouped.equipments = grouped.equipments.apply(lambda x : x.replace(']','').replace('[','').split(","))
    
#--------output result----------#

    #create a new dataframe to have only one equipment per country
    finalDf = pd.DataFrame(columns = ["location", "equipments"])
    
    #populate the new dataframe with the old entries
    for index, row in grouped.iterrows():
        for item in row["equipments"]:  
            finalDf = finalDf.append({'location': row["location"], 'equipments': item}, ignore_index=True)
    
    finalDf.to_csv('formattedEquipmentPerCountry.csv', sep='\t', encoding='utf-8')

    return finalDf