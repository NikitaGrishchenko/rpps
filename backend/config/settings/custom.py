# Setting application write here ...

# Setting editable in admin

CONSTANCE_CONFIG = {
    "SITE_NAME": ("My Title", "Website title"),
    "SITE_DESCRIPTION": ("", "Website description"),
    "THEME": ("light-blue", "Website theme"),
}

CONSTANCE_CONFIG_FIELDSETS = {
    "General Options": ("SITE_NAME", "SITE_DESCRIPTION"),
    "Theme Options": ("THEME",),
}
