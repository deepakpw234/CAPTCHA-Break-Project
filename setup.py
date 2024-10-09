from setuptools import find_packages,setup

HYPHEN_DOT_E = "-e ."
def get_requirements(text_file):
    with open(text_file,"r") as file:
        requirements = file.read().splitlines()

    if HYPHEN_DOT_E in requirements:
        requirements.remove(HYPHEN_DOT_E)

    return requirements


setup(
    name= "CAPTCHA Break",
    version= "0.0.0.1",
    description= "This app helps the user to break the captcha from the election commission website",
    long_description= "A user friendly app is created to break the captcha from the election commission website. This app is used the Random Forest model to predict the captcha",
    author= "Deepak Pawar",
    author_email="deepakpw234@gmail.com",
    packages = find_packages(),
    install_req = get_requirements("requirements.txt")
)
