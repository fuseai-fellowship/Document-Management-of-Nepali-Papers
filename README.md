# Nepali Document and Record Management System



https://github.com/user-attachments/assets/86e35e48-cd95-4ab8-8a66-fea9eba24571



## Introduction
In the digital age, maintaining the accessibility, security, and longevity of information requires effective document management and preservation. However,In Nepal, a large portion of crucial documents like historical archives, legal papers, or government documents are still stored in paper format. This dependence on the storage of information physically, comes with many disadvantages including destruction and misplacement of documents, as well as inefficiency in information retrieval.  Furthermore, the manual classification of these documents is often time-consuming and prone to human error, leading to inconsistent and unreliable categorization.

One more aspect which continues to aggravate the problems is that there is no proper Document and Record Management System (DRMS), specifically designed for Nepali documents. While global DRMS solutions exist, they often fail to account for the unique linguistic, cultural, and technical requirements of Nepali documents. Hence, it is apparent that there is a need of such system which is capable of not only digitizing the records but also bringing about a proper and efficient way of classifying the records.

This project aims to address these challenges by developing a DRMS that leverages Tesseract OCR technology to digitize Nepali documents and images, preserving their content in digital form. Additionally, the project will implement an automated document classifier capable of categorizing documents based on their content, thereby reducing the dependency on manual processes and enhancing the overall efficiency of document management. By focusing on the specific context of Nepal, this project seeks to fill the gaps in existing DRMS solutions and provide a more tailored approach to document and record management in the country.
## Goals
1. **Digitization of Nepali Documents**: Utilize Tesseract OCR technology to convert physical Nepali documents and images into digital format, preserving their content.
2. **Automated Document Classification**: Develop an automated document classifier using Bi-LSTM to categorize documents based on their content, reducing reliance on manual classification processes.
3. **Enhanced Information Retrieval**: Enable users to conduct full-text searches on document contents, allowing for quick and efficient location of relevant documents.
## Contributors
[**Arun Poudel**](https://github.com/poudelarun) - Built Image Preprocessing Pipeline, Dataset Generation, Streamlit UI Development

[**Pranjal Khadka**](https://github.com/pranzalkhadka) - Built Document Classification Model, Docker Containerization and Project Deployment

[**Samip Lamsal**](https://github.com/lamsalsamip1) - Fine Tuned Tesseract OCR, Built Augmentation Pipeline, Content-based Search & Project Integration


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
