import pymongo
import pandas as pd
import os

db_url = os.environ['MONGODB_URL']
client = pymongo.MongoClient(db_url)
db = client["test"]

def get_ep_data():
  df = pd.DataFrame(list(db.users.find()))

  # Remove unnecessary columns
  df = df.drop(["tokens", "__v", "password"], axis=1)

  return df

def get_symp_survey_data():
  df = pd.DataFrame(list(db.surveysymptoms.find()))
  df = df.drop(["__v", "_id"], axis=1)
  return df

def get_symptom_id_matching(symptom_id):
  return db.symptoms.find_one(
    {"_id" : symptom_id})

def get_symptom_id_matching_df():
  df = pd.DataFrame(list(db.symptoms.find()))
  return df

def get_ac_data():
  df = pd.DataFrame(list(db.phases.find()))

  # Remove unnecessary columns
  df = df.drop(["_id", "__v"], axis=1)

  new_rows = list()
  def merge_symptoms(row):
    symptoms = row["symptoms"]
    new_rows.append(symptoms)

  df.apply(merge_symptoms, axis=1)
  symptoms_df = pd.DataFrame(new_rows)

  symptoms_df.drop(["_id"], axis=1)
  df = df.drop(["symptoms"], axis=1)

  df = pd.concat([df, symptoms_df], axis=1)

  return df