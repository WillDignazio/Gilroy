import setuptools

with open("README.md", "r") as fh:
        long_description = fh.read()

        setuptools.setup(
                name="Traffic Display", # Replace with your own username
                version="0.0.1",
                author="Will Ziener-Dignazio",
                author_email="wdignazio@gmail.com",
                description="Real Time Traffic Monitor",
                long_description=long_description,
                long_description_content_type="text/markdown",
                url="digitalbebop.net",
                packages=setuptools.find_packages(),
                classifiers=[
                            "Programming Language :: Python :: 3",
                            "License :: OSI Approved :: MIT License",
                            "Operating System :: OS Independent",
                        ],
                python_requires='>=3.6',
            )
