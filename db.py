import pymongo
import pandas as pd
import os
import pathlib

db_url = os.environ['MONGODB_URL']
client = pymongo.MongoClient(db_url)
db = client["test"]
# def get_ep_data():
#   df = pd.DataFrame(list(db.users.find()))
#   # Remove unnecessary columns
#   df = df.drop(["tokens", "__v", "password"], axis=1)
#   return df
# def get_symp_survey_data():
#   df = pd.DataFrame(list(db.surveysymptoms.find()))
#   df = df.drop(["__v", "_id"], axis=1)
#   return df
# def get_symptom_id_matching(symptom_id):
#   return db.symptoms.find_one(
#     {"_id" : symptom_id})
# def get_symptom_id_matching_df():
#   df = pd.DataFrame(list(db.symptoms.find()))
#   return df
# def get_ac_data():
#   df = pd.DataFrame(list(db.phases.find()))
#   # Remove unnecessary columns
#   df = df.drop(["_id", "__v"], axis=1)
#
#   new_rows = list()
#   def merge_symptoms(row):
#     symptoms = row["symptoms"]
#     new_rows.append(symptoms)
#
#   df.apply(merge_symptoms, axis=1)
#   symptoms_df = pd.DataFrame(new_rows)
#
#   symptoms_df.drop(["_id"], axis=1)
#   df = df.drop(["symptoms"], axis=1)
#
#   df = pd.concat([df, symptoms_df], axis=1)
#
#   return df
#

###########################################
# Temp Read data from files directly
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("data").resolve()
df_user = pd.read_csv(DATA_PATH.joinpath("user.csv"))
df_baseline = pd.read_csv(DATA_PATH.joinpath("baseline.csv"))
df_symptoms = pd.read_csv(DATA_PATH.joinpath("symptoms.csv"))
df_survey = pd.read_csv(DATA_PATH.joinpath("survey.csv"))
df_events = pd.read_csv(DATA_PATH.joinpath("events.csv"))
df_medicine = pd.read_csv(DATA_PATH.joinpath("medicine.csv"))
df_user = df_user.drop(['id'], axis = 1)
df_survey = df_survey.drop(['id'], axis = 1)
df_symptoms = df_symptoms.drop(['id'], axis = 1)
df_baseline = df_baseline.drop(['id'], axis = 1)
df_events = df_events.drop(['id'], axis = 1)
df_medicine = df_medicine.drop(['id'], axis = 1)
df_user.drop(['email','password','dateUpdate'], axis = 1)
df_baseline.sort_values('dateAdded').drop_duplicates(['userId'],keep='last')
df_precovid= pd.merge(df_user,df_baseline)
df_symptoms.columns =[col.replace(',' ,'') for col in df_symptoms.columns]
postcovidcolumns=[col for col in df_symptoms if col.startswith('Symp')]
postcovidcolumns.insert(0,"User_ID")
postcovidcolumns.insert(1,"Date sumbission")
recovered_symptoms = df_symptoms[postcovidcolumns]
covidcolumns=[col for col in df_symptoms if col.startswith('cov')]
covidcolumns.insert(0,"User_ID")
covidcolumns.insert(1,"Date sumbission")
covid_symptoms = df_symptoms[covidcolumns]
df_medicine["startDate"] = pd.to_datetime(df_medicine["startDate"]).dt.date
df_medicine["endDate"] = pd.to_datetime(df_medicine["endDate"]).dt.date
df_medicine =pd.concat([pd.DataFrame({'Date': pd.date_range(row.startDate, row.endDate),
                         'userId': row.userId,
                         'What': row.What,
                         'howmuch': row.howmuch,
                         'units': row.units
                         },
                          columns=['Date','userId', 'What', 'howmuch', 'units'])
                          for  i,row in  df_medicine.iterrows()], ignore_index=True)
df_medicine =pd.get_dummies(df_medicine,prefix="cov", columns=['What'])


