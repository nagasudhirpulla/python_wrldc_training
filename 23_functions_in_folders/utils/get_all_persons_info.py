# utils/get_all_persons_Info.py
from stores.persons_store import persons
from utils.info_creator import createInfoForPerson

def getAllPersonsInfo():
    infoArray = []
    for p in persons:
        personInfo = createInfoForPerson(p)
        infoArray.append(personInfo)
    return infoArray