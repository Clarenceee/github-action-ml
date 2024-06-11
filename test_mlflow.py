#%%
import mlflow 
from datetime import datetime

# %%

mlflow.set_tracking_uri('http://localhost:5000')

# %%
experiment_name = "Test-Github-Action"
experiment = mlflow.get_experiment_by_name(experiment_name)
if experiment:
    experiment_id = experiment.experiment_id
else:
    experiment_id = mlflow.create_experiment(experiment_name, tags=experiment_tags)
    
# %%
current_datetime = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
new_run_name = "Training-"+ current_datetime
with mlflow.start_run(experiment_id=experiment_id, run_name=new_run_name):
    mlflow.log_param("lr_test", 0.001)
    mlflow.log_metric("loss_test", 0.1)
# %%
