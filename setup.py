from setuptools import setup, find_packages

with open("requirements.txt") as r:
    install_requires = r.read()

setup(
    name = "API_de_usuarios_v4",
    version = "0.0.1",
    description = "Rest API with Python and Flask",
    url = "https://github.com/lucasharzer/API_de_usuarios_v4",
    author = "Lucas Harzer",
    author_email = "lucasmatos592@gmail.com",
    packages = find_packages(),
    install_requires = [install_requires],
    zip_safe = "False"
)