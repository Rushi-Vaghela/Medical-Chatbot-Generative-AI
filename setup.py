from setuptools import find_packages, setup

# def get_requirements(file_path):
#     requirements = []
#     with open(file_path) as file_obj:
#         requirements = file_obj.readlines()
#         requirements = [req.replace("\n","") for req in requirements]
#     return requirements

setup(
    name = 'Genarative AI Project',
    version = '0.0.0',
    author = 'Rushi',
    author_email = 'rushivvaghela@gmail.com',
    packages = find_packages(),
    install_requires = []
) 
