#!/usr/bin/env python

#
# Generated Tue Dec  8 11:58:58 2020 by generateDS.py version 2.37.7.
# Python 3.8.5 (default, Jul 28 2020, 12:59:40)  [GCC 9.3.0]
#
# Command line options:
#   ('-o', 'siteXML.py')
#   ('-s', 'siteXMLsubs.py')
#
# Command line arguments:
#   /home/martin/Documents/ROB/Station-analyses/scripts/site-characterization-scheme/schema/QuakeML-SERA-1.2.xsd
#
# Command line:
#   /home/martin/.local/bin/generateDS -o "siteXML.py" -s "siteXMLsubs.py" /home/martin/Documents/ROB/Station-analyses/scripts/site-characterization-scheme/schema/QuakeML-SERA-1.2.xsd
#
# Current working directory (os.getcwd()):
#   HVSR_to_virtual_borehole
#

import os
import sys
from lxml import etree as etree_

import ??? as supermod

def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        parser = etree_.ETCompatXMLParser()
    try:
        if isinstance(infile, os.PathLike):
            infile = os.path.join(infile)
    except AttributeError:
        pass
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc

def parsexmlstring_(instring, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    element = etree_.fromstring(instring, parser=parser, **kwargs)
    return element

#
# Globals
#

ExternalEncoding = ''
SaveElementTreeNode = True

#
# Data representation classes
#


class SERA_quakemlSub(supermod.SERA_quakeml):
    def __init__(self, siteOwner=None, siteCharacterizationParameters=None, siteDescription=None, **kwargs_):
        super(SERA_quakemlSub, self).__init__(siteOwner, siteCharacterizationParameters, siteDescription,  **kwargs_)
supermod.SERA_quakeml.subclass = SERA_quakemlSub
# end class SERA_quakemlSub


class siteOwnerTypeSub(supermod.siteOwnerType):
    def __init__(self, publicID=None, codeName=None, fullName=None, contact=None, **kwargs_):
        super(siteOwnerTypeSub, self).__init__(publicID, codeName, fullName, contact,  **kwargs_)
supermod.siteOwnerType.subclass = siteOwnerTypeSub
# end class siteOwnerTypeSub


class contactTypeSub(supermod.contactType):
    def __init__(self, person=None, affiliation=None, **kwargs_):
        super(contactTypeSub, self).__init__(person, affiliation,  **kwargs_)
supermod.contactType.subclass = contactTypeSub
# end class contactTypeSub


class personTypeSub(supermod.personType):
    def __init__(self, personID=None, firstname=None, lastname=None, mbox=None, homepage=None, **kwargs_):
        super(personTypeSub, self).__init__(personID, firstname, lastname, mbox, homepage,  **kwargs_)
supermod.personType.subclass = personTypeSub
# end class personTypeSub


class affiliationTypeSub(supermod.affiliationType):
    def __init__(self, institution=None, department=None, function=None, **kwargs_):
        super(affiliationTypeSub, self).__init__(institution, department, function,  **kwargs_)
supermod.affiliationType.subclass = affiliationTypeSub
# end class affiliationTypeSub


class institutionTypeSub(supermod.institutionType):
    def __init__(self, identifier=None, name=None, mbox=None, phone=None, homepage=None, postalAddress=None, **kwargs_):
        super(institutionTypeSub, self).__init__(identifier, name, mbox, phone, homepage, postalAddress,  **kwargs_)
supermod.institutionType.subclass = institutionTypeSub
# end class institutionTypeSub


class identifierTypeSub(supermod.identifierType):
    def __init__(self, resourceID=None, **kwargs_):
        super(identifierTypeSub, self).__init__(resourceID,  **kwargs_)
supermod.identifierType.subclass = identifierTypeSub
# end class identifierTypeSub


class postalAddressTypeSub(supermod.postalAddressType):
    def __init__(self, streetAddress=None, locality=None, postalCode=None, country=None, **kwargs_):
        super(postalAddressTypeSub, self).__init__(streetAddress, locality, postalCode, country,  **kwargs_)
supermod.postalAddressType.subclass = postalAddressTypeSub
# end class postalAddressTypeSub


class countryTypeSub(supermod.countryType):
    def __init__(self, code=None, country=None, **kwargs_):
        super(countryTypeSub, self).__init__(code, country,  **kwargs_)
supermod.countryType.subclass = countryTypeSub
# end class countryTypeSub


class siteCharacterizationParametersTypeSub(supermod.siteCharacterizationParametersType):
    def __init__(self, publicID=None, Analysis=None, VelocityProfile=None, velocityProfileQindex1=None, velocityProfileReference=None, **kwargs_):
        super(siteCharacterizationParametersTypeSub, self).__init__(publicID, Analysis, VelocityProfile, velocityProfileQindex1, velocityProfileReference,  **kwargs_)
supermod.siteCharacterizationParametersType.subclass = siteCharacterizationParametersTypeSub
# end class siteCharacterizationParametersTypeSub


class AnalysisTypeSub(supermod.AnalysisType):
    def __init__(self, publicID=None, resonanceFrequency=None, resonanceFrequencyQindex1=None, resonanceFrequencyMethod=None, resonanceFrequencyReference=None, velocityS30=None, velocityS30Qindex1=None, velocityS30Method=None, velocityS30MethodCombIndex=None, velocityS30ManualIndex=None, velocityS30Reference=None, velocityProfileCount=None, sptLogsCount=None, cptLogsCount=None, boreholeLogsCount=None, valueOf_=None, mixedclass_=None, content_=None, **kwargs_):
        super(AnalysisTypeSub, self).__init__(publicID, resonanceFrequency, resonanceFrequencyQindex1, resonanceFrequencyMethod, resonanceFrequencyReference, velocityS30, velocityS30Qindex1, velocityS30Method, velocityS30MethodCombIndex, velocityS30ManualIndex, velocityS30Reference, velocityProfileCount, sptLogsCount, cptLogsCount, boreholeLogsCount, valueOf_, mixedclass_, content_,  **kwargs_)
supermod.AnalysisType.subclass = AnalysisTypeSub
# end class AnalysisTypeSub


class resonanceFrequencyTypeSub(supermod.resonanceFrequencyType):
    def __init__(self, value=None, uncertainty=None, **kwargs_):
        super(resonanceFrequencyTypeSub, self).__init__(value, uncertainty,  **kwargs_)
supermod.resonanceFrequencyType.subclass = resonanceFrequencyTypeSub
# end class resonanceFrequencyTypeSub


class resonanceFrequencyQindex1TypeSub(supermod.resonanceFrequencyQindex1Type):
    def __init__(self, value=None, **kwargs_):
        super(resonanceFrequencyQindex1TypeSub, self).__init__(value,  **kwargs_)
supermod.resonanceFrequencyQindex1Type.subclass = resonanceFrequencyQindex1TypeSub
# end class resonanceFrequencyQindex1TypeSub


class resonanceFrequencyReferenceTypeSub(supermod.resonanceFrequencyReferenceType):
    def __init__(self, literatureSource=None, FileResource=None, **kwargs_):
        super(resonanceFrequencyReferenceTypeSub, self).__init__(literatureSource, FileResource,  **kwargs_)
supermod.resonanceFrequencyReferenceType.subclass = resonanceFrequencyReferenceTypeSub
# end class resonanceFrequencyReferenceTypeSub


class literatureSourceTypeSub(supermod.literatureSourceType):
    def __init__(self, title=None, firstAuthor=None, secondaryAuthors=None, year=None, booktitle=None, language=None, DOI=None, **kwargs_):
        super(literatureSourceTypeSub, self).__init__(title, firstAuthor, secondaryAuthors, year, booktitle, language, DOI,  **kwargs_)
supermod.literatureSourceType.subclass = literatureSourceTypeSub
# end class literatureSourceTypeSub


class languageTypeSub(supermod.languageType):
    def __init__(self, code=None, **kwargs_):
        super(languageTypeSub, self).__init__(code,  **kwargs_)
supermod.languageType.subclass = languageTypeSub
# end class languageTypeSub


class FileResourceTypeSub(supermod.FileResourceType):
    def __init__(self, description=None, url=None, **kwargs_):
        super(FileResourceTypeSub, self).__init__(description, url,  **kwargs_)
supermod.FileResourceType.subclass = FileResourceTypeSub
# end class FileResourceTypeSub


class velocityS30TypeSub(supermod.velocityS30Type):
    def __init__(self, value=None, uncertainty=None, **kwargs_):
        super(velocityS30TypeSub, self).__init__(value, uncertainty,  **kwargs_)
supermod.velocityS30Type.subclass = velocityS30TypeSub
# end class velocityS30TypeSub


class velocityS30Qindex1TypeSub(supermod.velocityS30Qindex1Type):
    def __init__(self, value=None, **kwargs_):
        super(velocityS30Qindex1TypeSub, self).__init__(value,  **kwargs_)
supermod.velocityS30Qindex1Type.subclass = velocityS30Qindex1TypeSub
# end class velocityS30Qindex1TypeSub


class velocityS30ReferenceTypeSub(supermod.velocityS30ReferenceType):
    def __init__(self, literatureSource=None, FileResource=None, **kwargs_):
        super(velocityS30ReferenceTypeSub, self).__init__(literatureSource, FileResource,  **kwargs_)
supermod.velocityS30ReferenceType.subclass = velocityS30ReferenceTypeSub
# end class velocityS30ReferenceTypeSub


class literatureSourceType1Sub(supermod.literatureSourceType1):
    def __init__(self, title=None, firstAuthor=None, secondaryAuthors=None, year=None, booktitle=None, language=None, DOI=None, **kwargs_):
        super(literatureSourceType1Sub, self).__init__(title, firstAuthor, secondaryAuthors, year, booktitle, language, DOI,  **kwargs_)
supermod.literatureSourceType1.subclass = literatureSourceType1Sub
# end class literatureSourceType1Sub


class languageType2Sub(supermod.languageType2):
    def __init__(self, code=None, **kwargs_):
        super(languageType2Sub, self).__init__(code,  **kwargs_)
supermod.languageType2.subclass = languageType2Sub
# end class languageType2Sub


class FileResourceType3Sub(supermod.FileResourceType3):
    def __init__(self, description=None, url=None, **kwargs_):
        super(FileResourceType3Sub, self).__init__(description, url,  **kwargs_)
supermod.FileResourceType3.subclass = FileResourceType3Sub
# end class FileResourceType3Sub


class velocityProfileCountTypeSub(supermod.velocityProfileCountType):
    def __init__(self, value=None, **kwargs_):
        super(velocityProfileCountTypeSub, self).__init__(value,  **kwargs_)
supermod.velocityProfileCountType.subclass = velocityProfileCountTypeSub
# end class velocityProfileCountTypeSub


class sptLogsCountTypeSub(supermod.sptLogsCountType):
    def __init__(self, value=None, **kwargs_):
        super(sptLogsCountTypeSub, self).__init__(value,  **kwargs_)
supermod.sptLogsCountType.subclass = sptLogsCountTypeSub
# end class sptLogsCountTypeSub


class cptLogsCountTypeSub(supermod.cptLogsCountType):
    def __init__(self, value=None, **kwargs_):
        super(cptLogsCountTypeSub, self).__init__(value,  **kwargs_)
supermod.cptLogsCountType.subclass = cptLogsCountTypeSub
# end class cptLogsCountTypeSub


class boreholeLogsCountTypeSub(supermod.boreholeLogsCountType):
    def __init__(self, value=None, **kwargs_):
        super(boreholeLogsCountTypeSub, self).__init__(value,  **kwargs_)
supermod.boreholeLogsCountType.subclass = boreholeLogsCountTypeSub
# end class boreholeLogsCountTypeSub


class VelocityProfileTypeSub(supermod.VelocityProfileType):
    def __init__(self, layerCount=None, velocityProfileData=None, **kwargs_):
        super(VelocityProfileTypeSub, self).__init__(layerCount, velocityProfileData,  **kwargs_)
supermod.VelocityProfileType.subclass = VelocityProfileTypeSub
# end class VelocityProfileTypeSub


class layerCountTypeSub(supermod.layerCountType):
    def __init__(self, value=None, **kwargs_):
        super(layerCountTypeSub, self).__init__(value,  **kwargs_)
supermod.layerCountType.subclass = layerCountTypeSub
# end class layerCountTypeSub


class velocityProfileDataTypeSub(supermod.velocityProfileDataType):
    def __init__(self, density=None, velocityP=None, velocityS=None, layerThickness=None, **kwargs_):
        super(velocityProfileDataTypeSub, self).__init__(density, velocityP, velocityS, layerThickness,  **kwargs_)
supermod.velocityProfileDataType.subclass = velocityProfileDataTypeSub
# end class velocityProfileDataTypeSub


class densityTypeSub(supermod.densityType):
    def __init__(self, value=None, uncertainty=None, **kwargs_):
        super(densityTypeSub, self).__init__(value, uncertainty,  **kwargs_)
supermod.densityType.subclass = densityTypeSub
# end class densityTypeSub


class velocityPTypeSub(supermod.velocityPType):
    def __init__(self, value=None, uncertainty=None, **kwargs_):
        super(velocityPTypeSub, self).__init__(value, uncertainty,  **kwargs_)
supermod.velocityPType.subclass = velocityPTypeSub
# end class velocityPTypeSub


class velocitySTypeSub(supermod.velocitySType):
    def __init__(self, value=None, uncertainty=None, **kwargs_):
        super(velocitySTypeSub, self).__init__(value, uncertainty,  **kwargs_)
supermod.velocitySType.subclass = velocitySTypeSub
# end class velocitySTypeSub


class layerThicknessTypeSub(supermod.layerThicknessType):
    def __init__(self, layerTopDepth=None, layerBottomDepth=None, **kwargs_):
        super(layerThicknessTypeSub, self).__init__(layerTopDepth, layerBottomDepth,  **kwargs_)
supermod.layerThicknessType.subclass = layerThicknessTypeSub
# end class layerThicknessTypeSub


class layerTopDepthTypeSub(supermod.layerTopDepthType):
    def __init__(self, value=None, uncertainty=None, **kwargs_):
        super(layerTopDepthTypeSub, self).__init__(value, uncertainty,  **kwargs_)
supermod.layerTopDepthType.subclass = layerTopDepthTypeSub
# end class layerTopDepthTypeSub


class layerBottomDepthTypeSub(supermod.layerBottomDepthType):
    def __init__(self, value=None, uncertainty=None, **kwargs_):
        super(layerBottomDepthTypeSub, self).__init__(value, uncertainty,  **kwargs_)
supermod.layerBottomDepthType.subclass = layerBottomDepthTypeSub
# end class layerBottomDepthTypeSub


class velocityProfileQindex1TypeSub(supermod.velocityProfileQindex1Type):
    def __init__(self, value=None, **kwargs_):
        super(velocityProfileQindex1TypeSub, self).__init__(value,  **kwargs_)
supermod.velocityProfileQindex1Type.subclass = velocityProfileQindex1TypeSub
# end class velocityProfileQindex1TypeSub


class velocityProfileReferenceTypeSub(supermod.velocityProfileReferenceType):
    def __init__(self, literatureSource=None, FileResource=None, **kwargs_):
        super(velocityProfileReferenceTypeSub, self).__init__(literatureSource, FileResource,  **kwargs_)
supermod.velocityProfileReferenceType.subclass = velocityProfileReferenceTypeSub
# end class velocityProfileReferenceTypeSub


class literatureSourceType4Sub(supermod.literatureSourceType4):
    def __init__(self, title=None, firstAuthor=None, secondaryAuthors=None, year=None, booktitle=None, language=None, DOI=None, **kwargs_):
        super(literatureSourceType4Sub, self).__init__(title, firstAuthor, secondaryAuthors, year, booktitle, language, DOI,  **kwargs_)
supermod.literatureSourceType4.subclass = literatureSourceType4Sub
# end class literatureSourceType4Sub


class languageType5Sub(supermod.languageType5):
    def __init__(self, code=None, **kwargs_):
        super(languageType5Sub, self).__init__(code,  **kwargs_)
supermod.languageType5.subclass = languageType5Sub
# end class languageType5Sub


class FileResourceType6Sub(supermod.FileResourceType6):
    def __init__(self, description=None, url=None, **kwargs_):
        super(FileResourceType6Sub, self).__init__(description, url,  **kwargs_)
supermod.FileResourceType6.subclass = FileResourceType6Sub
# end class FileResourceType6Sub


class siteDescriptionTypeSub(supermod.siteDescriptionType):
    def __init__(self, latitude=None, longitude=None, altitude=None, minDistanceFromStation=None, maxDistanceFromStation=None, siteMorphology=None, siteTopology=None, OverallQindex=None, **kwargs_):
        super(siteDescriptionTypeSub, self).__init__(latitude, longitude, altitude, minDistanceFromStation, maxDistanceFromStation, siteMorphology, siteTopology, OverallQindex,  **kwargs_)
supermod.siteDescriptionType.subclass = siteDescriptionTypeSub
# end class siteDescriptionTypeSub


class latitudeTypeSub(supermod.latitudeType):
    def __init__(self, value=None, **kwargs_):
        super(latitudeTypeSub, self).__init__(value,  **kwargs_)
supermod.latitudeType.subclass = latitudeTypeSub
# end class latitudeTypeSub


class longitudeTypeSub(supermod.longitudeType):
    def __init__(self, value=None, **kwargs_):
        super(longitudeTypeSub, self).__init__(value,  **kwargs_)
supermod.longitudeType.subclass = longitudeTypeSub
# end class longitudeTypeSub


class altitudeTypeSub(supermod.altitudeType):
    def __init__(self, value=None, **kwargs_):
        super(altitudeTypeSub, self).__init__(value,  **kwargs_)
supermod.altitudeType.subclass = altitudeTypeSub
# end class altitudeTypeSub


class minDistanceFromStationTypeSub(supermod.minDistanceFromStationType):
    def __init__(self, value=None, **kwargs_):
        super(minDistanceFromStationTypeSub, self).__init__(value,  **kwargs_)
supermod.minDistanceFromStationType.subclass = minDistanceFromStationTypeSub
# end class minDistanceFromStationTypeSub


class maxDistanceFromStationTypeSub(supermod.maxDistanceFromStationType):
    def __init__(self, value=None, **kwargs_):
        super(maxDistanceFromStationTypeSub, self).__init__(value,  **kwargs_)
supermod.maxDistanceFromStationType.subclass = maxDistanceFromStationTypeSub
# end class maxDistanceFromStationTypeSub


class siteMorphologyTypeSub(supermod.siteMorphologyType):
    def __init__(self, siteClassEC8=None, siteClassEC8Qindex1=None, siteClassEC8Reference=None, bedrockDepth=None, bedrockDepthQindex1=None, bedrockDepthReference=None, h800=None, h800Qindex1=None, h800Reference=None, geologicalUnit=None, geologicalUnitQindex1=None, geologicalMapScale=None, geologicalUnitOGE=None, geologicalUnitReference=None, morphology=None, **kwargs_):
        super(siteMorphologyTypeSub, self).__init__(siteClassEC8, siteClassEC8Qindex1, siteClassEC8Reference, bedrockDepth, bedrockDepthQindex1, bedrockDepthReference, h800, h800Qindex1, h800Reference, geologicalUnit, geologicalUnitQindex1, geologicalMapScale, geologicalUnitOGE, geologicalUnitReference, morphology,  **kwargs_)
supermod.siteMorphologyType.subclass = siteMorphologyTypeSub
# end class siteMorphologyTypeSub


class siteClassEC8Qindex1TypeSub(supermod.siteClassEC8Qindex1Type):
    def __init__(self, value=None, **kwargs_):
        super(siteClassEC8Qindex1TypeSub, self).__init__(value,  **kwargs_)
supermod.siteClassEC8Qindex1Type.subclass = siteClassEC8Qindex1TypeSub
# end class siteClassEC8Qindex1TypeSub


class siteClassEC8ReferenceTypeSub(supermod.siteClassEC8ReferenceType):
    def __init__(self, literatureSource=None, FileResource=None, **kwargs_):
        super(siteClassEC8ReferenceTypeSub, self).__init__(literatureSource, FileResource,  **kwargs_)
supermod.siteClassEC8ReferenceType.subclass = siteClassEC8ReferenceTypeSub
# end class siteClassEC8ReferenceTypeSub


class literatureSourceType7Sub(supermod.literatureSourceType7):
    def __init__(self, title=None, firstAuthor=None, secondaryAuthors=None, year=None, booktitle=None, language=None, DOI=None, **kwargs_):
        super(literatureSourceType7Sub, self).__init__(title, firstAuthor, secondaryAuthors, year, booktitle, language, DOI,  **kwargs_)
supermod.literatureSourceType7.subclass = literatureSourceType7Sub
# end class literatureSourceType7Sub


class languageType8Sub(supermod.languageType8):
    def __init__(self, code=None, **kwargs_):
        super(languageType8Sub, self).__init__(code,  **kwargs_)
supermod.languageType8.subclass = languageType8Sub
# end class languageType8Sub


class FileResourceType9Sub(supermod.FileResourceType9):
    def __init__(self, description=None, url=None, **kwargs_):
        super(FileResourceType9Sub, self).__init__(description, url,  **kwargs_)
supermod.FileResourceType9.subclass = FileResourceType9Sub
# end class FileResourceType9Sub


class bedrockDepthTypeSub(supermod.bedrockDepthType):
    def __init__(self, value=None, uncertainty=None, **kwargs_):
        super(bedrockDepthTypeSub, self).__init__(value, uncertainty,  **kwargs_)
supermod.bedrockDepthType.subclass = bedrockDepthTypeSub
# end class bedrockDepthTypeSub


class bedrockDepthQindex1TypeSub(supermod.bedrockDepthQindex1Type):
    def __init__(self, value=None, **kwargs_):
        super(bedrockDepthQindex1TypeSub, self).__init__(value,  **kwargs_)
supermod.bedrockDepthQindex1Type.subclass = bedrockDepthQindex1TypeSub
# end class bedrockDepthQindex1TypeSub


class bedrockDepthReferenceTypeSub(supermod.bedrockDepthReferenceType):
    def __init__(self, literatureSource=None, FileResource=None, **kwargs_):
        super(bedrockDepthReferenceTypeSub, self).__init__(literatureSource, FileResource,  **kwargs_)
supermod.bedrockDepthReferenceType.subclass = bedrockDepthReferenceTypeSub
# end class bedrockDepthReferenceTypeSub


class literatureSourceType10Sub(supermod.literatureSourceType10):
    def __init__(self, title=None, firstAuthor=None, secondaryAuthors=None, year=None, booktitle=None, language=None, DOI=None, **kwargs_):
        super(literatureSourceType10Sub, self).__init__(title, firstAuthor, secondaryAuthors, year, booktitle, language, DOI,  **kwargs_)
supermod.literatureSourceType10.subclass = literatureSourceType10Sub
# end class literatureSourceType10Sub


class languageType11Sub(supermod.languageType11):
    def __init__(self, code=None, **kwargs_):
        super(languageType11Sub, self).__init__(code,  **kwargs_)
supermod.languageType11.subclass = languageType11Sub
# end class languageType11Sub


class FileResourceType12Sub(supermod.FileResourceType12):
    def __init__(self, description=None, url=None, **kwargs_):
        super(FileResourceType12Sub, self).__init__(description, url,  **kwargs_)
supermod.FileResourceType12.subclass = FileResourceType12Sub
# end class FileResourceType12Sub


class h800TypeSub(supermod.h800Type):
    def __init__(self, value=None, uncertainty=None, **kwargs_):
        super(h800TypeSub, self).__init__(value, uncertainty,  **kwargs_)
supermod.h800Type.subclass = h800TypeSub
# end class h800TypeSub


class h800Qindex1TypeSub(supermod.h800Qindex1Type):
    def __init__(self, value=None, **kwargs_):
        super(h800Qindex1TypeSub, self).__init__(value,  **kwargs_)
supermod.h800Qindex1Type.subclass = h800Qindex1TypeSub
# end class h800Qindex1TypeSub


class h800ReferenceTypeSub(supermod.h800ReferenceType):
    def __init__(self, literatureSource=None, FileResource=None, **kwargs_):
        super(h800ReferenceTypeSub, self).__init__(literatureSource, FileResource,  **kwargs_)
supermod.h800ReferenceType.subclass = h800ReferenceTypeSub
# end class h800ReferenceTypeSub


class literatureSourceType13Sub(supermod.literatureSourceType13):
    def __init__(self, title=None, firstAuthor=None, secondaryAuthors=None, year=None, booktitle=None, language=None, DOI=None, **kwargs_):
        super(literatureSourceType13Sub, self).__init__(title, firstAuthor, secondaryAuthors, year, booktitle, language, DOI,  **kwargs_)
supermod.literatureSourceType13.subclass = literatureSourceType13Sub
# end class literatureSourceType13Sub


class languageType14Sub(supermod.languageType14):
    def __init__(self, code=None, **kwargs_):
        super(languageType14Sub, self).__init__(code,  **kwargs_)
supermod.languageType14.subclass = languageType14Sub
# end class languageType14Sub


class FileResourceType15Sub(supermod.FileResourceType15):
    def __init__(self, description=None, url=None, **kwargs_):
        super(FileResourceType15Sub, self).__init__(description, url,  **kwargs_)
supermod.FileResourceType15.subclass = FileResourceType15Sub
# end class FileResourceType15Sub


class geologicalUnitQindex1TypeSub(supermod.geologicalUnitQindex1Type):
    def __init__(self, value=None, **kwargs_):
        super(geologicalUnitQindex1TypeSub, self).__init__(value,  **kwargs_)
supermod.geologicalUnitQindex1Type.subclass = geologicalUnitQindex1TypeSub
# end class geologicalUnitQindex1TypeSub


class geologicalUnitReferenceTypeSub(supermod.geologicalUnitReferenceType):
    def __init__(self, literatureSource=None, FileResource=None, **kwargs_):
        super(geologicalUnitReferenceTypeSub, self).__init__(literatureSource, FileResource,  **kwargs_)
supermod.geologicalUnitReferenceType.subclass = geologicalUnitReferenceTypeSub
# end class geologicalUnitReferenceTypeSub


class literatureSourceType16Sub(supermod.literatureSourceType16):
    def __init__(self, title=None, firstAuthor=None, secondaryAuthors=None, year=None, booktitle=None, language=None, DOI=None, **kwargs_):
        super(literatureSourceType16Sub, self).__init__(title, firstAuthor, secondaryAuthors, year, booktitle, language, DOI,  **kwargs_)
supermod.literatureSourceType16.subclass = literatureSourceType16Sub
# end class literatureSourceType16Sub


class languageType17Sub(supermod.languageType17):
    def __init__(self, code=None, **kwargs_):
        super(languageType17Sub, self).__init__(code,  **kwargs_)
supermod.languageType17.subclass = languageType17Sub
# end class languageType17Sub


class FileResourceType18Sub(supermod.FileResourceType18):
    def __init__(self, description=None, url=None, **kwargs_):
        super(FileResourceType18Sub, self).__init__(description, url,  **kwargs_)
supermod.FileResourceType18.subclass = FileResourceType18Sub
# end class FileResourceType18Sub


class siteTopologyTypeSub(supermod.siteTopologyType):
    def __init__(self, schemeA=None, schemeB=None, **kwargs_):
        super(siteTopologyTypeSub, self).__init__(schemeA, schemeB,  **kwargs_)
supermod.siteTopologyType.subclass = siteTopologyTypeSub
# end class siteTopologyTypeSub


class OverallQindexTypeSub(supermod.OverallQindexType):
    def __init__(self, value=None, **kwargs_):
        super(OverallQindexTypeSub, self).__init__(value,  **kwargs_)
supermod.OverallQindexType.subclass = OverallQindexTypeSub
# end class OverallQindexTypeSub


def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    rootClass = supermod.GDSClassesMapping.get(tag)
    if rootClass is None and hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'SERA_quakeml'
        rootClass = supermod.SERA_quakeml
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='',
            pretty_print=True)
    return rootObj


def parseEtree(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'SERA_quakeml'
        rootClass = supermod.SERA_quakeml
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    mapping = {}
    rootElement = rootObj.to_etree(None, name_=rootTag, mapping_=mapping)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(content)
        sys.stdout.write('\n')
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False):
    if sys.version_info.major == 2:
        from StringIO import StringIO
    else:
        from io import BytesIO as StringIO
    parser = None
    rootNode= parsexmlstring_(inString, parser)
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'SERA_quakeml'
        rootClass = supermod.SERA_quakeml
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='')
    return rootObj


def parseLiteral(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'SERA_quakeml'
        rootClass = supermod.SERA_quakeml
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('#from ??? import *\n\n')
        sys.stdout.write('import ??? as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    return rootObj


USAGE_TEXT = """
Usage: python ???.py <infilename>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    parse(infilename)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()
