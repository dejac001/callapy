import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name="callapy",
    version="0.0.2",
    author="Robert F. DeJaco",
    author_email="dejac001@umn.edu",
    description="Calculating the amount adsorbed from liquid-phase adsorption measurements",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dejac001/callapy",
    packages=['callapy'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering",
    ],
    python_requires='>=3.6',
    install_requires=["matplotlib==3.2.1", "numpy==1.18.4", "pandas==1.0.3", "Pint==0.11"]
)
