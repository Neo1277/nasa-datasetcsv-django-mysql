from django.db import models

# Source: Model field reference https://docs.djangoproject.com/en/3.1/ref/models/fields/#django.db.models.DateTimeField

# Dataset columns info: https://exoplanetarchive.ipac.caltech.edu/docs/API_PS_columns.html#stellardata

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

class DiscoveryMethod(models.Model):
    # discoverymethod

class DiscoveryFacility(models.Model):
    # disc_facility

class SolutionType(models.Model):
    # soltype

class SpectralType(models.Model):
    # st_spectype