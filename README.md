# Lung-Cancer-AI
Middle School Science Fair Project for GARSEF


Environment setup:  
Step 1:  Made a repository on GitHub call LUNG-CANCER-AI  
Step 2: Then we downloaded Github desktop and git  
Step 3: Using github we cloned the repository into a local directory called: 'C:\Users\samar\src\Lung-Cancer-AI'   
Step 4: We downladed and installed vscode  
Step 5: We opened source directory specified in step 3 in vscode and updated this read me 
Step 6: Installed python and said hello world for the millitonth time
Step 7: Added a requrements.txt file for all the libraries i think i will need for now  
Step 8: Installed the requirments using the following command 'pip install -r .\requirments.txt'  
Step 8.1: Every time I need a new library i can add it in requiments and run the code above again  

Data Aquisition:
Step 1: Downloaded Lung Cancer Dataset from Kaggle.com from 'https://www.kaggle.com/datasets/mysarahmadbhat/lung-cancer/'  
Step 2: Copied this file into the data directory for this project    
Step 3: renamed the file to 'survey_lung_cancer.csv'  

Understanding the Data:
Step 1: File is a csv file(comma seperated value)
Step 2: We will opent the file using pandas and examine the contents
Step 3: I read the csv using the read_csv function in the pandas library  
Step 4: I print the number of rows and columns using df.shape  
Step 5: I print all the name of the columns using df.columns
Step 6: The data is of current patients who tested for lung cancer and were given a diagnosis of positive or negative in the column LUNG_CANCER. The other column represents various attrubutes that were colle4cted for the patient such as age and smoking.  
Step 7: Our task in this project is to use this data to predict whether or not someone has lung cancer if we are provided all the attributes in this file.  



Splitting the Data:  
1. I got all the data in a jupyter notebook and then i converteed on datframe into two dataframes X and y. X represents the predictors which in this case are the symptoms and y is the result which in this case is wheter the patient has lung cancer or not  
2. now we split the data into train and test datasets using the command 'X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)'  
3. This splits 80 percent of data for training the ai and the remaining twenty for testing the ai model.  

Choosing the Algorithm:  
1. This problem requires us to use supervised learning to predict/classify if the patient has lung cancer or not  
2. Now we go and search algorithims available for classification.  
3. I tried to make the logistic regression due to logistic being yes or no and i fail on the second line of code
4. We took a litlle detour due to a error because the values for some columns were strings so we made them into numbers so that we could easily use logictic regression. *We tried to make logistical regression, is the reason it didnt work  
5. Today I finished most of the AI i just have to integrate it into a ai and then I have to finish tyhe posterboard tommorow.  


Creating web UI for this project  
1. Import flask in requirements.txt and install using pip 
2. Made a basic web page that we will expand on 
3. while expanding a note to self is that yf = yellow fingers.  
4. We added all of the possible symptoms to the html  
5. we made it to drop down using this'<label for="fatigue">Fatigue:</label><br>
<select id="fatigue" name="fatigue">
  <option value="Yes">Yes</option>
  <option value="No">No</option>
</select><br>'  
6. We made the lung cancer we just have to clean up the website  
7. 
