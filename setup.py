from setuptools import setup, find_packages

setup(
    name='doc-transformer',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandoc>=3.0',
        'python-docx>=1.0',
        'click>=8.0',
    ],
    entry_points={
        'console_scripts': [
            'dt=src.cli:cli',
        ],
    },
    author='DocTransformer',
    description='让 AI Agent 能够直接识别、编辑 Word/PDF 文档的工具链',
    python_requires='>=3.8',
)
