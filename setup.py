from setuptools import setup, find_packages
requirements = [
    'scipy==1.10.0',
    'simpy==4.0.1',
    'networkx==3.0',
    'geopy==2.3.0',
    'PyYAML==6.0',
    'numpy==1.24.2',
    'common-utils',
    'scikit-learn==1.2.1',
    'pandas==1.5.3',
    'matplotlib',
]

test_requirements = [
    'flake8',
    'nose2'
]

setup(
    name='coord-sim',
    version='2.1.1',
    description='Simulate flow-level, inter-node network coordination including scaling and placement of services and '
                'scheduling/balancing traffic between them.',
    url='https://github.com/RealVNF/coord-sim',
    author='Stefan Schneider',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=requirements,
    tests_require=test_requirements,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'coord-sim=coordsim.main:main',
            'animation=animations.animations:main',
            'lstm-predict=coordsim.traffic_predictor.lstm_predictor:main'
        ],
    },
)
