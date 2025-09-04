from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="system_expert_site",
    version="0.1.2",
    description="Website for System Expert built on Frappe/ERPNext Website",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Neotec",
    author_email="noor@neotec.ai",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
)
