# Probability Distribution Visualizer

This script provides a graphical interface for visualizing probability density functions of various statistical distributions. Users can select a distribution, set its parameters, and view the resulting probability density function plot.

## Setup Instructions

1. Ensure that you have the prerequisite Python libraries installed on your local machine:

    ```bash
    pip install streamlit numpy scipy matplotlib
    ```

2. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/{your-account-name}/Probability-Distribution-Visualizer.git
    ```

3. Navigate to the base directory of the cloned repository:

    ```bash
    cd Probability-Distribution-Visualizer/
    ```

4. Start the Streamlit app:

    ```bash
    streamlit run DistributionVisualizer.py
    ```

    If the web server initializes successfully, you should see the following message in your terminal:

    ```
    You can now view your Streamlit app in your browser.

    Local URL: http://localhost:8501
    Network URL: http://192.168.0.177:8501
    ```

    You will also be automatically directed to the base page of your web app.

## Supported Distributions

The script supports the following probability distributions:

### Binomial Distribution
- **Description**: Describes the number of successes in a fixed number of independent Bernoulli trials, each with the same probability of success.
- **Parameters**: 
  - Number of trials (n)
  - Probability of success (p)
- **Use Case**: Commonly used in quality control, genetics, and any scenario where you want to know the number of successes in a series of experiments.
- **Example**: If you flip a coin 10 times, how many times will it land on heads (n=10, p=0.5)?

### Cauchy Distribution
- **Description**: Known for its heavy tails and the fact that its mean and variance are undefined, making it an interesting example in probability theory.
- **Parameters**: 
  - Location (x0)
  - Scale (γ)
- **Use Case**: Used in physics and spectroscopy to describe resonance behavior.
- **Example**: Modeling the distribution of errors or noise in a signal.

### Chi-square Distribution
- **Description**: Used primarily in hypothesis testing, particularly in tests of independence and goodness of fit.
- **Parameters**: 
  - Degrees of freedom (k)
- **Use Case**: Common in statistical tests like the chi-square test for independence in contingency tables.
- **Example**: Testing if a die is fair by comparing observed and expected frequencies of rolls.

### Exponential Distribution
- **Description**: Describes the time between events in a Poisson process, where events occur continuously and independently at a constant rate.
- **Parameters**: 
  - Rate (λ)
- **Use Case**: Used in reliability engineering to model time to failure of components and in queuing theory.
- **Example**: The time until the next earthquake in a region where earthquakes occur at a constant average rate.

### F Distribution
- **Description**: Used primarily in analysis of variance (ANOVA) and in the F-test to compare two variances.
- **Parameters**: 
  - Degrees of freedom for the numerator (d1)
  - Degrees of freedom for the denominator (d2)
- **Use Case**: Comparing statistical models to determine if they explain the data well.
- **Example**: Testing the equality of variances of two samples.

### Gamma Distribution
- **Description**: A generalization of the exponential distribution, with applications in queuing models and reliability analysis.
- **Parameters**: 
  - Shape (k)
  - Rate (θ)
- **Use Case**: Modeling waiting times and life durations of objects.
- **Example**: Modeling the time until the next k events occur in a Poisson process.

### Geometric Distribution
- **Description**: Models the number of trials needed for the first success in a series of independent Bernoulli trials.
- **Parameters**: 
  - Probability of success (p)
- **Use Case**: Useful in scenarios like quality control and reliability testing where you count the number of trials until a success.
- **Example**: The number of coin flips needed to get the first heads.

### Hypergeometric Distribution
- **Description**: Describes the number of successes in a sequence of draws from a finite population without replacement.
- **Parameters**: 
  - Population size (N)
  - Number of successes in the population (K)
  - Number of draws (n)
- **Use Case**: Used in situations like quality control where sampling is done without replacement.
- **Example**: The number of defective items in a sample of 10 drawn from a lot of 100 items.

### Lognormal Distribution
- **Description**: A distribution of a variable whose logarithm is normally distributed, used in finance and environmental modeling.
- **Parameters**: 
  - Mean (μ)
  - Standard deviation (σ)
- **Use Case**: Modeling stock prices, survival times, and income distributions.
- **Example**: The distribution of income in an economy, where income is positively skewed.

### Normal Distribution
- **Description**: Also known as the Gaussian distribution, it describes a symmetrical, bell-shaped curve centered around the mean.
- **Parameters**: 
  - Mean (μ)
  - Standard deviation (σ)
- **Use Case**: Widely used in statistics and natural sciences to represent real-valued random variables.
- **Example**: Heights of adult humans, measurement errors, and standardized test scores.

### Poisson Distribution
- **Description**: Describes the number of events occurring within a fixed interval of time or space.
- **Parameters**: 
  - Rate (λ)
- **Use Case**: Commonly used in queuing theory, telecommunications, and reliability engineering.
- **Example**: The number of customer arrivals at a store in one hour.

### Uniform Distribution
- **Description**: All outcomes are equally likely within a given range, resulting in a flat distribution.
- **Parameters**: 
  - Lower bound (a)
  - Upper bound (b)
- **Use Case**: Used in simulations and random sampling where each outcome within a range is equally likely.
- **Example**: Rolling a fair six-sided die.

### Beta Distribution
- **Description**: Defined on the interval [0, 1], it is used in Bayesian statistics to model prior distributions.
- **Parameters**: 
  - Shape parameters (α, β)
- **Use Case**: Used in Bayesian inference, project planning (PERT), and modeling random variables limited to intervals of finite length.
- **Example**: Modeling the probability of success in a binomial experiment.

For each distribution, you can input the required parameters and generate the corresponding probability density function plot.

## Author

This script was authored by Lebuso Philly Tsilo.
