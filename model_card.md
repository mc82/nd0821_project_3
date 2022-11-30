# Model Card

The trained model predicts whether the income, based on socioeconomic features, is either above or below a salary of $ 50k.

## Model Details

The model is a Logistic Regression model created with scikit learn. The model uses the default parameters.

## Intended Use

The model was trained as part of a Nanodegree assignment at Udacity.

## Training Data

The underlaying data is census data. You can find more about the data-set [here](https://archive.ics.uci.edu/ml/datasets/census+income).
The overall data-set contains 32561 rows and 15 columns.
80% of this data-set has been used to train the model

## Evaluation Data

The evaluation data was created on a train / test split. 20% has been used as evaluation data.

## Metrics

The model has been evaluated based on the following metrics:

- precision
- recall
- f1

Following you will find the overall evaluation based on the test-set:

Performance on total: precision: 0.7172887172887172, recall: 0.26468260250118725, fbeta: 0.38667900092506935

In addition, slices on categorical values have been created and evaluated. Here are some experts of the evaluations:

Race:
Performance on race Black: precision: 0.5882352941176471, recall: 0.2702702702702703, fbeta: 0.37037037037037035
Performance on race White: precision: 0.7145708582834331, recall: 0.2590448625180897, fbeta: 0.38024429102496016
Performance on race Asian-Pac-Islander: precision: 0.6538461538461539, recall: 0.3333333333333333, fbeta: 0.44155844155844154

Gender:
Performance on sex Male: precision: 0.7488789237668162, recall: 0.26403162055335966, fbeta: 0.3904149620105202
Performance on sex Female: precision: 0.5403225806451613, recall: 0.25868725868725867, fbeta: 0.3498694516971279

## Ethical Considerations

## Caveats and Recommendations

The model was trained only to demonstrate skill during an assignment. Only limited tests were applied.
