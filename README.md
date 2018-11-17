# dance-moves-prediction

We aim to predict dance moves using a combination of Random Forest and Support Vector Machine
(SVM) to get the best possible accuracy. Train and test data are based on the readings obtained
from two sensors (GY-521 MPU6050 3-Axis Acceleration Gyroscope 6DOF Module) attached to the 
dancers wrists. The raw features are Acceleration x, y, z and Rotation x, y, z. There are a
total of 11 dance moves to be classified.

## Resolving Dependencies
1. Create a virtual environment in the directory
  ```shell
  python3 -m venv venv
  ```
2. Activate the virtual environment
  ```shell
  source venv/bin/activate
  ```
3. Install all the required dependencies
  ```shell
  pip install -r requirements.txt
  ```

## Generating Machine Learning Models
1. Activate the virtual environment
2. Resolve all the dependencies
3. Run `python train_random_forest.py` to generate Random Forest model
4. Find the models in `.sav` format in `models` directory

To generate SVM model, run `python train_svm.py` at Step 3 instead.

Alternatively, run `./fast_generate_models.sh` at Step 3 to generate both models at the same time.

**Note that each Machine Learning model takes around 1.5 hours to generate owing to the hyperparameter 
tuning involved. It is advised to run the model training from a detached session of a terminal multiplexer.**

## Plotting Graphs for All Dance Moves
1. Activate the virtual environment
2. Resolve all the dependencies
3. Make sure that the code below is commented out in `train_data.py` 👎
  ```python
    ##### COMMENT OUT THE CODE BELOW BEFORE RUNNING plot.py #####
    df_max_min = prep.flatten(df, interval)
    df_var = prep.flatten(df, 'var', interval)
    df_concat = prep.concat_df(df_max_min, df_var)
    df = prep.append_truth(df_concat, number)
    #############################################################
  ```
4. Run `python plot.py`
5. Find the graphs in `.png` format in `plots` directory   

## Testing Final Model
1. Activate the virtual environment
2. Resolve all the dependencies
3. Generate machine learning models
3. Customise how the models generated are utilised in MLModel class (`test_model/__init__.py` file)
4. Run `python test.py`

Note that final model can be a combination of both Random Forest and SVM.
