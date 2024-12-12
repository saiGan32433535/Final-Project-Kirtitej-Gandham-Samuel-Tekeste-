# Final-Project-Kirtitej-Gandham-Samuel-Tekeste-

## Final Project

##Third party module: PANDAS 

### ###Health based progra,


### Instructions: 
To install this Package you must open your terminal and type pip install pandas. 

**On Windows**
$ python -m pip install pandas

**On Mac**

$ python  pip install pandas

**Note**
Make sure you have acess to the 2 csv files for this project. Insurance.csv and Hospinfo.csv


### summary explained: 
To summarize what our project does is that it analyzes health related data to provide information and recommendations to the user base. In this project we used 2 different datasets from kaggle. One was on insurance data and one was on the information of different hospitals. We wanted to make a program that allowed the user to navigate between 2 options. One was estimating insurance costs based on their characteristics such as age, BMI, number of children, whether they are a smoker,  region they live in and more. The user would input these characteristics and the code will estimate what their health insurance costs typically would be. Additionally our project also allows them to look at different hospitals. Our program asks what state they prefer and what rating they prefer. Based on what the users chooses it outputs our recommended hospitals. During the project I worked on the insurance estimator while Samuel Tekeste worked on the hospital information. However we both looked at both portions and added what we thought was best. So we basically worked on the whole thing together rather than putting 100% focus on only one task.

### Code explained: 
To explain our code what we did was use pandas to read and import these datasets into our program thus creating a vast data frame. We have our main function which allows users to navigate the project. They choose 1 for the insurance estimation and they choose 2 for the hospital recommendation. What our insurance estimator does is that it asks the user for inputs on their age, gender, etc. After our code uses the .corr method to calculate the correlation coefficient of age, bmi and being a parent on lines 28-30. Line 34to 37 we print these out to inform the user on how these factors contribute to their insurance costs. The most important part of our code I believe is lines 42 to 84. Here we start with an empty list which is the final average. Based on what the user inputted, our code takes that and accesses the data frame. If the data frame consists of an element that has the user's input , it will filter out every other row that doesn’t include that. For instance, the user says they are 32 yrs old. Every row that doesn’t include that age will be filtered out. Every row with the age 32, will than calculate the average cost. So let’s say there were 10 people in the data set that were 32. We will find the average cost of those 10. This code basically does the same for every other variable such as smoking, number of children, region, bmi. As we find these averages we append them into the initial list which is the final average. Once our list is complete we make the final estimation on lines 82 to 84. Here we take the sum of all the sub averages and then divide it by the length of the list. After that we finally get the final estimation. On line 89 the next function is defined which is our hospital recommendation.  We use the .head method to give the user a preview of what the dataset looks like. The .head method outputs the first 5 rows. After that we ask the user for 2 inputs which include what state they prefer and the rating they want. The most important part of this function is lines 104 to 107. Based on the user input we filter out unwanted states and ratings. This data set was messy and had lots of data that was labeled not available. So we also had to filter those out ourselves. By the end this function prints out the users state, the hospitals from that state and the hospitals that are the rating the user asked for. Lines 125 to 147 is our main menu function. This is the first function the user will see. Here we ask the user to enter the number of their choice associated with what option they want. This follows by an if/else statement. If the user chooses 3 this breaks the loop and the code ends. So they will no longer be able to navigate the project until they run it again. The the purpose of this is to call the function the user chooses. 

### Practical use: 

As I mentioned before this program is focused on helping its users to estimate how much their insurance will cost while also recommending them the best hospitals that suit their preferences. Health insurance and looking for care is very stressful. Although this program is limited due to the data sets its relying on, a more advanced version of this program can help a lot of people. For example, if machine learning was used it can make more accurate estimations, and with more data it can recommend hospitals that are the most convenient to get to from their location, and also have a good reputation. 


### Future idea: 

I have a lot of ideas in the future I plan to work on. I had ideas prior to the one I worked on, but I wasn’t comfortable enough with my programming skills to make them. One idea I have is creating a program that can detect phishing websites based on the url the user inputs. So what the project will do is use an api key from different websites that will provide information and data on what phishing links look like. Using api keys and enough data sets, I will also create a data frame that showcases what a legitimate link by phishing link looks like. For example a lot of attackers use https rather than http. They also try to use an official domain, to mask a fake one with extra letters and wrong spellings. I would use machine learning libraries to test the data. Based on how well the program is trained it will be able to detect a phishing link when the user inputs it in. In the future, I also want to make more programs that are capable of making predictions based on the data it’s been given.  


