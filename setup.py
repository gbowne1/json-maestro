from setuptools import setup, find_packages

setup(
    name='my_module',  # The name of your module
    version='0.1',
    packages=find_packages(),  # Automatically finds all packages in the project
    install_requires=[],  # Add your dependencies here
    entry_points={
        'console_scripts': [
            'my_module=my_module.src.__main__:main',  # Defines a CLI command `my_module`
        ],
    },
    author='Your Name',
    author_email='you@example.com',
    description='A brief description of your module',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',  # Use markdown for the long description
    url='https://github.com/yourusername/my_module',  # Project's URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Minimum Python version
)