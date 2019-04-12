from setuptools import setup, find_packages

__version__ = '1.0.0'

setup(
    version=__version__,
    name='darksky-sdk-python',
    packages=find_packages(),

    install_requires=[
        'requests==2.21.0'
    ],

    description='The Dark Sky API wrapper',

    author='Detrous',
    author_email='detrous@protonmail.com',

    url='https://github.com/microparts/darksky-sdk-python',
    download_url='https://github.com/microparts/darksky-sdk-python/archive/%s.tar.gz' % __version__,

    license='MIT License',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
