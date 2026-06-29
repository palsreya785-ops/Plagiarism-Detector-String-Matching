from setuptools import setup, find_packages

setup(
    name="plagiarism-detector-backend",
    version="0.1.0",
    # Treat the current `backend` directory as the package root so
    # subpackages (algorithms, services, utils, etc.) are discovered.
    packages=find_packages(),
    package_dir={"": "."},
    install_requires=[
        "fastapi",
        "uvicorn",
        "python-multipart",
        "scikit-learn",
        "numpy",
        "python-docx",
        "PyPDF2",
    ],
)
