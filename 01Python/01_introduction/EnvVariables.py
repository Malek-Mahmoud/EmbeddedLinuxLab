import os

EnvironmentVariables = dict(os.environ)

for Variable in EnvironmentVariables.keys():
    Path = EnvironmentVariables.get(Variable)
    print(f"{Variable} : {Path}")