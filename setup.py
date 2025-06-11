from setuptools import setup, find_packages

setup(
    name='git-analyzer',
    version='0.2.2',
    packages=find_packages(),
    install_requires=[
        'GitPython',
        'rich',
    ],
    entry_points={
        'console_scripts': [
            'git-analyze = analyzer.__main__:main',
        ],
    },
)
