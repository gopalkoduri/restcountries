from setuptools import setup, find_packages

setup(
    name="restcountries",
    version="2024.04.29",
    description="Pythonic wrapper around data served by restcountries API",
    author="Gopala Krishna Koduri",
    author_email="gopal@riyazapp.com",
    url="https://github.com/gopalkoduri/restcountries",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # List your package dependencies here
        # 'numpy', 'pandas', etc.
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
