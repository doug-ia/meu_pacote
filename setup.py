from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

setup(
    name="meu_pacote",  # Nome do pacote no PyPI
    version="0.0.1",
    author="doug.ia",
    author_email="seuemail@example.com",
    description="Um pacote simples para dizer olá",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/doug-ia/meu_pacote.git",  # Seu repositório
    packages=find_packages(),
    python_requires=">=3.8",
)
