import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from planetary_systems.models import (
    PlanetarySystem,
    SpectralType,
    Star,
    DiscoveryMethod,
    DiscoveryFacility,
    SolutionType,
    Planet
)

"""
IMPORTANT: This file is executed where the manage.py file resides with the next command :
python3 manage.py runscript many_load
"""

def run():
    # Open and read csv file
    fhand = open('PS_2021.01.08_12.13.30.csv')
    reader = csv.reader(fhand)

    # next(reader)  # Advance past the header

    # Skip header rows
    # Source: https://stackoverflow.com/a/40404006/9655579
    for skip in range(104):
        next(reader)

    # Delete all data from tables to insert them again

    Planet.objects.all().delete()

    Star.objects.all().delete()

    SolutionType.objects.all().delete()

    DiscoveryFacility.objects.all().delete()

    DiscoveryMethod.objects.all().delete()

    SpectralType.objects.all().delete()

    PlanetarySystem.objects.all().delete()

    # Format
    # email,role,course
    # jane@tsugi.org,I,Python
    # ed@tsugi.org,L,Python


    # Iterate over each row
    for row in reader:
        print(row)

        """
        get_or_create
        This statement search if the data already exists and if it does exist it brings the data
        to save it with the table related foreign key or if it does not exist it save it
        and then save the another table with the id related foreign key.
        """

        index = 0
        for column in row:

            """
            If the column is empty set none to be able to save the entire row 
            with some null columns
            """
            if not column:
                row[index] = None
                # print(column)
            index = index + 1

        planetary_system, created = PlanetarySystem.objects.get_or_create(
            name = row[1],
            number_of_stars = row[8],
            number_of_planets = row[9],
            publication_reference = row[77],
            right_ascension_sexagesimal = row[78],
            right_ascension_decimal = row[79],
            declination_sexagesimal = row[80],
            declination_decimal = row[81],
            distance = row[82],
            distance_err1 = row[83],
            distance_err2 = row[84],
            brightness_v_magnitude = row[85],
            brightness_v_magnitude_err1 = row[86],
            brightness_v_magnitude_err2 = row[87],
            brightness_ks_magnitude = row[88],
            brightness_ks_magnitude_err1 = row[89],
            brightness_ks_magnitude_err2 = row[90],
            brightness_gaia_magnitude = row[91],
            brightness_gaia_magnitude_err1 = row[92],
            brightness_gaia_magnitude_err2 = row[93],
        )

        # Test if variable is None
        # Source: https://stackoverflow.com/a/43934358/9655579
        if row[55] is None:
            spectral_type = None
        else:
            spectral_type, created = SpectralType.objects.get_or_create(
                name=row[55]
            )

        star, created = Star.objects.get_or_create(
            hd_name = row[3],
            hip_name = row[4],
            tic_id = row[5],
            gaia_id = row[6],
            publication_reference = row[54],
            effective_temperature = row[56],
            effective_temperature_err1 = row[57],
            effective_temperature_err2 = row[58],
            effective_temperature_limit = row[59],
            radius = row[60],
            radius_err1 = row[61],
            radius_err2 = row[62],
            radius_limit = row[63],
            mass = row[64],
            mass_err1 = row[65],
            mass_err2 = row[66],
            mass_limit = row[67],
            measurement = row[68],
            measurement_err1 = row[69],
            measurement_err2 = row[70],
            measurement_limit = row[71],
            metallicity_ratio = row[72],
            surface_gravity = row[73],
            surface_gravity_err1 = row[74],
            surface_gravity_err2 = row[75],
            surface_gravity_limit = row[76],
            planetary_system = planetary_system,
            spectral_type = spectral_type
        )

        discovery_method, created = DiscoveryMethod.objects.get_or_create(
            name=row[10]
        )

        discovery_facility, created = DiscoveryFacility.objects.get_or_create(
            name=row[12]
        )

        solution_type, created = SolutionType.objects.get_or_create(
            name=row[13]
        )

        planet = Planet(
            name = row[0],
            planet_letter = row[2],
            explicit = row[7],
            discovery_year = row[11],
            controversial_flag = row[14],
            publication_reference = row[15],
            orbital_period = row[16],
            orbital_period_err1 = row[17],
            orbital_period_err2 = row[18],
            orbital_period_limit = row[19],
            orbit_semi_major_axis = row[20],
            orbit_semi_major_axis_err1 = row[21],
            orbit_semi_major_axis_err2 = row[22],
            orbit_semi_major_axis_limit = row[23],
            earth_radius = row[24],
            earth_radius_err1 = row[25],
            earth_radius_err2 = row[26],
            earth_radius_limit = row[27],
            jupiter_radius = row[28],
            jupiter_radius_err1 = row[29],
            jupiter_radius_err2 = row[30],
            jupiter_radius_limit = row[31],
            earth_mass = row[32],
            earth_mass_err1 = row[33],
            earth_mass_err2 = row[34],
            earth_mass_limit = row[35],
            jupiter_mass = row[36],
            jupiter_mass_err1 = row[37],
            jupiter_mass_err2 = row[38],
            jupiter_mass_limit = row[39],
            mass_provenance = row[40],
            eccentricity = row[41],
            eccentricity_err1 = row[42],
            eccentricity_err2 = row[43],
            eccentricity_limit = row[44],
            insolation_flux = row[45],
            insolation_flux_err1 = row[46],
            insolation_flux_err2 = row[47],
            insolation_flux_limit = row[48],
            equilibrium_temperature = row[49],
            equilibrium_temperature_err1 = row[50],
            equilibrium_temperature_err2 = row[51],
            equilibrium_temperature_limit = row[52],
            transit_timing_variations = row[53],
            date_last_update = row[94],
            reference_date_publication = row[95],
            release_date = row[96],
            planetary_system = planetary_system,
            discovery_method = discovery_method,
            discovery_facility = discovery_facility,
            solution_type = solution_type
        )

        planet.save()