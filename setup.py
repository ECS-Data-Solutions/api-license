from setuptools import setup

setup(
    name='ecs-license-api',
    packages=['elicense', 'elicense.v1'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-restful',
        'PyMongo'
    ],
)