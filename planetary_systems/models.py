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
    """
    hostname
    sy_snum
    sy_pnum
    sy_refname
    rastr
    ra
    decstr
    dec
    sy_dist
    sy_disterr1
    sy_disterr2
    sy_vmag
    sy_vmagerr1
    sy_vmagerr2
    sy_kmag
    sy_kmagerr1
    sy_kmagerr2
    sy_gaiamag
    sy_gaiamagerr1
    sy_gaiamagerr2
    """

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
        help_text="Date and time when the register was created updated"
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
        help_text="Date and time when the register was created updated"
    )

class Star(models.Model):
    """
    hd_name
    hip_name
    tic_id
    gaia_id
    st_refname
    st_teff
    st_tefferr1
    st_tefferr2
    st_tefflim
    st_rad
    st_raderr1
    st_raderr2	
    st_radlim
    st_mass
    st_masserr1
    st_masserr2
    st_masslim
    st_met
    st_meterr1
    st_meterr2
    st_metlim
    st_metratio
    st_logg
    st_loggerr1
    st_loggerr2
    st_logglim
    """

    id = UnsignedAutoField(
        unique=True,
        primary_key=True
    )

    # hd_name
    hd_name = models.CharField(
        max_length=255,
        help_text="Name of the star as given by the Henry Draper Catalog"
    )

    # hip_name
    hip_name = models.CharField(
        max_length=255,
        help_text="Name of the star as given by the Hipparcos Catalog"
    )

    # tic_id
    tic_id = models.CharField(
        max_length=255,
        help_text="Name of the star as given by the TESS Input Catalog"
    )

    # gaia_id
    gaia_id = models.CharField(
        max_length=255,
        help_text="Name of the star as given by the Gaia Catalog"
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
    effective_temperature_limit = models.PositiveSmallIntegerField(
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
    radius_limit = models.PositiveSmallIntegerField(
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
    mass_limit = models.PositiveSmallIntegerField(
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
    measurement_limit = models.PositiveSmallIntegerField(
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
    surface_gravity_limit = models.PositiveSmallIntegerField(
        null=True
    )

    planetary_system = models.ForeignKey(
        PlanetarySystem,
        on_delete=models.CASCADE,
        related_name='star_planetary_system'
    )

    spectral_type = models.ForeignKey(
        SpectralType,
        on_delete=models.CASCADE,
        related_name='star_spectral_type'
    )

    row_created_on = models.DateTimeField(
        auto_now_add=True,
        help_text="Date and time when the register was created"
    )

    row_updated_on = models.DateTimeField(
        auto_now=True,
        help_text="Date and time when the register was created updated"
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
        help_text="Date and time when the register was created updated"
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
        help_text="Date and time when the register was created updated"
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
        help_text="Date and time when the register was created updated"
    )

class Planet(models.Model):
    """
    pl_name
    pl_letter
    default_flag
    disc_year
    pl_controv_flag
    pl_refname
    pl_orbper
    pl_orbpererr1
    pl_orbpererr2
    pl_orbperlim
    pl_orbsmax
    pl_orbsmaxerr1
    pl_orbsmaxerr2
    pl_orbsmaxlim
    pl_rade
    pl_radeerr1
    pl_radeerr2
    pl_radelim
    pl_radj
    pl_radjerr1
    pl_radjerr2
    pl_radjlim
    pl_bmasse
    pl_bmasseerr1
    pl_bmasseerr2
    pl_bmasselim
    pl_bmassj
    pl_bmassjerr1
    pl_bmassjerr2
    pl_bmassjlim
    pl_bmassprov
    pl_orbeccen
    pl_orbeccenerr1
    pl_orbeccenerr2
    pl_orbeccenlim
    pl_insol
    pl_insolerr1
    pl_insolerr2
    pl_insollim
    pl_eqt
    pl_eqterr1
    pl_eqterr2
    pl_eqtlim
    ttv_flag
    rowupdate
    pl_pubdate
    releasedate
    """

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
    orbital_period_limit = models.PositiveSmallIntegerField(
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
    orbit_semi_major_axis_limit = models.PositiveSmallIntegerField()

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
    earth_radius_limit = models.PositiveSmallIntegerField(
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
    jupiter_radius_limit = models.PositiveSmallIntegerField(
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
    earth_mass_limit = models.PositiveSmallIntegerField(
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
    jupiter_mass_limit = models.PositiveSmallIntegerField(
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
    eccentricity_limit = models.PositiveSmallIntegerField(
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
    insolation_flux_limit = models.PositiveSmallIntegerField(
        null=True
    )

    # pl_eqt
    equilibrium_temperature = models.PositiveSmallIntegerField(
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
    equilibrium_temperature_limit = models.PositiveSmallIntegerField(
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
    reference_date_publication = models.DateTimeField(
        auto_now=False,
        auto_now_add=False
    )

    # releasedate
    release_date = models.DateField(
        auto_now=False,
        auto_now_add=False
    )

    planetary_system = models.ForeignKey(
        PlanetarySystem,
        on_delete=models.CASCADE,
        related_name='planet_planetary_system'
    )

    discovery_method = models.ForeignKey(
        DiscoveryMethod,
        on_delete=models.CASCADE,
        related_name='planet_discovery_method'
    )

    discovery_facility = models.ForeignKey(
        DiscoveryFacility,
        on_delete=models.CASCADE,
        related_name='planet_discovery_facility'
    )

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
        help_text="Date and time when the register was created updated"
    )
