import os
from pathlib import Path


# while True:
#     user_input = input('Enter Your Project Name:->')
#     if user_input !="":
#         break
user_input = 'src'


list_of_file = [
    f"{user_input}/__init__.py",
    
    f"{user_input}/componets/__init__.py",
    f"{user_input}/componets/data_ingestion.py",
    f"{user_input}/componets/data_preprocessing.py",
    f"{user_input}/componets/model_trainner.py",
    f"{user_input}/componets/model_evaluation.py",
    
    f"{user_input}/pipeline/__init__.py",
    f"{user_input}/pipeline/data_pipeline.py",
    f"{user_input}/pipeline/model_pipeline.py",
    
    f"{user_input}/exception.py",
    
    f"{user_input}/logger.py",
    
    f"{user_input}/utils.py",
    
    "setup.py",
    "app.py",
    "Dockerfile",
    ".dockerignore",
    "main.py"
]

for file in list_of_file:
    filepath = Path(file)
    filedir,filename = os.path.split(filepath)
    
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
        
    else:
        print(f"{filename} already exists")  # print the filename if it already exists
        
        
print('file creation successfull.')