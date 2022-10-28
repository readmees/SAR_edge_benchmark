# SAR image edge detection benchmark suite 
This GitHub repository is the benchmark suite of the [SAR image edge detection: review and benchmark experiments
](https://doi.org/10.1080/01431161.2022.2131480) paper. It contains all the information needed to evaluate and benchmark algorithms on the simulated SAR edge detection benchmark.
When you use our work, please cite: 
```
@article{meester2022,
 author = {M. J. Meester and A. S. Baslamisli},
 title = {SAR Image Edge Detection: Review and Benchmark Experiments},
 journal = {International Journal of Remote Sensing},
 volume = {43},
 number = {14},
 year = {2022},
 pages = {5372-5438},
 doi = {10.1080/01431161.2022.2131480}
}
```

Furthermore, when using the dataset, please also cite the original work that proposed it:
```
@article{liu2020,
 author = {C. Liu and F. Tupin and Y. Gousseau},
 title = {Training CNNs on Speckled Optical Dataset for Edge Detection in SAR Images},
 journal = {ISPRS Journal of Photogrammetry and Remote Sensing},
 volume = {170},
 year = {2020},
 pages = {88-102},
 doi = {10.1016/j.isprsjprs.2020.09.018}
}
```

The results of the evaluations on BSDS500-speckled are shown in the following table:  
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

## Step 4: Evaluating edge response maps - test
For qualitative evaluations of the real SAR images, you can compare with the methods in the paper. For the OIS (F1), ODS (F1), AP and ODS (F1) Threshold for the BSDS500-speckled Benchmark can be evaluated by applying a [Python port of BSDS 500 boundary prediction evaluation suite](https://github.com/Britefury/py-bsds500.git) with 30 thresholds.

## Further information
If you would like evaluate on Lely, simply run your edge detector on real_sar_data/Lely_input.png. And use the threshold found with [Evaluation of edge detectors.ipynb](https://github.com/readmees/SAR_edge_benchmark/blob/main/Evaluation%20of%20edge%20detectors.ipynb) in 'Step 3: Evaluating edge response maps - training', for obtaining a binary edge map. You can use this to calculate F1 score, see the Python code for these metrics [here](https://raw.githubusercontent.com/readmees/SAR_edge_benchmark/main/utils_confusion_matrix_analyser.py).
If you have any questions, please contact me at contact@meesmeester.nl. If you would like your edge detector to be ran on the benchmark and have the results published on this page, please let me know.
