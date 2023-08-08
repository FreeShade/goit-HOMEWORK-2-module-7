from setuptools import setup , find_namespace_packages

setup(name='clean-folder',
      version='0.0.1',
      description='My Very useful code',
      author='Natrix',
      author_email='test@example.com',
      license='MyIT',
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['clean-folder=goit-HOMEWORK-2-module-7.clean:main']},
#clean - команда яка повинна виконатись в терміналі
#після "=" пишемо шлях до файлу де знаходиться функція => goit-HOMEWORK-2-module-7.main
#після ":" пишемо назву функції normalize, process_folder
      classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
      ])