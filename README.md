# SAR edge benchmark
This GitHub repository contains the information needed to evaluate on a simulated SAR edge detection benchmark. For more information about this benchmark you can refer to [this thesis](https://github.com/readmees/SAR_edge_benchmark/blob/main/Thesis___Detecting_geometric_primitives_in_SAR_images%20(1).pdf). The data can be generated with the code from Chenguang on [this GitHub repository](https://github.com/ChenguangTelecom/GRHED). To evaluate the performance of new edge detectors the confusion matrices for the data ground truths should created for 21 different thresholds (0, 0.05 ..., 0.95, 1) and all the 28000 training images created from [here](https://github.com/ChenguangTelecom/GRHED).

To evaluate these confusion matrices a Jupyter Notebook file has been added to this GitHub repository. It evaluates .csv files in this format:
![Dataframe represenation of example .csv file](https://github.com/readmees/SAR_edge_benchmark/blob/main/format_confusion_matrices.png)]. 
The .csv files should be named '\[edge detector name\]\_measures.csv'.
