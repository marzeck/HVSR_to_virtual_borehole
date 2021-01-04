# http://pyrocko.org - GPLv3
#
# The Pyrocko Developers, 21st Century
# ---|P------/S----------~Lg----------

# preliminary version of a siteXML package realized for the pyrocko package
# structure is taken from quakeML and stationxml

from pyrocko.guts import (StringChoice, String, Int, Float, List, Object)

guts_xmlns = 'https://quake.ethz.ch/quakeml/QuakeML2.0'


class SiteXMLError(Exception):
    pass


class ValueInt(Object):
    value = Int.T()


class ValueDouble(Object):
    value = Float.T()


class QIndex(Object):
    """
    Quality index as defined in SERA D7.2
    range from 0 to 1.
    """
    value = Float.T()


class QuantitySet(Object):
    value = Float.T()
    uncertainty = Float.T(optional=True)


class QuantityUnset(Object):
    value = Float.T(optional=True)
    uncertainty = Float.T(optional=True)


class Language(StringChoice):
    xmltagname = 'code'
    choices = ['EN']


class LiteratureSource(Object):
    title = String.T()
    first_author = String.T(xmltagname='firstAuthor')
    secondary_authors = List.T(String.T(), xmltagname='secondaryAuthors')
    year = String.T()
    booktitle = String.T()
    language = Language.T()
    doi = String.T(xmltagname='DOI')


class FileResource(Object):
    description = String.T()
    url = List.T(String.T())


class Reference(Object):
    literature_source = LiteratureSource.T(xmltagname='literatureSource')
    file_resource = FileResource.T(xmltagname='FileResource')


class SiteTopology(Object):
    """or respective code, e.g., B2"""
    scheme_A = String.T(xmltagname='schemeA',
                        help='This is not included in 2.0')
    scheme_B = String.T(xmltagname='schemeB')


class SiteMorphology(Object):
    site_class_ec8 = String.T(optional=True,
                              xmltagname='siteClassEC8')
    site_class_ec8_q_index_1 = QIndex.T(optional=True,
                                        xmltagname='siteClassEC8Qindex1')
    site_class_ec8_reference = Reference.T(optional=True,
                                           xmltagname='siteClassEC8Reference')
    bedrock_depth = QuantityUnset.T(optional=True,
                                    xmltagname='bedrockDepth',
                                    help='Depth value in m')
    bedrock_depth_q_index_1 = QIndex.T(optional=True,
                                       xmltagname='bedrockDepthQindex1')
    bedrock_depth_reference = Reference.T(optional=True,
                                          xltagname='bedrockDepthReference')
    h800 = QuantityUnset.T(optional=True,
                           help='engineering bedrock depth value in m \nThis is not included in the 2.0 draft')
    h800_q_index_1 = QIndex.T(optional=True,
                              xmltagname='h800Qindex1')
    h800_reference = Reference.T(optional=True,
                                 xmltagname='h800Reference')
    geological_unit = String.T(optional=True,
                               xmltagname='geologicalUnit')
    geological_unit_q_index_1 = QIndex.T(optional=True,
                                         xmltagname='geologicalUnitQindex1')
    geological_map_scale = String.T(optional=True,
                                    xmltagname='geologicalMapScale')
    geological_unit_o_g_e = String.T(xmltagname='geologicalUnitOGE')
    geological_unit_reference = Reference.T(optional=True,
                                            xmltagname='geologicalUnitReference')
    morphology = String.T(help='This in not included in 2.0 draft')


class Layer(Object):
    layer_top_depth = QuantityUnset.T(optional=True,
                                      xmltagname='layerTopDepth',
                                      help='Depth value in m')
    layer_bottom_depth = QuantityUnset.T(optional=True,
                                         xmltagname='layerBottomDepth',
                                         help='Depth value in m')


class VelocityProfileData(Object):
    density = QuantitySet.T(optional=True,
                            help='Density value in kg/m^3')
    velocity_p = QuantityUnset.T(optional=True,
                                 xmltagname='velocityP',
                                 help='P-wave velocity value in m/s')
    velocity_s = QuantityUnset.T(optional=True,
                                 xmltagname='velocityS',
                                 help='S-wave velocity value in m/s')
    layer_thickness = Layer.T(optional=True,
                              xmltagname='layerThickness')


class VelocityProfile(Object):
    layer_count = ValueInt.T(optional=True,
                             xmltagname='layerCount')
    velocity_profile_data = List.T(VelocityProfileData.T(), xmltagname='velocityProfileData')


class SiteDescription(Object):
    latitude = ValueDouble.T(optional=True,
                             xmltagname='latitude')
    longitude = ValueDouble.T(optional=True,
                              xmltagname='longitude')
    altitude = ValueDouble.T(optional=True,
                             xmltagname='altitude')
    min_dist_from_station = ValueDouble.T(optional=True,
                                          xmltagname='minDistanceFromStation',
                                          help='Distance value in m \nprovide only if lat and lon not given.')
    max_dist_from_station = ValueDouble.T(optional=True,
                                          xmltagname='maxDistanceFromStation',
                                          help='Distance value in m \nprovide only if lat and lon not given.')
    site_morphology = SiteMorphology.T(xmltagname='siteMorphology')
    site_topology = SiteTopology.T(xmltagname='siteTopology')
    overall_q_index = QIndex.T(optional=True,
                               xmltagname='OverallQindex')


class Analysis(Object):
    public_id = String.T(xmlstyle='attribute',
                         xmltagname='publicID')
    resonance_frequency = QuantityUnset.T(optional=True,
                                          xmltagname='resonanceFrequency',
                                          help='Frequency value in Hz')
    resonance_frequency_q_index_1 = QIndex.T(optional=True,
                                             xmltagname='resonanceFrequencyQindex1')
    resonance_frequency_method = List.T(String.T(), xmltagname='resonanceFrequencyMethod')
    resonance_frequency_Reference = Reference.T(optional=True,
                                                xmltagname='resonanceFrequencyReference')
    vs30 = QuantityUnset.T(optional=True,
                           xmltagname='velocityS30',
                           help='Velocity value in m/s \nuncertainty as standard deviation')
    vs30_q_index_1 = QIndex.T(optional=True,
                              xmltagname='velocityS30Qindex1')
    vs30_method = List.T(String.T(), xmltagname='velocityS30Method')
    vs30_method_comb_index = String.T(optional=True,
                                      xmltagname='velocityS30MethodCombIndex')
    vs30_manual_index = String.T(optional=True,
                                 xmltagname='velocityS30ManualIndex')
    vs30_reference = Reference.T(optional=True,
                                 xmltagname='velocityS30Reference')
    velocity_profile_count = ValueInt.T(optional=True,
                                        xmltagname='velocityProfileCount')
    spt_logs_count = ValueInt.T(optional=True,
                                xmltagname='sptLogsCount')
    cpt_logs_count = ValueInt.T(optional=True,
                                xmltagname='cptLogsCount')
    borehole_logs_count = ValueInt.T(optional=True,
                                     xmltagname='boreholeLogsCount')


class SiteCharacterizationParameter(Object):
    public_id = String.T(
        xmlstyle='attribute', xmltagname='publicID')
    analysis = Analysis.T()
    velocity_profile = List.T(VelocityProfile.T(), xmltagname='VelocityProfile')
    velocity_profile_q_index_1 = QIndex.T(optional=True,
                                          xmltagname='velocityProfileQindex1')
    velocity_profile_reference = Reference.T(optional=True,
                                             xmltagname='velocityProfileReference')


class Country(Object):
    code = String.T()
    country = String.T()


class PostalAddres(Object):
    street_address = String.T(xmltagname='streetAddress')
    locality = String.T()
    postal_code = String.T(xmltagname='postalCode')
    country = Country.T()


class Institution(Object):
    identifier = List.T(String.T(), xmltagname='resourceID')
    name = String.T()
    mbox = String.T()
    phone = String.T()
    homepage = String.T()
    postal_address = PostalAddres.T(xmltagname='postalAddress')


class Affiliation(Object):
    institution = Institution.T()
    department = String.T()
    function = String.T()


class Person(Object):
    person_id = String.T(
        xmlstyle='attribute', xmltagname='personID')
    firstname = String.T()
    lastname = String.T()
    mbox = String.T()
    homepage = String.T()


class Contact(Object):
    public_id = String.T(
        xmlstyle='attribute', xmltagname='publicID')
    person = Person.T()
    affiliation = Affiliation.T()


class SiteOwner(Object):
    public_id = String.T(
        xmlstyle='attribute', xmltagname='publicID')
    code_name = String.T(xmltagname='codeName')
    full_name = String.T(xmltagname='fullName')
    contact = Contact.T()


class SiteXML(Object):
    xmlns = 'https://quake.ethz.ch/quakeml/QuakeML2.0'
    guessable_xmlns = [xmlns, guts_xmlns]

    site_owner = SiteOwner.T()
    site_characterization_parameters = SiteCharacterizationParameter.T(xmltagname='siteCharacterizationParameters')
    site_description = SiteDescription.T()
