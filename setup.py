import setuptools

with open("README.md",'r',encoding='utf-8') as f:
    long_description = f.read()

__version__ = '0.0.0'

REPO_NAME = 'Text_summarizer'
AUTHOR_USER_NAME = 'mujjmil'
SRC_REPO = "textSumarizer"
AUTHOR_EMAIL = 'mujjmil17397@gmail.com'

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Text summarizer package for NLP app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}',
    project_url={
        'bug Tracker': f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues',
    },
    package_dir={'':'src'},
    packages=setuptools.find_packages(where='src')
)