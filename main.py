import pandas as pd
import matplotlib.pyplot as plt
OID=pd.read_csv("zillow.csv")
df=OID.groupby(["Beds"])
figure, axes=plt.subplots(nrows=1,ncols=len(df.groups.keys()))
for (key, ax)in zip(df.groups.keys(), axes.flatten()):
    df.get_group(key).plot(ax=ax)
    ax.legend()
    ax.set_title(key)
plt.show()

