__The paper is currently being reviewed, so the paper is not publically availably yet.__
# SAR edge benchmark
This GitHub repository contains information needed to evaluate on the simulated SAR edge detection benchmark described in [this paper](paperlink). The results of the evaluations on BSDS500-speckled are shown in the following table:  
_BSDS500-speckled Benchmark. The rows are sorted by ODS F1. The best results are highlighted
in bold, while the second best results are underlined._
![](https://github.com/readmees/SAR_edge_benchmark/blob/main/Denoised%20BSDS500-speckled%20Benchmark.png?raw=true)
_BSDS500-speckled Noisy Benchmark. The rows are sorted by ODS F1. The best results are high-
lighted in bold, while the second best results are underlined._
![](https://github.com/readmees/SAR_edge_benchmark/blob/main/Noisy%20BSDS500-speckled%20Benchmark.png?raw=true)
_The performances of different methods on the Sentinel-1 Lelystad, ordered by F1 score_
![](https://github.com/readmees/SAR_edge_benchmark/blob/main/Lely%20Benchmark.png?raw=true)
Evaluating other edge detectors can be done in 4 steps.

## Step 1: Preparing the dataset
The BSDS500-speckled dataset can be generated with the code on [this GitHub repository](https://github.com/ChenguangTelecom/GRHED) further described by Chenguang. We denoised the images with SARBLF from [this repository](https://github.com/odhondt/ndsar), see the paper for parameter settings. The real SAR images of Lelystad, Flevoland, Netherlands and Odessa, Texas, United States shown in the paper can also be downloaded from this repository.

## Step 2: Creating edge response maps - training
For parameter tuning you can use the 28800 augmented speckled training images from [BSDS500-speckled](https://github.com/ChenguangTelecom/GRHED), use any edge detector of your choice.

## Step 3: Evaluating edge response maps - training
To evaluate the performance of new edge detectors the same way as the confusion matrices for the data ground truths should created for 21 different thresholds: 0, 0.05 ..., 0.95, 1. The confusion matrices should be stored in a Pandas dataframe with 28800 rows × 21 columns, one row for every image, with the 21 threshold values. Every confusion matrix should have the following format: ```"{'tn': 100368, 'fp': 99090, 'fn': 1530, 'tp': 7908}"```, which can be seen as a dictionary stored in a string. The Pandas dataframe should be saved as a .csv file, see [this file](https://github.com/readmees/SAR_edge_benchmark/blob/main/confusion_matrices/farid_measures.csv) as an example, used for the Farid edge detector evaluations in the paper.  The [Jupyter Notebook](https://github.com/readmees/SAR_edge_benchmark/blob/main/Evaluation%20of%20edge%20detectors.ipynb) will easilly create the ROC curves and metrics. For this program to smoothly work, the .csv files should be named '\[edge detector name\]\_measures.csv'.

## Step 4: Evaluating edge respons maps - test
For qualitative evaluations of the real SAR images, you can compare with the methods in the paper. For the OIS (F1), ODS (F1), AP and ODS (F1) Threshold for the BSDS500-speckled Benchmark can be evaluated by applying a [Python port of BSDS 500 boundary prediction evaluation suite](https://github.com/Britefury/py-bsds500.git) with 30 thresholds.

If you use this benchmark or have any questions, please let me know and contact me at contact@meesmeester.nl.
