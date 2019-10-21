from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name="ansible-terminal",
      version='0.10.0',
      long_description=long_description,
      long_description_content_type="text/markdown",
      python_requires='>=2.7, <=3.0',
      description='SSH/SFTP Terminal Manager for Ansible',
      author='Aytunc Beken',
      author_email='aytuncbeken.ab@gmail.com',
      packages=find_packages(exclude=["bin"]),
      install_requires=['ansible'],
      url="https://github.com/aytuncbeken/ansible-terminal",
      entry_points={
          'console_scripts': ['ansible-terminal=cli.main:main']
      })
