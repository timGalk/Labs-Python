
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, ttest_1samp
import warnings
# Task1
def generate_height_data(size=1000, mean=170, std_dev=10) -> np.ndarray:
    """ Generates dataset of 1000 heights with a mean of 170 cm and standard deviation of 10 cm.

    Args:
        size (int, optional): Defaults to 1000.
        mean (int, optional): Defaults to 170.
        std_dev (int, optional): Defaults to 10.

    Returns:
        np.ndarray: Array of heights
    Rises:
        ValueError: Size must be a positive integer.
        ValueError: Mean height must be a positive number.
        ValueError: Standard deviation must be a positive number.
        ValueError: Standard deviation must be less than the mean.
    """
    #Check of data types 
    if  not isinstance(size, int):
        raise TypeError("Size must be a positive integer.")
    if not isinstance(mean, (int, float)):
        raise TypeError("Mean height must be a positive number.")
    if  not isinstance(std_dev, (int, float)):
        raise TypeError("Standard deviation must be a positive number.")
    #Check of values
    if any([size <= 0, mean <= 0, std_dev <= 0]):
        raise ValueError("All inputs must be positive.")
    #Check of the standard deviation
    if std_dev > mean or not isinstance(mean, (int, float)):
        raise ValueError("Standard deviation must be less than the mean.")
    #Warning for the user about small size of the dataset. The part of code was added by ChatGPT for the question: "What is optimal size of the dataset?"
    #Find a conversation here https://chatgpt.com/share/675da94d-5ff0-800c-869f-0119ec943ea2
    if size < 300:
        warnings.warn("Warning: A sample size of less than 300 may not provide reliable statistical estimates.")
    # This part of code was generated by ChatGPT for the question: 
    # "Generate a dataset of 1000 heights with a mean of 170 cm and standard deviation of 10 cm."
    return np.random.normal(mean, std_dev, size) 

# Task2
def descriptive_statistics(height_data:np.array) -> tuple:
    """Calculates the mean, median and standard deviation of the height data.

    Args:
        height_data (np.array): 

    Returns:
        tuple: Mean, Median, Standard Deviation
    
    Raises:
        ValueError: Height data must be a numpy array.
        ValueError: Height data cannot be empty.
    
    """
    if not isinstance(height_data, np.ndarray):
        raise TypeError("Height data must be a numpy array.")
    if len(height_data) == 0:
        raise ValueError("Height data cannot be empty.")
    
    mean = np.mean(height_data)
    median = np.median(height_data)
    std_dev = np.std(height_data)
    return (mean, median, std_dev)

# Task3
def visualise_histogram(height_data:np.ndarray):
    """Creates a histogram of the height data.
    """
    if not isinstance(height_data, np.ndarray):
        raise TypeError("Height data must be a numpy array.")
    if len(height_data) == 0:
        raise ValueError("Height data cannot be empty.")
    plt.hist(height_data, bins=30, edgecolor='black', alpha=0.7)
    plt.title('Histogram of Heights')
    plt.xlabel('Height (cm)')
    plt.ylabel('Frequency')
    plt.grid(axis='y', alpha=0.75)
    plt.show()

# Task4
def calculate_percentiles(height_data:np.ndarray) -> tuple:
    """Calculates the 25th, 50th and 75th percentiles of the height data.

    Args:
        height_data (np.ndarray): Array of heights

    Returns:
        float: 25th percentile, 50th percentile, 75th percentile
    Raises:
        TypeError: Height data must be a numpy array.
        ValueError: Height data cannot be empty.
        
    """
    if not isinstance(height_data, np.ndarray):
        raise TypeError("Height data must be a numpy array.")
    if len(height_data) == 0:
        raise ValueError("Height data cannot be empty.")
    p25 = np.percentile(height_data, 25)
    p50 = np.percentile(height_data, 50)
    p75 = np.percentile(height_data, 75)
    return p25, p50, p75

# Task5
def identify_outliers(height_data:np.ndarray) -> np.ndarray:
    """Identifies outliers in the height data using the IQR method.

    Args:
        height_data (np.ndarray): Array of heights

    Returns:
        np.ndarray : Array of outliers
    Raises:
        TypeError: Height data must be a numpy array.
        ValueError: Height data cannot be empty.
    """
    if not isinstance(height_data, np.ndarray):
        raise TypeError("Height data must be a numpy array.")
    if len(height_data) == 0:
        raise ValueError("Height data cannot be empty.")
    
    q1 = np.percentile(height_data, 25)
    q3 = np.percentile(height_data, 75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    outliers = height_data[(height_data < lower_bound) | (height_data > upper_bound)]
    return outliers

# Task6
def random_sampling(height_data:np.ndarray) -> np.ndarray:
    """Performs random sampling of 50 heights from the data.

    Args:
        height_data (np.ndarray): Array of heights

    Returns:
        np.ndarray: Random sample of 50 heights
    Raises:
        TypeError: Height data must be a numpy array.
        ValueError: Height data cannot be empty.
    """
    if not isinstance(height_data, np.ndarray):
        raise TypeError("Height data must be a numpy array.")
    if len(height_data) == 0:
        raise ValueError("Height data cannot be empty.")
    sample = np.random.choice(height_data, size=50, replace=False)
    return sample

# Task7
def hypothesis_testing(data:np.ndarray, null_hypothesis_mean=165) -> tuple:
    """Performs a one-sample t-test to test the null hypothesis that the mean height is equal to 165 cm.

    Args:
        data (np.ndarray): Array of heights
        null_hypothesis_mean (int, optional): Mean height for the null hypothesis. Defaults to 165.

    Returns:
        : tuple: t-statistic, p-value
    """
    if not isinstance(data, np.ndarray):
        raise TypeError("Height data must be a numpy array.")
    if len(data) == 0:
        raise ValueError("Height data cannot be empty.")
    if not isinstance(null_hypothesis_mean, (int, float)):
        raise TypeError("Null hypothesis mean must be a number.")
    if null_hypothesis_mean <= 0:
        raise ValueError("Null hypothesis mean must be a positive number.")
    
    t_stat, p_value = ttest_1samp(data, null_hypothesis_mean)
    if p_value < 0.05:
        print("Reject the null hypothesis: The mean height is significantly different from the hypothesized mean.")
    else:
        print("Fail to reject the null hypothesis: The mean height is not significantly different from the hypothesized mean.")
    return (t_stat, p_value)

def calculate_probability(data:np.ndarray, threshold_height=180) -> np.float64:
    """Calculates the probability of finding a height greater than 180 cm in the dataset.

    Args:
        data (np.ndarray): Array of heights
        threshold_height (int, optional): . Defaults to 180.

    Returns:
        np.float64: 
    """
    if not isinstance(data, np.ndarray):
        raise TypeError("Height data must be a numpy array.")
    if len(data) == 0:
        raise ValueError("Height data cannot be empty.")
    if not isinstance(threshold_height, (int, float)):
        raise TypeError("Threshold height must be a number.")
    if threshold_height <= 0:
        raise ValueError("Threshold height must be a positive number.")
    mean = np.mean(data)
    std_dev = np.std(data)
    #The part of code below was generated by ChatGPT for the question: "Calculate the probability of finding a height greater than 180 cm in the dataset."
    probability = 1 - norm.cdf(threshold_height, loc=mean, scale=std_dev)
    return probability
# Example Usage
if __name__ == "__main__":
    # Generate height data
    heights = generate_height_data()
    # Calculate mean, median, and standard deviation
    mean, median, std_dev = descriptive_statistics(heights)
    print(f"Mean: {mean}, Median: {median}, Standard Deviation: {std_dev}")
    # Visualise the histogram
    visualise_histogram(heights)
    # Calculate percentiles
    p25, p50, p75 = calculate_percentiles(heights)
    print(f"25th Percentile: {p25}, 50th Percentile: {p50}, 75th Percentile: {p75}")
    # Identify outliers
    outliers = identify_outliers(heights)
    print("Outliers:", outliers)
    # Perform random sampling
    sample = random_sampling(heights)
    print("Random Sample:", sample)
    # Perform hypothesis testing
    t_stat, p_value = hypothesis_testing(heights)
    print(f"t-statistic: {t_stat}, p-value: {p_value}")
    # Calculate probability
    probability = calculate_probability(heights)
    print(f"Probability of finding a height greater than 180 cm: {probability}")
    