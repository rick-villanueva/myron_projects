import pandas as pd
import random


data_set = pd.read_csv("/Users/rickvillanueva/Documents/Myron/dated_random.csv")

random_data = data_set.MYRON_ACCT

random_names = []

random_gatherer = True
#Gathering random account numbers
while random_gatherer:
    one = random.choice(random_data)
    random_names.append(one)
    if len(random_names) < 50:
        random_gatherer = True
        continue
    else:
        break

len(random_names)
print(random_names)




