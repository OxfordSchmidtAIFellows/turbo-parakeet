
from setuptools import setup

setup(
    name='pytimeops',
    description='Time series processing and clustering',
    version='0.1',
    install_requires=[
        'numpy',
        'pandas'
    ],
    extras_require={
        'dev': [
            'flake8>=3',
        ],
    },
)
