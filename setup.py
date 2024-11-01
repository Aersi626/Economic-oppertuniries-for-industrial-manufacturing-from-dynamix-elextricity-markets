from setuptools import setup, find_packages

setup(
    name='Dynamic_electricity_price',                    # Name of your package
    version='0.1',                           # Version of your package
    packages=find_packages(where='src'),     # Directories to include as packages
    package_dir={'': 'src'},                 # Base directory for packages
    install_requires=[                       # List of dependencies
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
    author='Aersi A.',                      # Author of the package
    description='A machine learning project for predicting dynamic electricity prices',  # Short description
)
