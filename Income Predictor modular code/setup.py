from setuptools import find_packages, setup
from typing import List

Hypen_e_dot="-e ."

def get_requirements(filepath: str) ->List[str]:
    requirements=[]

    with open(filepath) as file_obj:
        requirements=file_obj.readlines()
        requirements=[ i.replace("\n","") for i in requirements]


        if Hypen_e_dot in requirements:
            requirements.remove(Hypen_e_dot)

setup(
name='Income Predictor ',
version='0.0.1',
author='Nikhil',
author_email='nickpaulzagde@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)