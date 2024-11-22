from setuptools import setup, find_packages

setup(
    name="SimpleFacturaSDK",
    version="1.0",
    description="SDK para la integración de Facturación Electrónica",
    author="Carlos perea",
    author_email="pereacarlos685@gmail.com",
    packages=find_packages(),
    install_requires=[
        "requests",
        "requests-toolbelt",
        "pydantic",
        "aiohttp",
        "pytest",
        "requests-mock",
        "python-dotenv"
    ],
    include_package_data=True,
)
