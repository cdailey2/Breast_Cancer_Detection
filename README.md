# Exploring the Efficacy of Supervised Machine Learning Models in Breast Cancer Detection Based on Cellular Characteristics

## Objective
This project aims to create verbose supervised machine learning models with good practice to detect malignant breast cancer tumors based on cellular characteristics and compare and contrast strengths and weaknesses of respective models as well as discuss possible use cases within the medical field. 

<br>

## Technologies
Jupyter Notebook was used packed with a number of data manipulation and analysis and machine learning libraries including numpy, pandas, matplotlib, seaborn, and sklearn. 

<br>

## Project Overview<br>
**Table of Contents**
1. [Problem Formulation](#problem-formulation)
1. [Data Dictionary](#data-dictionary)
1. [Data Collection, Storage, Cleaning, and Validation](#data-collection-storage-cleaning-and-validation)
1. [Machine Learning Models](#machine-learning-models)
1. [Comparative Analysis of Models](#comparative-analysis-of-models)
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
The dataset’s accuracy and reliability are strengthened by the fact that it comes from the <a href='https://archive.ics.uci.edu/'>University of California, Irvine (UCI) Machine Learning Repository</a>, a globally recognized source for curated datasets. The dataset is known as  <a href='https://archive.ics.uci.edu/dataset/15/breast+cancer+wisconsin+original'>Breast Cancer Wisconsin (Original)</a>. The data were relativeely clean, however, the dataset contained duplicates, as well as special characters ("?") for missing data. All of these were removed. Data is tied to a unique ID, meaning that all duplicates were actual duplicates (rather than just having identical data tied to them). Removing them would therefore inhibit accidental data skewing. Furthermore, rows with special characters were removed due to the fact that all data are discrete integers, meaning that it would not make sense to replace them with an average. 

<br>

### Machine Learning Models
<p>Two models were developed: a Random Forest model and an Artificial Neural Network (ANN). The following figures present accuracy metrics used to evaluate the performance of each model.</p>

**1. Random Forest** 
<p>The random forest model was created using 70% of the total data as training data and 30% of the total data as test data. Hyperparameters were tuned empirically through an extensive grid search with 3-fold cross-validation</p>
<br>
<p><b>Figure 1</b> displays a confusion matrix below shows the results of testing the Random Forest model using the test data, which was separate from the training data. The model demonstrated exceptional performance.</p>
<img src="https://i.imgur.com/bRQjtRc.png">
<sub><b>Figure 1</b>. Random Forest Confusion Matrix - Testing the model with test data</sub>
<p></p>
<p><b>Figure 2</b> displays a classification report in table format, displaying the results of testing the random forest model </p>
<img src="https://i.imgur.com/dS2c8kH.png">
<sub><b>Figure 2</b>. Random Forest Classification Report - Testing the model with test data</sub>
<p></p>

**2. Artificial Neural Network**
<p>As with the random forest model, the artificial neural network was created using 70% of the total data as training data and 30% of the total data as test data. Hyperparameters were tuned via elbow finding using a loss curve along with some manual empirical testing.</p>
<br>
<p><b>Figure 3</b> displays a confusion matrix below shows the results of testing the neural network model using the test data, which was separate from the training data. The model demonstrated exceptional performance as well. However, this model was slightly less accurate than the random forest </p>
<img src="https://i.imgur.com/HbW0QRR.png">
<sub><b>Figure 3</b>. Artificial Neural Network Confusion Matrix - Testing the model with test data</sub>
<p></p>
<p><b>Figure 4</b> displays a classification report in table format, displaying the results of testing the ANN model </p>
<img src="https://i.imgur.com/zZ5eFvz.png">
<sub><b>Figure 4</b>. Artificial Neural Network Classification Report - Testing the model with test data</sub>
<br>


### Comparative Analysis of Models
<p>Before comparing the models, it is first important to define which metric this should be guaged off of. Medical care is a very high stakes field. Getting both false-negatives and false-positives can be argued as equally detrimental. If the models mis-predict the benign class, patients may be led to not pursue treatment that they are in desperate need of. On the other hand, if models mispredict the malignant class, then patients may be led to pursue difficult, expensive and possibly life-changing treatment that they are not in need of. Therefore, I have concluded that total accuracy is the most important metric.</p>
<p>The Random Forest model achieves an accuracy of 99%, outperforming the Artificial Neural Network, which has an accuracy of 98%. This distinction is significant because, Proportions exhibit a multiplier effect because even small changes in percentages can lead to substantial impacts when applied to larger populations or quantities. When applied to a population of 100,000 people, it translates to a difference of 1,000 individuals being misdiagnosed.</p>
<p>Though the difference in accuracy is an important consideration, it does not necessarily mean that the random forest model is entirely better. ANNs are typically better at handling exctremely large datasets. The models seen here were created with only around 700 lines of data. One used in a real healthcare setting would need much more. Just because the random forest outperforms the ANN with this datset, does not necessarily mean that this will translate with a different, much larger dataset. On the other hand, explainability and transparency are crucial in high-stakes machine learning models because they foster trust and acceptance among stakeholders, enabling users to rely on decisions made by these systems. When models make mistakes, explainability allows stakeholders to understand the reasoning behind decisions, establishing accountability and ensuring compliance with regulations that mandate transparency in decision-making processes. Additionally, transparent models help detect and mitigate biases in the data, leading to fairer outcomes. By providing insights into how decisions are made, explainability aids in model improvement, empowering users—such as patients in healthcare—to engage more actively in their decisions. ANNs are often seen as more of a black box due to their complexity, non-linear transformations, and large number of parameters. Whereas, random forest is entirely based on feature importance, which is mapped into a decision tree, so if a rogue decision occurs, it can be traced from A to B. </p>


### Works Cited<br>
Wolberg, Wi. (1992). Breast Cancer Wisconsin (Original). UCI Machine Learning Repository. https://doi.org/10.24432/C5HP4Z

<br>

World Health Organization. (n.d.). WHO launches new roadmap on breast cancer. Www.who.int. https://www.who.int/news/item/03-02-2023-who-launches-new-roadmap-on-breast-cancer#:~:text=In%2095%25%20of%20countries%2C%20breast

<br>

World Health Organization. (2022, February 3). Cancer. World Health Organization. https://www.who.int/news-room/fact-sheets/detail/cancer

<br>

Zhang, B., Shi, H., & Wang, H. (2023). Machine Learning and AI in Cancer Prognosis, Prediction, and Treatment Selection: A Critical Approach. Machine Learning and AI in Cancer Prognosis, Prediction, and Treatment Selection: A Critical Approach, Volume 16(16), 1779–1791. https://doi.org/10.2147/jmdh.s410301




