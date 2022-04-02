import pandas as pd
import os
from pytz import timezone
from datetime import datetime
import datetime as dt

def timestamp_to_pst(timestamp):
    your_dt = dt.datetime.fromtimestamp(int(timestamp)/1000)
    convert_date = your_dt.strftime("%Y-%m-%d %H:%M:&S")
    datetime_obj = datetime.strptime(convert_date,"%Y-%m-%d %H:%M:%S")
    datetime_obj_utc = datetime_obj.replace(tzinfo=timezone('US/Pacific'))
    return datetime_obj_utc.strftime"%Y-%m-%d %H:%M:%S %Z")
curr_dir = os.getcwd()
df = pd.read_csv(curr_dir+"\\Jmeter.jtl", sep=',')
select_col = [i for i in df.columns if i == 'timeStamp' or i == 'label' or i == 'responseCode' or i == 'responseMessage' or i == 'failureMessage']
rslt_df = df[df['responseCode'] == 504]
rslt_df['timeStamp'] = rslt_df['timeStamp'].apply(timestamp_to_pst)
pd.set_option('display.max_columns', None)
final = rslt_df[select_col]
print(final)