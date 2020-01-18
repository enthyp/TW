from setuptools import setup

setup(
    name='traces',
    package_dir={'': 'src'},
    packages=['traces'],
    install_requires=[
        'graphviz',
        'pytest'
    ]
)
