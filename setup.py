import os
from setuptools import setup, find_packages


setup(
    name='chat_take',
    version='0.1.0',
    author='cpn',
    author_email='tsvetovpavel@gmail.com',
    description='chat_take',
    entry_points={
        'console_scripts': [
            'chat_take=chat_take.cli:cli',
        ],
    },
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    packages=find_packages('src'),
    package_dir={'': 'src'},
    extras_require={
        'test': [
            'factory-boy==2.6.1',
            'fake-factory==0.5.5',
            'mock==2.0.0',
            'pycodestyle==2.3.1',
            'pylint==1.7.1',
            'pytest==3.0.7',
            'pytest-cov==2.5.1',
            'pytest-mock==1.6.0',
            'pytest-tornado==0.4.5',
        ],
    },
)
