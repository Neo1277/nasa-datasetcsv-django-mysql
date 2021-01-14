from django.db import models

# Source: Model field reference https://docs.djangoproject.com/en/3.1/ref/models/fields/#module-django.db.models.fields

# Dataset columns info: https://exoplanetarchive.ipac.caltech.edu/docs/API_PS_columns.html#stellardata

# Generate custom field for primary key
# https://docs.djangoproject.com/en/3.1/howto/custom-model-fields/#custom-database-types
# https://stackoverflow.com/a/56306262/9655579
class UnsignedAutoField(models.AutoField):
    def db_type(self, connection):
        return 'INT(10) UNSIGNED ZEROFILL AUTO_INCREMENT'

    def rel_db_type(self, connection):
        return 'INT(10) UNSIGNED ZEROFILL'

class PlanetarySystem(models.Model):

    id = UnsignedAutoField(
        unique=True,
        primary_key=True
    )

    # hostname
    name = models.CharField(
        max_length=255
    )

    # sy_snum
    number_of_stars = models.PositiveSmallIntegerField()

    # sy_pnum
    number_of_planets = models.PositiveSmallIntegerField()

    # sy_refname
    publication_reference = models.CharField(
        max_length=255
    )

    # rastr
    right_ascension_sexagesimal = models.CharField(
        max_length=23
    )

    # ra
    right_ascension_decimal = models.DecimalField(
        max_digits=23,
        decimal_places=10
    )

    # decstr
    declination_sexagesimal = models.CharField(
        max_length=23
    )

    # dec
    declination_decimal = models.DecimalField(
        max_digits=23,
        decimal_places=10
    )

    # sy_dist
    distance = models.DecimalField(
        max_digits=23,
        decimal_places=10,
        null=True
    )

    # sy_disterr1
    distance_err1 = models.DecimalField(
        max_digits=23,
        decimal_places=10,
        null=True
    )

    # sy_disterr2
    distance_err2 = models.DecimalField(
        max_digits=23,
        decimal_places=10,
        null=True
    )

    # sy_vmag
    brightness_v_magnitude = models.DecimalField(
        max_digits=23,
        decimal_places=10,
        null=True
    )

    # sy_vmagerr1
    brightness_v_magnitude_err1 = models.DecimalField(
        max_digits=23,
        decimal_places=10,
        null=True
    )

    # sy_vmagerr2
    brightness_v_magnitude_err2 = models.DecimalField(
        max_digits=23,
        decimal_places=10,
        null=True
    )

    # sy_kmag
    brightness_ks_magnitude = models.DecimalField(
        max_digits=23,
        decimal_places=10,
        null=True
    )

    # sy_kmagerr1
    brightness_ks_magnitude_err1 = models.DecimalField(
        max_digits=23,
        decimal_places=10,
        null=True
    )

    # sy_kmagerr2
    brightness_ks_magnitude_err2 = models.DecimalField(
        max_digits=23,
        decimal_places=10,
        null=True
    )

    # sy_gaiamag
    brightness_gaia_magnitude = models.DecimalField(
        max_digits=23,
        decimal_places=10,
        null=True
    )

    # sy_gaiamagerr1
    brightness_gaia_magnitude_err1 = models.DecimalField(
        max_digits=23,
        decimal_places=10,
        null=True
    )

    # sy_gaiamagerr2
    brightness_gaia_magnitude_err2 = models.DecimalField(
        max_digits=23,
        decimal_places=10,
        null=True
    )

    row_created_on = models.DateTimeField(
        auto_now_add=True,
        help_text="Date and time when the register was created"
    )

    row_updated_on = models.DateTimeField(
        auto_now=True,
        help_text="Date and time when the register was updated"
    )

class SpectralType(models.Model):

    id = UnsignedAutoField(
        unique=True,
        primary_key=True
    )

    # st_spectype
    name = models.CharField(
        max_length=20
    )

    row_created_on = models.DateTimeField(
        auto_now_add=True,
        help_text="Date and time when the register was created"
    )

    row_updated_on = models.DateTimeField(
        auto_now=True,
        help_text="Date and time when the register was updated"
    )

class Star(models.Model):

    id = UnsignedAutoField(
        unique=True,
        primary_key=True
    )

    # hd_name
    hd_name = models.CharField(
        max_length=255,
        help_text="Name of the star as given by the Henry Draper Catalog",
        null=True
    )

    # hip_name
    hip_name = models.CharField(
        max_length=255,
        help_text="Name of the star as given by the Hipparcos Catalog",
        null=True
    )

    # tic_id
    tic_id = models.CharField(
        max_length=255,
        help_text="Name of the star as given by the TESS Input Catalog",
        null=True
    )

    # gaia_id
    gaia_id = models.CharField(
        max_length=255,
        help_text="Name of the star as given by the Gaia Catalog",
        null=True
    )

    # st_refname
    publication_reference = models.CharField(
        max_length=255
    )

    # st_teff
    effective_temperature = models.DecimalField(
        max_digits=10,
        decimal_places=4,
        null=True
    )

    # st_tefferr1
    effective_temperature_err1 = models.DecimalField(
        max_digits=10,
        decimal_places=4,
        null=True
    )

    # st_tefferr2
    effective_temperature_err2 = models.DecimalField(
        max_digits=10,
        decimal_places=4,
        null=True
    )

    # st_tefflim
    effective_temperature_limit = models.SmallIntegerField(
        null=True
    )

    # st_rad
    radius = models.DecimalField(
        max_digits=7,
        decimal_places=3,
        null=True
    )

    # st_raderr1
    radius_err1 = models.DecimalField(
        max_digits=7,
        decimal_places=3,
        null=True
    )

    # st_raderr2
    radius_err2 = models.DecimalField(
        max_digits=7,
        decimal_places=3,
        null=True
    )

    # st_radlim
    radius_limit = models.SmallIntegerField(
        null=True
    )

    # st_mass
    mass = models.DecimalField(
        max_digits=7,
        decimal_places=3,
        null=True
    )

    # st_masserr1
    mass_err1 = models.DecimalField(
        max_digits=7,
        decimal_places=3,
        null=True
    )

    # st_masserr2
    mass_err2 = models.DecimalField(
        max_digits=7,
        decimal_places=3,
        null=True
    )

    # st_masslim
    mass_limit = models.SmallIntegerField(
        null=True
    )

    # st_met
    measurement = models.DecimalField(
        max_digits=7,
        decimal_places=4,
        null=True
    )

    # st_meterr1
    measurement_err1 = models.DecimalField(
        max_digits=7,
        decimal_places=4,
        null=True
    )

    # st_meterr2
    measurement_err2 = models.DecimalField(
        max_digits=7,
        decimal_places=4,
        null=True
    )

    # st_metlim
    measurement_limit = models.SmallIntegerField(
        null=True
    )

    # st_metratio
    metallicity_ratio = models.CharField(
        max_length=20,
        null=True
    )

    # st_logg
    surface_gravity = models.DecimalField(
        max_digits=7,
        decimal_places=3,
        null=True
    )

    # st_loggerr1
    surface_gravity_err1 = models.DecimalField(
        max_digits=7,
        decimal_places=3,
        null=True
    )

    # st_loggerr2
    surface_gravity_err2 = models.DecimalField(
        max_digits=7,
        decimal_places=3,
        null=True
    )

    # st_logglim
    surface_gravity_limit = models.SmallIntegerField(
        null=True
    )

    # Foreign key field
    planetary_system = models.ForeignKey(
        PlanetarySystem,
        on_delete=models.CASCADE,
        related_name='star_planetary_system'
    )

    # Foreign key field
    spectral_type = models.ForeignKey(
        SpectralType,
        on_delete=models.CASCADE,
        related_name='star_spectral_type',
        null=True
    )

    row_created_on = models.DateTimeField(
        auto_now_add=True,
        help_text="Date and time when the register was created"
    )

    row_updated_on = models.DateTimeField(
        auto_now=True,
        help_text="Date and time when the register was updated"
    )

class DiscoveryMethod(models.Model):

    id = UnsignedAutoField(
        unique=True,
        primary_key=True
    )

    # discoverymethod
    name = models.CharField(
        max_length=255
    )

    row_created_on = models.DateTimeField(
        auto_now_add=True,
        help_text="Date and time when the register was created"
    )

    row_updated_on = models.DateTimeField(
        auto_now=True,
        help_text="Date and time when the register was updated"
    )

class DiscoveryFacility(models.Model):

    id = UnsignedAutoField(
        unique=True,
        primary_key=True
    )

    # disc_facility
    name = models.CharField(
        max_length=255
    )

    row_created_on = models.DateTimeField(
        auto_now_add=True,
        help_text="Date and time when the register was created"
    )

    row_updated_on = models.DateTimeField(
        auto_now=True,
        help_text="Date and time when the register was updated"
    )

class SolutionType(models.Model):

    id = UnsignedAutoField(
        unique=True,
        primary_key=True
    )

    # soltype
    name = models.CharField(
        max_length=255
    )

    row_created_on = models.DateTimeField(
        auto_now_add=True,
        help_text="Date and time when the register was created"
    )

    row_updated_on = models.DateTimeField(
        auto_now=True,
        help_text="Date and time when the register was updated"
    )

class Planet(models.Model):

    id = UnsignedAutoField(
        unique=True,
        primary_key=True
    )

    # pl_name
    name = models.CharField(
        max_length=255
    )

    # pl_letter
    planet_letter = models.CharField(
        max_length=1
    )

    # default_flag
    explicit = models.BooleanField()

    # disc_year
    discovery_year = models.PositiveSmallIntegerField()

    # pl_controv_flag
    controversial_flag = models.BooleanField()

    # pl_refname
    publication_reference = models.CharField(
        max_length=255
    )

    # pl_orbper
    orbital_period = models.DecimalField(
        max_digits=25,
        decimal_places=10,
        null=True
    )

    # pl_orbpererr1
    orbital_period_err1 = models.DecimalField(
        max_digits=25,
        decimal_places=10,
        null=True
    )

    # pl_orbpererr2
    orbital_period_err2 = models.DecimalField(
        max_digits=25,
        decimal_places=10,
        null=True
    )

    # pl_orbperlim
    orbital_period_limit = models.SmallIntegerField(
        null=True
    )

    # pl_orbsmax
    orbit_semi_major_axis = models.DecimalField(
        max_digits=23,
        decimal_places=10,
        null=True
    )

    # pl_orbsmaxerr1
    orbit_semi_major_axis_err1 = models.DecimalField(
        max_digits=23,
        decimal_places=10,
        null=True
    )

    # pl_orbsmaxerr2
    orbit_semi_major_axis_err2 = models.DecimalField(
        max_digits=23,
        decimal_places=10,
        null=True
    )

    # pl_orbsmaxlim
    orbit_semi_major_axis_limit = models.SmallIntegerField(
        null=True
    )

    # pl_rade
    earth_radius = models.DecimalField(
        max_digits=9,
        decimal_places=4,
        null=True
    )

    # pl_radeerr1
    earth_radius_err1 = models.DecimalField(
        max_digits=9,
        decimal_places=4,
        null=True
    )

    # pl_radeerr2
    earth_radius_err2 = models.DecimalField(
        max_digits=9,
        decimal_places=4,
        null=True
    )

    # pl_radelim
    earth_radius_limit = models.SmallIntegerField(
        null=True
    )

    # pl_radj
    jupiter_radius = models.DecimalField(
        max_digits=9,
        decimal_places=4,
        null=True
    )

    # pl_radjerr1
    jupiter_radius_err1 = models.DecimalField(
        max_digits=9,
        decimal_places=4,
        null=True
    )

    # pl_radjerr2
    jupiter_radius_err2 = models.DecimalField(
        max_digits=9,
        decimal_places=4,
        null=True
    )

    # pl_radjlim
    jupiter_radius_limit = models.SmallIntegerField(
        null=True
    )

    # pl_bmasse
    earth_mass = models.DecimalField(
        max_digits=23,
        decimal_places=10,
        null=True
    )

    # pl_bmasseerr1
    earth_mass_err1 = models.DecimalField(
        max_digits=23,
        decimal_places=10,
        null=True
    )

    # pl_bmasseerr2
    earth_mass_err2 = models.DecimalField(
        max_digits=23,
        decimal_places=10,
        null=True
    )

    # pl_bmasselim
    earth_mass_limit = models.SmallIntegerField(
        null=True
    )

    # pl_bmassj
    jupiter_mass = models.DecimalField(
        max_digits=23,
        decimal_places=10,
        null=True
    )

    # pl_bmassjerr1
    jupiter_mass_err1 = models.DecimalField(
        max_digits=23,
        decimal_places=10,
        null=True
    )

    # pl_bmassjerr2
    jupiter_mass_err2 = models.DecimalField(
        max_digits=23,
        decimal_places=10,
        null=True
    )

    # pl_bmassjlim
    jupiter_mass_limit = models.SmallIntegerField(
        null=True
    )

    # pl_bmassprov
    mass_provenance = models.CharField(
        max_length=20,
        null=True
    )

    # pl_orbeccen
    eccentricity = models.DecimalField(
        max_digits=14,
        decimal_places=10,
        null=True
    )

    # pl_orbeccenerr1
    eccentricity_err1 = models.DecimalField(
        max_digits=14,
        decimal_places=10,
        null=True
    )

    # pl_orbeccenerr2
    eccentricity_err2 = models.DecimalField(
        max_digits=14,
        decimal_places=10,
        null=True
    )

    # pl_orbeccenlim
    eccentricity_limit = models.SmallIntegerField(
        null=True
    )

    # pl_insol
    insolation_flux = models.DecimalField(
        max_digits=8,
        decimal_places=3,
        null=True
    )

    # pl_insolerr1
    insolation_flux_err1 = models.DecimalField(
        max_digits=8,
        decimal_places=3,
        null=True
    )

    # pl_insolerr2
    insolation_flux_err2 = models.DecimalField(
        max_digits=8,
        decimal_places=3,
        null=True
    )

    # pl_insollim
    insolation_flux_limit = models.SmallIntegerField(
        null=True
    )

    # pl_eqt
    equilibrium_temperature = models.SmallIntegerField(
        null=True
    )

    # pl_eqterr1
    equilibrium_temperature_err1 = models.SmallIntegerField(
        null=True
    )

    # pl_eqterr2
    equilibrium_temperature_err2 = models.SmallIntegerField(
        null=True
    )

    # pl_eqtlim
    equilibrium_temperature_limit = models.SmallIntegerField(
        null=True
    )

    # ttv_flag
    transit_timing_variations = models.BooleanField()

    # rowupdate
    date_last_update = models.DateField(
        auto_now=False,
        auto_now_add=False
    )

    # pl_pubdate
    reference_date_publication = models.CharField(
        max_length=25
    )

    # releasedate
    release_date = models.CharField(
        max_length=25
    )

    # Foreign key field
    planetary_system = models.ForeignKey(
        PlanetarySystem,
        on_delete=models.CASCADE,
        related_name='planet_planetary_system'
    )

    # Foreign key field
    discovery_method = models.ForeignKey(
        DiscoveryMethod,
        on_delete=models.CASCADE,
        related_name='planet_discovery_method'
    )

    # Foreign key field
    discovery_facility = models.ForeignKey(
        DiscoveryFacility,
        on_delete=models.CASCADE,
        related_name='planet_discovery_facility'
    )

    # Foreign key field
    solution_type = models.ForeignKey(
        SolutionType,
        on_delete=models.CASCADE,
        related_name='planet_solution_type'
    )

    row_created_on = models.DateTimeField(
        auto_now_add=True,
        help_text="Date and time when the register was created"
    )

    row_updated_on = models.DateTimeField(
        auto_now=True,
        help_text="Date and time when the register was updated"
    )
