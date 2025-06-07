from setuptools import find_packages,setup
from typing import List

hyphen_e_dor='-e .'
def get_requirements(file_path: str) -> List[str]:
    with open(file_path) as f:
        requirements=[line.strip() for line in f if line.strip() and not line.startswith("#")]
        if hyphen_e_dor in requirements:
            requirements.remove(hyphen_e_dor)
    return requirements
setup(
    name="demo_project_ds",
    version="0.0.1",
    packages=find_packages(),
    author="talhaasif",
    author_email= "muhammadtalhaasif90@gmail.com",
    install_requires=get_requirements('requirements.txt')
)