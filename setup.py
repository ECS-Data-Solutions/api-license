from setuptools import setup

setup(
    name='ecs-license-api',
    packages=['elicense'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-restful',
        'Flask-PyMongo'
    ],
)