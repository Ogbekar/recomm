from setuptools import setup
setup(
    name='mrecomm',
    version='0.0.1',
    author='Arjun',
    author_email='arjun@spiced-academy.com',
    packages=['mrecomm'],
    url='https://github.com/Ajax121/movie_recomm',
    license='MIT',
    description='A very simple movie recommender that gives a random movie', 
    install_requires = ['pandas','numpy'],
    package_data= {
        'mrecomm': ['data/*.txt']
    },
                                
)
