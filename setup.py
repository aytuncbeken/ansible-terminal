from setuptools import setup, find_packages

setup(name="ansible-terminal",
      version='0.4.0',
      python_requires='>=2.7, <=3.0',
      description='SSH/SFTP Terminal Manager for Ansible',
      author='Aytunc Beken',
      author_email='aytuncbeken.ab@gmail.com',
      packages=find_packages(exclude=["bin"]),
      install_requires=['ansible'],
      entry_points={
          'console_scripts': ['ansible-terminal=cli.main:main']
      })
