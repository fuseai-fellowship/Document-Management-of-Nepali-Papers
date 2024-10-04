# Nepali Document and Record Management System



https://github.com/user-attachments/assets/86e35e48-cd95-4ab8-8a66-fea9eba24571



## Introduction
In the digital age, maintaining the accessibility, security, and longevity of information requires effective document management and preservation. However,In Nepal, a large portion of crucial documents like historical archives, legal papers, or government documents are still stored in paper format. This dependence on the storage of information physically, comes with many disadvantages including destruction and misplacement of documents, as well as broken retrieval systems. Additionally, these papers were usually organized manually and in most cases, the sorting produces unreliable results, which explains the poor organization of such documents.
One more aspect which continues to aggravate the problems is that there is no proper Document and Record Management System (DRMS) which is specifically designed for Nepalese documents. Such global DRMS solutions do exist, however, most do not take into consideration the types of documents which are of Nepali origin and the type of software which supports these documents. Consequently, it is apparent that there is an urgent need of such system which is capable of not only digitizing the records but also bringing about a proper and efficient way of classifying the records.
The aim is to overcome these obstacles by making a DRMS which involves the use of Tesseract OCR technology to convert Nepali documents and images into digital form. Furthermore, the project will incorporate a machine that can automatically classify the documents according to the content making the use of manual work minimal and optimizing the document management processes. Targeting particularly the case of Nepal, this project endeavors to narrow the discrepancy between DOIM (Document and Information Management) needs and current DRMS (Document and Record Management systems) provisions.
## Goals
## Contributors
## Project Architecture

# Status
## Known Issue
## High Level Next Steps


# Usage
## Installation
To begin this project, use the included `Makefile`

#### Creating Virtual Environment

This package is built using `python-3.8`. 
We recommend creating a virtual environment and using a matching version to ensure compatibility.

#### pre-commit

`pre-commit` will automatically format and lint your code. You can install using this by using
`make use-pre-commit`. It will take effect on your next `git commit`

#### pip-tools

The method of managing dependencies in this package is using `pip-tools`. To begin, run `make use-pip-tools` to install. 

Then when adding a new package requirement, update the `requirements.in` file with 
the package name. You can include a specific version if desired but it is not necessary. 

To install and use the new dependency you can run `make deps-install` or equivalently `make`

If you have other packages installed in the environment that are no longer needed, you can you `make deps-sync` to ensure that your current development environment matches the `requirements` files. 

## Usage Instructions


# Data Source
## Code Structure
## Artifacts Location

# Results
## Metrics Used
## Evaluation Results
