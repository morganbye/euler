from setuptools import setup, find_packages

setup(
    name='euler',
    version='0.1.0',
    author='Morgan Bye',
    description=('Euler Project problems'),
    license='All rights reserved',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: POSIX',
        'Topic :: Software Development',
    ],
    install_requires=[
        'pytest>=3.7.0',
        'pytest-cov',
        'pytest-pep8',
    ],
    zip_safe=True,
)
