from setuptools import setup, find_packages

setup(
    name="meu_pacote",  # Nome do pacote no PyPI
    version="0.0.1",
    author="Jonatan Mateus",
    author_email="seuemail@example.com",
    description="Um pacote simples para dizer olá",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/seuusuario/meu_pacote",  # Seu repositório
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
