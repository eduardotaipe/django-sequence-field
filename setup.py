from setuptools import setup

description = "Generic JSON model and form fields."

try:
    with open("README.md") as f:
        long_description = f.read()
except IOError:
    long_description = description

setup(
    name="django-sequence-field",
    version="0.2",
    description=description,
    author="Eduardo Taipe",
    author_email="eduardotl@eduardotaipe.com",
    url="https://github.com/eduardotaipe/django-sequence-field",
    long_description=long_description,
    packages=["sequence_field"],
    install_requires=["django == 3.2"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
