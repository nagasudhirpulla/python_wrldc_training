# example.py
from utils.get_all_persons_info import getAllPersonsInfo

personsInfoList = getAllPersonsInfo()

print('All persons in the store are ...')
print('\n'.join(personsInfoList))