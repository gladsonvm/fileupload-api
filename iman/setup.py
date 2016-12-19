from setuptools import setup, find_packages

setup(
    name='iman',
    packages=find_packages(),
    url='https://github.abc.com/gladsonvm/fileupload-api',
    description='An api to C/R/U/D files using Django Rest Framework',
    long_description=open('README.md').read(),
    install_requires=[
        "djangorestframework",
        ],
    dependency_links = [
     "git+git://github.com/gladsonvm/fileupload-api.git#egg=fileupload-api",
    ],
    include_package_data=True,
)