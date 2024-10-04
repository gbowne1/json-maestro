from setuptools import setup, find_packages

setup(
    name='jsonmaestro',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
                        'jsonmaestro=jsonmaestro.src.main:main',
        ],
    },
    author='Gregory Bowne',
    description='JSONMaestro is a powerful tool designed for cleaning and processing JSON-like files. It simplifies tasks such as removing comments, eliminating duplicate keys, adding schema keys, and sorting keys. Ideal for developers working with configuration files and API responses, JSONMaestro enhances data integrity and prepares JSON data for further analysis',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/my_module',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)