from setuptools import setup

setup(
    name="rdkit_wrapper",
    version="0.0.1",
    description="Test of a rdkit wrapper",
    url="https://github.com/sgenheden/rdkit-wrapper",
    author="Samuel Genheden",
    author_email="samuel.genheden@gmail.com",
    packages=["rdkit_wrapper"],
    install_requires=["black"],
    entry_points={"console_scripts": ["smiles2inchikey = rdkit_wrapper.chem:main"]},
)
