import setuptools

with open('README.md', 'r', encoding='utf8') as f:
    long_description = f.read()


setuptools.setup(
    name='istop',
    version='0.0.1',
    author='Egemen Zeytinci',
    author_email='egemenzeytinci@gmail.com',
    description='Python implementation of TOPSIS method',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/egemenzeytinci/istop',
    packages=['istop'],
    include_package_data=True,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux"
    ],
    install_requires=[
        'numpy',
    ]
)
