from setuptools import setup, find_packages

setup(name="ansible-ssh",
      version='1.1.0',
      python_requires='>=2.7, <=3.0',
      description='SSH/SFTP Connection Manager for Ansible',
      author='Aytunc Beken',
      author_email='aytuncbeken.ab@gmail.com',
      packages=find_packages(exclude=["bin"]),
      install_requires=['ansible'],
      entry_points={
          'console_scripts': ['ansible-ssh=cli.main:main']
      })
