import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv(r'C:\Users\study\Desktop\Checkpoint_1\CSV\Birth_rate.csv')

np_india = df.loc[106,:].to_numpy()
np_butan = df.loc[29,:].to_numpy()
np_nepal = df.loc[175,:].to_numpy()


np_india = np_india[1:]
np_butan = np_butan[1:]
np_nepal = np_nepal[1:]
np_year = np.arange(1960,2021,1)

plt.plot(np_year,np_india, "r",label='India')
plt.plot(np_year,np_butan, "g",label='Butan')
plt.plot(np_year,np_nepal, "b",label='Nepal')

plt.title('Birth Rate Data')
plt.legend()
plt.xlabel('Year')
plt.ylabel('Birth Rate')
plt.show()
