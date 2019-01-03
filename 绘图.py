import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns

model_names=['KNN','SVM','逻辑回归','Tree','GRADIENT BOOSTING','Random forests','Bagging','ExtraTrees','XGBoost','Voting']
pre_accuracy=[0.544522,0.526924,0.530452,0.573124,0.57906,0.636905,0.613788,0.625042,0.577755,0.653592]
after_accuracy=[0.586320651,0.618869584,0.534418298,0.574664614,0.629425995,0.666153508,0.65427754,0.665053882,0.662854629,0.661947805]
result_frame=pd.DataFrame({'Model':model_names,'Accuracy before adjustment':pre_accuracy,'Accuracy after adjustment':after_accuracy})
result_frame.set_index('Model',inplace=True)
a=result_frame.plot.barh()
plt.show()