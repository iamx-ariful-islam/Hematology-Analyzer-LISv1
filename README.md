# Hematology Analyzer LISv1

### **A Python-based _hematology analyzer lis system_ using [PyQT5](https://www.riverbankcomputing.com/static/Docs/PyQt5/) GUI**


[PyQt](https://wiki.python.org/moin/PyQt) is a set of Python binding for the Qt Framework from C++ that can be used to create Desktop Graphical User Interfaces. PyQt gives you all the complex functionalities of C++ Qt while allowing swift development in Python.
<br/>

[Hematology Analyzer LIS](https://www.healio.com/news/hematology-oncology/20120331/what-is-hematology) is a software system that records, manages, updates and stores patient testing data for pathology laboratories, including receiving tests orders, sending orders to laboratory analyzers, tracking orders, results and quality control and transmitting results to print with graphs as pdf or docx.
<br/>

**Pathology analyzer communication supporting serial and network protocols with simulates and data exchange with host system. `It will work on any hematology analyzer`.**

## Task Description
This project fully customizable and dynamic and to build a Python and PyQT5-based desktop application and it's directly connect hematology analyzer with network or serial port communcation and receive data from analyzer then change or edit result and print. Printable report generated or design by python package [`reportlab`](https://www.reportlab.com/) library or use `Microsoft Office Docx` file. You can add pathologist information, doctor information with signature. Everyday create report folder with file name is current date and printed result stored as pdf. Already `100+ Diagnostic Medical Center or Hospital` use this. Here are some special features added.

* **Hematology Analyzer LIS v2023.x (Last updated-17.02.2025)**
* **Add image as theme wallpaper**
* **Change any theme color**
* **Change report font color**
* **Live data receive from analyzer**
* **Use docx file template for result**
* **Send/Receive data from database or server using API/Local**

## Task Requirements & Testing Environment
This project was developed using the latest operating systems, software, and tools.

* **Operating System :** Windows7, Windows10, Windows11, Kali Linux2022.4 and MacOS Sierra 10.12
* **Software :** Python3.11 and Visual Studio Code
* **System Type :** 32-bit and 64-bit
* **Analyzer Company :** ExcBio, Hermes, Dymind, Genrui, Sysmex, Beckman Coulter, Arrows, Zybio, BioElab, Mindray, Erba etc as tested.
* **Database :** SQLite3, MySQL Server, MongoDB etc.


## Installation
First [download](https://www.python.org/downloads/), install and configure [python](https://www.python.org/doc/). Then use the package manager [pip](https://pip.pypa.io/en/stable/) to install on.

* Windows installation
* Kali linux installation
* Mac installation
---

## Clone the Repository

```bash
git clone https://github.com/iam-ariful-islam/hematology-analyzer-lisv1.git
```

## Notes
The `requirements.txt` file, lists of all the Python libraries that my "**_hematology analyzer lis system_**" depends on and installs those packages from the file and for better use, configure the system by looking at the `notes.txt` name file:

```
pip install -r requirements.txt
```

### **or**

```
sudo pip install -r requirements.txt
```

## Project screenshots
**Main Window**<br/>
<img alt="main" src="https://github.com/iam-ariful-islam/Hematology-Analyzer-LISv1/blob/main/screenshots/main.png" />

**Admin Page**<br/>
<img alt="admin" src="https://github.com/iam-ariful-islam/Hematology-Analyzer-LISv1/blob/main/screenshots/admin.png" />

**Login Page**<br/>
<img alt="login" src="https://github.com/iam-ariful-islam/Hematology-Analyzer-LISv1/blob/main/screenshots/login.png" />

**Change Login System**<br/>
<img alt="change_login" src="https://github.com/iam-ariful-islam/Hematology-Analyzer-LISv1/blob/main/screenshots/change_login.png" />

**Settings Page**<br/>
<img alt="settings" src="https://github.com/iam-ariful-islam/Hematology-Analyzer-LISv1/blob/main/screenshots/settings.png" />

**Extra Settings Page**<br/>
<img alt="extra_settings" src="https://github.com/iam-ariful-islam/Hematology-Analyzer-LISv1/blob/main/screenshots/extra_settings.png" />

**Pathologist Setup**<br/>
<img alt="pathologist" src="https://github.com/iam-ariful-islam/Hematology-Analyzer-LISv1/blob/main/screenshots/pathologist.png" />

**Doctor Setup**<br/>
<img alt="doctor" src="https://github.com/iam-ariful-islam/Hematology-Analyzer-LISv1/blob/main/screenshots/doctor.png" />

**Reference value Setup Page**<br/>
<img alt="reference_value" src="https://github.com/iam-ariful-islam/Hematology-Analyzer-LISv1/blob/main/screenshots/reference_value.png" />

**API Setup**<br/>
<img alt="api_setup" src="https://github.com/iam-ariful-islam/Hematology-Analyzer-LISv1/blob/main/screenshots/api_setup.png" />

**Report Page**<br/>
<img alt="report_page" src="https://github.com/iam-ariful-islam/Hematology-Analyzer-LISv1/blob/main/screenshots/report_page.png" />

**Machine Result**<br/>
<img alt="machine_result" src="https://github.com/iam-ariful-islam/Hematology-Analyzer-LISv1/blob/main/screenshots/machine_result.png" />

**Statement Page**<br/>
<img alt="statement_page" src="https://github.com/iam-ariful-islam/Hematology-Analyzer-LISv1/blob/main/screenshots/statement_page.png" />

**With Histogram-Reportlab**<br/>
<img alt="with_graph" src="https://github.com/iam-ariful-islam/Hematology-Analyzer-LISv1/blob/main/screenshots/with_graph.png" />

**Without Histogram-Reportlab**<br/>
<img alt="without_graph" src="https://github.com/iam-ariful-islam/Hematology-Analyzer-LISv1/blob/main/screenshots/without_graph.png" />

**With Histogram-Docx**<br/>
<img alt="with_graph2" src="https://github.com/iam-ariful-islam/Hematology-Analyzer-LISv1/blob/main/screenshots/with_graph2.png" />

**Without Histogram-Docx**<br/>
<img alt="without_graph2" src="https://github.com/iam-ariful-islam/Hematology-Analyzer-LISv1/blob/main/screenshots/without_graph2.png" />

**Report Folder**<br/>
<img alt="report_folder" src="https://github.com/iam-ariful-islam/Hematology-Analyzer-LISv1/blob/main/screenshots/report_folder.png" />

**Code Snapshot**<br/>
<img alt="code_snapshot" src="https://github.com/iam-ariful-islam/Hematology-Analyzer-LISv1/blob/main/screenshots/code_snapshot.png" />

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## For more or connect with me

<p align='center'>
  <a href="https://github.com/iam-ariful-islam"><img src="https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white" /></a>&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="https://twitter.com/am_ariful_islam"><img src="https://img.shields.io/badge/twitter-%231DA1F2.svg?&style=for-the-badge&logo=twitter&logoColor=white" /></a>&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="https://bd.linkedin.com/in/im-ariful-islam"><img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" /></a>&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="https://www.facebook.com/jonakisoft.net/"><img src="https://img.shields.io/badge/Facebook-%231877F2.svg?style=for-the-badge&logo=Facebook&logoColor=white" /></a>&nbsp;&nbsp;&nbsp;&nbsp;
</p>

## License

The [MIT](https://choosealicense.com/licenses/mit/) License (MIT)
