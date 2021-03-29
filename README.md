# Attraqt movie recommendation
This is the submission code for movies recommender test.

Please read the documentation below to run the code and generate the results.

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
* **It is assumed that the true ratings are stored in the file true_ratings.csv in the path data/true_ratings.csv** and has the following column names: **UserId, ModelId, TrueRating**

## Usage






## true results should have TrueRating as header

