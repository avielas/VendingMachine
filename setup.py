from setuptools import setup, find_packages

lPackages = find_packages(exclude=('tests', 'tests.*'))


setup(name='template_home_assignment',
    version='0.1.0',
    description='Template home assignment',
    author='na',
    author_email='na',

    packages=lPackages,

    install_requires=[
        # 'enum34;python_version<"3.4"',
    ],
)
