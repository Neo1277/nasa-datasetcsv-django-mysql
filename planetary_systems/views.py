from django.shortcuts import render
from .models import (
    PlanetarySystem,
    SpectralType,
    Star,
    DiscoveryMethod,
    DiscoveryFacility,
    SolutionType,
    Planet
)
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.db.models import F, Count

class PlanetarySystemsListView(ListView):
    """
    Sub-class the ListView to pass the request to the form.
    """
    # model = PlanetarySystem
    # By convention:
    template_name = "planetary_systems/planetary_system_list.html"

    def get_queryset(self):
        """Return all the planetary systems, with related stars and planets"""

        """
        Denormalizing database
        
        INNER JOIN, source: 
        https://stackoverflow.com/a/21360352/9655579
        
        Set alias for fields, source: 
        https://stackoverflow.com/a/46471483/9655579
        """

        planetary_systems = PlanetarySystem.objects.values(
            'id',
            'name',
            'number_of_stars',
            'number_of_planets',
            'publication_reference',
            'right_ascension_sexagesimal',
            'right_ascension_decimal',
            'declination_sexagesimal',
            'declination_decimal',
            'distance',
            'distance_err1',
            'distance_err2',
            'brightness_v_magnitude',
            'brightness_v_magnitude_err1',
            'brightness_v_magnitude_err2',
            'brightness_ks_magnitude',
            'brightness_ks_magnitude_err1',
            'brightness_ks_magnitude_err2',
            'brightness_gaia_magnitude',
            'brightness_gaia_magnitude_err1',
            'brightness_gaia_magnitude_err2',
            'brightness_gaia_magnitude_err2',


            'star_planetary_system__hd_name',
            'star_planetary_system__hip_name',
            'star_planetary_system__tic_id',
            'star_planetary_system__gaia_id',
            'star_planetary_system__publication_reference',
            'star_planetary_system__effective_temperature',
            'star_planetary_system__effective_temperature_err1',
            'star_planetary_system__effective_temperature_err2',
            'star_planetary_system__effective_temperature_limit',
            'star_planetary_system__radius',
            'star_planetary_system__radius_err1',
            'star_planetary_system__radius_err2',
            'star_planetary_system__radius_limit',
            'star_planetary_system__mass',
            'star_planetary_system__mass_err1',
            'star_planetary_system__mass_err2',
            'star_planetary_system__mass_limit',
            'star_planetary_system__measurement',
            'star_planetary_system__measurement_err1',
            'star_planetary_system__measurement_err2',
            'star_planetary_system__measurement_limit',
            'star_planetary_system__metallicity_ratio',
            'star_planetary_system__surface_gravity',
            'star_planetary_system__surface_gravity_err1',
            'star_planetary_system__surface_gravity_err2',
            'star_planetary_system__surface_gravity_limit',
            'star_planetary_system__planetary_system_id',

            'star_planetary_system__spectral_type',


            'planet_planetary_system',
            'planet_planetary_system__name',
            'planet_planetary_system__planet_letter',
            'planet_planetary_system__explicit',
            'planet_planetary_system__discovery_year',
            'planet_planetary_system__controversial_flag',
            'planet_planetary_system__publication_reference',
            'planet_planetary_system__orbital_period',
            'planet_planetary_system__orbital_period_err1',
            'planet_planetary_system__orbital_period_err2',
            'planet_planetary_system__orbital_period_limit',
            'planet_planetary_system__orbit_semi_major_axis',
            'planet_planetary_system__orbit_semi_major_axis_err1',
            'planet_planetary_system__orbit_semi_major_axis_err2',
            'planet_planetary_system__orbit_semi_major_axis_limit',
            'planet_planetary_system__earth_radius',
            'planet_planetary_system__earth_radius_err1',
            'planet_planetary_system__earth_radius_err2',
            'planet_planetary_system__earth_radius_limit',
            'planet_planetary_system__jupiter_radius',
            'planet_planetary_system__jupiter_radius_err1',
            'planet_planetary_system__jupiter_radius_err2',
            'planet_planetary_system__jupiter_radius_limit',
            'planet_planetary_system__earth_mass',
            'planet_planetary_system__earth_mass_err1',
            'planet_planetary_system__earth_mass_err2',
            'planet_planetary_system__earth_mass_limit',
            'planet_planetary_system__jupiter_mass',
            'planet_planetary_system__jupiter_mass_err1',
            'planet_planetary_system__jupiter_mass_err2',
            'planet_planetary_system__jupiter_mass_limit',
            'planet_planetary_system__mass_provenance',
            'planet_planetary_system__eccentricity',
            'planet_planetary_system__eccentricity_err1',
            'planet_planetary_system__eccentricity_err2',
            'planet_planetary_system__eccentricity_limit',
            'planet_planetary_system__insolation_flux',
            'planet_planetary_system__insolation_flux_err1',
            'planet_planetary_system__insolation_flux_err2',
            'planet_planetary_system__insolation_flux_limit',
            'planet_planetary_system__equilibrium_temperature',
            'planet_planetary_system__equilibrium_temperature_err1',
            'planet_planetary_system__equilibrium_temperature_err2',
            'planet_planetary_system__equilibrium_temperature_limit',
            'planet_planetary_system__transit_timing_variations',
            'planet_planetary_system__date_last_update',
            'planet_planetary_system__reference_date_publication',
            'planet_planetary_system__release_date',

            'planet_planetary_system__discovery_method__name',
            'planet_planetary_system__discovery_facility__name',
            'planet_planetary_system__solution_type__name'

        ).annotate(

            # Set alias for fields
            planetary_system_name=F('name'),
            planetary_system_number_of_stars=F('number_of_stars'),
            planetary_system_number_of_planets=F('number_of_planets'),
            planetary_system_publication_reference=F('publication_reference'),
            planetary_system_right_ascension_sexagesimal=F('right_ascension_sexagesimal'),
            planetary_system_right_ascension_decimal=F('right_ascension_decimal'),
            planetary_system_declination_sexagesimal=F('declination_sexagesimal'),
            planetary_system_declination_decimal=F('declination_decimal'),
            planetary_system_distance=F('distance'),
            planetary_system_distance_err1=F('distance_err1'),
            planetary_system_distance_err2=F('distance_err2'),
            planetary_system_brightness_v_magnitude=F('brightness_v_magnitude'),
            planetary_system_brightness_v_magnitude_err1=F('brightness_v_magnitude_err1'),
            planetary_system_brightness_v_magnitude_err2=F('brightness_v_magnitude_err2'),
            planetary_system_brightness_ks_magnitude=F('brightness_ks_magnitude'),
            planetary_system_brightness_ks_magnitude_err1=F('brightness_ks_magnitude_err1'),
            planetary_system_brightness_ks_magnitude_err2=F('brightness_ks_magnitude_err2'),
            planetary_system_brightness_gaia_magnitude=F('brightness_gaia_magnitude'),
            planetary_system_brightness_gaia_magnitude_err1=F('brightness_gaia_magnitude_err1'),
            planetary_system_brightness_gaia_magnitude_err2=F('brightness_gaia_magnitude_err2'),

            star_hd_name=F('star_planetary_system__hd_name'),
            star_hip_name=F('star_planetary_system__hip_name'),
            star_tic_id=F('star_planetary_system__tic_id'),
            star_gaia_id=F('star_planetary_system__gaia_id'),
            star_publication_reference=F('star_planetary_system__publication_reference'),
            star_effective_temperature=F('star_planetary_system__effective_temperature'),
            star_effective_temperature_err1=F('star_planetary_system__effective_temperature_err1'),
            star_effective_temperature_err2=F('star_planetary_system__effective_temperature_err2'),
            star_effective_temperature_limit=F('star_planetary_system__effective_temperature_limit'),
            star_radius=F('star_planetary_system__radius'),
            star_radius_err1=F('star_planetary_system__radius_err1'),
            star_radius_err2=F('star_planetary_system__radius_err2'),
            star_radius_limit=F('star_planetary_system__radius_limit'),
            star_mass=F('star_planetary_system__mass'),
            star_mass_err1=F('star_planetary_system__mass_err1'),
            star_mass_err2=F('star_planetary_system__mass_err2'),
            star_mass_limit=F('star_planetary_system__mass_limit'),
            star_measurement=F('star_planetary_system__measurement'),
            star_measurement_err1=F('star_planetary_system__measurement_err1'),
            star_measurement_err2=F('star_planetary_system__measurement_err2'),
            star_measurement_limit=F('star_planetary_system__measurement_limit'),
            star_metallicity_ratio=F('star_planetary_system__metallicity_ratio'),
            star_surface_gravity=F('star_planetary_system__surface_gravity'),
            star_surface_gravity_err1=F('star_planetary_system__surface_gravity_err1'),
            star_surface_gravity_err2=F('star_planetary_system__surface_gravity_err2'),
            star_surface_gravity_limit=F('star_planetary_system__surface_gravity_limit'),
            star_planetary_system_id=F('star_planetary_system__planetary_system_id'),
            star_spectral_type=F('star_planetary_system__spectral_type'),

            planet_id=F('planet_planetary_system'),
            planet_name=F('planet_planetary_system__name'),
            planet_planet_letter=F('planet_planetary_system__planet_letter'),
            planet_explicit=F('planet_planetary_system__explicit'),
            planet_discovery_year=F('planet_planetary_system__discovery_year'),
            planet_controversial_flag=F('planet_planetary_system__controversial_flag'),
            planet_publication_reference=F('planet_planetary_system__publication_reference'),
            planet_orbital_period=F('planet_planetary_system__orbital_period'),
            planet_orbital_period_err1=F('planet_planetary_system__orbital_period_err1'),
            planet_orbital_period_err2=F('planet_planetary_system__orbital_period_err2'),
            planet_orbital_period_limit=F('planet_planetary_system__orbital_period_limit'),
            planet_orbit_semi_major_axis=F('planet_planetary_system__orbit_semi_major_axis'),
            planet_orbit_semi_major_axis_err1=F('planet_planetary_system__orbit_semi_major_axis_err1'),
            planet_orbit_semi_major_axis_err2=F('planet_planetary_system__orbit_semi_major_axis_err2'),
            planet_orbit_semi_major_axis_limit=F('planet_planetary_system__orbit_semi_major_axis_limit'),
            planet_earth_radius=F('planet_planetary_system__earth_radius'),
            planet_earth_radius_err1=F('planet_planetary_system__earth_radius_err1'),
            planet_earth_radius_err2=F('planet_planetary_system__earth_radius_err2'),
            planet_earth_radius_limit=F('planet_planetary_system__earth_radius_limit'),
            planet_jupiter_radius=F('planet_planetary_system__jupiter_radius'),
            planet_jupiter_radius_err1=F('planet_planetary_system__jupiter_radius_err1'),
            planet_jupiter_radius_err2=F('planet_planetary_system__jupiter_radius_err2'),
            planet_jupiter_radius_limit=F('planet_planetary_system__jupiter_radius_limit'),
            planet_earth_mass=F('planet_planetary_system__earth_mass'),
            planet_earth_mass_err1=F('planet_planetary_system__earth_mass_err1'),
            planet_earth_mass_err2=F('planet_planetary_system__earth_mass_err2'),
            planet_earth_mass_limit=F('planet_planetary_system__earth_mass_limit'),
            planet_jupiter_mass=F('planet_planetary_system__jupiter_mass'),
            planet_jupiter_mass_err1=F('planet_planetary_system__jupiter_mass_err1'),
            planet_jupiter_mass_err2=F('planet_planetary_system__jupiter_mass_err2'),
            planet_jupiter_mass_limit=F('planet_planetary_system__jupiter_mass_limit'),
            planet_mass_provenance=F('planet_planetary_system__mass_provenance'),
            planet_eccentricity=F('planet_planetary_system__eccentricity'),
            planet_eccentricity_err1=F('planet_planetary_system__eccentricity_err1'),
            planet_eccentricity_err2=F('planet_planetary_system__eccentricity_err2'),
            planet_eccentricity_limit=F('planet_planetary_system__eccentricity_limit'),
            planet_insolation_flux=F('planet_planetary_system__insolation_flux'),
            planet_insolation_flux_err1=F('planet_planetary_system__insolation_flux_err1'),
            planet_insolation_flux_err2=F('planet_planetary_system__insolation_flux_err2'),
            planet_insolation_flux_limit=F('planet_planetary_system__insolation_flux_limit'),
            planet_equilibrium_temperature=F('planet_planetary_system__equilibrium_temperature'),
            planet_equilibrium_temperature_err1=F('planet_planetary_system__equilibrium_temperature_err1'),
            planet_equilibrium_temperature_err2=F('planet_planetary_system__equilibrium_temperature_err2'),
            planet_equilibrium_temperature_limit=F('planet_planetary_system__equilibrium_temperature_limit'),
            planet_transit_timing_variations=F('planet_planetary_system__transit_timing_variations'),
            planet_date_last_update=F('planet_planetary_system__date_last_update'),
            planet_reference_date_publication=F('planet_planetary_system__reference_date_publication'),
            planet_release_date=F('planet_planetary_system__release_date'),
            planet_discovery_method_name=F('planet_planetary_system__discovery_method__name'),
            planet_discovery_facility_name=F('planet_planetary_system__discovery_facility__name'),
            planet_solution_type_name=F('planet_planetary_system__solution_type__name'),

            # Group by to remove duplicated rows from query
            # https://stackoverflow.com/a/45547675/9655579
            count=Count('planet_id')
        )

        return planetary_systems

# References
# https://docs.djangoproject.com/en/3.0/topics/class-based-views/generic-display/