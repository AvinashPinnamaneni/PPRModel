from setuptools import setup, find_packages

setup(
    name='Production_PPR',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'et-xmlfile==1.1.0',
        'numpy==1.26.3',
        'openpyxl==3.1.2',
        'pandas==2.1.4',
        'python-dateutil==2.8.2',
        'pytz==2023.3.post1',
        'simpy==4.1.1',
        'six==1.16.0',
        'tzdata==2023.4',
        'zope.interface==6.1',
        'DateTime==5.4'
    ],
    python_requires='>=3.6',
)
