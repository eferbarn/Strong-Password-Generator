from setuptools import setup, find_packages

setup(
    name='passgen',
    version='1.0.0',
    description='Generate random passwords with customizable options',
    author='Efer Barn',
    author_email='eferbarndefi@gmail.com',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'passgen = Package.passgen:CLI',
        ],
    },
    py_modules=['passgen'],
    install_requires=[
        'argparse',
    ],
)
