# Python Forensics

Code from the Python as a Forensic Tool presentation

## About this project

This project was originally formed for a presentation on the usefulness of Python as a
Forensic Tool. The code examples are free to use, modify and distribute under the
GPLv2 Licence terms.

### Notebooks

Below is a summary of the notebooks developed in this repository

#### Using Jupyter

A good starting point for those new to the Jupyter system. Has an introduction on how to use the notebooks and resources for learning more about Python for those new to scripting.

#### Registry

This notebook introduces the [python-registry](https://github.com/williballenthin/python-registry) module and demonstrates how to interact with keys and values to extract useful information from the Windows Registry.

## Installation

Install Python3 on your system and from the directory containing this `README.md` run the below. The notebooks use Python 3.5.1.

### On Windows

```batch
$ pip insall virtualenv
$ virtualenv -p [path to python] venv3
$ venv3/Scripts/activate.bat
(venv3) $ pip install -r requirements.py3.txt
(venv3) $ jupyter notebook
```

### On macOS/Linux

```bash
$ pip insall virtualenv
$ virtualenv -p [path to python] venv3
$ source venv3/bin/activate
(venv3) $ pip install -r requirements.py3.txt
(venv3) $ jupyter notebook
```

## Setup

Once you run the `jupyter notebook` command above, your browser should open at [http://localhost:8888](http://localhost:8888). From this page, navigate into the `jupyter-notebooks` directory and click on a Notebook to get started.

## More Resources

- [Learning Python for Forensics](https://amzn.to/2vm50YQ)
- [Python Digital Forensics Cookbook](https://amzn.to/2qzxzMx)
- [Blog on Python resources for Forensics](http://www.writeblocked.org/index.php/25-resources-for-learning-python-for-forensics.html)

## Support

If you'd like to contribute to this repository - feel free to open a ticket or pull request.

[Wanna buy me a cup of coffee?](https://ko-fi.com/chapin)