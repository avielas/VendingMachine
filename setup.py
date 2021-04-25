from setuptools import setup, find_packages

lPackages = find_packages(exclude=('tests', 'tests.*'))


setup(name='aviela_home_assignment',
    python_requires='>3.8',
    version='0.1.0',
    description='Aviel A home assignment',
    author='na',
    author_email='na',

    packages=lPackages,

    install_requires=[
        # 'enum34;python_version<"3.8"',
        'pytest', 'plantuml'
    ],
)
