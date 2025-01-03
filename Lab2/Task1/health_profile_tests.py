import unittest
import health_profile
from health_profile import HealthProfile
from datetime import  date

class TestHealthProfile(unittest.TestCase):
    def setUp(self):
        """Set up test cases with valid data"""
        self.valid_name = "John Doe"
        self.valid_dob = 1990
        self.valid_height = 175
        self.valid_weight = 70

    def test_valid_initialization(self):
        """Test initialization with valid data"""
        profile = HealthProfile(
            self.valid_name,
            self.valid_dob,
            self.valid_height,
            self.valid_weight
        )

        self.assertEqual(profile.name, self.valid_name)
        self.assertEqual(profile.dob, self.valid_dob)
        self.assertEqual(profile.height, self.valid_height)
        self.assertEqual(profile.weight, self.valid_weight)

    def test_invalid_name(self):
        """Test initialization with invalid name values"""
        invalid_names = [
            "",  # Empty string
            " ",  # Whitespace
            123,  # Number
            None,  # None
            [],  # List
            bool
        ]

        for name in invalid_names:
            with self.assertRaises(ValueError) as context:
                HealthProfile(name, self.valid_dob, self.valid_height, self.valid_weight)
            self.assertTrue("Name must be a non-empty string" in str(context.exception))

    def test_invalid_dob(self):
        """Test initialization with invalid date of birth values"""
        current_year = date.today().year
        invalid_dobs = [
            current_year + 1,  # Future year
            1899,  # Too old
            "1990",  # String instead of int
            None,  # None
            0,  # Zero
            -1990,  # Negative
        ]

        for dob in invalid_dobs:
            with self.assertRaises(ValueError) as context:
                HealthProfile(self.valid_name, dob, self.valid_height, self.valid_weight)
            self.assertTrue("Data of birth must be an integer" in str(context.exception))

    def test_invalid_height(self):
        """Test initialization with invalid height values"""
        invalid_heights = [
            0,  # Zero
            -175,  # Negative
            "175",  # String
            None,  # None
            [],  # List
        ]

        for height in invalid_heights:
            with self.assertRaises(ValueError) as context:
                HealthProfile(self.valid_name, self.valid_dob, height, self.valid_weight)
            self.assertTrue("Height must be a positive number" in str(context.exception))

    def test_invalid_weight(self):
        """Test initialization with invalid weight values"""
        invalid_weights = [
            0,  # Zero
            -70,  # Negative
            "70",  # String
            None,  # None
            [],  # List
        ]

        for weight in invalid_weights:
            with self.assertRaises(ValueError) as context:
                HealthProfile(self.valid_name, self.valid_dob, self.valid_height, weight)
            self.assertTrue("Weight must be a positive number" in str(context.exception))

    def test_float_values(self):
        """Test initialization with float values for height and weight"""
        profile = HealthProfile(self.valid_name, self.valid_dob, 175.5, 70.5)
        self.assertEqual(profile.height, 175.5)
        self.assertEqual(profile.weight, 70.5)

    def test_get_age_valid (self):
        """Test get_age method"""
        profile = HealthProfile(self.valid_name, self.valid_dob, self.valid_height, self.valid_weight)
        self.assertEqual(profile.get_age(), 34)
    def test_get_age_invalid(self):
        """Test get_age method with invalid date of birth values"""
        current_year = date.today().year
        invalid_dobs = [
            current_year + 1,  # Future year
            1899,  # Too old
            "1990",  # String instead of int
            None,  # None
            0,  # Zero
            -1990,  # Negative
        ]

        for dob in invalid_dobs:
            with self.assertRaises(ValueError) as context:
                HealthProfile(self.valid_name, dob, self.valid_height, self.valid_weight)
            self.assertTrue("Data of birth must be an integer" in str(context.exception))

    def test_calculate_age_stats_empty(self):
        """Test for raising ValueError when profiles list is empty."""
        with self.assertRaises(ValueError):
            HealthProfile.calculate_age_stats([])

    def test_calculate_age_stats_single_profile(self):
        """Test for standard deviation of 0 when only one profile is provided."""
        single_profile = [HealthProfile("John Doe", 1990, 175, 70)]
        mean_age, std_dev_age = HealthProfile.calculate_age_stats(single_profile)
        self.assertEqual(mean_age, 34)
        self.assertEqual(std_dev_age, 0)

    def test_find_people_at_risk_valid(self):
        """Test to find people at risk due to BMI outside healthy range."""
        healthy_profiles = [HealthProfile("John Doe", 1990, 175, 67),
                            HealthProfile("Jane Doe", 1980, 180, 70)]
        self.assertEqual(len(healthy_profiles), 2)  # profile3 and profile4 should be at risk

    def test_find_people_at_risk_empty(self):
        """Test for raising ValueError when profiles list is empty."""
        with self.assertRaises(ValueError):
            HealthProfile.find_people_at_risk([])

    def test_find_people_at_risk_no_at_risk(self):
        """Test for returning an empty list when all profiles are healthy."""
        healthy_profiles = [HealthProfile("John Doe", 1990, 175, 100),
                            HealthProfile("Jane Doe", 1980, 180, 100)]
        at_risk = HealthProfile.find_people_at_risk(healthy_profiles)
        self.assertEqual(len(at_risk), 2)

if __name__ == '__main__':
    unittest.main()