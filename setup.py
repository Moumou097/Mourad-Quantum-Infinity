from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="mourad-quantum-infinity",
    version="0.1.0",
    author="Moumou097",
    author_email="moumou097@example.com",
    description="Integrated Quantum AI, Computing, and Cybersecurity Platform",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Moumou097/Mourad-Quantum-Infinity",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Physics",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.9",
    install_requires=requirements,
    keywords="quantum ai machine learning cybersecurity computing",
    project_urls={
        "Bug Reports": "https://github.com/Moumou097/Mourad-Quantum-Infinity/issues",
        "Documentation": "https://github.com/Moumou097/Mourad-Quantum-Infinity/tree/main/docs",
    },
)
