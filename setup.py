from setuptools import setup, find_packages

setup(
    name='Dynamic_electricity_price',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[ 
        'numpy',
        'pandas',
        'scikit-learn',
        'matplotlib',
        'seaborn',
        'matplotlib',
        'statsmodels',
        'sklearn',
        'scipy',
        'datetime',
        'plotly'
    ],
    author='Aersi A.', 
    description='A machine learning project for predicting dynamic electricity prices',
)
