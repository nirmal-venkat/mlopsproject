import os
from pathlib import Path

# print(Path("""a\\b\\c.txt"""))

list_of_files = [
                #  ".github/workflows/.gitkeep", 
                 "src/__init__.py",
                #  "src/components/__init__.py",
                #  "src/components/data_ingestion.py",
                #  "src/components/data_transformation.py",
                #  "src/components/model_trainer.py",
                #  "src/components/model_evaluation.py",
                #  "src/pipeline/__init__.py",
                #  "src/pipeline/training_pipeline.py",
                #  "src/pipeline/prediction_pipeline.py",
                #  "src/utils/utils.py",
                 "src/utils/__init__.py",
                 "src/logging/logging.py",
                 "src/exception/exception.py",
                 "src/exception/__init__.py",
                 "test/unit/__init__.py",
                #  "test/integration/__init__.py"
                #  "init_setup.sh",
                #  "requirements.txt",
                #  "requirements_dev.txt",
                #  "setup.py",
                #  "setup.cfg",
                #  "pyproject.toml",
                #  "tox.ini",
                #  "experiment/experiments.pynb"
                ]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        print(filedir)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass # create an empty file
