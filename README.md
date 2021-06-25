# SAR edge benchmark
This GitHub repository contains the information needed to evaluate on a simulated SAR edge detection benchmark. For more information about this benchmark you can refer to [this thesis](https://github.com/readmees/SAR_edge_benchmark/blob/main/Thesis___Detecting_geometric_primitives_in_SAR_images%20(1).pdf). The data can be generated with the code from Chenguang on [this GitHub repository](https://github.com/ChenguangTelecom/GRHED). We denoised the images with SARBLF from [this repository](https://github.com/odhondt/ndsar) as decriped in [the thesis](https://github.com/readmees/SAR_edge_benchmark/blob/main/Thesis___Detecting_geometric_primitives_in_SAR_images%20(1).pdf). To evaluate the performance of new edge detectors the confusion matrices for the data ground truths should created for 21 different thresholds (0, 0.05 ..., 0.95, 1) and all the 28000 training images created from [here](https://github.com/ChenguangTelecom/GRHED).

To evaluate these confusion matrices [a Jupyter Notebook](https://github.com/readmees/SAR_edge_benchmark/blob/main/Evaluation%20of%20the%20edge%20detectors.ipynb) file has been added to this GitHub repository. It evaluates .csv files in the format shown in the DataFrame represenation of example .csv file:

<img src="https://github.com/readmees/SAR_edge_benchmark/blob/main/format_confusion_matrices.png" width="400">

The .csv files should be named '\[edge detector name\]\_measures.csv'.

In [the thesis](https://github.com/readmees/SAR_edge_benchmark/blob/main/Thesis___Detecting_geometric_primitives_in_SAR_images%20(1).pdf) we refer to the real SAR images, since they did not fit in the appendix, these can be found [here](https://github.com/readmees/SAR_edge_benchmark/tree/main/ODESSA_data).

For questions and further explaination you are welcome to contact contact@meesmeester.nl by email.
