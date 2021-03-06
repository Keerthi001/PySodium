import setuptools

with open('README.md', 'r', encoding='utf8') as fh:
    long_description = fh.read()

with open('requirements.txt', 'r') as fh:
    required = fh.read().splitlines()

setuptools.setup(
    name="py-sodium",  # Replace with your own username
    version="0.0.2",
    author="Keerthi",
    author_email="kkeerthi432@gmail.com",
    description="PySodium",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Keerthi001/PySodium",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=required,
    include_package_data=True,
)
