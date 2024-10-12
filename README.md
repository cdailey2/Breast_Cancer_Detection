# Exploring the Efficacy of Supervised Machine Learning Models in Breast Cancer Detection Based on Cellular Characteristics

## Objective
This project aims to create verbose supervised machine learning models with good practice to detect malignant breast cancer tumors based on cellular characteristics and compare and contrast strengths and weaknesses of respective models as well as discuss possible use cases within the medical field. 

<br>

## Technologies
Jupyter Notebook was used packed with a number of data manipulation and analysis and machine learning libraries including numpy, pandas, matplotlib, seaborn, and sklearn. More on this can be found in the [project documentation](https://github.com/cdailey2/Breast_Cancer_Detection/blob/main/docs/project_documentation.md).

<br>

## Project Overview<br>
**Table of Contents**
1. [Problem Formulation](#problem-formulation)
1. [Data Dictionary](#data-dictionary)
1. [Data Collection, Storage, Cleaning, and Validation](#data-collection-storage-cleaning-and-validation)
1. [Machine Learning Models](#machine-learning-models)
1. [Works Cited](#works-cited)

---

### Problem Formulation
Cancer is a prominent issue within the healthcare system due to its high incidence and mortality rate. The WHO states “Cancer is a leading cause of death worldwide, accounting for nearly 10 million deaths in 2020” (World Health Organization, ¶1). One of the most common and dangerous types of cancer is breast cancer. According to the WHO, breast cancer was the leading cancer diagnosis in 2020 with 2.26 million cases. Furthermore, Breast cancer accounted for 685 000 deaths in 2020, which places it in 6th among all cancer forms for highest mortality. While significant progress has been made to diagnose and treat patients suffering from the disease, Significant disparities are seen in survival rates of breast cancer based on differences in human development. Dr Tedros Adhanom Ghebreyesus, Director-General of WHO stated “[c]ountries with weaker health systems are least able to manage the increasing burden of breast cancer. It places a tremendous strain on individuals, families, communities, health systems, and economies[...]” (World Health Organization, ¶3). Furthermore, the WHO states “[...] 80% of deaths from breast and cervical cancer occur in low- and middle-income countries” (World Health Organization, ¶2). Therefore, overstrained and underfinanced healthcare systems in areas with lower human development require aid in order to properly diagnose and treat patients suffering from this ailment. One of the easiest ways to achieve this is automation. Machine Learning has in some cases proven to be more accurate than medical doctors in diagnosing illness. This report aims to find trends in breast cancer cell characteristics to determine what factors likely indicate malignant cancers as well as create machine learning models and use data visualizations to assess the accuracy and effectiveness of these models.

<br>

### Data Dictionary
1. Sample code number:            ID number
2. Clump Thickness:               1 - 10
3. Uniformity of Cell Size:       1 - 10
4. Uniformity of Cell Shape:      1 - 10
5. Marginal Adhesion:             1 - 10
6. Single Epithelial Cell Size:   1 - 10
7. Bare Nuclei:                   1 - 10
8. Bland Chromatin:               1 - 10
9. Normal Nucleoli:               1 - 10
10. Mitoses:                      1 - 10
11. Class:                        (2 for benign, 4 for malignant)

(Wolberg, 1992)

<br>

### Data Collection, Storage, Cleaning, and Validation
- Details in [project documentation](https://github.com/cdailey2/Breast_Cancer_Detection/blob/main/docs/project_documentation.md).

<br>

### Machine Learning Models
**1. Random Forest** 
<br>
<img src="https://i.imgur.com/bRQjtRc.png">
<br>
<img src="https://i.imgur.com/dS2c8kH.png">
<br>

**2. Artificial Neural Network**
<br>
<img src="https://i.imgur.com/HbW0QRR.png">

<img src="https://i.imgur.com/zZ5eFvz.png">
<br>

### Works Cited<br>
Wolberg, Wi. (1992). Breast Cancer Wisconsin (Original). UCI Machine Learning Repository. https://doi.org/10.24432/C5HP4Z

<br>

World Health Organization. (n.d.). WHO launches new roadmap on breast cancer. Www.who.int. https://www.who.int/news/item/03-02-2023-who-launches-new-roadmap-on-breast-cancer#:~:text=In%2095%25%20of%20countries%2C%20breast

<br>

World Health Organization. (2022, February 3). Cancer. World Health Organization. https://www.who.int/news-room/fact-sheets/detail/cancer

<br>

Zhang, B., Shi, H., & Wang, H. (2023). Machine Learning and AI in Cancer Prognosis, Prediction, and Treatment Selection: A Critical Approach. Machine Learning and AI in Cancer Prognosis, Prediction, and Treatment Selection: A Critical Approach, Volume 16(16), 1779–1791. https://doi.org/10.2147/jmdh.s410301




