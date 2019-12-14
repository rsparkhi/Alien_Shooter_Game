import pygame

class Settings():
    """A class to store all the settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""

        # Screen settings.
        self.screen_width = 1366
        self.screen_height = 695
        self.bg_color = (0,0,0)

        # Ship settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # Bullet Settings
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullet_allowed = 3

        #Alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10

        #How quickly the game speeds up.
        self.speedup_scale = 1.3

        #How quickly the alien point values increases.
        self.score_scale = 1.5  

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the gmame."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        #fleet_directio of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        #scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)