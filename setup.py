from setuptools import setup, find_packages

setup(
    name='malware-detection-pipeline',
    version='0.1.0',
    author='Aman Rao',
    author_email='amanrao032@gmail.com',
    description='ML Workflow to train malware detection model',
    url='https://github.com/MercMayhem/malware-detection-pipeline',
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
