import os 
from pathlib import path
import logging 

logging.basicConfig(level=logging.INFO)

project_name="DAP"
list_of_file= [ 
f"src/{ project_name }/__init__.py"
f"src/{ project_name}/components/__init__.py",
f"src/{ project_name}/components/data_ingestion.py",
f"src/{ project_name}/components/data_transformation.py",
f"src/{ project_name}/components/model_trainer.py",
f"src/{ project_name}/components/data_monitoring.py",
f"src/{ project_name}/pipelines/__init__.py",
f"src/{ project_name}/pipelines/training_pipeline.py",
f"src/{ project_name}/pipelines/prediction_pipeline.py",
f"src/{ project_name}/exception.py",
f"src/{ project_name}/logger.py",
f"src/{ project_name}/utils.py",
"app.py"
"Dockerfile"
"requirements.txt"
"setup.py"



]