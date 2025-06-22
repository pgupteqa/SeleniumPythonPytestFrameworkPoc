import os

import pytest
from dotenv import load_dotenv
from simple_salesforce import Salesforce, SalesforceAuthenticationFailed
load_dotenv()


## Different functions to get

class SalesforceUtils:

    def __init__(self):
        self.sf = self.authenticate_salesforce()

    def authenticate_salesforce(self):
        try:
            sf_username = os.getenv("SF_USERNAME")
            sf_password = os.getenv("PASSWORD")
            sf_instance_url = os.getenv("INSTANCE_URL")
            sf_consumer_key = os.getenv("CONSUMER_KEY")
            sf_consumer_secret = os.getenv("CONSUMER_SECRET")

            if not all([sf_username, sf_password, sf_instance_url, sf_consumer_key, sf_consumer_secret]):
                raise ValueError("Missing Salesforce authentication configuration.")

            sf = Salesforce(
                username=sf_username,
                password=sf_password,
                instance_url=sf_instance_url,
                consumer_key=sf_consumer_key,
                consumer_secret=sf_consumer_secret
            )
            print(f"[INFO] Connected to Salesforce: {sf.base_url}")
            return sf
        except SalesforceAuthenticationFailed as e:
            print(f"[ERROR] Salesforce authentication failed: {e}")
            raise
        except Exception as ex:
            print(f"[ERROR] Error connecting to Salesforce: {ex}")
            raise


    def get_contact_detail_by_lastname(self, lastName):
        global contact_id, contactname
        soql = f"SELECT Id, Name from Contact where LastName='{lastName}'"
        responseresult = self.sf.query(soql)
        print(responseresult)

        if responseresult['totalSize'] > 0 and 'records' in responseresult:
            for record in responseresult['records']:
                contact_id = record['Id']
                contactname = record['Name']
        else:
            print("no records are found")

        return {'Id': contact_id, 'Name': contactname}