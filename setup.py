from setuptools import find_packages, setup

HYPEN_E_DOT='-e .'


def get_requirements(file_path):
    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", " ") for req in requirements]

    return requirements


setup(
    name="DAP",
    version="1.0.0",
    author="Nauman",
    author_email="legendofcs1@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)