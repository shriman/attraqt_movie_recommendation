# Attraqt movie recommendation
This is the submission code for movies recommender test.

Please read the documentation below to run the code and generate the results.

## Colab notebooks and preliminary data explorations
The repository contains two colab notebooks, which can be viewed either here in GitHub or in Google Colab (links are in files.)
* [**Attraqt.ipynb**](https://github.com/shriman/attraqt_movie_recommendation/blob/main/Attraqt.ipynb) : 
  * Initial data exploration and data cleaning.
  * **Basic recommender**: Recommender based solely on movie ratings. Predicts top n movies of all time.
  * **Genre-based movie recommender (top-K movies)**: Recommends top-n movies in each genre. 
  * **Metadata-based recommender / Content-based filtering** Recommends movies based on **tagline** and **overview**, using tfidf on text.
  
* [**Attraqt_collaborative_filtering_svd.ipynb**](https://github.com/shriman/attraqt_movie_recommendation/blob/main/Attraqt_collaborative_filtering_svd.ipynb):  
  * **Collaborative filtering based recommender** using the user ratings.
  * **Submission**: code to generate the submission results.
  * **Advanced recommender**: using a combination of collaborative filtering and content-based filtering approach.

## Set-up
* Clone the repository into your local folder.
* To run the code, you will need to have **Python 3.9** and **pip** installed. 
* Run the make command to create your virtual environemnt:
 ``` make ```
* Activate your virtual environment 
```source venv/bin/activate``` 

## Intial configuration and Data files
* The file ```configs/config.yml``` contains path to all the source files as well output files
* The data files are located in the folder ```data``` in the project path, where project path is the same as the 
  directory of this README file.
* Please note that the config file has three sections:
  * **data** : path to data files (movies_metadata.csv, ratings.csv, evaluation_ratings.csv, and true_ratings.csv)
  * **output**: path to output files 
  * **model**: path to trained model
```yaml
data:
  movies_metadata: 'data/movies_metadata.csv'
  ratings: 'data/ratings.csv'
  evaluation_ratings: 'data/evaluation_ratings.csv'
  true_ratings: 'data/true_ratings.csv'

output:
  submission: 'data/outputs/submission.csv'
  bonus_submission: 'data/outputs/bonus_submission.csv'

model:
  trained_model_path: 'data/outputs/svd_trained'
```
* **It is assumed that the true ratings are stored in the file true_ratings.csv in the path data/true_ratings.csv** and has the following column names: **UserId, ModelId, TrueRating**

## Usage
The project used **cli** to run the commands
* Train and save the model on the disk
```shell
# train the model and save to disk
$ python -m attraqt train
```
* Predict the ratings on evaluation dataset and generate the submissions file
```shell
# predict the ratings on the evaluation dataset
# and save results to submission.csv
$ python -m attraqt predict
```
* Evaluate the results using RMSE
```shell
# predict the ratings on the evaluation dataset
# and save results to submission.csv
$ python -m attraqt evaluate
```
* **To correctly run the evaluation, it is assumed that the true ratings are stored in the file true_ratings.csv in the path data/true_ratings.csv** 
  and have the following column names: **UserId, ModelId, TrueRating**
  
* The trained model is can be downloaded from [here](https://drive.google.com/file/d/13l6Sf27bBjoaoLsHjxN25OQHarzksOiP/view?usp=sharing)  
* The initial submissions file can be downloaded from [here](https://drive.google.com/file/d/1w-3kaRHxRYEb7bbpi208xuEoH08JtBOu/view?usp=sharing)

