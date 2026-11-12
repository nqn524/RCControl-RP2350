from setuptools import setup, find_packages

setup(
    name = "RCControl",
    description = "Library to make it easier to wirelessly connect a Raspberry PI Pico 2 W using Bluetooth Low Energy or WiFi making use of websockets",
    readme = "README.md",
    long_description = "See the [GitHub](https://github.com/nqn524/RCControl-RP2350) or the [controller website](www-users.york.ac.uk/~nqn524) for more details",
    long_description_content_type = "text/markdown",
    version = "1.1",
    author = "E Smirthwaite", 
    author_email="nqn524@york.ac.uk",
    project_urls = {
        "Github": "https://github.com/nqn524/RCControl-RP2350",
        "Controller Website": "https://www-users.york.ac.uk/~nqn524/"
    },
    install_requires = [
        "picozero==0.6.1",
        "microdot==2.7.0"
    ],
    packages = find_packages(),
    include_package_data = True,
    package_data = {
        "RCControl": [
            "website/*.html",
            "website/*.js",
        ],
    },
    license = "MIT",
    license_files = "LICENSE"
)