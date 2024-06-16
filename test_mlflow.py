#%%
import mlflow 
import dagshub
from datetime import datetime

# %%
print("Setting Tracking URI")

# mlflow.set_tracking_uri('http://192.168.1.17:5000')
dagshub.init("github-action-ml", "Clarenceee", mlflow=True)

# %%
experiment_name = "Test-Github-Action"
experiment = mlflow.get_experiment_by_name(experiment_name)
if experiment:
    experiment_id = experiment.experiment_id
    print("Experiment ID = ", experiment_id)

    current_datetime = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    new_run_name = "Training-"+ current_datetime

    with mlflow.start_run(experiment_id=experiment_id, run_name=new_run_name):
        mlflow.log_param("lr_test", 0.002)
        mlflow.log_metric("loss_test", 0.1)
else:
    print("Experiment not found")
    
# Transfer artifacts file out
# %%
