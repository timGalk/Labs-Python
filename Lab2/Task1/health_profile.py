from datetime import date
import math
from statistics import mean, stdev


class HealthProfile:
    # Class attribute for healthy BMI range
    healthy_bmi_range = (18.5, 24.9)

    def __init__(self, name, dob, height, weight):
        """Initialize HealthProfile with name, year of birth, height in cm, and weight in kg."""

        # Input validation
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string.")
        if not isinstance(dob, int) or dob > date.today().year or dob < 1900:
            raise ValueError("Data of birth must be an integer representing a reasonable year.")
        if not isinstance(height, (int, float)) or height <= 0:
            raise ValueError("Height must be a positive number.")
        if not isinstance(weight, (int, float)) or weight <= 0:
            raise ValueError("Weight must be a positive number.")

        self.name = name
        self.dob = dob  # year of birth
        self.height = height  # in cm
        self.weight = weight  # in kg

    def get_age(self):
        """Calculate and return age based on current year."""
        current_year = date.today().year
        return current_year - self.dob

    def get_target_hr(self):
        """Calculate and return target heart rate for moderate-intensity exercise."""
        age = self.get_age()
        max_hr = 220 - age
        if max_hr <= 0:
            raise ValueError("Maximum heart rate calculation is invalid due to age.")

        # Target HR is 50-70% of max HR
        target_hr_min = max_hr * 0.5
        target_hr_max = max_hr * 0.7
        return (target_hr_min, target_hr_max)

    def get_bmi(self):
        """Calculate and return BMI."""
        if self.height == 0:
            raise ValueError("Height cannot be zero when calculating BMI.")
        height_m = self.height / 100  # convert height to meters
        bmi = self.weight / (height_m ** 2)
        return bmi

    @staticmethod
    def calculate_age_stats(profiles):
        """Calculate mean and standard deviation of ages in a list of HealthProfile objects."""
        if not profiles:
            raise ValueError("No profiles provided for age statistics calculation.")

        ages = [profile.get_age() for profile in profiles]
        mean_age = mean(ages)
        std_dev_age = stdev(ages) if len(ages) > 1 else 0
        return mean_age, std_dev_age

    @staticmethod
    def find_people_at_risk(profiles):
        """Find profiles with BMI outside the healthy range."""
        if not profiles:
            raise ValueError("No profiles provided for BMI risk assessment.")

        at_risk = []
        for profile in profiles:
            bmi = profile.get_bmi()
            if bmi < HealthProfile.healthy_bmi_range[0] or bmi > HealthProfile.healthy_bmi_range[1]:
                at_risk.append(profile)
        return at_risk


# Demonstration code for HealthProfile class functionality
if __name__ == "__main__":
    try:
        # Create sample profiles
        profile1 = HealthProfile("Alice", 1985, 170, 65)
        profile2 = HealthProfile("Bob", 1990, 180, 85)
        profile3 = HealthProfile("Charlie", 2000, 160, 45)

        profiles = [profile1, profile2, profile3]

        # Display profile data and methods output
        for profile in profiles:
            print(
                f"{profile.name}: Age = {profile.get_age()}, Target HR = {profile.get_target_hr()}, BMI = {profile.get_bmi()}")

        # Calculate age statistics
        mean_age, std_dev_age = HealthProfile.calculate_age_stats(profiles)
        print(f"Mean Age: {mean_age}, Standard Deviation of Age: {std_dev_age}")

        # Find people at risk based on BMI
        at_risk_profiles = HealthProfile.find_people_at_risk(profiles)
        print("People at risk based on BMI:")
        for profile in at_risk_profiles:
            print(profile.name)

    except ValueError as e:
        print(f"Error: {e}")
