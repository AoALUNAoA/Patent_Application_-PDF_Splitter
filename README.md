![Build Status](https://github.com/AoALUNAoA/Patent_Application_-PDF_Splitter/actions/workflows/python-app.yml/badge.svg)

# Patent_Application_PDF_Splitter(专利申请PDF文件拆分器)
Patent agents and process specialists in China who lack automated tools may face the challenge of splitting patent applications into 4 or 5 sub-documents during submission. To address this, I offer a straightforward command-line tool that can quickly divide these documents without the need for a complex setup.


## 1.Install Python3
```shell
https://www.python.org/downloads/
```
## 2.Dependency
```python
pip install PyPDF2
```
## 3.Usage
In this Python script, **define the file path of your patent application PDF and the destination directories for the five segmented output files**.
```shell
python Patent_Application_ PDF_ Splitter.py
```
FYI, Please pay close attention to the formatting of the sample application file.
The spacing between keywords like "Specification"(说明书) and "Claims"(权利要求书) in the header is crucial for keyword recognition.

# Note
I am a dedicated patent agent. This code is a personal project and is not guaranteed to be suitable for production environments. Use at your own risk.
