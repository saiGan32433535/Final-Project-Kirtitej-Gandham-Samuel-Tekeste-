
import pandas as pd


#Kirtitej Gandham & Sameul Tekeste

#Imports to the 2 csv files that are being used for the project incuding the datasetson Hositpal info and insurance
hospital_df = pd.read_csv('HospInfo.csv')
insurance_df = pd.read_csv('insurance.csv')
insurance_df['bmi'] = insurance_df['bmi'].astype(int)


#Defining a function that will generate the estimated cost of user insurance based on the data they give
def estimate_insurance_cost():
    print("Insurance Cost Estimator")

    #This is where we will be askig users questions about themsleves. Code will not run properly if their is any typos

    age = int(input("Enter your age: "))
    gender = input("Enter your gender (male/female): ").lower()
    bmi = int(input("Enter your BMI (must be an integer between 15 and 50): "))
    children = int(input("Enter number of children: "))
    smoker = input("Are you a smoker? (yes/no): ").lower()
    region = input("Enter your region (northeast/northwest/southeast/southwest): ").lower()


    # Calculates the correlation coefficients to see relationship between certain factors like age, and the charges
    age_corr = insurance_df['age'].corr(insurance_df['charges'])
    bmi_corr = insurance_df['bmi'].corr(insurance_df['charges'])
    children_corr = insurance_df['children'].corr(insurance_df['charges'])

    #prints the correlation  coefficients

    print("here is some information about the correlations between the cost and factors.(age, bmi, and number of children)")
    print(age_corr)
    print(bmi_corr)
    print(children_corr)




    finalaverage = []


    # calculates the average cost of the age that the user inputed
    user_age = insurance_df[insurance_df['age'] == age]
    if not user_age.empty:
        age_average = user_age['charges'].mean()
        finalaverage.append(age_average)

    # calculates Average cost of all smokers in the dataset
    smokerr = insurance_df[insurance_df['smoker'] == smoker]
    if not smokerr.empty:
        smoker_average = smokerr['charges'].mean()
        finalaverage.append(smoker_average)

    # calculates the average cost of the gender the user inputs
    user_gender = insurance_df[insurance_df['sex'] == gender]
    if not user_gender.empty:
        gender_average = user_gender['charges'].mean()
        finalaverage.append(gender_average)

    # Average cost of BMI the user inputs
    user_bmi = insurance_df[insurance_df['bmi'] == bmi]
    if not user_bmi.empty:
        bmi_average = user_bmi['charges'].mean()
        finalaverage.append(bmi_average)

    # Average cost of parents based on the number of kids the users said they have
    user_children = insurance_df[insurance_df['children'] == children]
    if not user_children.empty:
        children_average = user_children['charges'].mean()
        finalaverage.append(children_average)

    # Average cost of the region that the user put
    user_region = insurance_df[insurance_df['region'] == region]
    if not user_region.empty:
        region_average = user_region['charges'].mean()
        finalaverage.append(region_average)

    # Calculates all the average of the averages and finally gives the user their estimated insurance cost
        final_insuranceestimate = sum(finalaverage) / len(finalaverage)
        print(f"\nFinal Estimated Insurance Cost:")
        print(final_insuranceestimate)


        #Next fucntion that was defined to give users recomendations of hospltials they can visit based on their prefences

def recommend_hospital():

    print(hospital_df.head())

    print("Hospital Recommendation")
        # asks user for what state they prefer to get recomendations from

    user_state = input("Enter the state you prefer(Please use abbreviations. For example NJ): ").strip().upper()


    user_rating = int(input("Enter the hospital rating you want to filter by (1-5): "))

            #filters out every other state from the dataframe and outputs it


    state_hospitals = hospital_df[hospital_df['State'] == user_state]
    filtered_hospitals = state_hospitals[
    (state_hospitals['Hospital overall rating'] == user_rating) &
    (state_hospitals['Hospital overall rating'] != 'Not Available')


]


#filters hospital that doesn't alighn with users ratings

    #prints the filtered states than hospitals
    print("\nHospitals in ")
    print(user_state)

    print(state_hospitals[['Hospital Name', 'City', 'State', 'Hospital overall rating']])
    print(f"\nHospitals in the state and star ratings they have:")
    print(filtered_hospitals[['Hospital Name', 'City', 'State', 'Hospital overall rating']])

    # defines our main function menu

def mainmenu():
  #gives user the option to navigate the program
    while True:
        print("\n--- Final Project Main Menu ---")
        print("1. Estimate Insurance Cost")
        print("2. Recommend a Hospital")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        #based on the choice the user makes, it will call that fucntion and naviagte the user to it. if they choose to exit the loop breaks and the program ends

        if choice == '1':
            estimate_insurance_cost()
        elif choice == '2':
            recommend_hospital()
        elif choice == '3':
            print("ending the program. Thanks for looking at our final project!")
            break
        else:
            print("Please enter 1, 2, or 3.")

mainmenu()