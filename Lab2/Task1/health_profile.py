from datetime import date

class HealthProfile:
    # Class attribute for healthy BMI range
    healthy_bmi_range = (18.5, 24.9)

    def __init__(self, name, dob, height, weight):
        """Initialize HealthProfile with name, year of birth, height in cm, and weight in kg."""
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
        # Target HR is 50-70% of max HR
        target_hr_min = max_hr * 0.5
        target_hr_max = max_hr * 0.7
        return (target_hr_min, target_hr_max)

    def get_bmi(self):
        """Calculate and return BMI."""
        height_m = self.height / 100  # convert height to meters
        bmi = self.weight / (height_m ** 2)
        return bmi