from Distribution_inputs.Distribution_inputs import distribution_inputs
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom, cauchy, chi2, expon, f, gamma, geom, hypergeom, lognorm, norm, poisson, uniform, beta

distribution_functions = {
    "Binomial": binom,
    "Cauchy": cauchy,
    "Chi-square": chi2,
    "Exponential": expon,
    "F": f,
    "Gamma": gamma,
    "Geometric": geom,
    "Hypergeometric": hypergeom,
    "Lognormal": lognorm,
    "Normal": norm,
    "Poisson": poisson,
    "Uniform": uniform,
    "Beta": beta
}


class DistributionVisualizer:
    """
    Probability Distribution Visualizer.

    Author: Lebuso Philly Tsilo.

    Description: This class provides a graphical interface for visualizing probability density functions
    of various statistical distributions. Users can select a distribution, set its parameters, and view the resulting
    probability density function plot.

    Methods:
    - __init__: Initializes the visualizer and sets up the Streamlit application.
    - binomial_distribution: Handles input and visualization for the Binomial distribution.
    - cauchy_distribution: Handles input and visualization for the Cauchy distribution.
    - Chi_square: Handles input and visualization for the Chi-square distribution.
    - Exponential: Handles input and visualization for the Exponential distribution.
    - run: Executes the visualizer based on the selected distribution.

    Usage:
    if __name__ == "__main__":
        visualizer = DistributionVisualizer()
        visualizer.run()
    """
    def __init__(self):
        st.title("Probability Distribution Visualizer")
        st.write("Select a distribution and set its parameters to visualize the probability density function.")
        self.selected_distribution = st.sidebar.selectbox("Select a Distribution", list(distribution_functions.keys()))

    # Decorate the method with distribution-specific input handling
    @distribution_inputs("Binomial")
    def binomial_distribution(size, prob):
        """
        Handles input and visualization for the Binomial distribution.

        Parameters:
        - size (int): The size parameter for the Binomial distribution.
        - prob (float): The probability of success for the Binomial distribution.

        Returns:
        None
        """
        
        ###### plots code here ###########
        if st.button("plot"):
        
            x = np.arange(0, 31)

            # Calculate the binomial probabilities
            pmf = binom.pmf(x, size, prob)

            plt.figure(figsize=(10, 6))
            # Build the probability plot
            plt.bar(x, pmf, width=1.0, align='center', alpha=0.7, label='Binomial Probability')
            plt.xlabel("Number of successful experiments")
            plt.ylabel("Probability")
            plt.title("Binomial Distribution")
            plt.axhline(y=0, color='black', linestyle='--', label='Zero Line')
            plt.legend()
            st.pyplot(plt)
        pass
      
        
        
       
    # Decorate the method with distribution-specific input handling
    @distribution_inputs("Cauchy")
    def cauchy_distribution(location, scale):
        
        ###### plots code here ###########
        if st.button("Plot"):
            x = np.linspace(location - 5, location +5, 1000)
        
            plt.figure(figsize=(10,6))

            pdf = cauchy.pdf(x, loc=location,  scale= scale)

            plt.plot(x, pdf, lw =2, label= "Cauchy Probabilty Density", color= 'blue')
            plt.xlabel("Probability Density")
            plt.xlabel("X")
            plt.title("Cauchy Distribition")
            plt.axhline(y=0, color= "black", linestyle="--", label= "Zero Line")
            plt.legend()
            st.pyplot(plt)

        pass

    @distribution_inputs("Chi-square")
    def Chi_square(df):
        
        ###### plots code here ###########
        if st.button("Plot"):
            # Create a range of x values for the plot
            x = np.linspace(5, 50, 1000)

            # Calculate the Chi-square probability density function
            pdf = chi2.pdf(x, df)

            # Calculate the 95th percentile point for shading
            x_95th = chi2.ppf(0.95, df)

            plt.figure(figsize=(10, 6))
            # Build the probability plot
            plt.plot(x, pdf, lw=2, label='Chi-square Probability Density', color='blue')
            plt.xlabel("Random Variable X")
            plt.ylabel("Probability Density")
            plt.title("Chi-square Distribution")
            plt.axhline(y=0, color='black', linestyle='--', label='Zero Line')
            plt.axvline(x=x_95th, color='red', linestyle='--', label='95th Percentile', alpha=0.7)
            plt.fill_between(x, pdf, where=(x >= x_95th), alpha=0.2, color='red', label='5% Area')
            plt.annotate(f'{x_95th:.2f}', (x_95th, 0.001), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=8)
            plt.legend()
            st.pyplot(plt)
        pass


    @distribution_inputs("Exponential")   
    def Exponential(rate):
        
        ###### plots code here ###########
        if st.button("Plot"):
            # Create a range of x values for the plot
            x = np.linspace(0, 5, 1000)

            # Calculate the Exponential probability density function
            pdf = expon.pdf(x, scale=1/rate)

            # Set the figure size (adjust width and height as needed)
            plt.figure(figsize=(10, 6))

            # Build the probability plot
            plt.plot(x, pdf, lw=2, label='Exponential Probability Density', color='blue')
            plt.xlabel("Random Variable X")
            plt.ylabel("Probability Density")
            plt.title("Exponential Distribution")
            plt.axhline(y=0, color='black', linestyle='--', label='Zero Line')
            plt.legend()

            # Add text annotations within the graph
            plt.text(4, 0.8, r'$\mu = \frac{1}{\lambda}$', fontsize=12, verticalalignment='bottom', horizontalalignment='right')
            plt.text(4, 0.7, r'$\sigma^2 = \frac{1}{\lambda^2}$', fontsize=12, verticalalignment='bottom', horizontalalignment='right')
            plt.text(4, 0.6, r'$f(x) = \lambda e^{-\lambda x}$', fontsize=12, verticalalignment='bottom', horizontalalignment='right')
            st.pyplot(plt)
        pass

    @distribution_inputs("F")
    def F(df1,df2):
        
        if st.button("Plot"):
            # Create a range of x values for the plot
            x = np.linspace(0, 4, 1000)

            # Calculate the F-distribution probability density function
            pdf = f.pdf(x, df1, df2)

            # Set the figure size (adjust width and height as needed)
            plt.figure(figsize=(10, 6))

            # Build the probability plot
            plt.plot(x, pdf, lw=2, label='F-distribution Probability Density', color='blue')
            plt.xlabel("Random Variable X")
            plt.ylabel("Probability Density")
            plt.title("F-distribution")
            plt.axhline(y=0, color='black', linestyle='--', label='Zero Line')
            plt.legend()
            # Add lines and text annotations within the graph
            x_quantile = f.ppf(0.95, df1, df2)
            plt.axvline(x_quantile, linestyle='--', color='red')
            plt.axvline(0, linestyle='--', color='red')
            plt.text(x_quantile, 0, f'{round(x_quantile, 2)}', horizontalalignment='center', verticalalignment='bottom')
            plt.text(1, 0.4, "95%")
            plt.text(2.5, 0, "5%", horizontalalignment='left', verticalalignment='top')
            plt.text(4, 0.8, r'$F_{n,m} = \frac{\chi_n^2 / n}{\chi_m^2 / m}$', fontsize=12, verticalalignment='bottom', horizontalalignment='right')
            st.pyplot(plt)
        pass

    @distribution_inputs("Gamma")
    def gamma(shape,rate):
        
        if st.button("Plot"):
            # Create a range of x values for the plot
            x = np.linspace(0, 10, 1000)

            # Calculate the Gamma distribution probability density function
            pdf = gamma.pdf(x, shape, loc=0, scale=1/rate)

            # Set the figure size (adjust width and height as needed)
            plt.figure(figsize=(10, 6))

            # Build the probability plot
            plt.plot(x, pdf, lw=2, label='Gamma Probability Density', color='blue')
            plt.xlabel("Random Variable X")
            plt.ylabel("Probability Density")
            plt.title("Gamma Distribution")
            plt.axhline(y=0, color='black', linestyle='--', label='Zero Line')
            plt.legend()
            st.pyplot(plt)

        pass

    @distribution_inputs("Geometric")
    def geometric(prob):
        if st.button("Plot"):
            # Create a range of x values for the plot
            x = np.arange(0, 41)

            # Calculate the Geometric distribution probabilities
            pmf = geom.pmf(x, prob)

            # Set the figure size (adjust width and height as needed)
            plt.figure(figsize=(10, 6))

            # Build the probability plot
            plt.bar(x, pmf, width=1.0, align='center', alpha=0.7, label='Geometric Probability')
            plt.xlabel("Items extracted until first success")
            plt.ylabel("Probability")
            plt.title("Geometric Distribution")
            plt.axhline(y=0, color='black', linestyle='--', label='Zero Line')
            plt.legend()
            plt.ylim(0, prob)
            st.pyplot(plt)
        pass

    @distribution_inputs("Hypergeometric")
    def hypergeometric(m,n,k):
        if st.button("Plot"):
            # Create a range of x values for the plot
            x = np.arange(0, k + 1)

            # Calculate the Hypergeometric distribution probabilities
            pmf = hypergeom.pmf(x, m + n, m, k)

            # Set the figure size (adjust width and height as needed)
            plt.figure(figsize=(10, 6))

            # Build the probability plot
            plt.bar(x, pmf, width=1.0, align='center', alpha=0.7, label='Hypergeometric Probability')
            plt.xlabel("Elements in class")
            plt.ylabel("Probability")
            plt.title("Hypergeometric Distribution")
            plt.axhline(y=0, color='black', linestyle='--', label='Zero Line')
            plt.legend()
            plt.ylim(0, 1)  # Set the y-axis limit to match the specified ylim
            plt.text(4, 0.45, r'$\mu = kp$', fontsize=12, verticalalignment='bottom', horizontalalignment='right')
            plt.text(4, 0.40, r'$\sigma^2 = kp(1-p)$', fontsize=12, verticalalignment='bottom', horizontalalignment='right')
            plt.text(4, 0.30, r'$P(x) = \frac{\left(\frac{(n+m)p}{x}\right)\left(\frac{(n+m)(1-p)}{k-x}\right)}{\frac{(n+m)}{k}}$', fontsize=10, verticalalignment='bottom', horizontalalignment='right')
            st.pyplot(plt)

        pass

    @distribution_inputs("Lognormal")
    def lognormal(meanlog,sdlog):
        if st.button("Plot"):
            # Calculate the shape parameter (sigma) for the lognormal distribution
            sigma = np.sqrt(np.log(1 + (sdlog ** 2) / (meanlog ** 2)))

            # Calculate the scale parameter (mu) for the lognormal distribution
            mu = np.log(meanlog) - (sigma ** 2) / 2

            # Create a range of x values for the plot
            x = np.linspace(0, 6, 1000)

            # Calculate the Lognormal distribution probability density function
            pdf = lognorm.pdf(x, scale=np.exp(mu), s=sigma)

            # Set the figure size (adjust width and height as needed)
            plt.figure(figsize=(10, 6))

            # Build the probability plot
            plt.plot(x, pdf, lw=2, label='Lognormal Probability Density', color='blue')
            plt.xlabel("Random Variable X > 0")
            plt.ylabel("Probability Density")
            plt.title("Lognormal Distribution")
            plt.axhline(y=0, color='black', linestyle='--', label='Zero Line')
            plt.legend()
            plt.ylim(0, 0.9)  # Set the y-axis limit to match the specified ylim

            # Add text annotations within the graph
            plt.text(5, 0.70, r'$\mu = e^{\left(\mu_N + \frac{\sigma^2}{2}\right)}$', fontsize=12, verticalalignment='bottom', horizontalalignment='right')
            plt.text(5, 0.55, r'$\sigma^2 = e^{(2\mu_N + (\sigma^2)_N \cdot e^{(\sigma^2)_N-1})}$', fontsize=12, verticalalignment='bottom', horizontalalignment='right')
            plt.text(5, 0.4, r'$f(x) = \frac{1}{x\sigma_N\sqrt{2\pi}}e^{-\frac{(\ln(x)-\sigma_N)^2}{2(\sigma^2)_N}}$', fontsize=10, verticalalignment='bottom', horizontalalignment='right')
            st.pyplot(plt)

        pass

    @distribution_inputs("Normal")
    def normal(mean, sd):
        if st.button("Plot"):
            # Create a range of x values for the plot
            x = np.linspace(mean - 3 * sd, mean + 3 * sd, 1000)

            # Calculate the Normal distribution probability density function
            pdf = norm.pdf(x, loc=mean, scale=sd)

            # Set the figure size (adjust width and height as needed)
            plt.figure(figsize=(10, 6))

            # Build the probability plot
            plt.plot(x, pdf, lw=2, label='Normal Probability Density', color='blue')
            plt.xlabel("Random Variable X")
            plt.ylabel("Probability Density")
            plt.title("Normal Distribution")
            plt.axhline(y=0, color='black', linestyle='--', label='Zero Line')
            plt.legend()
            # Add text annotations within the graph
            plt.text(2.5, 0.34, r'$\mu = 0$', fontsize=12, verticalalignment='bottom', horizontalalignment='right')
            plt.text(2.5, 0.30, r'$\sigma = 1$', fontsize=12, verticalalignment='bottom', horizontalalignment='right')
            plt.text(2.8, 0.27, r'$f(x) = \frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}$', fontsize=10, verticalalignment='bottom', horizontalalignment='right')
            st.pyplot(plt)
        pass

    @distribution_inputs("Poisson")
    def poisson(lambda_value):
        if st.button("Plot"):
            # Create a range of x values for the plot
            x = np.arange(0, 21)

            # Calculate the Poisson distribution probabilities
            pmf = poisson.pmf(x, mu=lambda_value)

            # Set the figure size (adjust width and height as needed)
            plt.figure(figsize=(10, 6))

            # Build the probability plot
            plt.bar(x, pmf, width=1.0, align='center', alpha=0.7, label='Poisson Probability')
            plt.xlabel("Number of successful experiments per unit")
            plt.ylabel("Probability")
            plt.title("Poisson Distribution")
            plt.axhline(y=0, color='black', linestyle='--', label='Zero Line')
            plt.legend()
            plt.ylim(0, 0.35)  # Set the y-axis limit to match the specified ylim

            # Add text annotations
            plt.text(20, 0.175, r'$\mu = \lambda$', fontsize=12, ha='center')
            plt.text(20, 0.150, r'$\sigma^2 = \lambda$', fontsize=12, ha='center')
            plt.text(20, 0.120, r'$P(x) = \frac{e^{-\lambda}\lambda^x}{x!}$', fontsize=12, ha='center')
            st.pyplot(plt)
        pass

    @distribution_inputs("Uniform")
    def uniform(min_value, max_value):
        if st.button("Plot"):
            # Create a range of x values for the plot
            x = np.linspace(min_value - 0.5, max_value + 0.5, 1000)

            # Calculate the Uniform distribution probability density function
            pdf = uniform.pdf(x, loc=min_value, scale=max_value - min_value)

            # Set the figure size (adjust width and height as needed)
            plt.figure(figsize=(10, 6))

            # Build the probability plot
            plt.plot(x, pdf, lw=2, label='Uniform Probability Density', color='blue')
            plt.xlabel("Random Variable X")
            plt.ylabel("Probability Density")
            plt.title("Uniform Distribution")
            plt.axhline(y=0, color='black', linestyle='--', label='Zero Line')
            plt.legend()
            plt.ylim(0, 1.1)  # Set the y-axis limit to match the specified ylim

            # Add text annotations
            plt.text(1.25, 1.0, r'$\mu = \frac{b + a}{2}$', fontsize=12, ha='center')
            plt.text(1.25, 0.9, r'$\sigma^2 = \frac{1}{12}(b - a)^2$', fontsize=12, ha='center')
            plt.text(1.3, 0.7, r'$f(x) = \frac{1}{b - a},\ a \leq x \leq b$', fontsize=12, ha='center')
            st.pyplot(plt)

        pass

    @distribution_inputs("Beta")
    def beta(shape1, shape2):
        if st.button("Plot"):
            # Generate data points for the x-axis
            x = np.linspace(0, 1, 1000)

            # Calculate the PDF of the Beta distribution
            pdf = beta.pdf(x, shape1, shape2)

            plt.figure(figsize=(10, 6))
            # Plot the Beta distribution
            plt.plot(x, pdf, linewidth=3)
            plt.xlabel("Random Variable X")
            plt.ylabel("Probability Density")
            plt.title("Beta Distribution")
            plt.ylim(0, 3)
            plt.axhline(0, color='black', linestyle='--')
            st.pyplot(plt)

        pass



    def run(self):
        if self.selected_distribution == "Binomial":
            self.binomial_distribution()
        elif self.selected_distribution == "Cauchy":
            self.cauchy_distribution()
        elif self.selected_distribution == "Chi-square":
            self.Chi_square()
        elif self.selected_distribution == "Exponential":
            self.Exponential()
        elif self.selected_distribution == "F":
            self.F()
        elif self.selected_distribution == "Gamma":
            self.gamma()
        elif self.selected_distribution == "Geometric":
            self.geometric()
        elif self.selected_distribution == "Hypergeometric":
            self.hypergeometric()
        elif self.selected_distribution == "Lognormal":
            self.lognormal()
        elif self.selected_distribution == "Normal":
            self.normal()
        elif self.selected_distribution == "Poisson":
            self.poisson()
        elif self.selected_distribution == "Uniform":
            self.uniform()
        elif self.selected_distribution == "Beta":
            self.beta()


if __name__ == "__main__":
    visualizer = DistributionVisualizer()
    visualizer.run()