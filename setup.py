from setuptools import setup, find_packages

setup(
    name='konkani_tokenizer',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'sentencepiece'
    ],
    authors='Banashankar',
    description='Konkani Tokenizer using SentencePiece',
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
)
