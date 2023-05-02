from setuptools import setup, find_packages

setup(name = "Test",
      version = "0.1",
      author = "Ayush Gandhi",
      author_email="ayushgandhi904@gmail.com",
      packages = find_packages(),
      install_packages = ["pandas", "numpy", "matplotlib"]
      )
