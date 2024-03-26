import streamlit as st

# Define a decorator to handle distribution-specific inputs
def distribution_inputs(distribution_name):
    """
    distribution-specific inputs.

    Author: Lebuso Philly Tsilo.

    Description: This decorator function is designed to handle distribution-specific inputs for statistical distributions.
    It creates a Streamlit sidebar with input fields specific to the given distribution_name.

    Parameters:
    - distribution_name (str): The name of the distribution for which the input fields are defined.

    Returns:
    - wrapper (function): The decorated function with the input handling logic based on the specified distribution.
    """
    def decorator(func):
        def wrapper(*arg, **kwargs ):
            st.sidebar.header(f"{distribution_name} Distribution")

            # Input handling logic based on the distribution
            if distribution_name == 'Binomial':
                st.title(f"{distribution_name} Distribution")
                st.write("Enter an integer size value and a probability of success.")
                while True:
                    try:
                        size = st.number_input('Type the size value:', key=1, min_value = 1, step = 1)
                        if size is not None and size > 0:
                            break
                        st.error('Error! The size must be an integer greater than 0.')
                    except ValueError:
                        st.error('Error! please enter a valid integer')

                while True:
                    try:
                        prob = st.number_input('Type the probability of success value:', key=2, min_value=0.0, max_value=1.0, step=0.01)
                        if prob is not None and 0 <= prob <= 1:
                            break
                        st.error('Error! The probability of success must be between 0 and 1.')
                    except ValueError:
                        st.error('Error! please enter a valid number between 0 and 1')
                    break
                if size is not None and prob is not None:
                    st.success(f"Size entered: {size}")
                    st.success(f"Probability of success entered: {prob}")
                
                return func(size, prob)
                
                

            ######## Cauchy Distribution #########
            if distribution_name == "Cauchy":
                st.title(f"{distribution_name} Distribution")
                st.write('Enter the location value and the dcale value')
                location = st.number_input("Type the location value: ", key=3, min_value= 0, step = 1)
                # set the scale value
                while True:
                    try:
                        scale = st.number_input('Type the scale value:', key= 4, min_value= 1, step=1)
                        if scale is not None and scale<0:
                            st.error('Error! the scale must be greater than 0')
                            break
                    except ValueError:
                        st.error('Error! Please enter a value a value greater than 0')
                    break
                if location is not None and scale is not None:
                    st.success(f'location entered: {location}')
                    st.success(f'Scale entered: {scale}')
                return func(location, scale)

                
            

                ##############Chi-square###########
            if distribution_name == "Chi-square":
                st.title(f'{distribution_name} Distribution')
                st.write('Enter degree of freeedom')

                while True:
                    try:
                        df = st.number_input("Type the degrees of freedom value: ", key = 5, min_value = 1, step = 1)
                        if df <= 0 and df is not None:
                            st.error('Error! the degree of freedom must be a value greater than 0.')
                            break
                    except ValueError:
                        st.error('Error! please enter a value greater than 0.')
                    break
                if df is not None:
                    st.success(f'Degree of freedom entered: {df}')

                return func(df)  
                pass


                    ### EXPONENTIAL DISTRIBUTION ###

            if distribution_name == "Exponential":
                st.title(f'{distribution_name} Distribution')
                st.write("Enter the rate value")

                while True:
                    try:
                        rate = st.number_input("Type the rate value: ", key = 6, min_value=0, step =0)
                        if rate is not None and rate < 0:
                            st.error("Error! Rate must be non-negative.")
                            break
                    except ValueError:
                        st.error("Error! please enter a value greater than 0.")
                    break
                if rate is not None :
                    st.success(f'The rate entered: {rate}')

                return func(rate)
                
                                    
            if distribution_name == "F":
                st.title(f'{distribution_name} Distribution')
                st.write('Enter the degree of freedoms.')

                while True:
                    try:
                        df1 = st.number_input("Type the first degrees of freedom value: ", key = 7, min_value = 1, step=1)
                        if df1 is not None and df1 <0:
                            st.error("Error! The first degrees of freedom value must be greater than 0.")
                            break
                    except ValueError:
                        st.error('Error! please enter a value greater than 0.')
                    break   
                    
                while True:
                    try:
                        df2 = st.number_input("Type the second degrees of freedom value: ", key = 'df2', min_value =1 , step=1)
                        if df2 is not None and df2<0:
                            st.error("Error! The second degrees of freedom value must be greater than 0.")
                            break
                    except ValueError:
                        st.error('Error! please enter a value greater than 0.')
                    break
                if df1 is not None and df2 is not None:
                    st.success(f'first degree of freedom entered: {df1}')
                    st.success(f'Second degree of freedom entered: {df2}')
                    
                return func(df1,df2)
            
            ######### GAMMA DISTRIBUTION##############

            if distribution_name == "Gamma":
                #set the shape value
                st.title(f'{distribution_name} Distribution')

                while True:
                    try:
                        shape = st.number_input('Type the shape value: ', key= 'shape', min_value= 0, step=1)
                        if shape is not None and shape < 0:
                            st.error("Error! The shape value must greater than 0")
                            break
                    except ValueError:
                        st.error("Error! Please enter a value greater than 0")
                        
                    while True:
                        try:
                            rate_2 = st.number_input("Type The rate value: ", key="rate", min_value = 0,  step = 1)
                            if rate_2 is not None and rate_2 < 0:
                                st.error("Error! The shape value must be greater than 0.")
                            break
                        except ValueError:
                            st.error("Error! Please enter a value greater than 0")
                        break
                    if rate_2 is not None and shape is not None:
                        st.success(f'shape entered: {shape}')
                        st.success(f'rate entered: {rate_2}')
                        
                    return func(shape,rate_2)
            

                ### GEOMETRIC DISTRIBUTION ###
            if distribution_name == "Geometric":
                st.title(f'{distribution_name} Distribution')
                while True:
                    try:
                        prob = st.number_input("Type the probability of success in each trial: ", key= "Prob2", min_value=0.0, max_value=1.0, step=0.1)
                        if prob <0 or prob > 1:
                            st.error("Error! The probability of success in each trial must be between 0 and 1.")
                        break
                    except ValueError:
                        st.error("Error! please enter value between 0 and 1")
                    break
                if prob is not None:
                    st.success(f'Probability of success entered: {prob}')
                
                    
                    
                return func(prob)
            ### HYPERGEOMETRIC DISRIBUTION ###
            if distribution_name == "Hypergeometric":
                st.title(f'{distribution_name} Distribution')
                while True:
                    try:
                        m = st.number_input('Type the m value: ', key= 'm', min_value= 0, step=1)
                        if m < 0:
                            st.error("Error! The m value must greater than 0")
                        break
                    except ValueError:
                        st.error("Error! Please enter a value greater than 0")
                while True:    
                    try:
                        n = st.number_input('Type the n value: ', key= 'n', min_value= 0, step=1)
                        if n < 0:
                            st.error("Error! The shape value must greater than 0")
                        
                    except ValueError:
                        st.error("Error! Please enter a value greater than 0")
                    break
                while True:
                    try:
                        k = st.number_input('Type the k value: ', key= 'k', min_value= 0, step=1)
                        if k < 0 or k > min(m,n):

                            st.error(f"Error! k must be an integer between 0 and {min(m, n)}.")
                        
                    except ValueError:
                        st.error(f"Error! Please enter a integer between 0 and {min(m, n)}")
                    break
                if m is not None and n is not None and k is not None:
                        st.success(f'm value entered: {m}')
                        st.success(f'n value entered: {n}')
                        st.success(f'k value entered: {k}')
                return func(m,n,k)
                    
            ### LOGNORMAL DISTRIBUTION ###
            if distribution_name == "Lognormal":
                st.title(f'{distribution_name} Distribution')
                while True:
                    try:
                        meanlog = st.number_input("Type the mean value: ", key="mean",min_value=0, step=1)
                        if meanlog < 0:
                            st.error("Error! The mean value must be a positive number.")
                        break
                    except  ValueError:
                        st.error("Error! Please enter a positive number.")
                
                while True:
                    try:
                        sdlog = st.number_input("Type the standard deviation: ", key="sdlog", min_value=0.0, step=0.1)
                        if sdlog <0:
                            st.error("Error! The standard deviation must be greater than 0.")
                        break
                    except ValueError:
                        st.error("Error! Please enter a number greater than 0")
                    
                    break
                if meanlog is not None and sdlog is not None:
                        st.success(f'mean value entered: {meanlog}')
                        st.success(f'standard deviation value entered: {sdlog}')

                return func(meanlog,sdlog)

        
            if distribution_name == "Normal":
                st.title(f'{distribution_name} Distribution')
                mean = st.number_input("Type the mean(mu): ", key="norm", min_value= 0, step=1)
                while True:
                    try:
                        sd =st.number_input("Type the standard deviation (sigma): ", key= "sigma", min_value=0.0, step=0.1)
                        if sd < 0:
                            st.error("Error! Sigma must be greater than 0.")
                        break
                    except ValueError:
                        st.error("Error! Please enter a number greater than 0")

                    break
                if mean is not None  and sd is not None:
                    st.success(f'mean value entered: {mean}')
                    st.success(f'standard deviation value entered: {sd}')

                return func(mean, sd)
            
            if distribution_name == "Poisson":
                st.title(f'{distribution_name} Distribution')
                while True:
                    try:
                        lambda_value = st.number_input("Type the lambda value: ", key = "lambda", min_value= 0.0, step=1)
                        if lambda_value < 0:
                            st.error("Error! Lambda must be greater than 0.")
                        break
                    except ValueError:
                        st.error("Error! Please enter a number greater than 0")

                    break
                if lambda_value is not None:
                    st.success(f"Lambda value entered: {lambda_value}")

                return func(lambda_value)
            
            if distribution_name == "Uniform":

                while True:
                    try:
                        mini_value = st.number_input("Type the lower limit: ", key="min", min_value=0, step=1)
                        break
                    except ValueError:
                        st.error("Error! Please enter a valid number for the lower limit.")

                while True:
                    try:
                        maxi_value = st.number_input("Type the upper limit: ", key="max", min_value=0, step=1)
                        break
                    except ValueError:
                        st.error("Error! Please enter a valid number for the upper limit.")

                    break
                if mini_value is not None and maxi_value is not None:
                    st.success(f"Lower limit entered:  {mini_value}")
                    st.success(f"Upper limit entered:  {maxi_value}")

                return func(mini_value, maxi_value)
            
            if distribution_name == "Beta":
                st.title(f'{distribution_name} Distribution')
                while True:
                    try:
                        shape1 = st.number_input("Type the shape1 value: ", key= "shape1", min_value= 0, step=1)
                        shape2 = st.number_input("Type the shape2 value: ", key= "shape2", min_value= 0, step=1)
                        if shape1 < 0 or shape2 <0:
                            st.error("Error! The shape value must be greater than 0: ")
                            break
                    except ValueError:
                        st.error("Error! Please enter a value greater than 0")
                    break
                if shape1 is not None and shape2 is not None:
                    st.success(f'Shape 1 entered: {shape1}')
                    st.success(f'Shape 2 entered: {shape2}')

                return func(shape1, shape2)


        return wrapper

    return decorator