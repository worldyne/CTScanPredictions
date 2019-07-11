# Overview: [CT Predictions](https://docs.google.com/presentation/d/18sDxk-tp57OcvZb_ZAvChxeDB3WP5Uiagb1IaXPrymE/edit?usp=sharing)
## Business Understanding
I am interested in the CT scans of the head. I would like to classify whether a patient has intraparenchymal (IPH), intraventricular (IVH), subdural (SDH), extradural (EDH) and subarachnoid (SAH) hemorrhages, calvarial fractures, or midline shift and mass effect.

## Data Understanding
I will use the [qure.ai](http://headctstudy.qure.ai/dataset) dataset. 

## Data Preparation
I'll store the images in an S3 bucket. I’ll use the labels provided by the 3 radiologists who were a part of the study. I will write a function to format the images into appropriately pre-processed floating point tensors that can be fed into the network.

## Modeling
I'll set aside a final validation set of labeled images, maybe 20% for each class. Then I'll use Keras to build an image classifier by fine-tuning a pre-trained base model and tf.keras.Sequential. I'll also try using deep feature extraction on the images and making predictions using logistic regression, random forest, XGBoost.

## Evaluation
I will report both the accuracy score and cross entropy loss, on training and test data. I plan to use k-fold cross-validation to do any needed parameter tuning.

## Deployment
The model will be deployed as a Flask app that can be used to upload a picture of a CT scan from a computer to get a prediction of the status of the head.

## User Story: 
Research Doctor uploads CT image to website. Website returns the probability of each of the classes of hemorrhages, calvarial fractures, or midline shift.
