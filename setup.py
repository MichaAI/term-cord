from setuptools import setup, find_packages


def readme():
    with open('README.md', 'r') as f:
        return f.read()


setup(
  name='term-cord',
  version='0.0.1',
  author='MichaAI',
  author_email='misha-8-filatov@yandex.ru',
  description='Small discord client in python and py-cord',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/MichaAI/term-cord',
  packages=find_packages(),
  install_requires=['py-cord>=2.4.1'],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: AGPL-3.0 license',
    'Operating System :: OS Independent'
  ],
  keywords='discord python',
  project_urls={
    'Documentation': 'link'
  },
  python_requires='>=3.9'
)
