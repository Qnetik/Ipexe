from setuptools import setup, find_packages

setup(
    name="ipexe",
    version="1.0",
    packages=find_packages(),  
    install_requires=[
        "requests",
        "rich",
    ],
    entry_points={
        "console_scripts": [
            "ipexe=ipexe.ip_checker:main",  
        ],
    },
)

