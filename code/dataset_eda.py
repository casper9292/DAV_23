#############################################################
# tryout    
#############################################################
# Load libraries
import numpy as np
import pandas as pd
import json
import csv
from bokeh.plotting import figure
from bokeh.io import output_file, show

def main():
    # load json
    data = pd.read_json("dataset.json", lines=True)
    print('data geladen')

    table = data[['incident_id', 'participant_status', 'participant_age', 'participant_age_group', 'participant_relationship', 'participant_type', 'participant_gender', 'participant_name']]
    # table = data[['incident_id', 'participant_name']]

    result_table = get_incident_table(table, 0)

    # for counter in range(1, len(table.index)):
    for counter in range(1, 1000):
        incident_table  = get_incident_table(table, counter)
        result_table = result_table.append(incident_table)
        if counter%100 == 0:
            print('gelukt tot deze counter: {}'.format(counter))
    
    # runnen als je json wilt opslaan
    result_table.to_json('incident_table_del.json', orient='records', lines=True)




# get table of one incident
def get_incident_table(table, counter):
    df = pd.DataFrame()

    for colname, values in table.iteritems():
    #     print('colname= {colname}: value={value}'.format(colname=colname, value=values[0]))
        value = values[counter]
        if colname == 'incident_id':
            id = value
            idlist = []

        else:
            keys = []
            tempdf = pd.DataFrame()
            
            if value != 'NaN':
                for value_key in value:
                    keys.append(value[value_key])

                tempdf[colname] = keys
                new = pd.concat([tempdf, df], axis=1) 
                df = new
            
            if value == 'NaN':
                tempdf[colname] = ['NaN']
                new = pd.concat([tempdf, df], axis=1)
                df = new
                
    
    # add current incident id to every row
    number_of_rows = new.index[-1] + 1
    for i in range(number_of_rows):
        idlist.append(id)
    new.insert(loc=0, column = 'incident_id', value=idlist)
    
    return new
    

if __name__ == "__main__":
    main()