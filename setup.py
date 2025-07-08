from setuptools import setup, find_packages

setup(
    name="niftyTradeCalendar",
    version="0.4.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    author="Sonu Kumar",
    author_email="skrdeveloper1@gmail.com",
    description="Holiday and Trading Day Calendar for NIFTY",
    url="https://github.com/sonu-kumar-full-stack-dev/niftyTradeCalendar",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
    project_urls={
        "LinkedIn": "https://www.linkedin.com/in/sonu-kumar-full-stack-dev",
        "GitHub": "https://github.com/sonu-kumar-full-stack-dev/niftyTradeCalendar",
    },
    python_requires=">=3.6",
)