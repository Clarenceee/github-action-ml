#%%
import os
import mlflow 
import dagshub
from datetime import datetime

os.environ['MLFLOW_TRACKING_USERNAME'] = 'Clarenceee'
os.environ['MLFLOW_TRACKING_PASSWORD'] = 'f3874a38d72fbe0ff4ff316dba160cb01cce861f'

# %%
print("Setting Tracking URI")
mlflow.set_tracking_uri('https://dagshub.com/Clarenceee/github-action-ml.mlflow/')

# %%
experiment_name = "Test-Github-Action"
experiment = mlflow.get_experiment_by_name(experiment_name)
if experiment:
    experiment_id = experiment.experiment_id
    print("Experiment ID = ", experiment_id)

    current_datetime = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    new_run_name = "Training-"+ current_datetime

    with mlflow.start_run(experiment_id=experiment_id, run_name=new_run_name):
        mlflow.log_param("lr_test", 0.001)
        mlflow.log_metric("loss_test", 0.2)
else:
    print("Experiment not found")
    
# Transfer artifacts file out
