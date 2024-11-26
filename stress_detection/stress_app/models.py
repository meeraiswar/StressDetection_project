# stress_app/models.py
from django.db import models
from django.contrib.auth.models import User

class StressData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,max_length=100, null=True, blank=True)
    snoring_rate = models.FloatField(default=0.0)
    limb_movement = models.FloatField(default=0.0)
    eye_movement = models.FloatField(default=0.0)
    sleeping_hours = models.FloatField(default=0.0)
    respiratory_rate = models.FloatField(default=0.0)
    body_temperature = models.FloatField(default=36.5)  # Default body temperature
    heart_rate = models.FloatField(default=70.0)  # Default resting heart rate
    blood_oxygen = models.FloatField(default=98.0)  # Default blood oxygen level
    stress_level = models.FloatField(null=True, blank=True)  # Calculated, can be null
    is_stressed = models.BooleanField(default=False)  # Whether the user is stressed

    def calculate_stress(self):
        """
        Calculate the stress score and determine if the user is stressed.
        """
        # Define thresholds for stress-indicating parameters
        stress_indicators = 0

        if self.snoring_rate > 10:  # Snoring rate above 10
            stress_indicators += 1
        if self.limb_movement > 15:  # Excessive limb movement
            stress_indicators += 1
        if self.eye_movement > 12:  # High eye movement
            stress_indicators += 1
        if self.sleeping_hours < 5:  # Poor sleep
            stress_indicators += 1
        if self.respiratory_rate > 20:  # Elevated respiratory rate
            stress_indicators += 1
        if self.body_temperature > 38:  # Fever or high temperature
            stress_indicators += 1
        if self.heart_rate > 100:  # High heart rate
            stress_indicators += 1
        if self.blood_oxygen < 95:  # Low blood oxygen level
            stress_indicators += 1

        # Calculate stress level based on the number of stress-indicating parameters
        self.stress_level = stress_indicators / 8  # Normalize to a scale of 0-1

        # Determine if the user is stressed based on a threshold
        self.is_stressed = stress_indicators >= 3  # If 3 or more indicators are present, consider stressed

        # Save the updated model
        self.save()
