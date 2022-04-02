import xml.etree.ElementTree as ET
from datetime import datetime
from datetime import timedelta
import os

curr_dir = os.getcwd()
def xml_modify(x,y):
    if str(x).strip().isdigit() and str(y).strip().isdigit():
        mytree = ET.parse(curr_dir+"\\test_payload1.xml")
        myroot = mytree.getroot()
        for depart in myroot.iter('DEPART'):
            updated_x = datetime.now() + timedelta(days = x)
            depart.text = str(updated_x)
        for r in myroot.iter('RETURN'):
            updated_y = datetime.now() + timedelta(days = y)
            r.text = str(updated_y)
        mytree.write(curr_dir+"\\output.xml")
    else:
        print("please provide the correct number)

xml_obj = xml_modify(10,5)
     