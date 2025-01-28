from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e.'
def requirements(file_path:str)->List[str]:
    """This functio will return the 
    requirements from the file"""

    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements
setup(
    name = 'Accident Prediction',
    Version='0.0.1',
    author = 'Aditya AK',
    author_email = 'aditya@gmail.com',
    packages = find_packages(),
    install_requires = requirements('requirements.txt'),
)
