from setuptools import setup

setup(
    name="ccal",
    version="1.0.0",
    description="Like the 'cal' command, but doesn't put spaces between months",
    author="Roland Crosby",
    author_email="roland@rolandcrosby.com",
    url="https://github.com/rolandcrosby/ccal",
    entry_points={
        "console_scripts": [
            "ccal = ccal:main"
        ]
    },
    packages=["ccal"],
    install_requires=["docopt", "ansicolors"]
)
