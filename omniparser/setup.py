import setuptools

__version__ = "1.1.0"

tests_require = [
    "pytest",
    "mypy",
]

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt") as f:
    install_requires = f.readlines()

setuptools.setup(
    name="omniparser",
    version=__version__,
    author="Suresh Nakkeran",
    author_email="suresh.nakkeran@healthec.com",
    description="A python wrapper for omniparser",
    long_description=long_description,
    python_requires=">=3.7",
    packages=[
        "omniparser",
        "omniparser.bin",
    ],
    include_package_data=True,
    install_requires=install_requires,
    tests_require=tests_require,
)
