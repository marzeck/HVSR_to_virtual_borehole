#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
# Current working directory (os.getcwd()):siteCharacterizationParameter
#   HVSR_to_virtual_borehole
#

import sys

try:
    ModulenotfoundExp_ = ModuleNotFoundError
except NameError:
    ModulenotfoundExp_ = ImportError
from six.moves import zip_longest
import os
import re as re_
import base64
import datetime as datetime_
import decimal as decimal_

try:
    from lxml import etree as etree_
except ModulenotfoundExp_:
    from xml.etree import ElementTree as etree_

Validate_simpletypes_ = True
SaveElementTreeNode = True
if sys.version_info.major == 2:
    BaseStrType_ = basestring
else:
    BaseStrType_ = str

try:
    unicode
except NameError:
    unicode = str

def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
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
# Namespace prefix definition table (and other attributes, too)
#
# The module generatedsnamespaces, if it is importable, must contain
# a dictionary named GeneratedsNamespaceDefs.  This Python dictionary
# should map element type names (strings) to XML schema namespace prefix
# definitions.  The export method for any class for which there is
# a namespace prefix definition, will export that definition in the
# XML representation of that element.  See the export method of
# any generated element type class for an example of the use of this
# table.
# A sample table is:
#
#     # File: generatedsnamespaces.py
#
#     GenerateDSNamespaceDefs = {
#         "ElementtypeA": "http://www.xxx.com/namespaceA",
#         "ElementtypeB": "http://www.xxx.com/namespaceB",
#     }
#
# Additionally, the generatedsnamespaces module can contain a python
# dictionary named GenerateDSNamespaceTypePrefixes that associates element
# types with the namespace prefixes that are to be added to the
# "xsi:type" attribute value.  See the exportAttributes method of
# any generated element type and the generation of "xsi:type" for an
# example of the use of this table.
# An example table:
#
#     # File: generatedsnamespaces.py
#
#     GenerateDSNamespaceTypePrefixes = {
#         "ElementtypeC": "aaa:",
#         "ElementtypeD": "bbb:",
#     }
#

try:
    from generatedsnamespaces import GenerateDSNamespaceDefs as GenerateDSNamespaceDefs_
except ModulenotfoundExp_:
    GenerateDSNamespaceDefs_ = {}
try:
    from generatedsnamespaces import GenerateDSNamespaceTypePrefixes as GenerateDSNamespaceTypePrefixes_
except ModulenotfoundExp_:
    GenerateDSNamespaceTypePrefixes_ = {}

#
# You can replace the following class definition by defining an
# importable module named "generatedscollector" containing a class
# named "GdsCollector".  See the default class definition below for
# clues about the possible content of that class.
#
try:
    from generatedscollector import GdsCollector as GdsCollector_
except ModulenotfoundExp_:

    class GdsCollector_(object):

        def __init__(self, messages=None):
            if messages is None:
                self.messages = []
            else:
                self.messages = messages

        def add_message(self, msg):
            self.messages.append(msg)

        def get_messages(self):
            return self.messages

        def clear_messages(self):
            self.messages = []

        def print_messages(self):
            for msg in self.messages:
                print("Warning: {}".format(msg))

        def write_messages(self, outstream):
            for msg in self.messages:
                outstream.write("Warning: {}\n".format(msg))

#
# The super-class for enum types
#

try:
    from enum import Enum
except ModulenotfoundExp_:
    Enum = object

#
# The root super-class for element type classes
#
# Calls to the methods in these classes are generated by generateDS.py.
# You can replace these methods by re-implementing the following class
#   in a module named generatedssuper.py.

try:
    from generatedssuper import GeneratedsSuper
except ModulenotfoundExp_ as exp:

    class GeneratedsSuper(object):
        __hash__ = object.__hash__
        tzoff_pattern = re_.compile(r'(\+|-)((0\d|1[0-3]):[0-5]\d|14:00)$')

        class _FixedOffsetTZ(datetime_.tzinfo):
            def __init__(self, offset, name):
                self.__offset = datetime_.timedelta(minutes=offset)
                self.__name = name

            def utcoffset(self, dt):
                return self.__offset

            def tzname(self, dt):
                return self.__name

            def dst(self, dt):
                return None

        def gds_format_string(self, input_data, input_name=''):
            return input_data

        def gds_parse_string(self, input_data, node=None, input_name=''):
            return input_data

        def gds_validate_string(self, input_data, node=None, input_name=''):
            if not input_data:
                return ''
            else:
                return input_data

        def gds_format_base64(self, input_data, input_name=''):
            return base64.b64encode(input_data)

        def gds_validate_base64(self, input_data, node=None, input_name=''):
            return input_data

        def gds_format_integer(self, input_data, input_name=''):
            return '%d' % input_data

        def gds_parse_integer(self, input_data, node=None, input_name=''):
            try:
                ival = int(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires integer value: %s' % exp)
            return ival

        def gds_validate_integer(self, input_data, node=None, input_name=''):
            try:
                value = int(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires integer value')
            return value

        def gds_format_integer_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)

        def gds_validate_integer_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    int(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of integer valuess')
            return values

        def gds_format_float(self, input_data, input_name=''):
            return ('%.15f' % input_data).rstrip('0')

        def gds_parse_float(self, input_data, node=None, input_name=''):
            try:
                fval_ = float(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires float or double value: %s' % exp)
            return fval_

        def gds_validate_float(self, input_data, node=None, input_name=''):
            try:
                value = float(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires float value')
            return value

        def gds_format_float_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)

        def gds_validate_float_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    float(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of float values')
            return values

        def gds_format_decimal(self, input_data, input_name=''):
            return_value = '%s' % input_data
            if '.' in return_value:
                return_value = return_value.rstrip('0')
                if return_value.endswith('.'):
                    return_value = return_value.rstrip('.')
            return return_value

        def gds_parse_decimal(self, input_data, node=None, input_name=''):
            try:
                decimal_value = decimal_.Decimal(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires decimal value')
            return decimal_value

        def gds_validate_decimal(self, input_data, node=None, input_name=''):
            try:
                value = decimal_.Decimal(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires decimal value')
            return value

        def gds_format_decimal_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return ' '.join([self.gds_format_decimal(item) for item in input_data])

        def gds_validate_decimal_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    decimal_.Decimal(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of decimal values')
            return values

        def gds_format_double(self, input_data, input_name=''):
            return '%e' % input_data

        def gds_parse_double(self, input_data, node=None, input_name=''):
            try:
                fval_ = float(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires double or float value: %s' % exp)
            return fval_

        def gds_validate_double(self, input_data, node=None, input_name=''):
            try:
                value = float(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires double or float value')
            return value

        def gds_format_double_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)

        def gds_validate_double_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    float(value)
                except (TypeError, ValueError):
                    raise_parse_error(
                        node, 'Requires sequence of double or float values')
            return values

        def gds_format_boolean(self, input_data, input_name=''):
            return ('%s' % input_data).lower()

        def gds_parse_boolean(self, input_data, node=None, input_name=''):
            if input_data in ('true', '1'):
                bval = True
            elif input_data in ('false', '0'):
                bval = False
            else:
                raise_parse_error(node, 'Requires boolean value')
            return bval

        def gds_validate_boolean(self, input_data, node=None, input_name=''):
            if input_data not in (True, 1, False, 0,):
                raise_parse_error(
                    node,
                    'Requires boolean value '
                    '(one of True, 1, False, 0)')
            return input_data

        def gds_format_boolean_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)

        def gds_validate_boolean_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                if value not in (True, 1, False, 0,):
                    raise_parse_error(
                        node,
                        'Requires sequence of boolean values '
                        '(one of True, 1, False, 0)')
            return values

        def gds_validate_datetime(self, input_data, node=None, input_name=''):
            return input_data

        def gds_format_datetime(self, input_data, input_name=''):
            if input_data.microsecond == 0:
                _svalue = '%04d-%02d-%02dT%02d:%02d:%02d' % (
                    input_data.year,
                    input_data.month,
                    input_data.day,
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                )
            else:
                _svalue = '%04d-%02d-%02dT%02d:%02d:%02d.%s' % (
                    input_data.year,
                    input_data.month,
                    input_data.day,
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                    ('%f' % (float(input_data.microsecond) / 1000000))[2:],
                )
            if input_data.tzinfo is not None:
                tzoff = input_data.tzinfo.utcoffset(input_data)
                if tzoff is not None:
                    total_seconds = tzoff.seconds + (86400 * tzoff.days)
                    if total_seconds == 0:
                        _svalue += 'Z'
                    else:
                        if total_seconds < 0:
                            _svalue += '-'
                            total_seconds *= -1
                        else:
                            _svalue += '+'
                        hours = total_seconds // 3600
                        minutes = (total_seconds - (hours * 3600)) // 60
                        _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
            return _svalue

        @classmethod
        def gds_parse_datetime(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            time_parts = input_data.split('.')
            if len(time_parts) > 1:
                micro_seconds = int(float('0.' + time_parts[1]) * 1000000)
                input_data = '%s.%s' % (
                    time_parts[0], "{}".format(micro_seconds).rjust(6, "0"),)
                dt = datetime_.datetime.strptime(
                    input_data, '%Y-%m-%dT%H:%M:%S.%f')
            else:
                dt = datetime_.datetime.strptime(
                    input_data, '%Y-%m-%dT%H:%M:%S')
            dt = dt.replace(tzinfo=tz)
            return dt

        def gds_validate_date(self, input_data, node=None, input_name=''):
            return input_data

        def gds_format_date(self, input_data, input_name=''):
            _svalue = '%04d-%02d-%02d' % (
                input_data.year,
                input_data.month,
                input_data.day,
            )
            try:
                if input_data.tzinfo is not None:
                    tzoff = input_data.tzinfo.utcoffset(input_data)
                    if tzoff is not None:
                        total_seconds = tzoff.seconds + (86400 * tzoff.days)
                        if total_seconds == 0:
                            _svalue += 'Z'
                        else:
                            if total_seconds < 0:
                                _svalue += '-'
                                total_seconds *= -1
                            else:
                                _svalue += '+'
                            hours = total_seconds // 3600
                            minutes = (total_seconds - (hours * 3600)) // 60
                            _svalue += '{0:02d}:{1:02d}'.format(
                                hours, minutes)
            except AttributeError:
                pass
            return _svalue

        @classmethod
        def gds_parse_date(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            dt = datetime_.datetime.strptime(input_data, '%Y-%m-%d')
            dt = dt.replace(tzinfo=tz)
            return dt.date()

        def gds_validate_time(self, input_data, node=None, input_name=''):
            return input_data

        def gds_format_time(self, input_data, input_name=''):
            if input_data.microsecond == 0:
                _svalue = '%02d:%02d:%02d' % (
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                )
            else:
                _svalue = '%02d:%02d:%02d.%s' % (
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                    ('%f' % (float(input_data.microsecond) / 1000000))[2:],
                )
            if input_data.tzinfo is not None:
                tzoff = input_data.tzinfo.utcoffset(input_data)
                if tzoff is not None:
                    total_seconds = tzoff.seconds + (86400 * tzoff.days)
                    if total_seconds == 0:
                        _svalue += 'Z'
                    else:
                        if total_seconds < 0:
                            _svalue += '-'
                            total_seconds *= -1
                        else:
                            _svalue += '+'
                        hours = total_seconds // 3600
                        minutes = (total_seconds - (hours * 3600)) // 60
                        _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
            return _svalue

        def gds_validate_simple_patterns(self, patterns, target):
            # pat is a list of lists of strings/patterns.
            # The target value must match at least one of the patterns
            # in order for the test to succeed.
            found1 = True
            for patterns1 in patterns:
                found2 = False
                for patterns2 in patterns1:
                    mo = re_.search(patterns2, target)
                    if mo is not None and len(mo.group(0)) == len(target):
                        found2 = True
                        break
                if not found2:
                    found1 = False
                    break
            return found1

        @classmethod
        def gds_parse_time(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            if len(input_data.split('.')) > 1:
                dt = datetime_.datetime.strptime(input_data, '%H:%M:%S.%f')
            else:
                dt = datetime_.datetime.strptime(input_data, '%H:%M:%S')
            dt = dt.replace(tzinfo=tz)
            return dt.time()

        def gds_check_cardinality_(
                self, value, input_name,
                min_occurs=0, max_occurs=1, required=None):
            if value is None:
                length = 0
            elif isinstance(value, list):
                length = len(value)
            else:
                length = 1
            if required is not None:
                if required and length < 1:
                    self.gds_collector_.add_message(
                        "Required value {}{} is missing".format(
                            input_name, self.gds_get_node_lineno_()))
            if length < min_occurs:
                self.gds_collector_.add_message(
                    "Number of values for {}{} is below "
                    "the minimum allowed, "
                    "expected at least {}, found {}".format(
                        input_name, self.gds_get_node_lineno_(),
                        min_occurs, length))
            elif length > max_occurs:
                self.gds_collector_.add_message(
                    "Number of values for {}{} is above "
                    "the maximum allowed, "
                    "expected at most {}, found {}".format(
                        input_name, self.gds_get_node_lineno_(),
                        max_occurs, length))

        def gds_validate_builtin_ST_(
                self, validator, value, input_name,
                min_occurs=None, max_occurs=None, required=None):
            if value is not None:
                try:
                    validator(value, input_name=input_name)
                except GDSParseError as parse_error:
                    self.gds_collector_.add_message(str(parse_error))

        def gds_validate_defined_ST_(
                self, validator, value, input_name,
                min_occurs=None, max_occurs=None, required=None):
            if value is not None:
                try:
                    validator(value)
                except GDSParseError as parse_error:
                    self.gds_collector_.add_message(str(parse_error))

        def gds_str_lower(self, instring):
            return instring.lower()

        def get_path_(self, node):
            path_list = []
            self.get_path_list_(node, path_list)
            path_list.reverse()
            path = '/'.join(path_list)
            return path

        Tag_strip_pattern_ = re_.compile(r'\{.*\}')

        def get_path_list_(self, node, path_list):
            if node is None:
                return
            tag = GeneratedsSuper.Tag_strip_pattern_.sub('', node.tag)
            if tag:
                path_list.append(tag)
            self.get_path_list_(node.getparent(), path_list)

        def get_class_obj_(self, node, default_class=None):
            class_obj1 = default_class
            if 'xsi' in node.nsmap:
                classname = node.get('{%s}type' % node.nsmap['xsi'])
                if classname is not None:
                    names = classname.split(':')
                    if len(names) == 2:
                        classname = names[1]
                    class_obj2 = globals().get(classname)
                    if class_obj2 is not None:
                        class_obj1 = class_obj2
            return class_obj1

        def gds_build_any(self, node, type_name=None):
            # provide default value in case option --disable-xml is used.
            content = ""
            content = etree_.tostring(node, encoding="unicode")
            return content

        @classmethod
        def gds_reverse_node_mapping(cls, mapping):
            return dict(((v, k) for k, v in mapping.items()))

        @staticmethod
        def gds_encode(instring):
            if sys.version_info.major == 2:
                if ExternalEncoding:
                    encoding = ExternalEncoding
                else:
                    encoding = 'utf-8'
                return instring.encode(encoding)
            else:
                return instring

        @staticmethod
        def convert_unicode(instring):
            if isinstance(instring, str):
                result = quote_xml(instring)
            elif sys.version_info.major == 2 and isinstance(instring, unicode):
                result = quote_xml(instring).encode('utf8')
            else:
                result = GeneratedsSuper.gds_encode(str(instring))
            return result

        def __eq__(self, other):
            def excl_select_objs_(obj):
                return (obj[0] != 'parent_object_' and
                        obj[0] != 'gds_collector_')

            if type(self) != type(other):
                return False
            return all(x == y for x, y in zip_longest(
                filter(excl_select_objs_, self.__dict__.items()),
                filter(excl_select_objs_, other.__dict__.items())))

        def __ne__(self, other):
            return not self.__eq__(other)

        # Django ETL transform hooks.
        def gds_djo_etl_transform(self):
            pass

        def gds_djo_etl_transform_db_obj(self, dbobj):
            pass

        # SQLAlchemy ETL transform hooks.
        def gds_sqa_etl_transform(self):
            return 0, None

        def gds_sqa_etl_transform_db_obj(self, dbobj):
            pass

        def gds_get_node_lineno_(self):
            if (hasattr(self, "gds_elementtree_node_") and
                    self.gds_elementtree_node_ is not None):
                return ' near line {}'.format(
                    self.gds_elementtree_node_.sourceline)
            else:
                return ""


    def getSubclassFromModule_(module, class_):
        '''Get the subclass of a class from a specific module.'''
        name = class_.__name__ + 'Sub'
        if hasattr(module, name):
            return getattr(module, name)
        else:
            return None

#
# If you have installed IPython you can uncomment and use the following.
# IPython is available from http://ipython.scipy.org/.
#

## from IPython.Shell import IPShellEmbed
## args = ''
## ipshell = IPShellEmbed(args,
##     banner = 'Dropping into IPython',
##     exit_msg = 'Leaving Interpreter, back to program.')

# Then use the following line where and when you want to drop into the
# IPython shell:
#    ipshell('<some message> -- Entering ipshell.\nHit Ctrl-D to exit')

#
# Globals
#

ExternalEncoding = ''
# Set this to false in order to deactivate during export, the use of
# name space prefixes captured from the input document.
UseCapturedNS_ = True
CapturedNsmap_ = {}
Tag_pattern_ = re_.compile(r'({.*})?(.*)')
String_cleanup_pat_ = re_.compile(r"[\n\r\s]+")
Namespace_extract_pat_ = re_.compile(r'{(.*)}(.*)')
CDATA_pattern_ = re_.compile(r"<!\[CDATA\[.*?\]\]>", re_.DOTALL)

# Change this to redirect the generated superclass module to use a
# specific subclass module.
CurrentSubclassModule_ = None


#
# Support/utility functions.
#


def showIndent(outfile, level, pretty_print=True):
    if pretty_print:
        for idx in range(level):
            outfile.write('    ')


def quote_xml(inStr):
    "Escape markup chars, but do not modify CDATA sections."
    if not inStr:
        return ''
    s1 = (isinstance(inStr, BaseStrType_) and inStr or '%s' % inStr)
    s2 = ''
    pos = 0
    matchobjects = CDATA_pattern_.finditer(s1)
    for mo in matchobjects:
        s3 = s1[pos:mo.start()]
        s2 += quote_xml_aux(s3)
        s2 += s1[mo.start():mo.end()]
        pos = mo.end()
    s3 = s1[pos:]
    s2 += quote_xml_aux(s3)
    return s2


def quote_xml_aux(inStr):
    s1 = inStr.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    return s1


def quote_attrib(inStr):
    s1 = (isinstance(inStr, BaseStrType_) and inStr or '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    if '"' in s1:
        if "'" in s1:
            s1 = '"%s"' % s1.replace('"', "&quot;")
        else:
            s1 = "'%s'" % s1
    else:
        s1 = '"%s"' % s1
    return s1


def quote_python(inStr):
    s1 = inStr
    if s1.find("'") == -1:
        if s1.find('\n') == -1:
            return "'%s'" % s1
        else:
            return "'''%s'''" % s1
    else:
        if s1.find('"') != -1:
            s1 = s1.replace('"', '\\"')
        if s1.find('\n') == -1:
            return '"%s"' % s1
        else:
            return '"""%s"""' % s1


def get_all_text_(node):
    if node.text is not None:
        text = node.text
    else:
        text = ''
    for child in node:
        if child.tail is not None:
            text += child.tail
    return text


def find_attr_value_(attr_name, node):
    attrs = node.attrib
    attr_parts = attr_name.split(':')
    value = None
    if len(attr_parts) == 1:
        value = attrs.get(attr_name)
    elif len(attr_parts) == 2:
        prefix, name = attr_parts
        namespace = node.nsmap.get(prefix)
        if namespace is not None:
            value = attrs.get('{%s}%s' % (namespace, name,))
    return value


def encode_str_2_3(instr):
    return instr


class GDSParseError(Exception):
    pass


def raise_parse_error(node, msg):
    if node is not None:
        msg = '%s (element %s/line %d)' % (msg, node.tag, node.sourceline,)
    raise GDSParseError(msg)


class MixedContainer:
    # Constants for category:
    CategoryNone = 0
    CategoryText = 1
    CategorySimple = 2
    CategoryComplex = 3
    # Constants for content_type:
    TypeNone = 0
    TypeText = 1
    TypeString = 2
    TypeInteger = 3
    TypeFloat = 4
    TypeDecimal = 5
    TypeDouble = 6
    TypeBoolean = 7
    TypeBase64 = 8

    def __init__(self, category, content_type, name, value):
        self.category = category
        self.content_type = content_type
        self.name = name
        self.value = value

    def getCategory(self):
        return self.category

    def getContenttype(self, content_type):
        return self.content_type

    def getValue(self):
        return self.value

    def getName(self):
        return self.name

    def export(self, outfile, level, name, namespace,
               pretty_print=True):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip():
                outfile.write(self.value)
        elif self.category == MixedContainer.CategorySimple:
            self.exportSimple(outfile, level, name)
        else:  # category == MixedContainer.CategoryComplex
            self.value.export(
                outfile, level, namespace, name_=name,
                pretty_print=pretty_print)

    def exportSimple(self, outfile, level, name):
        if self.content_type == MixedContainer.TypeString:
            outfile.write('<%s>%s</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeInteger or \
                self.content_type == MixedContainer.TypeBoolean:
            outfile.write('<%s>%d</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeFloat or \
                self.content_type == MixedContainer.TypeDecimal:
            outfile.write('<%s>%f</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeDouble:
            outfile.write('<%s>%g</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeBase64:
            outfile.write('<%s>%s</%s>' % (
                self.name,
                base64.b64encode(self.value),
                self.name))

    def to_etree(self, element, mapping_=None, nsmap_=None):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip():
                if len(element) > 0:
                    if element[-1].tail is None:
                        element[-1].tail = self.value
                    else:
                        element[-1].tail += self.value
                else:
                    if element.text is None:
                        element.text = self.value
                    else:
                        element.text += self.value
        elif self.category == MixedContainer.CategorySimple:
            subelement = etree_.SubElement(
                element, '%s' % self.name)
            subelement.text = self.to_etree_simple()
        else:  # category == MixedContainer.CategoryComplex
            self.value.to_etree(element)

    def to_etree_simple(self, mapping_=None, nsmap_=None):
        if self.content_type == MixedContainer.TypeString:
            text = self.value
        elif (self.content_type == MixedContainer.TypeInteger or
              self.content_type == MixedContainer.TypeBoolean):
            text = '%d' % self.value
        elif (self.content_type == MixedContainer.TypeFloat or
              self.content_type == MixedContainer.TypeDecimal):
            text = '%f' % self.value
        elif self.content_type == MixedContainer.TypeDouble:
            text = '%g' % self.value
        elif self.content_type == MixedContainer.TypeBase64:
            text = '%s' % base64.b64encode(self.value)
        return text

    def exportLiteral(self, outfile, level, name):
        if self.category == MixedContainer.CategoryText:
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s", "%s"),\n' % (
                    self.category, self.content_type,
                    self.name, self.value))
        elif self.category == MixedContainer.CategorySimple:
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s", "%s"),\n' % (
                    self.category, self.content_type,
                    self.name, self.value))
        else:  # category == MixedContainer.CategoryComplex
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s",\n' % (
                    self.category, self.content_type, self.name,))
            self.value.exportLiteral(outfile, level + 1)
            showIndent(outfile, level)
            outfile.write(')\n')


class MemberSpec_(object):
    def __init__(self, name='', data_type='', container=0,
                 optional=0, child_attrs=None, choice=None):
        self.name = name
        self.data_type = data_type
        self.container = container
        self.child_attrs = child_attrs
        self.choice = choice
        self.optional = optional

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_data_type(self, data_type):
        self.data_type = data_type

    def get_data_type_chain(self):
        return self.data_type

    def get_data_type(self):
        if isinstance(self.data_type, list):
            if len(self.data_type) > 0:
                return self.data_type[-1]
            else:
                return 'xs:string'
        else:
            return self.data_type

    def set_container(self, container):
        self.container = container

    def get_container(self):
        return self.container

    def set_child_attrs(self, child_attrs):
        self.child_attrs = child_attrs

    def get_child_attrs(self):
        return self.child_attrs

    def set_choice(self, choice):
        self.choice = choice

    def get_choice(self):
        return self.choice

    def set_optional(self, optional):
        self.optional = optional

    def get_optional(self):
        return self.optional


def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)


#
# Data representation classes.
#


class SERA_quakeml(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, siteOwner=None, siteCharacterizationParameters=None, siteDescription=None, gds_collector_=None,
                 **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.siteOwner = siteOwner
        self.siteOwner_nsprefix_ = None
        self.siteCharacterizationParameters = siteCharacterizationParameters
        self.siteCharacterizationParameters_nsprefix_ = None
        self.siteDescription = siteDescription
        self.siteDescription_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SERA_quakeml)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SERA_quakeml.subclass:
            return SERA_quakeml.subclass(*args_, **kwargs_)
        else:
            return SERA_quakeml(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_siteOwner(self):
        return self.siteOwner

    def set_siteOwner(self, siteOwner):
        self.siteOwner = siteOwner

    def get_siteCharacterizationParameters(self):
        return self.siteCharacterizationParameters

    def set_siteCharacterizationParameters(self, siteCharacterizationParameters):
        self.siteCharacterizationParameters = siteCharacterizationParameters

    def get_siteDescription(self):
        return self.siteDescription

    def set_siteDescription(self, siteDescription):
        self.siteDescription = siteDescription

    def hasContent_(self):
        if (
                self.siteOwner is not None or
                self.siteCharacterizationParameters is not None or
                self.siteDescription is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ', name_='SERA_quakeml',
               pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SERA_quakeml')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SERA_quakeml':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SERA_quakeml')
        if self.hasContent_():
            outfile.write('>%s' % (eol_,))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SERA_quakeml',
                                pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='SERA_quakeml'):
        pass

    def exportChildren(self, outfile, level, namespaceprefix_='',
                       namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ', name_='SERA_quakeml',
                       fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.siteOwner is not None:
            namespaceprefix_ = self.siteOwner_nsprefix_ + ':' if (UseCapturedNS_ and self.siteOwner_nsprefix_) else ''
            self.siteOwner.export(outfile, level, namespaceprefix_, namespacedef_='', name_='siteOwner',
                                  pretty_print=pretty_print)
        if self.siteCharacterizationParameters is not None:
            namespaceprefix_ = self.siteCharacterizationParameters_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.siteCharacterizationParameters_nsprefix_) else ''
            self.siteCharacterizationParameters.export(outfile, level, namespaceprefix_, namespacedef_='',
                                                       name_='siteCharacterizationParameters',
                                                       pretty_print=pretty_print)
        if self.siteDescription is not None:
            namespaceprefix_ = self.siteDescription_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.siteDescription_nsprefix_) else ''
            self.siteDescription.export(outfile, level, namespaceprefix_, namespacedef_='', name_='siteDescription',
                                        pretty_print=pretty_print)

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def buildAttributes(self, node, attrs, already_processed):
        pass

    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'siteOwner':
            obj_ = siteOwner.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.siteOwner = obj_
            obj_.original_tagname_ = 'siteOwner'
        elif nodeName_ == 'siteCharacterizationParameters':
            obj_ = siteCharacterizationParameters.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.siteCharacterizationParameters = obj_
            obj_.original_tagname_ = 'siteCharacterizationParameters'
        elif nodeName_ == 'siteDescription':
            obj_ = siteDescription.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.siteDescription = obj_
            obj_.original_tagname_ = 'siteDescription'


# end class SERA_quakeml


class siteOwner(GeneratedsSuper):
    """siteOwner is not defined in QuakeML 2.0 draft"""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, publicID=None, codeName=None, fullName=None, contact=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.publicID = _cast(None, publicID)
        self.publicID_nsprefix_ = None
        self.codeName = codeName
        self.codeName_nsprefix_ = None
        self.fullName = fullName
        self.fullName_nsprefix_ = None
        self.contact = contact
        self.contact_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, siteOwner)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if siteOwner.subclass:
            return siteOwner.subclass(*args_, **kwargs_)
        else:
            return siteOwner(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_codeName(self):
        return self.codeName

    def set_codeName(self, codeName):
        self.codeName = codeName

    def get_fullName(self):
        return self.fullName

    def set_fullName(self, fullName):
        self.fullName = fullName

    def get_contact(self):
        return self.contact

    def set_contact(self, contact):
        self.contact = contact

    def get_publicID(self):
        return self.publicID

    def set_publicID(self, publicID):
        self.publicID = publicID

    def hasContent_(self):
        if (
                self.codeName is not None or
                self.fullName is not None or
                self.contact is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ', name_='siteOwner',
               pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('siteOwner')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'siteOwner':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='siteOwner')
        if self.hasContent_():
            outfile.write('>%s' % (eol_,))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='siteOwner',
                                pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='siteOwner'):
        if self.publicID is not None and 'publicID' not in already_processed:
            already_processed.add('publicID')
            outfile.write(' publicID=%s' % (
                self.gds_encode(self.gds_format_string(quote_attrib(self.publicID), input_name='publicID')),))

    def exportChildren(self, outfile, level, namespaceprefix_='',
                       namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ', name_='siteOwner',
                       fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.codeName is not None:
            namespaceprefix_ = self.codeName_nsprefix_ + ':' if (UseCapturedNS_ and self.codeName_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scodeName>%s</%scodeName>%s' % (
                namespaceprefix_,
                self.gds_encode(self.gds_format_string(quote_xml(self.codeName), input_name='codeName')),
                namespaceprefix_, eol_))
        if self.fullName is not None:
            namespaceprefix_ = self.fullName_nsprefix_ + ':' if (UseCapturedNS_ and self.fullName_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sfullName>%s</%sfullName>%s' % (
                namespaceprefix_,
                self.gds_encode(self.gds_format_string(quote_xml(self.fullName), input_name='fullName')),
                namespaceprefix_, eol_))
        if self.contact is not None:
            namespaceprefix_ = self.contact_nsprefix_ + ':' if (UseCapturedNS_ and self.contact_nsprefix_) else ''
            self.contact.export(outfile, level, namespaceprefix_, namespacedef_='', name_='contact',
                                pretty_print=pretty_print)

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('publicID', node)
        if value is not None and 'publicID' not in already_processed:
            already_processed.add('publicID')
            self.publicID = value

    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'codeName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'codeName')
            value_ = self.gds_validate_string(value_, node, 'codeName')
            self.codeName = value_
            self.codeName_nsprefix_ = child_.prefix
        elif nodeName_ == 'fullName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'fullName')
            value_ = self.gds_validate_string(value_, node, 'fullName')
            self.fullName = value_
            self.fullName_nsprefix_ = child_.prefix
        elif nodeName_ == 'contact':
            obj_ = contact.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.contact = obj_
            obj_.original_tagname_ = 'contact'


# end class siteOwner


class contact(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, person=None, affiliation=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.person = person
        self.person_nsprefix_ = None
        self.affiliation = affiliation
        self.affiliation_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, contact)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if contact.subclass:
            return contact.subclass(*args_, **kwargs_)
        else:
            return contact(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_person(self):
        return self.person

    def set_person(self, person):
        self.person = person

    def get_affiliation(self):
        return self.affiliation

    def set_affiliation(self, affiliation):
        self.affiliation = affiliation

    def hasContent_(self):
        if (
                self.person is not None or
                self.affiliation is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ', name_='contact',
               pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('contact')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'contact':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='contact')
        if self.hasContent_():
            outfile.write('>%s' % (eol_,))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='contact',
                                pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='contact'):
        pass

    def exportChildren(self, outfile, level, namespaceprefix_='',
                       namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ', name_='contact',
                       fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.person is not None:
            namespaceprefix_ = self.person_nsprefix_ + ':' if (UseCapturedNS_ and self.person_nsprefix_) else ''
            self.person.export(outfile, level, namespaceprefix_, namespacedef_='', name_='person',
                               pretty_print=pretty_print)
        if self.affiliation is not None:
            namespaceprefix_ = self.affiliation_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.affiliation_nsprefix_) else ''
            self.affiliation.export(outfile, level, namespaceprefix_, namespacedef_='', name_='affiliation',
                                    pretty_print=pretty_print)

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def buildAttributes(self, node, attrs, already_processed):
        pass

    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'person':
            obj_ = person.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.person = obj_
            obj_.original_tagname_ = 'person'
        elif nodeName_ == 'affiliation':
            obj_ = affiliation.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.affiliation = obj_
            obj_.original_tagname_ = 'affiliation'


# end class contact


class person(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, personID=None, firstname=None, lastname=None, mbox=None, homepage=None, gds_collector_=None,
                 **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.personID = _cast(None, personID)
        self.personID_nsprefix_ = None
        self.firstname = firstname
        self.firstname_nsprefix_ = None
        self.lastname = lastname
        self.lastname_nsprefix_ = None
        self.mbox = mbox
        self.mbox_nsprefix_ = None
        self.homepage = homepage
        self.homepage_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, person)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if person.subclass:
            return person.subclass(*args_, **kwargs_)
        else:
            return person(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_firstname(self):
        return self.firstname

    def set_firstname(self, firstname):
        self.firstname = firstname

    def get_lastname(self):
        return self.lastname

    def set_lastname(self, lastname):
        self.lastname = lastname

    def get_mbox(self):
        return self.mbox

    def set_mbox(self, mbox):
        self.mbox = mbox

    def get_homepage(self):
        return self.homepage

    def set_homepage(self, homepage):
        self.homepage = homepage

    def get_personID(self):
        return self.personID

    def set_personID(self, personID):
        self.personID = personID

    def hasContent_(self):
        if (
                self.firstname is not None or
                self.lastname is not None or
                self.mbox is not None or
                self.homepage is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ', name_='person',
               pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('person')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'person':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='person')
        if self.hasContent_():
            outfile.write('>%s' % (eol_,))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='person',
                                pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='person'):
        if self.personID is not None and 'personID' not in already_processed:
            already_processed.add('personID')
            outfile.write(' personID=%s' % (
                self.gds_encode(self.gds_format_string(quote_attrib(self.personID), input_name='personID')),))

    def exportChildren(self, outfile, level, namespaceprefix_='',
                       namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ', name_='person',
                       fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.firstname is not None:
            namespaceprefix_ = self.firstname_nsprefix_ + ':' if (UseCapturedNS_ and self.firstname_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sfirstname>%s</%sfirstname>%s' % (namespaceprefix_, self.gds_encode(
                self.gds_format_string(quote_xml(self.firstname), input_name='firstname')), namespaceprefix_, eol_))
        if self.lastname is not None:
            namespaceprefix_ = self.lastname_nsprefix_ + ':' if (UseCapturedNS_ and self.lastname_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slastname>%s</%slastname>%s' % (
                namespaceprefix_,
                self.gds_encode(self.gds_format_string(quote_xml(self.lastname), input_name='lastname')),
                namespaceprefix_, eol_))
        if self.mbox is not None:
            namespaceprefix_ = self.mbox_nsprefix_ + ':' if (UseCapturedNS_ and self.mbox_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smbox>%s</%smbox>%s' % (
                namespaceprefix_, self.gds_encode(self.gds_format_string(quote_xml(self.mbox), input_name='mbox')),
                namespaceprefix_, eol_))
        if self.homepage is not None:
            namespaceprefix_ = self.homepage_nsprefix_ + ':' if (UseCapturedNS_ and self.homepage_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%shomepage>%s</%shomepage>%s' % (
                namespaceprefix_,
                self.gds_encode(self.gds_format_string(quote_xml(self.homepage), input_name='homepage')),
                namespaceprefix_, eol_))

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('personID', node)
        if value is not None and 'personID' not in already_processed:
            already_processed.add('personID')
            self.personID = value

    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'firstname':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'firstname')
            value_ = self.gds_validate_string(value_, node, 'firstname')
            self.firstname = value_
            self.firstname_nsprefix_ = child_.prefix
        elif nodeName_ == 'lastname':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'lastname')
            value_ = self.gds_validate_string(value_, node, 'lastname')
            self.lastname = value_
            self.lastname_nsprefix_ = child_.prefix
        elif nodeName_ == 'mbox':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'mbox')
            value_ = self.gds_validate_string(value_, node, 'mbox')
            self.mbox = value_
            self.mbox_nsprefix_ = child_.prefix
        elif nodeName_ == 'homepage':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'homepage')
            value_ = self.gds_validate_string(value_, node, 'homepage')
            self.homepage = value_
            self.homepage_nsprefix_ = child_.prefix


# end class person


class affiliation(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, institution=None, department=None, function=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.institution = institution
        self.institution_nsprefix_ = None
        self.department = department
        self.department_nsprefix_ = None
        self.function = function
        self.function_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, affiliation)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if affiliation.subclass:
            return affiliation.subclass(*args_, **kwargs_)
        else:
            return affiliation(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_institution(self):
        return self.institution

    def set_institution(self, institution):
        self.institution = institution

    def get_department(self):
        return self.department

    def set_department(self, department):
        self.department = department

    def get_function(self):
        return self.function

    def set_function(self, function):
        self.function = function

    def hasContent_(self):
        if (
                self.institution is not None or
                self.department is not None or
                self.function is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ', name_='affiliation',
               pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('affiliation')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'affiliation':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='affiliation')
        if self.hasContent_():
            outfile.write('>%s' % (eol_,))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='affiliation',
                                pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='affiliation'):
        pass

    def exportChildren(self, outfile, level, namespaceprefix_='',
                       namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ', name_='affiliation',
                       fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.institution is not None:
            namespaceprefix_ = self.institution_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.institution_nsprefix_) else ''
            self.institution.export(outfile, level, namespaceprefix_, namespacedef_='', name_='institution',
                                    pretty_print=pretty_print)
        if self.department is not None:
            namespaceprefix_ = self.department_nsprefix_ + ':' if (UseCapturedNS_ and self.department_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdepartment>%s</%sdepartment>%s' % (namespaceprefix_, self.gds_encode(
                self.gds_format_string(quote_xml(self.department), input_name='department')), namespaceprefix_, eol_))
        if self.function is not None:
            namespaceprefix_ = self.function_nsprefix_ + ':' if (UseCapturedNS_ and self.function_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sfunction>%s</%sfunction>%s' % (
                namespaceprefix_,
                self.gds_encode(self.gds_format_string(quote_xml(self.function), input_name='function')),
                namespaceprefix_, eol_))

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def buildAttributes(self, node, attrs, already_processed):
        pass

    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'institution':
            obj_ = institution.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.institution = obj_
            obj_.original_tagname_ = 'institution'
        elif nodeName_ == 'department':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'department')
            value_ = self.gds_validate_string(value_, node, 'department')
            self.department = value_
            self.department_nsprefix_ = child_.prefix
        elif nodeName_ == 'function':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'function')
            value_ = self.gds_validate_string(value_, node, 'function')
            self.function = value_
            self.function_nsprefix_ = child_.prefix


# end class affiliation


class institution(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, identifier=None, name=None, mbox=None, phone=None, homepage=None, postalAddress=None,
                 gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.identifier = identifier
        self.identifier_nsprefix_ = None
        self.name = name
        self.name_nsprefix_ = None
        self.mbox = mbox
        self.mbox_nsprefix_ = None
        self.phone = phone
        self.phone_nsprefix_ = None
        self.homepage = homepage
        self.homepage_nsprefix_ = None
        self.postalAddress = postalAddress
        self.postalAddress_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, institution)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if institution.subclass:
            return institution.subclass(*args_, **kwargs_)
        else:
            return institution(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_identifier(self):
        return self.identifier

    def set_identifier(self, identifier):
        self.identifier = identifier

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_mbox(self):
        return self.mbox

    def set_mbox(self, mbox):
        self.mbox = mbox

    def get_phone(self):
        return self.phone

    def set_phone(self, phone):
        self.phone = phone

    def get_homepage(self):
        return self.homepage

    def set_homepage(self, homepage):
        self.homepage = homepage

    def get_postalAddress(self):
        return self.postalAddress

    def set_postalAddress(self, postalAddress):
        self.postalAddress = postalAddress

    def hasContent_(self):
        if (
                self.identifier is not None or
                self.name is not None or
                self.mbox is not None or
                self.phone is not None or
                self.homepage is not None or
                self.postalAddress is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ', name_='institution',
               pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('institution')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'institution':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='institution')
        if self.hasContent_():
            outfile.write('>%s' % (eol_,))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='institution',
                                pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='institution'):
        pass

    def exportChildren(self, outfile, level, namespaceprefix_='',
                       namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ', name_='institution',
                       fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.identifier is not None:
            namespaceprefix_ = self.identifier_nsprefix_ + ':' if (UseCapturedNS_ and self.identifier_nsprefix_) else ''
            self.identifier.export(outfile, level, namespaceprefix_, namespacedef_='', name_='identifier',
                                   pretty_print=pretty_print)
        if self.name is not None:
            namespaceprefix_ = self.name_nsprefix_ + ':' if (UseCapturedNS_ and self.name_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sname>%s</%sname>%s' % (
                namespaceprefix_, self.gds_encode(self.gds_format_string(quote_xml(self.name), input_name='name')),
                namespaceprefix_, eol_))
        if self.mbox is not None:
            namespaceprefix_ = self.mbox_nsprefix_ + ':' if (UseCapturedNS_ and self.mbox_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smbox>%s</%smbox>%s' % (
                namespaceprefix_, self.gds_encode(self.gds_format_string(quote_xml(self.mbox), input_name='mbox')),
                namespaceprefix_, eol_))
        if self.phone is not None:
            namespaceprefix_ = self.phone_nsprefix_ + ':' if (UseCapturedNS_ and self.phone_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sphone>%s</%sphone>%s' % (
                namespaceprefix_, self.gds_encode(self.gds_format_string(quote_xml(self.phone), input_name='phone')),
                namespaceprefix_, eol_))
        if self.homepage is not None:
            namespaceprefix_ = self.homepage_nsprefix_ + ':' if (UseCapturedNS_ and self.homepage_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%shomepage>%s</%shomepage>%s' % (
                namespaceprefix_,
                self.gds_encode(self.gds_format_string(quote_xml(self.homepage), input_name='homepage')),
                namespaceprefix_, eol_))
        if self.postalAddress is not None:
            namespaceprefix_ = self.postalAddress_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.postalAddress_nsprefix_) else ''
            self.postalAddress.export(outfile, level, namespaceprefix_, namespacedef_='', name_='postalAddress',
                                      pretty_print=pretty_print)

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def buildAttributes(self, node, attrs, already_processed):
        pass

    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'identifier':
            obj_ = identifier.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.identifier = obj_
            obj_.original_tagname_ = 'identifier'
        elif nodeName_ == 'name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'name')
            value_ = self.gds_validate_string(value_, node, 'name')
            self.name = value_
            self.name_nsprefix_ = child_.prefix
        elif nodeName_ == 'mbox':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'mbox')
            value_ = self.gds_validate_string(value_, node, 'mbox')
            self.mbox = value_
            self.mbox_nsprefix_ = child_.prefix
        elif nodeName_ == 'phone':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'phone')
            value_ = self.gds_validate_string(value_, node, 'phone')
            self.phone = value_
            self.phone_nsprefix_ = child_.prefix
        elif nodeName_ == 'homepage':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'homepage')
            value_ = self.gds_validate_string(value_, node, 'homepage')
            self.homepage = value_
            self.homepage_nsprefix_ = child_.prefix
        elif nodeName_ == 'postalAddress':
            obj_ = postalAddress.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.postalAddress = obj_
            obj_.original_tagname_ = 'postalAddress'


# end class institution


class identifier(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, resourceID=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.resourceID = resourceID
        self.resourceID_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, identifier)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if identifier.subclass:
            return identifier.subclass(*args_, **kwargs_)
        else:
            return identifier(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_resourceID(self):
        return self.resourceID

    def set_resourceID(self, resourceID):
        self.resourceID = resourceID

    def hasContent_(self):
        if (
                self.resourceID is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ', name_='identifier',
               pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('identifier')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'identifier':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='identifier')
        if self.hasContent_():
            outfile.write('>%s' % (eol_,))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='identifier',
                                pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='identifier'):
        pass

    def exportChildren(self, outfile, level, namespaceprefix_='',
                       namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ', name_='identifier',
                       fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.resourceID is not None:
            namespaceprefix_ = self.resourceID_nsprefix_ + ':' if (UseCapturedNS_ and self.resourceID_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sresourceID>%s</%sresourceID>%s' % (namespaceprefix_, self.gds_encode(
                self.gds_format_string(quote_xml(self.resourceID), input_name='resourceID')), namespaceprefix_, eol_))

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def buildAttributes(self, node, attrs, already_processed):
        pass

    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'resourceID':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'resourceID')
            value_ = self.gds_validate_string(value_, node, 'resourceID')
            self.resourceID = value_
            self.resourceID_nsprefix_ = child_.prefix


# end class identifier


class postalAddress(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, streetAddress=None, locality=None, postalCode=None, country=None, gds_collector_=None,
                 **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.streetAddress = streetAddress
        self.streetAddress_nsprefix_ = None
        self.locality = locality
        self.locality_nsprefix_ = None
        self.postalCode = postalCode
        self.postalCode_nsprefix_ = None
        self.country = country
        self.country_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, postalAddress)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if postalAddress.subclass:
            return postalAddress.subclass(*args_, **kwargs_)
        else:
            return postalAddress(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_streetAddress(self):
        return self.streetAddress

    def set_streetAddress(self, streetAddress):
        self.streetAddress = streetAddress

    def get_locality(self):
        return self.locality

    def set_locality(self, locality):
        self.locality = locality

    def get_postalCode(self):
        return self.postalCode

    def set_postalCode(self, postalCode):
        self.postalCode = postalCode

    def get_country(self):
        return self.country

    def set_country(self, country):
        self.country = country

    def hasContent_(self):
        if (
                self.streetAddress is not None or
                self.locality is not None or
                self.postalCode is not None or
                self.country is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ', name_='postalAddress',
               pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('postalAddress')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'postalAddress':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='postalAddress')
        if self.hasContent_():
            outfile.write('>%s' % (eol_,))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='postalAddress',
                                pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='postalAddress'):
        pass

    def exportChildren(self, outfile, level, namespaceprefix_='',
                       namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ',
                       name_='postalAddress', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.streetAddress is not None:
            namespaceprefix_ = self.streetAddress_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.streetAddress_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sstreetAddress>%s</%sstreetAddress>%s' % (namespaceprefix_, self.gds_encode(
                self.gds_format_string(quote_xml(self.streetAddress), input_name='streetAddress')), namespaceprefix_,
                                                                       eol_))
        if self.locality is not None:
            namespaceprefix_ = self.locality_nsprefix_ + ':' if (UseCapturedNS_ and self.locality_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slocality>%s</%slocality>%s' % (
                namespaceprefix_,
                self.gds_encode(self.gds_format_string(quote_xml(self.locality), input_name='locality')),
                namespaceprefix_, eol_))
        if self.postalCode is not None:
            namespaceprefix_ = self.postalCode_nsprefix_ + ':' if (UseCapturedNS_ and self.postalCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spostalCode>%s</%spostalCode>%s' % (namespaceprefix_, self.gds_encode(
                self.gds_format_string(quote_xml(self.postalCode), input_name='postalCode')), namespaceprefix_, eol_))
        if self.country is not None:
            namespaceprefix_ = self.country_nsprefix_ + ':' if (UseCapturedNS_ and self.country_nsprefix_) else ''
            self.country.export(outfile, level, namespaceprefix_, namespacedef_='', name_='country',
                                pretty_print=pretty_print)

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def buildAttributes(self, node, attrs, already_processed):
        pass

    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'streetAddress':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'streetAddress')
            value_ = self.gds_validate_string(value_, node, 'streetAddress')
            self.streetAddress = value_
            self.streetAddress_nsprefix_ = child_.prefix
        elif nodeName_ == 'locality':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'locality')
            value_ = self.gds_validate_string(value_, node, 'locality')
            self.locality = value_
            self.locality_nsprefix_ = child_.prefix
        elif nodeName_ == 'postalCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'postalCode')
            value_ = self.gds_validate_string(value_, node, 'postalCode')
            self.postalCode = value_
            self.postalCode_nsprefix_ = child_.prefix
        elif nodeName_ == 'country':
            obj_ = country.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.country = obj_
            obj_.original_tagname_ = 'country'


# end class postalAddress


class country(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, code=None, country=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.code = code
        self.code_nsprefix_ = None
        self.country = country
        self.country_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, country)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if country.subclass:
            return country.subclass(*args_, **kwargs_)
        else:
            return country(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_code(self):
        return self.code

    def set_code(self, code):
        self.code = code

    def get_country(self):
        return self.country

    def set_country(self, country):
        self.country = country

    def hasContent_(self):
        if (
                self.code is not None or
                self.country is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ', name_='country',
               pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('country')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'country':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='country')
        if self.hasContent_():
            outfile.write('>%s' % (eol_,))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='country',
                                pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='country'):
        pass

    def exportChildren(self, outfile, level, namespaceprefix_='',
                       namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ', name_='country',
                       fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.code is not None:
            namespaceprefix_ = self.code_nsprefix_ + ':' if (UseCapturedNS_ and self.code_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scode>%s</%scode>%s' % (
                namespaceprefix_, self.gds_encode(self.gds_format_string(quote_xml(self.code), input_name='code')),
                namespaceprefix_, eol_))
        if self.country is not None:
            namespaceprefix_ = self.country_nsprefix_ + ':' if (UseCapturedNS_ and self.country_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scountry>%s</%scountry>%s' % (
                namespaceprefix_,
                self.gds_encode(self.gds_format_string(quote_xml(self.country), input_name='country')),
                namespaceprefix_, eol_))

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def buildAttributes(self, node, attrs, already_processed):
        pass

    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'code')
            value_ = self.gds_validate_string(value_, node, 'code')
            self.code = value_
            self.code_nsprefix_ = child_.prefix
        elif nodeName_ == 'country':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'country')
            value_ = self.gds_validate_string(value_, node, 'country')
            self.country = value_
            self.country_nsprefix_ = child_.prefix


# end class country


class siteCharacterizationParameters(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, publicID=None, Analysis=None, VelocityProfile=None, velocityProfileQindex1=None,
                 velocityProfileReference=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.publicID = _cast(None, publicID)
        self.publicID_nsprefix_ = None
        self.Analysis = Analysis
        self.Analysis_nsprefix_ = None
        if VelocityProfile is None:
            self.VelocityProfile = []
        else:
            self.VelocityProfile = VelocityProfile
        self.VelocityProfile_nsprefix_ = None
        self.velocityProfileQindex1 = velocityProfileQindex1
        self.velocityProfileQindex1_nsprefix_ = None
        self.velocityProfileReference = velocityProfileReference
        self.velocityProfileReference_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, siteCharacterizationParameters)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if siteCharacterizationParameters.subclass:
            return siteCharacterizationParameters.subclass(*args_, **kwargs_)
        else:
            return siteCharacterizationParameters(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_Analysis(self):
        return self.Analysis

    def set_Analysis(self, Analysis):
        self.Analysis = Analysis

    def get_VelocityProfile(self):
        return self.VelocityProfile

    def set_VelocityProfile(self, VelocityProfile):
        self.VelocityProfile = VelocityProfile

    def add_VelocityProfile(self, value):
        self.VelocityProfile.append(value)

    def insert_VelocityProfile_at(self, index, value):
        self.VelocityProfile.insert(index, value)

    def replace_VelocityProfile_at(self, index, value):
        self.VelocityProfile[index] = value

    def get_velocityProfileQindex1(self):
        return self.velocityProfileQindex1

    def set_velocityProfileQindex1(self, velocityProfileQindex1):
        self.velocityProfileQindex1 = velocityProfileQindex1

    def get_velocityProfileReference(self):
        return self.velocityProfileReference

    def set_velocityProfileReference(self, velocityProfileReference):
        self.velocityProfileReference = velocityProfileReference

    def get_publicID(self):
        return self.publicID

    def set_publicID(self, publicID):
        self.publicID = publicID

    def hasContent_(self):
        if (
                self.Analysis is not None or
                self.VelocityProfile or
                self.velocityProfileQindex1 is not None or
                self.velocityProfileReference is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ',
               name_='siteCharacterizationParameters', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('siteCharacterizationParameters')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'siteCharacterizationParameters':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_,
                              name_='siteCharacterizationParameters')
        if self.hasContent_():
            outfile.write('>%s' % (eol_,))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_,
                                name_='siteCharacterizationParameters', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='',
                         name_='siteCharacterizationParameters'):
        if self.publicID is not None and 'publicID' not in already_processed:
            already_processed.add('publicID')
            outfile.write(' publicID=%s' % (
                self.gds_encode(self.gds_format_string(quote_attrib(self.publicID), input_name='publicID')),))

    def exportChildren(self, outfile, level, namespaceprefix_='',
                       namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ',
                       name_='siteCharacterizationParameters', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Analysis is not None:
            namespaceprefix_ = self.Analysis_nsprefix_ + ':' if (UseCapturedNS_ and self.Analysis_nsprefix_) else ''
            self.Analysis.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Analysis',
                                 pretty_print=pretty_print)
        for VelocityProfile_ in self.VelocityProfile:
            namespaceprefix_ = self.VelocityProfile_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.VelocityProfile_nsprefix_) else ''
            VelocityProfile_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='VelocityProfile',
                                    pretty_print=pretty_print)
        if self.velocityProfileQindex1 is not None:
            namespaceprefix_ = self.velocityProfileQindex1_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.velocityProfileQindex1_nsprefix_) else ''
            self.velocityProfileQindex1.export(outfile, level, namespaceprefix_, namespacedef_='',
                                               name_='velocityProfileQindex1', pretty_print=pretty_print)
        if self.velocityProfileReference is not None:
            namespaceprefix_ = self.velocityProfileReference_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.velocityProfileReference_nsprefix_) else ''
            self.velocityProfileReference.export(outfile, level, namespaceprefix_, namespacedef_='',
                                                 name_='velocityProfileReference', pretty_print=pretty_print)

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('publicID', node)
        if value is not None and 'publicID' not in already_processed:
            already_processed.add('publicID')
            self.publicID = value

    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Analysis':
            obj_ = Analysis.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Analysis = obj_
            obj_.original_tagname_ = 'Analysis'
        elif nodeName_ == 'VelocityProfile':
            obj_ = VelocityProfile.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.VelocityProfile.append(obj_)
            obj_.original_tagname_ = 'VelocityProfile'
        elif nodeName_ == 'velocityProfileQindex1':
            obj_ = velocityProfileQindex1.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.velocityProfileQindex1 = obj_
            obj_.original_tagname_ = 'velocityProfileQindex1'
        elif nodeName_ == 'velocityProfileReference':
            obj_ = velocityProfileReference.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.velocityProfileReference = obj_
            obj_.original_tagname_ = 'velocityProfileReference'


# end class siteCharacterizationParameters


class Analysis(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, publicID=None, resonanceFrequency=None, resonanceFrequencyQindex1=None,
                 resonanceFrequencyMethod=None, resonanceFrequencyReference=None, velocityS30=None,
                 velocityS30Qindex1=None, velocityS30Method=None, velocityS30MethodCombIndex=None,
                 velocityS30ManualIndex=None, velocityS30Reference=None, velocityProfileCount=None, sptLogsCount=None,
                 cptLogsCount=None, boreholeLogsCount=None, valueOf_=None, mixedclass_=None, content_=None,
                 gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.publicID = _cast(None, publicID)
        self.publicID_nsprefix_ = None
        self.resonanceFrequency = resonanceFrequency
        self.resonanceFrequency_nsprefix_ = None
        self.resonanceFrequencyQindex1 = resonanceFrequencyQindex1
        self.resonanceFrequencyQindex1_nsprefix_ = None
        if resonanceFrequencyMethod is None:
            self.resonanceFrequencyMethod = []
        else:
            self.resonanceFrequencyMethod = resonanceFrequencyMethod
        self.resonanceFrequencyMethod_nsprefix_ = None
        self.resonanceFrequencyReference = resonanceFrequencyReference
        self.resonanceFrequencyReference_nsprefix_ = None
        self.velocityS30 = velocityS30
        self.velocityS30_nsprefix_ = None
        self.velocityS30Qindex1 = velocityS30Qindex1
        self.velocityS30Qindex1_nsprefix_ = None
        if velocityS30Method is None:
            self.velocityS30Method = []
        else:
            self.velocityS30Method = velocityS30Method
        self.velocityS30Method_nsprefix_ = None
        self.velocityS30MethodCombIndex = velocityS30MethodCombIndex
        self.velocityS30MethodCombIndex_nsprefix_ = None
        self.velocityS30ManualIndex = velocityS30ManualIndex
        self.velocityS30ManualIndex_nsprefix_ = None
        self.velocityS30Reference = velocityS30Reference
        self.velocityS30Reference_nsprefix_ = None
        self.velocityProfileCount = velocityProfileCount
        self.velocityProfileCount_nsprefix_ = None
        self.sptLogsCount = sptLogsCount
        self.sptLogsCount_nsprefix_ = None
        self.cptLogsCount = cptLogsCount
        self.cptLogsCount_nsprefix_ = None
        self.boreholeLogsCount = boreholeLogsCount
        self.boreholeLogsCount_nsprefix_ = None
        self.valueOf_ = valueOf_
        if mixedclass_ is None:
            self.mixedclass_ = MixedContainer
        else:
            self.mixedclass_ = mixedclass_
        if content_ is None:
            self.content_ = []
        else:
            self.content_ = content_
        self.valueOf_ = valueOf_

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Analysis)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Analysis.subclass:
            return Analysis.subclass(*args_, **kwargs_)
        else:
            return Analysis(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_resonanceFrequency(self):
        return self.resonanceFrequency

    def set_resonanceFrequency(self, resonanceFrequency):
        self.resonanceFrequency = resonanceFrequency

    def get_resonanceFrequencyQindex1(self):
        return self.resonanceFrequencyQindex1

    def set_resonanceFrequencyQindex1(self, resonanceFrequencyQindex1):
        self.resonanceFrequencyQindex1 = resonanceFrequencyQindex1

    def get_resonanceFrequencyMethod(self):
        return self.resonanceFrequencyMethod

    def set_resonanceFrequencyMethod(self, resonanceFrequencyMethod):
        self.resonanceFrequencyMethod = resonanceFrequencyMethod

    def add_resonanceFrequencyMethod(self, value):
        self.resonanceFrequencyMethod.append(value)

    def insert_resonanceFrequencyMethod_at(self, index, value):
        self.resonanceFrequencyMethod.insert(index, value)

    def replace_resonanceFrequencyMethod_at(self, index, value):
        self.resonanceFrequencyMethod[index] = value

    def get_resonanceFrequencyReference(self):
        return self.resonanceFrequencyReference

    def set_resonanceFrequencyReference(self, resonanceFrequencyReference):
        self.resonanceFrequencyReference = resonanceFrequencyReference

    def get_velocityS30(self):
        return self.velocityS30

    def set_velocityS30(self, velocityS30):
        self.velocityS30 = velocityS30

    def get_velocityS30Qindex1(self):
        return self.velocityS30Qindex1

    def set_velocityS30Qindex1(self, velocityS30Qindex1):
        self.velocityS30Qindex1 = velocityS30Qindex1

    def get_velocityS30Method(self):
        return self.velocityS30Method

    def set_velocityS30Method(self, velocityS30Method):
        self.velocityS30Method = velocityS30Method

    def add_velocityS30Method(self, value):
        self.velocityS30Method.append(value)

    def insert_velocityS30Method_at(self, index, value):
        self.velocityS30Method.insert(index, value)

    def replace_velocityS30Method_at(self, index, value):
        self.velocityS30Method[index] = value

    def get_velocityS30MethodCombIndex(self):
        return self.velocityS30MethodCombIndex

    def set_velocityS30MethodCombIndex(self, velocityS30MethodCombIndex):
        self.velocityS30MethodCombIndex = velocityS30MethodCombIndex

    def get_velocityS30ManualIndex(self):
        return self.velocityS30ManualIndex

    def set_velocityS30ManualIndex(self, velocityS30ManualIndex):
        self.velocityS30ManualIndex = velocityS30ManualIndex

    def get_velocityS30Reference(self):
        return self.velocityS30Reference

    def set_velocityS30Reference(self, velocityS30Reference):
        self.velocityS30Reference = velocityS30Reference

    def get_velocityProfileCount(self):
        return self.velocityProfileCount

    def set_velocityProfileCount(self, velocityProfileCount):
        self.velocityProfileCount = velocityProfileCount

    def get_sptLogsCount(self):
        return self.sptLogsCount

    def set_sptLogsCount(self, sptLogsCount):
        self.sptLogsCount = sptLogsCount

    def get_cptLogsCount(self):
        return self.cptLogsCount

    def set_cptLogsCount(self, cptLogsCount):
        self.cptLogsCount = cptLogsCount

    def get_boreholeLogsCount(self):
        return self.boreholeLogsCount

    def set_boreholeLogsCount(self, boreholeLogsCount):
        self.boreholeLogsCount = boreholeLogsCount

    def get_publicID(self):
        return self.publicID

    def set_publicID(self, publicID):
        self.publicID = publicID

    def get_valueOf_(self):
        return self.valueOf_

    def set_valueOf_(self, valueOf_):
        self.valueOf_ = valueOf_

    def hasContent_(self):
        if (
                self.resonanceFrequency is not None or
                self.resonanceFrequencyQindex1 is not None or
                self.resonanceFrequencyMethod or
                self.resonanceFrequencyReference is not None or
                self.velocityS30 is not None or
                self.velocityS30Qindex1 is not None or
                self.velocityS30Method or
                self.velocityS30MethodCombIndex is not None or
                self.velocityS30ManualIndex is not None or
                self.velocityS30Reference is not None or
                self.velocityProfileCount is not None or
                self.sptLogsCount is not None or
                self.cptLogsCount is not None or
                self.boreholeLogsCount is not None or
                (1 if type(self.valueOf_) in [int, float] else self.valueOf_) or
                self.content_
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ', name_='Analysis',
               pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Analysis')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Analysis':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Analysis')
        if self.hasContent_():
            outfile.write('>%s' % (eol_,))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Analysis',
                                pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Analysis'):
        if self.publicID is not None and 'publicID' not in already_processed:
            already_processed.add('publicID')
            outfile.write(' publicID=%s' % (
                self.gds_encode(self.gds_format_string(quote_attrib(self.publicID), input_name='publicID')),))

    def exportChildren(self, outfile, level, namespaceprefix_='',
                       namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ', name_='Analysis',
                       fromsubclass_=False, pretty_print=True):
        if not fromsubclass_:
            for item_ in self.content_:
                item_.export(outfile, level, item_.name, namespaceprefix_, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.resonanceFrequency is not None:
            namespaceprefix_ = self.resonanceFrequency_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.resonanceFrequency_nsprefix_) else ''
            self.resonanceFrequency.export(outfile, level, namespaceprefix_, namespacedef_='',
                                           name_='resonanceFrequency', pretty_print=pretty_print)
        if self.resonanceFrequencyQindex1 is not None:
            namespaceprefix_ = self.resonanceFrequencyQindex1_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.resonanceFrequencyQindex1_nsprefix_) else ''
            self.resonanceFrequencyQindex1.export(outfile, level, namespaceprefix_, namespacedef_='',
                                                  name_='resonanceFrequencyQindex1', pretty_print=pretty_print)
        for resonanceFrequencyMethod_ in self.resonanceFrequencyMethod:
            namespaceprefix_ = self.resonanceFrequencyMethod_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.resonanceFrequencyMethod_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sresonanceFrequencyMethod>%s</%sresonanceFrequencyMethod>%s' % (namespaceprefix_,
                                                                                             self.gds_encode(
                                                                                                 self.gds_format_string(
                                                                                                     quote_xml(
                                                                                                         resonanceFrequencyMethod_),
                                                                                                     input_name='resonanceFrequencyMethod')),
                                                                                             namespaceprefix_, eol_))
        if self.resonanceFrequencyReference is not None:
            namespaceprefix_ = self.resonanceFrequencyReference_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.resonanceFrequencyReference_nsprefix_) else ''
            self.resonanceFrequencyReference.export(outfile, level, namespaceprefix_, namespacedef_='',
                                                    name_='resonanceFrequencyReference', pretty_print=pretty_print)
        if self.velocityS30 is not None:
            namespaceprefix_ = self.velocityS30_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.velocityS30_nsprefix_) else ''
            self.velocityS30.export(outfile, level, namespaceprefix_, namespacedef_='', name_='velocityS30',
                                    pretty_print=pretty_print)
        if self.velocityS30Qindex1 is not None:
            namespaceprefix_ = self.velocityS30Qindex1_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.velocityS30Qindex1_nsprefix_) else ''
            self.velocityS30Qindex1.export(outfile, level, namespaceprefix_, namespacedef_='',
                                           name_='velocityS30Qindex1', pretty_print=pretty_print)
        for velocityS30Method_ in self.velocityS30Method:
            namespaceprefix_ = self.velocityS30Method_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.velocityS30Method_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svelocityS30Method>%s</%svelocityS30Method>%s' % (namespaceprefix_, self.gds_encode(
                self.gds_format_string(quote_xml(velocityS30Method_), input_name='velocityS30Method')),
                                                                               namespaceprefix_, eol_))
        if self.velocityS30MethodCombIndex is not None:
            namespaceprefix_ = self.velocityS30MethodCombIndex_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.velocityS30MethodCombIndex_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svelocityS30MethodCombIndex>%s</%svelocityS30MethodCombIndex>%s' % (namespaceprefix_,
                                                                                                 self.gds_encode(
                                                                                                     self.gds_format_string(
                                                                                                         quote_xml(
                                                                                                             self.velocityS30MethodCombIndex),
                                                                                                         input_name='velocityS30MethodCombIndex')),
                                                                                                 namespaceprefix_,
                                                                                                 eol_))
        if self.velocityS30ManualIndex is not None:
            namespaceprefix_ = self.velocityS30ManualIndex_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.velocityS30ManualIndex_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svelocityS30ManualIndex>%s</%svelocityS30ManualIndex>%s' % (namespaceprefix_,
                                                                                         self.gds_encode(
                                                                                             self.gds_format_string(
                                                                                                 quote_xml(
                                                                                                     self.velocityS30ManualIndex),
                                                                                                 input_name='velocityS30ManualIndex')),
                                                                                         namespaceprefix_, eol_))
        if self.velocityS30Reference is not None:
            namespaceprefix_ = self.velocityS30Reference_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.velocityS30Reference_nsprefix_) else ''
            self.velocityS30Reference.export(outfile, level, namespaceprefix_, namespacedef_='',
                                             name_='velocityS30Reference', pretty_print=pretty_print)
        if self.velocityProfileCount is not None:
            namespaceprefix_ = self.velocityProfileCount_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.velocityProfileCount_nsprefix_) else ''
            self.velocityProfileCount.export(outfile, level, namespaceprefix_, namespacedef_='',
                                             name_='velocityProfileCount', pretty_print=pretty_print)
        if self.sptLogsCount is not None:
            namespaceprefix_ = self.sptLogsCount_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.sptLogsCount_nsprefix_) else ''
            self.sptLogsCount.export(outfile, level, namespaceprefix_, namespacedef_='', name_='sptLogsCount',
                                     pretty_print=pretty_print)
        if self.cptLogsCount is not None:
            namespaceprefix_ = self.cptLogsCount_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.cptLogsCount_nsprefix_) else ''
            self.cptLogsCount.export(outfile, level, namespaceprefix_, namespacedef_='', name_='cptLogsCount',
                                     pretty_print=pretty_print)
        if self.boreholeLogsCount is not None:
            namespaceprefix_ = self.boreholeLogsCount_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.boreholeLogsCount_nsprefix_) else ''
            self.boreholeLogsCount.export(outfile, level, namespaceprefix_, namespacedef_='', name_='boreholeLogsCount',
                                          pretty_print=pretty_print)

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        if node.text is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                                    MixedContainer.TypeNone, '', node.text)
            self.content_.append(obj_)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('publicID', node)
        if value is not None and 'publicID' not in already_processed:
            already_processed.add('publicID')
            self.publicID = value

    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'resonanceFrequency':
            obj_ = resonanceFrequency.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                                    MixedContainer.TypeNone, 'resonanceFrequency', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_resonanceFrequency'):
                self.add_resonanceFrequency(obj_.value)
            elif hasattr(self, 'set_resonanceFrequency'):
                self.set_resonanceFrequency(obj_.value)
        elif nodeName_ == 'resonanceFrequencyQindex1':
            obj_ = resonanceFrequencyQindex1.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                                    MixedContainer.TypeNone, 'resonanceFrequencyQindex1', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_resonanceFrequencyQindex1'):
                self.add_resonanceFrequencyQindex1(obj_.value)
            elif hasattr(self, 'set_resonanceFrequencyQindex1'):
                self.set_resonanceFrequencyQindex1(obj_.value)
        elif nodeName_ == 'resonanceFrequencyMethod' and child_.text is not None:
            valuestr_ = child_.text
            valuestr_ = self.gds_parse_string(valuestr_, node, 'resonanceFrequencyMethod')
            valuestr_ = self.gds_validate_string(valuestr_, node, 'resonanceFrequencyMethod')
            obj_ = self.mixedclass_(MixedContainer.CategorySimple,
                                    MixedContainer.TypeString, 'resonanceFrequencyMethod', valuestr_)
            self.content_.append(obj_)
            self.resonanceFrequencyMethod_nsprefix_ = child_.prefix
        elif nodeName_ == 'resonanceFrequencyReference':
            obj_ = resonanceFrequencyReference.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                                    MixedContainer.TypeNone, 'resonanceFrequencyReference', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_resonanceFrequencyReference'):
                self.add_resonanceFrequencyReference(obj_.value)
            elif hasattr(self, 'set_resonanceFrequencyReference'):
                self.set_resonanceFrequencyReference(obj_.value)
        elif nodeName_ == 'velocityS30':
            obj_ = velocityS30.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                                    MixedContainer.TypeNone, 'velocityS30', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_velocityS30'):
                self.add_velocityS30(obj_.value)
            elif hasattr(self, 'set_velocityS30'):
                self.set_velocityS30(obj_.value)
        elif nodeName_ == 'velocityS30Qindex1':
            obj_ = velocityS30Qindex1.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                                    MixedContainer.TypeNone, 'velocityS30Qindex1', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_velocityS30Qindex1'):
                self.add_velocityS30Qindex1(obj_.value)
            elif hasattr(self, 'set_velocityS30Qindex1'):
                self.set_velocityS30Qindex1(obj_.value)
        elif nodeName_ == 'velocityS30Method' and child_.text is not None:
            valuestr_ = child_.text
            valuestr_ = self.gds_parse_string(valuestr_, node, 'velocityS30Method')
            valuestr_ = self.gds_validate_string(valuestr_, node, 'velocityS30Method')
            obj_ = self.mixedclass_(MixedContainer.CategorySimple,
                                    MixedContainer.TypeString, 'velocityS30Method', valuestr_)
            self.content_.append(obj_)
            self.velocityS30Method_nsprefix_ = child_.prefix
        elif nodeName_ == 'velocityS30MethodCombIndex' and child_.text is not None:
            valuestr_ = child_.text
            valuestr_ = self.gds_parse_string(valuestr_, node, 'velocityS30MethodCombIndex')
            valuestr_ = self.gds_validate_string(valuestr_, node, 'velocityS30MethodCombIndex')
            obj_ = self.mixedclass_(MixedContainer.CategorySimple,
                                    MixedContainer.TypeString, 'velocityS30MethodCombIndex', valuestr_)
            self.content_.append(obj_)
            self.velocityS30MethodCombIndex_nsprefix_ = child_.prefix
        elif nodeName_ == 'velocityS30ManualIndex' and child_.text is not None:
            valuestr_ = child_.text
            valuestr_ = self.gds_parse_string(valuestr_, node, 'velocityS30ManualIndex')
            valuestr_ = self.gds_validate_string(valuestr_, node, 'velocityS30ManualIndex')
            obj_ = self.mixedclass_(MixedContainer.CategorySimple,
                                    MixedContainer.TypeString, 'velocityS30ManualIndex', valuestr_)
            self.content_.append(obj_)
            self.velocityS30ManualIndex_nsprefix_ = child_.prefix
        elif nodeName_ == 'velocityS30Reference':
            obj_ = velocityS30Reference.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                                    MixedContainer.TypeNone, 'velocityS30Reference', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_velocityS30Reference'):
                self.add_velocityS30Reference(obj_.value)
            elif hasattr(self, 'set_velocityS30Reference'):
                self.set_velocityS30Reference(obj_.value)
        elif nodeName_ == 'velocityProfileCount':
            obj_ = velocityProfileCount.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                                    MixedContainer.TypeNone, 'velocityProfileCount', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_velocityProfileCount'):
                self.add_velocityProfileCount(obj_.value)
            elif hasattr(self, 'set_velocityProfileCount'):
                self.set_velocityProfileCount(obj_.value)
        elif nodeName_ == 'sptLogsCount':
            obj_ = sptLogsCount.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                                    MixedContainer.TypeNone, 'sptLogsCount', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_sptLogsCount'):
                self.add_sptLogsCount(obj_.value)
            elif hasattr(self, 'set_sptLogsCount'):
                self.set_sptLogsCount(obj_.value)
        elif nodeName_ == 'cptLogsCount':
            obj_ = cptLogsCount.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                                    MixedContainer.TypeNone, 'cptLogsCount', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_cptLogsCount'):
                self.add_cptLogsCount(obj_.value)
            elif hasattr(self, 'set_cptLogsCount'):
                self.set_cptLogsCount(obj_.value)
        elif nodeName_ == 'boreholeLogsCount':
            obj_ = boreholeLogsCount.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                                    MixedContainer.TypeNone, 'boreholeLogsCount', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_boreholeLogsCount'):
                self.add_boreholeLogsCount(obj_.value)
            elif hasattr(self, 'set_boreholeLogsCount'):
                self.set_boreholeLogsCount(obj_.value)
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                                    MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)


# end class Analysis


class resonanceFrequency(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, value=None, uncertainty=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.value = value
        self.value_nsprefix_ = None
        self.uncertainty = uncertainty
        self.uncertainty_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, resonanceFrequency)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if resonanceFrequency.subclass:
            return resonanceFrequency.subclass(*args_, **kwargs_)
        else:
            return resonanceFrequency(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_uncertainty(self):
        return self.uncertainty

    def set_uncertainty(self, uncertainty):
        self.uncertainty = uncertainty

    def hasContent_(self):
        if (
                self.value is not None or
                self.uncertainty is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ', name_='resonanceFrequency',
               pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('resonanceFrequency')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'resonanceFrequency':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='resonanceFrequency')
        if self.hasContent_():
            outfile.write('>%s' % (eol_,))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='resonanceFrequency',
                                pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='resonanceFrequency'):
        pass

    def exportChildren(self, outfile, level, namespaceprefix_='',
                       namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ',
                       name_='resonanceFrequency', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.value is not None:
            namespaceprefix_ = self.value_nsprefix_ + ':' if (UseCapturedNS_ and self.value_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svalue>%s</%svalue>%s' % (
                namespaceprefix_, self.gds_format_double(self.value, input_name='value'), namespaceprefix_, eol_))
        if self.uncertainty is not None:
            namespaceprefix_ = self.uncertainty_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.uncertainty_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%suncertainty>%s</%suncertainty>%s' % (
                namespaceprefix_, self.gds_format_double(self.uncertainty, input_name='uncertainty'), namespaceprefix_,
                eol_))

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def buildAttributes(self, node, attrs, already_processed):
        pass

    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'value' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'value')
            fval_ = self.gds_validate_double(fval_, node, 'value')
            self.value = fval_
            self.value_nsprefix_ = child_.prefix
        elif nodeName_ == 'uncertainty' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'uncertainty')
            fval_ = self.gds_validate_double(fval_, node, 'uncertainty')
            self.uncertainty = fval_
            self.uncertainty_nsprefix_ = child_.prefix


# end class resonanceFrequency


class resonanceFrequencyQindex1(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, value=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.value = value
        self.value_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, resonanceFrequencyQindex1)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if resonanceFrequencyQindex1.subclass:
            return resonanceFrequencyQindex1.subclass(*args_, **kwargs_)
        else:
            return resonanceFrequencyQindex1(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def hasContent_(self):
        if (
                self.value is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ',
               name_='resonanceFrequencyQindex1', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('resonanceFrequencyQindex1')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'resonanceFrequencyQindex1':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_,
                              name_='resonanceFrequencyQindex1')
        if self.hasContent_():
            outfile.write('>%s' % (eol_,))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_,
                                name_='resonanceFrequencyQindex1', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='',
                         name_='resonanceFrequencyQindex1'):
        pass

    def exportChildren(self, outfile, level, namespaceprefix_='',
                       namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ',
                       name_='resonanceFrequencyQindex1', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.value is not None:
            namespaceprefix_ = self.value_nsprefix_ + ':' if (UseCapturedNS_ and self.value_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svalue>%s</%svalue>%s' % (
                namespaceprefix_, self.gds_format_double(self.value, input_name='value'), namespaceprefix_, eol_))

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def buildAttributes(self, node, attrs, already_processed):
        pass

    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'value' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'value')
            fval_ = self.gds_validate_double(fval_, node, 'value')
            self.value = fval_
            self.value_nsprefix_ = child_.prefix


# end class resonanceFrequencyQindex1


class resonanceFrequencyReference(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, literatureSource=None, FileResource=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.literatureSource = literatureSource
        self.literatureSource_nsprefix_ = None
        self.FileResource = FileResource
        self.FileResource_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, resonanceFrequencyReference)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if resonanceFrequencyReference.subclass:
            return resonanceFrequencyReference.subclass(*args_, **kwargs_)
        else:
            return resonanceFrequencyReference(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_literatureSource(self):
        return self.literatureSource

    def set_literatureSource(self, literatureSource):
        self.literatureSource = literatureSource

    def get_FileResource(self):
        return self.FileResource

    def set_FileResource(self, FileResource):
        self.FileResource = FileResource

    def hasContent_(self):
        if (
                self.literatureSource is not None or
                self.FileResource is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ',
               name_='resonanceFrequencyReference', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('resonanceFrequencyReference')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'resonanceFrequencyReference':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_,
                              name_='resonanceFrequencyReference')
        if self.hasContent_():
            outfile.write('>%s' % (eol_,))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_,
                                name_='resonanceFrequencyReference', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='',
                         name_='resonanceFrequencyReference'):
        pass

    def exportChildren(self, outfile, level, namespaceprefix_='',
                       namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ',
                       name_='resonanceFrequencyReference', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.literatureSource is not None:
            namespaceprefix_ = self.literatureSource_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.literatureSource_nsprefix_) else ''
            self.literatureSource.export(outfile, level, namespaceprefix_, namespacedef_='', name_='literatureSource',
                                         pretty_print=pretty_print)
        if self.FileResource is not None:
            namespaceprefix_ = self.FileResource_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.FileResource_nsprefix_) else ''
            self.FileResource.export(outfile, level, namespaceprefix_, namespacedef_='', name_='FileResource',
                                     pretty_print=pretty_print)

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def buildAttributes(self, node, attrs, already_processed):
        pass

    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'literatureSource':
            obj_ = literatureSource.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.literatureSource = obj_
            obj_.original_tagname_ = 'literatureSource'
        elif nodeName_ == 'FileResource':
            obj_ = FileResource.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.FileResource = obj_
            obj_.original_tagname_ = 'FileResource'


# end class resonanceFrequencyReference


class literatureSource(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, title=None, firstAuthor=None, secondaryAuthors=None, year=None, booktitle=None, language=None,
                 DOI=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.title = title
        self.title_nsprefix_ = None
        self.firstAuthor = firstAuthor
        self.firstAuthor_nsprefix_ = None
        if secondaryAuthors is None:
            self.secondaryAuthors = []
        else:
            self.secondaryAuthors = secondaryAuthors
        self.secondaryAuthors_nsprefix_ = None
        self.year = year
        self.year_nsprefix_ = None
        self.booktitle = booktitle
        self.booktitle_nsprefix_ = None
        self.language = language
        self.language_nsprefix_ = None
        self.DOI = DOI
        self.DOI_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, literatureSource)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if literatureSource.subclass:
            return literatureSource.subclass(*args_, **kwargs_)
        else:
            return literatureSource(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_firstAuthor(self):
        return self.firstAuthor

    def set_firstAuthor(self, firstAuthor):
        self.firstAuthor = firstAuthor

    def get_secondaryAuthors(self):
        return self.secondaryAuthors

    def set_secondaryAuthors(self, secondaryAuthors):
        self.secondaryAuthors = secondaryAuthors

    def add_secondaryAuthors(self, value):
        self.secondaryAuthors.append(value)

    def insert_secondaryAuthors_at(self, index, value):
        self.secondaryAuthors.insert(index, value)

    def replace_secondaryAuthors_at(self, index, value):
        self.secondaryAuthors[index] = value

    def get_year(self):
        return self.year

    def set_year(self, year):
        self.year = year

    def get_booktitle(self):
        return self.booktitle

    def set_booktitle(self, booktitle):
        self.booktitle = booktitle

    def get_language(self):
        return self.language

    def set_language(self, language):
        self.language = language

    def get_DOI(self):
        return self.DOI

    def set_DOI(self, DOI):
        self.DOI = DOI

    def hasContent_(self):
        if (
                self.title is not None or
                self.firstAuthor is not None or
                self.secondaryAuthors or
                self.year is not None or
                self.booktitle is not None or
                self.language is not None or
                self.DOI is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ', name_='literatureSource',
               pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('literatureSource')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'literatureSource':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='literatureSource')
        if self.hasContent_():
            outfile.write('>%s' % (eol_,))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='literatureSource',
                                pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='literatureSource'):
        pass

    def exportChildren(self, outfile, level, namespaceprefix_='',
                       namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ',
                       name_='literatureSource', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.title is not None:
            namespaceprefix_ = self.title_nsprefix_ + ':' if (UseCapturedNS_ and self.title_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stitle>%s</%stitle>%s' % (
                namespaceprefix_, self.gds_encode(self.gds_format_string(quote_xml(self.title), input_name='title')),
                namespaceprefix_, eol_))
        if self.firstAuthor is not None:
            namespaceprefix_ = self.firstAuthor_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.firstAuthor_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sfirstAuthor>%s</%sfirstAuthor>%s' % (namespaceprefix_, self.gds_encode(
                self.gds_format_string(quote_xml(self.firstAuthor), input_name='firstAuthor')), namespaceprefix_, eol_))
        for secondaryAuthors_ in self.secondaryAuthors:
            namespaceprefix_ = self.secondaryAuthors_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.secondaryAuthors_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%ssecondaryAuthors>%s</%ssecondaryAuthors>%s' % (namespaceprefix_, self.gds_encode(
                self.gds_format_string(quote_xml(secondaryAuthors_), input_name='secondaryAuthors')), namespaceprefix_,
                                                                             eol_))
        if self.year is not None:
            namespaceprefix_ = self.year_nsprefix_ + ':' if (UseCapturedNS_ and self.year_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%syear>%s</%syear>%s' % (
                namespaceprefix_, self.gds_format_integer(self.year, input_name='year'), namespaceprefix_, eol_))
        if self.booktitle is not None:
            namespaceprefix_ = self.booktitle_nsprefix_ + ':' if (UseCapturedNS_ and self.booktitle_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sbooktitle>%s</%sbooktitle>%s' % (namespaceprefix_, self.gds_encode(
                self.gds_format_string(quote_xml(self.booktitle), input_name='booktitle')), namespaceprefix_, eol_))
        if self.language is not None:
            namespaceprefix_ = self.language_nsprefix_ + ':' if (UseCapturedNS_ and self.language_nsprefix_) else ''
            self.language.export(outfile, level, namespaceprefix_, namespacedef_='', name_='language',
                                 pretty_print=pretty_print)
        if self.DOI is not None:
            namespaceprefix_ = self.DOI_nsprefix_ + ':' if (UseCapturedNS_ and self.DOI_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sDOI>%s</%sDOI>%s' % (
                namespaceprefix_, self.gds_encode(self.gds_format_string(quote_xml(self.DOI), input_name='DOI')),
                namespaceprefix_, eol_))

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def buildAttributes(self, node, attrs, already_processed):
        pass

    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'title':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'title')
            value_ = self.gds_validate_string(value_, node, 'title')
            self.title = value_
            self.title_nsprefix_ = child_.prefix
        elif nodeName_ == 'firstAuthor':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'firstAuthor')
            value_ = self.gds_validate_string(value_, node, 'firstAuthor')
            self.firstAuthor = value_
            self.firstAuthor_nsprefix_ = child_.prefix
        elif nodeName_ == 'secondaryAuthors':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'secondaryAuthors')
            value_ = self.gds_validate_string(value_, node, 'secondaryAuthors')
            self.secondaryAuthors.append(value_)
            self.secondaryAuthors_nsprefix_ = child_.prefix
        elif nodeName_ == 'year' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'year')
            ival_ = self.gds_validate_integer(ival_, node, 'year')
            self.year = ival_
            self.year_nsprefix_ = child_.prefix
        elif nodeName_ == 'booktitle':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'booktitle')
            value_ = self.gds_validate_string(value_, node, 'booktitle')
            self.booktitle = value_
            self.booktitle_nsprefix_ = child_.prefix
        elif nodeName_ == 'language':
            obj_ = language.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.language = obj_
            obj_.original_tagname_ = 'language'
        elif nodeName_ == 'DOI':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'DOI')
            value_ = self.gds_validate_string(value_, node, 'DOI')
            self.DOI = value_
            self.DOI_nsprefix_ = child_.prefix


# end class literatureSource


class language(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, code=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.code = code
        self.code_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, language)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if language.subclass:
            return language.subclass(*args_, **kwargs_)
        else:
            return language(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_code(self):
        return self.code

    def set_code(self, code):
        self.code = code

    def hasContent_(self):
        if (
                self.code is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ', name_='language',
               pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('language')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'language':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='language')
        if self.hasContent_():
            outfile.write('>%s' % (eol_,))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='language',
                                pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='language'):
        pass

    def exportChildren(self, outfile, level, namespaceprefix_='',
                       namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ', name_='language',
                       fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.code is not None:
            namespaceprefix_ = self.code_nsprefix_ + ':' if (UseCapturedNS_ and self.code_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scode>%s</%scode>%s' % (
                namespaceprefix_, self.gds_encode(self.gds_format_string(quote_xml(self.code), input_name='code')),
                namespaceprefix_, eol_))

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def buildAttributes(self, node, attrs, already_processed):
        pass

    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'code')
            value_ = self.gds_validate_string(value_, node, 'code')
            self.code = value_
            self.code_nsprefix_ = child_.prefix


# end class language


class FileResource(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, description=None, url=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.description = description
        self.description_nsprefix_ = None
        if url is None:
            self.url = []
        else:
            self.url = url
        self.url_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, FileResource)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if FileResource.subclass:
            return FileResource.subclass(*args_, **kwargs_)
        else:
            return FileResource(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def get_url(self):
        return self.url

    def set_url(self, url):
        self.url = url

    def add_url(self, value):
        self.url.append(value)

    def insert_url_at(self, index, value):
        self.url.insert(index, value)

    def replace_url_at(self, index, value):
        self.url[index] = value

    def hasContent_(self):
        if (
                self.description is not None or
                self.url
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ', name_='FileResource',
               pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('FileResource')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'FileResource':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='FileResource')
        if self.hasContent_():
            outfile.write('>%s' % (eol_,))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='FileResource',
                                pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='FileResource'):
        pass

    def exportChildren(self, outfile, level, namespaceprefix_='',
                       namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ',
                       name_='FileResource', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.description is not None:
            namespaceprefix_ = self.description_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.description_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdescription>%s</%sdescription>%s' % (namespaceprefix_, self.gds_encode(
                self.gds_format_string(quote_xml(self.description), input_name='description')), namespaceprefix_, eol_))
        for url_ in self.url:
            namespaceprefix_ = self.url_nsprefix_ + ':' if (UseCapturedNS_ and self.url_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%surl>%s</%surl>%s' % (
                namespaceprefix_, self.gds_encode(self.gds_format_string(quote_xml(url_), input_name='url')),
                namespaceprefix_, eol_))

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def buildAttributes(self, node, attrs, already_processed):
        pass

    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'description':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'description')
            value_ = self.gds_validate_string(value_, node, 'description')
            self.description = value_
            self.description_nsprefix_ = child_.prefix
        elif nodeName_ == 'url':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'url')
            value_ = self.gds_validate_string(value_, node, 'url')
            self.url.append(value_)
            self.url_nsprefix_ = child_.prefix


# end class FileResource


class velocityS30(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, value=None, uncertainty=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.value = value
        self.value_nsprefix_ = None
        self.uncertainty = uncertainty
        self.uncertainty_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, velocityS30)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if velocityS30.subclass:
            return velocityS30.subclass(*args_, **kwargs_)
        else:
            return velocityS30(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_uncertainty(self):
        return self.uncertainty

    def set_uncertainty(self, uncertainty):
        self.uncertainty = uncertainty

    def hasContent_(self):
        if (
                self.value is not None or
                self.uncertainty is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ', name_='velocityS30',
               pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('velocityS30')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'velocityS30':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='velocityS30')
        if self.hasContent_():
            outfile.write('>%s' % (eol_,))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='velocityS30',
                                pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='velocityS30'):
        pass

    def exportChildren(self, outfile, level, namespaceprefix_='',
                       namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ', name_='velocityS30',
                       fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.value is not None:
            namespaceprefix_ = self.value_nsprefix_ + ':' if (UseCapturedNS_ and self.value_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svalue>%s</%svalue>%s' % (
                namespaceprefix_, self.gds_format_double(self.value, input_name='value'), namespaceprefix_, eol_))
        if self.uncertainty is not None:
            namespaceprefix_ = self.uncertainty_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.uncertainty_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%suncertainty>%s</%suncertainty>%s' % (
                namespaceprefix_, self.gds_format_double(self.uncertainty, input_name='uncertainty'), namespaceprefix_,
                eol_))

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def buildAttributes(self, node, attrs, already_processed):
        pass

    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'value' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'value')
            fval_ = self.gds_validate_double(fval_, node, 'value')
            self.value = fval_
            self.value_nsprefix_ = child_.prefix
        elif nodeName_ == 'uncertainty' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'uncertainty')
            fval_ = self.gds_validate_double(fval_, node, 'uncertainty')
            self.uncertainty = fval_
            self.uncertainty_nsprefix_ = child_.prefix


# end class velocityS30


class velocityS30Qindex1(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, value=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.value = value
        self.value_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, velocityS30Qindex1)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if velocityS30Qindex1.subclass:
            return velocityS30Qindex1.subclass(*args_, **kwargs_)
        else:
            return velocityS30Qindex1(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def hasContent_(self):
        if (
                self.value is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ', name_='velocityS30Qindex1',
               pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('velocityS30Qindex1')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'velocityS30Qindex1':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='velocityS30Qindex1')
        if self.hasContent_():
            outfile.write('>%s' % (eol_,))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='velocityS30Qindex1',
                                pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='velocityS30Qindex1'):
        pass

    def exportChildren(self, outfile, level, namespaceprefix_='',
                       namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ',
                       name_='velocityS30Qindex1', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.value is not None:
            namespaceprefix_ = self.value_nsprefix_ + ':' if (UseCapturedNS_ and self.value_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svalue>%s</%svalue>%s' % (
                namespaceprefix_, self.gds_format_double(self.value, input_name='value'), namespaceprefix_, eol_))

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def buildAttributes(self, node, attrs, already_processed):
        pass

    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'value' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'value')
            fval_ = self.gds_validate_double(fval_, node, 'value')
            self.value = fval_
            self.value_nsprefix_ = child_.prefix


# end class velocityS30Qindex1


class velocityS30Reference(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, literatureSource=None, FileResource=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.literatureSource = literatureSource
        self.literatureSource_nsprefix_ = None
        self.FileResource = FileResource
        self.FileResource_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, velocityS30Reference)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if velocityS30Reference.subclass:
            return velocityS30Reference.subclass(*args_, **kwargs_)
        else:
            return velocityS30Reference(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_literatureSource(self):
        return self.literatureSource

    def set_literatureSource(self, literatureSource):
        self.literatureSource = literatureSource

    def get_FileResource(self):
        return self.FileResource

    def set_FileResource(self, FileResource):
        self.FileResource = FileResource

    def hasContent_(self):
        if (
                self.literatureSource is not None or
                self.FileResource is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ',
               name_='velocityS30Reference', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('velocityS30Reference')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'velocityS30Reference':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='velocityS30Reference')
        if self.hasContent_():
            outfile.write('>%s' % (eol_,))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='velocityS30Reference',
                                pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='',
                         name_='velocityS30Reference'):
        pass

    def exportChildren(self, outfile, level, namespaceprefix_='',
                       namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ',
                       name_='velocityS30Reference', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.literatureSource is not None:
            namespaceprefix_ = self.literatureSource_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.literatureSource_nsprefix_) else ''
            self.literatureSource.export(outfile, level, namespaceprefix_, namespacedef_='', name_='literatureSource',
                                         pretty_print=pretty_print)
        if self.FileResource is not None:
            namespaceprefix_ = self.FileResource_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.FileResource_nsprefix_) else ''
            self.FileResource.export(outfile, level, namespaceprefix_, namespacedef_='', name_='FileResource',
                                     pretty_print=pretty_print)

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def buildAttributes(self, node, attrs, already_processed):
        pass

    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'literatureSource':
            obj_ = literatureSource.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.literatureSource = obj_
            obj_.original_tagname_ = 'literatureSource'
        elif nodeName_ == 'FileResource':
            obj_ = FileResource.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.FileResource = obj_
            obj_.original_tagname_ = 'FileResource'


# end class velocityS30Reference


class velocityProfileCount(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, value=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.value = value
        self.value_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, velocityProfileCount)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if velocityProfileCount.subclass:
            return velocityProfileCount.subclass(*args_, **kwargs_)
        else:
            return velocityProfileCount(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def hasContent_(self):
        if (
                self.value is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ',
               name_='velocityProfileCount', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('velocityProfileCount')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'velocityProfileCount':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='velocityProfileCount')
        if self.hasContent_():
            outfile.write('>%s' % (eol_,))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='velocityProfileCount',
                                pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='',
                         name_='velocityProfileCount'):
        pass

    def exportChildren(self, outfile, level, namespaceprefix_='',
                       namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ',
                       name_='velocityProfileCount', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.value is not None:
            namespaceprefix_ = self.value_nsprefix_ + ':' if (UseCapturedNS_ and self.value_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svalue>%s</%svalue>%s' % (
                namespaceprefix_, self.gds_format_integer(self.value, input_name='value'), namespaceprefix_, eol_))

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def buildAttributes(self, node, attrs, already_processed):
        pass

    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'value' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'value')
            ival_ = self.gds_validate_integer(ival_, node, 'value')
            self.value = ival_
            self.value_nsprefix_ = child_.prefix


# end class velocityProfileCount


class sptLogsCount(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, value=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.value = value
        self.value_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, sptLogsCount)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if sptLogsCount.subclass:
            return sptLogsCount.subclass(*args_, **kwargs_)
        else:
            return sptLogsCount(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def hasContent_(self):
        if (
                self.value is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ', name_='sptLogsCount',
               pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('sptLogsCount')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'sptLogsCount':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='sptLogsCount')
        if self.hasContent_():
            outfile.write('>%s' % (eol_,))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='sptLogsCount',
                                pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='sptLogsCount'):
        pass

    def exportChildren(self, outfile, level, namespaceprefix_='',
                       namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ',
                       name_='sptLogsCount', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.value is not None:
            namespaceprefix_ = self.value_nsprefix_ + ':' if (UseCapturedNS_ and self.value_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svalue>%s</%svalue>%s' % (
                namespaceprefix_, self.gds_format_integer(self.value, input_name='value'), namespaceprefix_, eol_))

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def buildAttributes(self, node, attrs, already_processed):
        pass

    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'value' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'value')
            ival_ = self.gds_validate_integer(ival_, node, 'value')
            self.value = ival_
            self.value_nsprefix_ = child_.prefix


# end class sptLogsCount


class cptLogsCount(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, value=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.value = value
        self.value_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, cptLogsCount)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if cptLogsCount.subclass:
            return cptLogsCount.subclass(*args_, **kwargs_)
        else:
            return cptLogsCount(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def hasContent_(self):
        if (
                self.value is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ', name_='cptLogsCount',
               pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('cptLogsCount')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'cptLogsCount':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='cptLogsCount')
        if self.hasContent_():
            outfile.write('>%s' % (eol_,))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='cptLogsCount',
                                pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='cptLogsCount'):
        pass

    def exportChildren(self, outfile, level, namespaceprefix_='',
                       namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ',
                       name_='cptLogsCount', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.value is not None:
            namespaceprefix_ = self.value_nsprefix_ + ':' if (UseCapturedNS_ and self.value_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svalue>%s</%svalue>%s' % (
                namespaceprefix_, self.gds_format_integer(self.value, input_name='value'), namespaceprefix_, eol_))

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def buildAttributes(self, node, attrs, already_processed):
        pass

    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'value' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'value')
            ival_ = self.gds_validate_integer(ival_, node, 'value')
            self.value = ival_
            self.value_nsprefix_ = child_.prefix


# end class cptLogsCount


class boreholeLogsCount(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, value=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.value = value
        self.value_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, boreholeLogsCount)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if boreholeLogsCount.subclass:
            return boreholeLogsCount.subclass(*args_, **kwargs_)
        else:
            return boreholeLogsCount(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def hasContent_(self):
        if (
                self.value is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ', name_='boreholeLogsCount',
               pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('boreholeLogsCount')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'boreholeLogsCount':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='boreholeLogsCount')
        if self.hasContent_():
            outfile.write('>%s' % (eol_,))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='boreholeLogsCount',
                                pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='boreholeLogsCount'):
        pass

    def exportChildren(self, outfile, level, namespaceprefix_='',
                       namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ',
                       name_='boreholeLogsCount', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.value is not None:
            namespaceprefix_ = self.value_nsprefix_ + ':' if (UseCapturedNS_ and self.value_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svalue>%s</%svalue>%s' % (
                namespaceprefix_, self.gds_format_integer(self.value, input_name='value'), namespaceprefix_, eol_))

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def buildAttributes(self, node, attrs, already_processed):
        pass

    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'value' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'value')
            ival_ = self.gds_validate_integer(ival_, node, 'value')
            self.value = ival_
            self.value_nsprefix_ = child_.prefix


# end class boreholeLogsCount


class VelocityProfile(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, layerCount=None, velocityProfileData=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if layerCount is None:
            self.layerCount = []
        else:
            self.layerCount = layerCount
        self.layerCount_nsprefix_ = None
        if velocityProfileData is None:
            self.velocityProfileData = []
        else:
            self.velocityProfileData = velocityProfileData
        self.velocityProfileData_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, VelocityProfile)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if VelocityProfile.subclass:
            return VelocityProfile.subclass(*args_, **kwargs_)
        else:
            return VelocityProfile(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_layerCount(self):
        return self.layerCount

    def set_layerCount(self, layerCount):
        self.layerCount = layerCount

    def add_layerCount(self, value):
        self.layerCount.append(value)

    def insert_layerCount_at(self, index, value):
        self.layerCount.insert(index, value)

    def replace_layerCount_at(self, index, value):
        self.layerCount[index] = value

    def get_velocityProfileData(self):
        return self.velocityProfileData

    def set_velocityProfileData(self, velocityProfileData):
        self.velocityProfileData = velocityProfileData

    def add_velocityProfileData(self, value):
        self.velocityProfileData.append(value)

    def insert_velocityProfileData_at(self, index, value):
        self.velocityProfileData.insert(index, value)

    def replace_velocityProfileData_at(self, index, value):
        self.velocityProfileData[index] = value

    def hasContent_(self):
        if (
                self.layerCount or
                self.velocityProfileData
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ', name_='VelocityProfile',
               pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('VelocityProfile')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'VelocityProfile':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='VelocityProfile')
        if self.hasContent_():
            outfile.write('>%s' % (eol_,))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='VelocityProfile',
                                pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='VelocityProfile'):
        pass

    def exportChildren(self, outfile, level, namespaceprefix_='',
                       namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ',
                       name_='VelocityProfile', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for layerCount_ in self.layerCount:
            namespaceprefix_ = self.layerCount_nsprefix_ + ':' if (UseCapturedNS_ and self.layerCount_nsprefix_) else ''
            layerCount_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='layerCount',
                               pretty_print=pretty_print)
        for velocityProfileData_ in self.velocityProfileData:
            namespaceprefix_ = self.velocityProfileData_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.velocityProfileData_nsprefix_) else ''
            velocityProfileData_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='velocityProfileData',
                                        pretty_print=pretty_print)

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def buildAttributes(self, node, attrs, already_processed):
        pass

    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'layerCount':
            obj_ = layerCount.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.layerCount.append(obj_)
            obj_.original_tagname_ = 'layerCount'
        elif nodeName_ == 'velocityProfileData':
            obj_ = velocityProfileData.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.velocityProfileData.append(obj_)
            obj_.original_tagname_ = 'velocityProfileData'


# end class VelocityProfile


class layerCount(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, value=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.value = value
        self.value_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, layerCount)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if layerCount.subclass:
            return layerCount.subclass(*args_, **kwargs_)
        else:
            return layerCount(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def hasContent_(self):
        if (
                self.value is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ', name_='layerCount',
               pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('layerCount')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'layerCount':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='layerCount')
        if self.hasContent_():
            outfile.write('>%s' % (eol_,))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='layerCount',
                                pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='layerCount'):
        pass

    def exportChildren(self, outfile, level, namespaceprefix_='',
                       namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ', name_='layerCount',
                       fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.value is not None:
            namespaceprefix_ = self.value_nsprefix_ + ':' if (UseCapturedNS_ and self.value_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svalue>%s</%svalue>%s' % (
                namespaceprefix_, self.gds_format_integer(self.value, input_name='value'), namespaceprefix_, eol_))

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def buildAttributes(self, node, attrs, already_processed):
        pass

    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'value' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'value')
            ival_ = self.gds_validate_integer(ival_, node, 'value')
            self.value = ival_
            self.value_nsprefix_ = child_.prefix


# end class layerCount


class velocityProfileData(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, density=None, velocityP=None, velocityS=None, layerThickness=None, gds_collector_=None,
                 **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if density is None:
            self.density = []
        else:
            self.density = density
        self.density_nsprefix_ = None
        if velocityP is None:
            self.velocityP = []
        else:
            self.velocityP = velocityP
        self.velocityP_nsprefix_ = None
        if velocityS is None:
            self.velocityS = []
        else:
            self.velocityS = velocityS
        self.velocityS_nsprefix_ = None
        if layerThickness is None:
            self.layerThickness = []
        else:
            self.layerThickness = layerThickness
        self.layerThickness_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, velocityProfileData)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if velocityProfileData.subclass:
            return velocityProfileData.subclass(*args_, **kwargs_)
        else:
            return velocityProfileData(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_density(self):
        return self.density

    def set_density(self, density):
        self.density = density

    def add_density(self, value):
        self.density.append(value)

    def insert_density_at(self, index, value):
        self.density.insert(index, value)

    def replace_density_at(self, index, value):
        self.density[index] = value

    def get_velocityP(self):
        return self.velocityP

    def set_velocityP(self, velocityP):
        self.velocityP = velocityP

    def add_velocityP(self, value):
        self.velocityP.append(value)

    def insert_velocityP_at(self, index, value):
        self.velocityP.insert(index, value)

    def replace_velocityP_at(self, index, value):
        self.velocityP[index] = value

    def get_velocityS(self):
        return self.velocityS

    def set_velocityS(self, velocityS):
        self.velocityS = velocityS

    def add_velocityS(self, value):
        self.velocityS.append(value)

    def insert_velocityS_at(self, index, value):
        self.velocityS.insert(index, value)

    def replace_velocityS_at(self, index, value):
        self.velocityS[index] = value

    def get_layerThickness(self):
        return self.layerThickness

    def set_layerThickness(self, layerThickness):
        self.layerThickness = layerThickness

    def add_layerThickness(self, value):
        self.layerThickness.append(value)

    def insert_layerThickness_at(self, index, value):
        self.layerThickness.insert(index, value)

    def replace_layerThickness_at(self, index, value):
        self.layerThickness[index] = value

    def hasContent_(self):
        if (
                self.density or
                self.velocityP or
                self.velocityS or
                self.layerThickness
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ', name_='velocityProfileData',
               pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('velocityProfileData')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'velocityProfileData':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='velocityProfileData')
        if self.hasContent_():
            outfile.write('>%s' % (eol_,))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='velocityProfileData',
                                pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='velocityProfileData'):
        pass

    def exportChildren(self, outfile, level, namespaceprefix_='',
                       namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ',
                       name_='velocityProfileData', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for density_ in self.density:
            namespaceprefix_ = self.density_nsprefix_ + ':' if (UseCapturedNS_ and self.density_nsprefix_) else ''
            density_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='density',
                            pretty_print=pretty_print)
        for velocityP_ in self.velocityP:
            namespaceprefix_ = self.velocityP_nsprefix_ + ':' if (UseCapturedNS_ and self.velocityP_nsprefix_) else ''
            velocityP_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='velocityP',
                              pretty_print=pretty_print)
        for velocityS_ in self.velocityS:
            namespaceprefix_ = self.velocityS_nsprefix_ + ':' if (UseCapturedNS_ and self.velocityS_nsprefix_) else ''
            velocityS_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='velocityS',
                              pretty_print=pretty_print)
        for layerThickness_ in self.layerThickness:
            namespaceprefix_ = self.layerThickness_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.layerThickness_nsprefix_) else ''
            layerThickness_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='layerThickness',
                                   pretty_print=pretty_print)

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def buildAttributes(self, node, attrs, already_processed):
        pass

    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'density':
            obj_ = density.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.density.append(obj_)
            obj_.original_tagname_ = 'density'
        elif nodeName_ == 'velocityP':
            obj_ = velocityP.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.velocityP.append(obj_)
            obj_.original_tagname_ = 'velocityP'
        elif nodeName_ == 'velocityS':
            obj_ = velocityS.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.velocityS.append(obj_)
            obj_.original_tagname_ = 'velocityS'
        elif nodeName_ == 'layerThickness':
            obj_ = layerThickness.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.layerThickness.append(obj_)
            obj_.original_tagname_ = 'layerThickness'


# end class velocityProfileData


class density(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, value=None, uncertainty=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.value = value
        self.value_nsprefix_ = None
        self.uncertainty = uncertainty
        self.uncertainty_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, density)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if density.subclass:
            return density.subclass(*args_, **kwargs_)
        else:
            return density(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_uncertainty(self):
        return self.uncertainty

    def set_uncertainty(self, uncertainty):
        self.uncertainty = uncertainty

    def hasContent_(self):
        if (
                self.value is not None or
                self.uncertainty is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ', name_='density',
               pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('density')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'density':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='density')
        if self.hasContent_():
            outfile.write('>%s' % (eol_,))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='density',
                                pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='density'):
        pass

    def exportChildren(self, outfile, level, namespaceprefix_='',
                       namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ', name_='density',
                       fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.value is not None:
            namespaceprefix_ = self.value_nsprefix_ + ':' if (UseCapturedNS_ and self.value_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svalue>%s</%svalue>%s' % (
                namespaceprefix_, self.gds_format_double(self.value, input_name='value'), namespaceprefix_, eol_))
        if self.uncertainty is not None:
            namespaceprefix_ = self.uncertainty_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.uncertainty_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%suncertainty>%s</%suncertainty>%s' % (
                namespaceprefix_, self.gds_format_double(self.uncertainty, input_name='uncertainty'), namespaceprefix_,
                eol_))

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def buildAttributes(self, node, attrs, already_processed):
        pass

    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'value' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'value')
            fval_ = self.gds_validate_double(fval_, node, 'value')
            self.value = fval_
            self.value_nsprefix_ = child_.prefix
        elif nodeName_ == 'uncertainty' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'uncertainty')
            fval_ = self.gds_validate_double(fval_, node, 'uncertainty')
            self.uncertainty = fval_
            self.uncertainty_nsprefix_ = child_.prefix


# end class density


class velocityP(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, value=None, uncertainty=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.value = value
        self.value_nsprefix_ = None
        self.uncertainty = uncertainty
        self.uncertainty_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, velocityP)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if velocityP.subclass:
            return velocityP.subclass(*args_, **kwargs_)
        else:
            return velocityP(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_uncertainty(self):
        return self.uncertainty

    def set_uncertainty(self, uncertainty):
        self.uncertainty = uncertainty

    def hasContent_(self):
        if (
                self.value is not None or
                self.uncertainty is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ', name_='velocityP',
               pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('velocityP')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'velocityP':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='velocityP')
        if self.hasContent_():
            outfile.write('>%s' % (eol_,))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='velocityP',
                                pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='velocityP'):
        pass

    def exportChildren(self, outfile, level, namespaceprefix_='',
                       namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ', name_='velocityP',
                       fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.value is not None:
            namespaceprefix_ = self.value_nsprefix_ + ':' if (UseCapturedNS_ and self.value_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svalue>%s</%svalue>%s' % (
                namespaceprefix_, self.gds_format_double(self.value, input_name='value'), namespaceprefix_, eol_))
        if self.uncertainty is not None:
            namespaceprefix_ = self.uncertainty_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.uncertainty_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%suncertainty>%s</%suncertainty>%s' % (
                namespaceprefix_, self.gds_format_double(self.uncertainty, input_name='uncertainty'), namespaceprefix_,
                eol_))

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def buildAttributes(self, node, attrs, already_processed):
        pass

    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'value' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'value')
            fval_ = self.gds_validate_double(fval_, node, 'value')
            self.value = fval_
            self.value_nsprefix_ = child_.prefix
        elif nodeName_ == 'uncertainty' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'uncertainty')
            fval_ = self.gds_validate_double(fval_, node, 'uncertainty')
            self.uncertainty = fval_
            self.uncertainty_nsprefix_ = child_.prefix


# end class velocityP


class velocityS(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, value=None, uncertainty=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.value = value
        self.value_nsprefix_ = None
        self.uncertainty = uncertainty
        self.uncertainty_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, velocityS)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if velocityS.subclass:
            return velocityS.subclass(*args_, **kwargs_)
        else:
            return velocityS(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_uncertainty(self):
        return self.uncertainty

    def set_uncertainty(self, uncertainty):
        self.uncertainty = uncertainty

    def hasContent_(self):
        if (
                self.value is not None or
                self.uncertainty is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ', name_='velocityS',
               pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('velocityS')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'velocityS':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='velocityS')
        if self.hasContent_():
            outfile.write('>%s' % (eol_,))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='velocityS',
                                pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='velocityS'):
        pass

    def exportChildren(self, outfile, level, namespaceprefix_='',
                       namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ', name_='velocityS',
                       fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.value is not None:
            namespaceprefix_ = self.value_nsprefix_ + ':' if (UseCapturedNS_ and self.value_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svalue>%s</%svalue>%s' % (
                namespaceprefix_, self.gds_format_double(self.value, input_name='value'), namespaceprefix_, eol_))
        if self.uncertainty is not None:
            namespaceprefix_ = self.uncertainty_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.uncertainty_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%suncertainty>%s</%suncertainty>%s' % (
                namespaceprefix_, self.gds_format_double(self.uncertainty, input_name='uncertainty'), namespaceprefix_,
                eol_))

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def buildAttributes(self, node, attrs, already_processed):
        pass

    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'value' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'value')
            fval_ = self.gds_validate_double(fval_, node, 'value')
            self.value = fval_
            self.value_nsprefix_ = child_.prefix
        elif nodeName_ == 'uncertainty' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'uncertainty')
            fval_ = self.gds_validate_double(fval_, node, 'uncertainty')
            self.uncertainty = fval_
            self.uncertainty_nsprefix_ = child_.prefix


# end class velocityS


class layerThickness(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, layerTopDepth=None, layerBottomDepth=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.layerTopDepth = layerTopDepth
        self.layerTopDepth_nsprefix_ = None
        self.layerBottomDepth = layerBottomDepth
        self.layerBottomDepth_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, layerThickness)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if layerThickness.subclass:
            return layerThickness.subclass(*args_, **kwargs_)
        else:
            return layerThickness(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_layerTopDepth(self):
        return self.layerTopDepth

    def set_layerTopDepth(self, layerTopDepth):
        self.layerTopDepth = layerTopDepth

    def get_layerBottomDepth(self):
        return self.layerBottomDepth

    def set_layerBottomDepth(self, layerBottomDepth):
        self.layerBottomDepth = layerBottomDepth

    def hasContent_(self):
        if (
                self.layerTopDepth is not None or
                self.layerBottomDepth is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ', name_='layerThickness',
               pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('layerThickness')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'layerThickness':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='layerThickness')
        if self.hasContent_():
            outfile.write('>%s' % (eol_,))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='layerThickness',
                                pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='layerThickness'):
        pass

    def exportChildren(self, outfile, level, namespaceprefix_='',
                       namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ',
                       name_='layerThickness', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.layerTopDepth is not None:
            namespaceprefix_ = self.layerTopDepth_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.layerTopDepth_nsprefix_) else ''
            self.layerTopDepth.export(outfile, level, namespaceprefix_, namespacedef_='', name_='layerTopDepth',
                                      pretty_print=pretty_print)
        if self.layerBottomDepth is not None:
            namespaceprefix_ = self.layerBottomDepth_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.layerBottomDepth_nsprefix_) else ''
            self.layerBottomDepth.export(outfile, level, namespaceprefix_, namespacedef_='', name_='layerBottomDepth',
                                         pretty_print=pretty_print)

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def buildAttributes(self, node, attrs, already_processed):
        pass

    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'layerTopDepth':
            obj_ = layerTopDepth.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.layerTopDepth = obj_
            obj_.original_tagname_ = 'layerTopDepth'
        elif nodeName_ == 'layerBottomDepth':
            obj_ = layerBottomDepth.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.layerBottomDepth = obj_
            obj_.original_tagname_ = 'layerBottomDepth'


# end class layerThickness


class layerTopDepth(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, value=None, uncertainty=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.value = value
        self.value_nsprefix_ = None
        self.uncertainty = uncertainty
        self.uncertainty_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, layerTopDepth)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if layerTopDepth.subclass:
            return layerTopDepth.subclass(*args_, **kwargs_)
        else:
            return layerTopDepth(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_uncertainty(self):
        return self.uncertainty

    def set_uncertainty(self, uncertainty):
        self.uncertainty = uncertainty

    def hasContent_(self):
        if (
                self.value is not None or
                self.uncertainty is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ', name_='layerTopDepth',
               pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('layerTopDepth')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'layerTopDepth':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='layerTopDepth')
        if self.hasContent_():
            outfile.write('>%s' % (eol_,))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='layerTopDepth',
                                pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='layerTopDepth'):
        pass

    def exportChildren(self, outfile, level, namespaceprefix_='',
                       namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ',
                       name_='layerTopDepth', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.value is not None:
            namespaceprefix_ = self.value_nsprefix_ + ':' if (UseCapturedNS_ and self.value_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svalue>%s</%svalue>%s' % (
                namespaceprefix_, self.gds_format_double(self.value, input_name='value'), namespaceprefix_, eol_))
        if self.uncertainty is not None:
            namespaceprefix_ = self.uncertainty_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.uncertainty_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%suncertainty>%s</%suncertainty>%s' % (
                namespaceprefix_, self.gds_format_double(self.uncertainty, input_name='uncertainty'), namespaceprefix_,
                eol_))

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def buildAttributes(self, node, attrs, already_processed):
        pass

    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'value' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'value')
            fval_ = self.gds_validate_double(fval_, node, 'value')
            self.value = fval_
            self.value_nsprefix_ = child_.prefix
        elif nodeName_ == 'uncertainty' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'uncertainty')
            fval_ = self.gds_validate_double(fval_, node, 'uncertainty')
            self.uncertainty = fval_
            self.uncertainty_nsprefix_ = child_.prefix


# end class layerTopDepth


class layerBottomDepth(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, value=None, uncertainty=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.value = value
        self.value_nsprefix_ = None
        self.uncertainty = uncertainty
        self.uncertainty_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, layerBottomDepth)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if layerBottomDepth.subclass:
            return layerBottomDepth.subclass(*args_, **kwargs_)
        else:
            return layerBottomDepth(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_uncertainty(self):
        return self.uncertainty

    def set_uncertainty(self, uncertainty):
        self.uncertainty = uncertainty

    def hasContent_(self):
        if (
                self.value is not None or
                self.uncertainty is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ', name_='layerBottomDepth',
               pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('layerBottomDepth')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'layerBottomDepth':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='layerBottomDepth')
        if self.hasContent_():
            outfile.write('>%s' % (eol_,))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='layerBottomDepth',
                                pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='layerBottomDepth'):
        pass

    def exportChildren(self, outfile, level, namespaceprefix_='',
                       namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ',
                       name_='layerBottomDepth', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.value is not None:
            namespaceprefix_ = self.value_nsprefix_ + ':' if (UseCapturedNS_ and self.value_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svalue>%s</%svalue>%s' % (
                namespaceprefix_, self.gds_format_double(self.value, input_name='value'), namespaceprefix_, eol_))
        if self.uncertainty is not None:
            namespaceprefix_ = self.uncertainty_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.uncertainty_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%suncertainty>%s</%suncertainty>%s' % (
                namespaceprefix_, self.gds_format_double(self.uncertainty, input_name='uncertainty'), namespaceprefix_,
                eol_))

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def buildAttributes(self, node, attrs, already_processed):
        pass

    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'value' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'value')
            fval_ = self.gds_validate_double(fval_, node, 'value')
            self.value = fval_
            self.value_nsprefix_ = child_.prefix
        elif nodeName_ == 'uncertainty' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'uncertainty')
            fval_ = self.gds_validate_double(fval_, node, 'uncertainty')
            self.uncertainty = fval_
            self.uncertainty_nsprefix_ = child_.prefix


# end class layerBottomDepth


class velocityProfileQindex1(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, value=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.value = value
        self.value_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, velocityProfileQindex1)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if velocityProfileQindex1.subclass:
            return velocityProfileQindex1.subclass(*args_, **kwargs_)
        else:
            return velocityProfileQindex1(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def hasContent_(self):
        if (
                self.value is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ',
               name_='velocityProfileQindex1', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('velocityProfileQindex1')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'velocityProfileQindex1':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='velocityProfileQindex1')
        if self.hasContent_():
            outfile.write('>%s' % (eol_,))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='velocityProfileQindex1',
                                pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='',
                         name_='velocityProfileQindex1'):
        pass

    def exportChildren(self, outfile, level, namespaceprefix_='',
                       namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ',
                       name_='velocityProfileQindex1', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.value is not None:
            namespaceprefix_ = self.value_nsprefix_ + ':' if (UseCapturedNS_ and self.value_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svalue>%s</%svalue>%s' % (
                namespaceprefix_, self.gds_format_double(self.value, input_name='value'), namespaceprefix_, eol_))

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def buildAttributes(self, node, attrs, already_processed):
        pass

    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'value' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'value')
            fval_ = self.gds_validate_double(fval_, node, 'value')
            self.value = fval_
            self.value_nsprefix_ = child_.prefix


# end class velocityProfileQindex1


class velocityProfileReference(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, literatureSource=None, FileResource=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.literatureSource = literatureSource
        self.literatureSource_nsprefix_ = None
        self.FileResource = FileResource
        self.FileResource_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, velocityProfileReference)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if velocityProfileReference.subclass:
            return velocityProfileReference.subclass(*args_, **kwargs_)
        else:
            return velocityProfileReference(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_literatureSource(self):
        return self.literatureSource

    def set_literatureSource(self, literatureSource):
        self.literatureSource = literatureSource

    def get_FileResource(self):
        return self.FileResource

    def set_FileResource(self, FileResource):
        self.FileResource = FileResource

    def hasContent_(self):
        if (
                self.literatureSource is not None or
                self.FileResource is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ',
               name_='velocityProfileReference', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('velocityProfileReference')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'velocityProfileReference':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='velocityProfileReference')
        if self.hasContent_():
            outfile.write('>%s' % (eol_,))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_,
                                name_='velocityProfileReference', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='',
                         name_='velocityProfileReference'):
        pass

    def exportChildren(self, outfile, level, namespaceprefix_='',
                       namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ',
                       name_='velocityProfileReference', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.literatureSource is not None:
            namespaceprefix_ = self.literatureSource_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.literatureSource_nsprefix_) else ''
            self.literatureSource.export(outfile, level, namespaceprefix_, namespacedef_='', name_='literatureSource',
                                         pretty_print=pretty_print)
        if self.FileResource is not None:
            namespaceprefix_ = self.FileResource_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.FileResource_nsprefix_) else ''
            self.FileResource.export(outfile, level, namespaceprefix_, namespacedef_='', name_='FileResource',
                                     pretty_print=pretty_print)

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def buildAttributes(self, node, attrs, already_processed):
        pass

    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'literatureSource':
            obj_ = literatureSource.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.literatureSource = obj_
            obj_.original_tagname_ = 'literatureSource'
        elif nodeName_ == 'FileResource':
            obj_ = FileResource.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.FileResource = obj_
            obj_.original_tagname_ = 'FileResource'


# end class velocityProfileReference


class siteDescription(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, latitude=None, longitude=None, altitude=None, minDistanceFromStation=None,
                 maxDistanceFromStation=None, siteMorphology=None, siteTopology=None, OverallQindex=None,
                 gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.latitude = latitude
        self.latitude_nsprefix_ = None
        self.longitude = longitude
        self.longitude_nsprefix_ = None
        self.altitude = altitude
        self.altitude_nsprefix_ = None
        self.minDistanceFromStation = minDistanceFromStation
        self.minDistanceFromStation_nsprefix_ = None
        self.maxDistanceFromStation = maxDistanceFromStation
        self.maxDistanceFromStation_nsprefix_ = None
        self.siteMorphology = siteMorphology
        self.siteMorphology_nsprefix_ = None
        self.siteTopology = siteTopology
        self.siteTopology_nsprefix_ = None
        self.OverallQindex = OverallQindex
        self.OverallQindex_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, siteDescription)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if siteDescription.subclass:
            return siteDescription.subclass(*args_, **kwargs_)
        else:
            return siteDescription(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_latitude(self):
        return self.latitude

    def set_latitude(self, latitude):
        self.latitude = latitude

    def get_longitude(self):
        return self.longitude

    def set_longitude(self, longitude):
        self.longitude = longitude

    def get_altitude(self):
        return self.altitude

    def set_altitude(self, altitude):
        self.altitude = altitude

    def get_minDistanceFromStation(self):
        return self.minDistanceFromStation

    def set_minDistanceFromStation(self, minDistanceFromStation):
        self.minDistanceFromStation = minDistanceFromStation

    def get_maxDistanceFromStation(self):
        return self.maxDistanceFromStation

    def set_maxDistanceFromStation(self, maxDistanceFromStation):
        self.maxDistanceFromStation = maxDistanceFromStation

    def get_siteMorphology(self):
        return self.siteMorphology

    def set_siteMorphology(self, siteMorphology):
        self.siteMorphology = siteMorphology

    def get_siteTopology(self):
        return self.siteTopology

    def set_siteTopology(self, siteTopology):
        self.siteTopology = siteTopology

    def get_OverallQindex(self):
        return self.OverallQindex

    def set_OverallQindex(self, OverallQindex):
        self.OverallQindex = OverallQindex

    def hasContent_(self):
        if (
                self.latitude is not None or
                self.longitude is not None or
                self.altitude is not None or
                self.minDistanceFromStation is not None or
                self.maxDistanceFromStation is not None or
                self.siteMorphology is not None or
                self.siteTopology is not None or
                self.OverallQindex is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ', name_='siteDescription',
               pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('siteDescription')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'siteDescription':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='siteDescription')
        if self.hasContent_():
            outfile.write('>%s' % (eol_,))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='siteDescription',
                                pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='siteDescription'):
        pass

    def exportChildren(self, outfile, level, namespaceprefix_='',
                       namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ',
                       name_='siteDescription', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.latitude is not None:
            namespaceprefix_ = self.latitude_nsprefix_ + ':' if (UseCapturedNS_ and self.latitude_nsprefix_) else ''
            self.latitude.export(outfile, level, namespaceprefix_, namespacedef_='', name_='latitude',
                                 pretty_print=pretty_print)
        if self.longitude is not None:
            namespaceprefix_ = self.longitude_nsprefix_ + ':' if (UseCapturedNS_ and self.longitude_nsprefix_) else ''
            self.longitude.export(outfile, level, namespaceprefix_, namespacedef_='', name_='longitude',
                                  pretty_print=pretty_print)
        if self.altitude is not None:
            namespaceprefix_ = self.altitude_nsprefix_ + ':' if (UseCapturedNS_ and self.altitude_nsprefix_) else ''
            self.altitude.export(outfile, level, namespaceprefix_, namespacedef_='', name_='altitude',
                                 pretty_print=pretty_print)
        if self.minDistanceFromStation is not None:
            namespaceprefix_ = self.minDistanceFromStation_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.minDistanceFromStation_nsprefix_) else ''
            self.minDistanceFromStation.export(outfile, level, namespaceprefix_, namespacedef_='',
                                               name_='minDistanceFromStation', pretty_print=pretty_print)
        if self.maxDistanceFromStation is not None:
            namespaceprefix_ = self.maxDistanceFromStation_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.maxDistanceFromStation_nsprefix_) else ''
            self.maxDistanceFromStation.export(outfile, level, namespaceprefix_, namespacedef_='',
                                               name_='maxDistanceFromStation', pretty_print=pretty_print)
        if self.siteMorphology is not None:
            namespaceprefix_ = self.siteMorphology_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.siteMorphology_nsprefix_) else ''
            self.siteMorphology.export(outfile, level, namespaceprefix_, namespacedef_='', name_='siteMorphology',
                                       pretty_print=pretty_print)
        if self.siteTopology is not None:
            namespaceprefix_ = self.siteTopology_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.siteTopology_nsprefix_) else ''
            self.siteTopology.export(outfile, level, namespaceprefix_, namespacedef_='', name_='siteTopology',
                                     pretty_print=pretty_print)
        if self.OverallQindex is not None:
            namespaceprefix_ = self.OverallQindex_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.OverallQindex_nsprefix_) else ''
            self.OverallQindex.export(outfile, level, namespaceprefix_, namespacedef_='', name_='OverallQindex',
                                      pretty_print=pretty_print)

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def buildAttributes(self, node, attrs, already_processed):
        pass

    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'latitude':
            obj_ = latitude.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.latitude = obj_
            obj_.original_tagname_ = 'latitude'
        elif nodeName_ == 'longitude':
            obj_ = longitude.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.longitude = obj_
            obj_.original_tagname_ = 'longitude'
        elif nodeName_ == 'altitude':
            obj_ = altitude.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.altitude = obj_
            obj_.original_tagname_ = 'altitude'
        elif nodeName_ == 'minDistanceFromStation':
            obj_ = minDistanceFromStation.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.minDistanceFromStation = obj_
            obj_.original_tagname_ = 'minDistanceFromStation'
        elif nodeName_ == 'maxDistanceFromStation':
            obj_ = maxDistanceFromStation.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.maxDistanceFromStation = obj_
            obj_.original_tagname_ = 'maxDistanceFromStation'
        elif nodeName_ == 'siteMorphology':
            obj_ = siteMorphology.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.siteMorphology = obj_
            obj_.original_tagname_ = 'siteMorphology'
        elif nodeName_ == 'siteTopology':
            obj_ = siteTopology.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.siteTopology = obj_
            obj_.original_tagname_ = 'siteTopology'
        elif nodeName_ == 'OverallQindex':
            obj_ = OverallQindex.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.OverallQindex = obj_
            obj_.original_tagname_ = 'OverallQindex'


# end class siteDescription


class latitude(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, value=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.value = value
        self.value_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, latitude)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if latitude.subclass:
            return latitude.subclass(*args_, **kwargs_)
        else:
            return latitude(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def hasContent_(self):
        if (
                self.value is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ', name_='latitude',
               pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('latitude')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'latitude':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='latitude')
        if self.hasContent_():
            outfile.write('>%s' % (eol_,))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='latitude',
                                pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='latitude'):
        pass

    def exportChildren(self, outfile, level, namespaceprefix_='',
                       namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ', name_='latitude',
                       fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.value is not None:
            namespaceprefix_ = self.value_nsprefix_ + ':' if (UseCapturedNS_ and self.value_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svalue>%s</%svalue>%s' % (
                namespaceprefix_, self.gds_format_double(self.value, input_name='value'), namespaceprefix_, eol_))

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def buildAttributes(self, node, attrs, already_processed):
        pass

    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'value' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'value')
            fval_ = self.gds_validate_double(fval_, node, 'value')
            self.value = fval_
            self.value_nsprefix_ = child_.prefix


# end class latitude


class longitude(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, value=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.value = value
        self.value_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, longitude)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if longitude.subclass:
            return longitude.subclass(*args_, **kwargs_)
        else:
            return longitude(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def hasContent_(self):
        if (
                self.value is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ', name_='longitude',
               pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('longitude')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'longitude':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='longitude')
        if self.hasContent_():
            outfile.write('>%s' % (eol_,))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='longitude',
                                pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='longitude'):
        pass

    def exportChildren(self, outfile, level, namespaceprefix_='',
                       namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ', name_='longitude',
                       fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.value is not None:
            namespaceprefix_ = self.value_nsprefix_ + ':' if (UseCapturedNS_ and self.value_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svalue>%s</%svalue>%s' % (
                namespaceprefix_, self.gds_format_double(self.value, input_name='value'), namespaceprefix_, eol_))

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def buildAttributes(self, node, attrs, already_processed):
        pass

    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'value' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'value')
            fval_ = self.gds_validate_double(fval_, node, 'value')
            self.value = fval_
            self.value_nsprefix_ = child_.prefix


# end class longitude


class altitude(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, value=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.value = value
        self.value_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, altitude)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if altitude.subclass:
            return altitude.subclass(*args_, **kwargs_)
        else:
            return altitude(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def hasContent_(self):
        if (
                self.value is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ', name_='altitude',
               pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('altitude')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'altitude':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='altitude')
        if self.hasContent_():
            outfile.write('>%s' % (eol_,))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='altitude',
                                pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='altitude'):
        pass

    def exportChildren(self, outfile, level, namespaceprefix_='',
                       namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ', name_='altitude',
                       fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.value is not None:
            namespaceprefix_ = self.value_nsprefix_ + ':' if (UseCapturedNS_ and self.value_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svalue>%s</%svalue>%s' % (
                namespaceprefix_, self.gds_format_double(self.value, input_name='value'), namespaceprefix_, eol_))

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def buildAttributes(self, node, attrs, already_processed):
        pass

    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'value' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'value')
            fval_ = self.gds_validate_double(fval_, node, 'value')
            self.value = fval_
            self.value_nsprefix_ = child_.prefix


# end class altitude


class minDistanceFromStation(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, value=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.value = value
        self.value_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, minDistanceFromStation)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if minDistanceFromStation.subclass:
            return minDistanceFromStation.subclass(*args_, **kwargs_)
        else:
            return minDistanceFromStation(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def hasContent_(self):
        if (
                self.value is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ',
               name_='minDistanceFromStation', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('minDistanceFromStation')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'minDistanceFromStation':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='minDistanceFromStation')
        if self.hasContent_():
            outfile.write('>%s' % (eol_,))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='minDistanceFromStation',
                                pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='',
                         name_='minDistanceFromStation'):
        pass

    def exportChildren(self, outfile, level, namespaceprefix_='',
                       namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ',
                       name_='minDistanceFromStation', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.value is not None:
            namespaceprefix_ = self.value_nsprefix_ + ':' if (UseCapturedNS_ and self.value_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svalue>%s</%svalue>%s' % (
                namespaceprefix_, self.gds_format_double(self.value, input_name='value'), namespaceprefix_, eol_))

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def buildAttributes(self, node, attrs, already_processed):
        pass

    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'value' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'value')
            fval_ = self.gds_validate_double(fval_, node, 'value')
            self.value = fval_
            self.value_nsprefix_ = child_.prefix


# end class minDistanceFromStation


class maxDistanceFromStation(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, value=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.value = value
        self.value_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, maxDistanceFromStation)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if maxDistanceFromStation.subclass:
            return maxDistanceFromStation.subclass(*args_, **kwargs_)
        else:
            return maxDistanceFromStation(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def hasContent_(self):
        if (
                self.value is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ',
               name_='maxDistanceFromStation', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('maxDistanceFromStation')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'maxDistanceFromStation':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='maxDistanceFromStation')
        if self.hasContent_():
            outfile.write('>%s' % (eol_,))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='maxDistanceFromStation',
                                pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='',
                         name_='maxDistanceFromStation'):
        pass

    def exportChildren(self, outfile, level, namespaceprefix_='',
                       namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ',
                       name_='maxDistanceFromStation', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.value is not None:
            namespaceprefix_ = self.value_nsprefix_ + ':' if (UseCapturedNS_ and self.value_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svalue>%s</%svalue>%s' % (
                namespaceprefix_, self.gds_format_double(self.value, input_name='value'), namespaceprefix_, eol_))

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def buildAttributes(self, node, attrs, already_processed):
        pass

    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'value' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'value')
            fval_ = self.gds_validate_double(fval_, node, 'value')
            self.value = fval_
            self.value_nsprefix_ = child_.prefix


# end class maxDistanceFromStation


class siteMorphology(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, siteClassEC8=None, siteClassEC8Qindex1=None, siteClassEC8Reference=None, bedrockDepth=None,
                 bedrockDepthQindex1=None, bedrockDepthReference=None, h800=None, h800Qindex1=None, h800Reference=None,
                 geologicalUnit=None, geologicalUnitQindex1=None, geologicalMapScale=None, geologicalUnitOGE=None,
                 geologicalUnitReference=None, morphology=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.siteClassEC8 = siteClassEC8
        self.siteClassEC8_nsprefix_ = None
        self.siteClassEC8Qindex1 = siteClassEC8Qindex1
        self.siteClassEC8Qindex1_nsprefix_ = None
        self.siteClassEC8Reference = siteClassEC8Reference
        self.siteClassEC8Reference_nsprefix_ = None
        self.bedrockDepth = bedrockDepth
        self.bedrockDepth_nsprefix_ = None
        self.bedrockDepthQindex1 = bedrockDepthQindex1
        self.bedrockDepthQindex1_nsprefix_ = None
        self.bedrockDepthReference = bedrockDepthReference
        self.bedrockDepthReference_nsprefix_ = None
        self.h800 = h800
        self.h800_nsprefix_ = None
        self.h800Qindex1 = h800Qindex1
        self.h800Qindex1_nsprefix_ = None
        self.h800Reference = h800Reference
        self.h800Reference_nsprefix_ = None
        self.geologicalUnit = geologicalUnit
        if self.geologicalUnit is not None:
            self.validate_geologicalUnit(self.geologicalUnit)
        self.geologicalUnit_nsprefix_ = None
        self.geologicalUnitQindex1 = geologicalUnitQindex1
        self.geologicalUnitQindex1_nsprefix_ = None
        self.geologicalMapScale = geologicalMapScale
        self.geologicalMapScale_nsprefix_ = None
        self.geologicalUnitOGE = geologicalUnitOGE
        self.geologicalUnitOGE_nsprefix_ = None
        self.geologicalUnitReference = geologicalUnitReference
        self.geologicalUnitReference_nsprefix_ = None
        self.morphology = morphology
        self.morphology_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, siteMorphology)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if siteMorphology.subclass:
            return siteMorphology.subclass(*args_, **kwargs_)
        else:
            return siteMorphology(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_siteClassEC8(self):
        return self.siteClassEC8

    def set_siteClassEC8(self, siteClassEC8):
        self.siteClassEC8 = siteClassEC8

    def get_siteClassEC8Qindex1(self):
        return self.siteClassEC8Qindex1

    def set_siteClassEC8Qindex1(self, siteClassEC8Qindex1):
        self.siteClassEC8Qindex1 = siteClassEC8Qindex1

    def get_siteClassEC8Reference(self):
        return self.siteClassEC8Reference

    def set_siteClassEC8Reference(self, siteClassEC8Reference):
        self.siteClassEC8Reference = siteClassEC8Reference

    def get_bedrockDepth(self):
        return self.bedrockDepth

    def set_bedrockDepth(self, bedrockDepth):
        self.bedrockDepth = bedrockDepth

    def get_bedrockDepthQindex1(self):
        return self.bedrockDepthQindex1

    def set_bedrockDepthQindex1(self, bedrockDepthQindex1):
        self.bedrockDepthQindex1 = bedrockDepthQindex1

    def get_bedrockDepthReference(self):
        return self.bedrockDepthReference

    def set_bedrockDepthReference(self, bedrockDepthReference):
        self.bedrockDepthReference = bedrockDepthReference

    def get_h800(self):
        return self.h800

    def set_h800(self, h800):
        self.h800 = h800

    def get_h800Qindex1(self):
        return self.h800Qindex1

    def set_h800Qindex1(self, h800Qindex1):
        self.h800Qindex1 = h800Qindex1

    def get_h800Reference(self):
        return self.h800Reference

    def set_h800Reference(self, h800Reference):
        self.h800Reference = h800Reference

    def get_geologicalUnit(self):
        return self.geologicalUnit

    def set_geologicalUnit(self, geologicalUnit):
        self.geologicalUnit = geologicalUnit

    def get_geologicalUnitQindex1(self):
        return self.geologicalUnitQindex1

    def set_geologicalUnitQindex1(self, geologicalUnitQindex1):
        self.geologicalUnitQindex1 = geologicalUnitQindex1

    def get_geologicalMapScale(self):
        return self.geologicalMapScale

    def set_geologicalMapScale(self, geologicalMapScale):
        self.geologicalMapScale = geologicalMapScale

    def get_geologicalUnitOGE(self):
        return self.geologicalUnitOGE

    def set_geologicalUnitOGE(self, geologicalUnitOGE):
        self.geologicalUnitOGE = geologicalUnitOGE

    def get_geologicalUnitReference(self):
        return self.geologicalUnitReference

    def set_geologicalUnitReference(self, geologicalUnitReference):
        self.geologicalUnitReference = geologicalUnitReference

    def get_morphology(self):
        return self.morphology

    def set_morphology(self, morphology):
        self.morphology = morphology

    def validate_geologicalUnit(self, value):
        result = True
        # Validate type geologicalUnitType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value,
                                                                                                  "lineno": lineno, })
                return False
            if len(value) > 255:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on geologicalUnitType' % {
                        "value": encode_str_2_3(value), "lineno": lineno})
                result = False
        return result

    def hasContent_(self):
        if (
                self.siteClassEC8 is not None or
                self.siteClassEC8Qindex1 is not None or
                self.siteClassEC8Reference is not None or
                self.bedrockDepth is not None or
                self.bedrockDepthQindex1 is not None or
                self.bedrockDepthReference is not None or
                self.h800 is not None or
                self.h800Qindex1 is not None or
                self.h800Reference is not None or
                self.geologicalUnit is not None or
                self.geologicalUnitQindex1 is not None or
                self.geologicalMapScale is not None or
                self.geologicalUnitOGE is not None or
                self.geologicalUnitReference is not None or
                self.morphology is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ', name_='siteMorphology',
               pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('siteMorphology')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'siteMorphology':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='siteMorphology')
        if self.hasContent_():
            outfile.write('>%s' % (eol_,))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='siteMorphology',
                                pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='siteMorphology'):
        pass

    def exportChildren(self, outfile, level, namespaceprefix_='',
                       namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ',
                       name_='siteMorphology', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.siteClassEC8 is not None:
            namespaceprefix_ = self.siteClassEC8_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.siteClassEC8_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%ssiteClassEC8>%s</%ssiteClassEC8>%s' % (namespaceprefix_, self.gds_encode(
                self.gds_format_string(quote_xml(self.siteClassEC8), input_name='siteClassEC8')), namespaceprefix_,
                                                                     eol_))
        if self.siteClassEC8Qindex1 is not None:
            namespaceprefix_ = self.siteClassEC8Qindex1_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.siteClassEC8Qindex1_nsprefix_) else ''
            self.siteClassEC8Qindex1.export(outfile, level, namespaceprefix_, namespacedef_='',
                                            name_='siteClassEC8Qindex1', pretty_print=pretty_print)
        if self.siteClassEC8Reference is not None:
            namespaceprefix_ = self.siteClassEC8Reference_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.siteClassEC8Reference_nsprefix_) else ''
            self.siteClassEC8Reference.export(outfile, level, namespaceprefix_, namespacedef_='',
                                              name_='siteClassEC8Reference', pretty_print=pretty_print)
        if self.bedrockDepth is not None:
            namespaceprefix_ = self.bedrockDepth_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.bedrockDepth_nsprefix_) else ''
            self.bedrockDepth.export(outfile, level, namespaceprefix_, namespacedef_='', name_='bedrockDepth',
                                     pretty_print=pretty_print)
        if self.bedrockDepthQindex1 is not None:
            namespaceprefix_ = self.bedrockDepthQindex1_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.bedrockDepthQindex1_nsprefix_) else ''
            self.bedrockDepthQindex1.export(outfile, level, namespaceprefix_, namespacedef_='',
                                            name_='bedrockDepthQindex1', pretty_print=pretty_print)
        if self.bedrockDepthReference is not None:
            namespaceprefix_ = self.bedrockDepthReference_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.bedrockDepthReference_nsprefix_) else ''
            self.bedrockDepthReference.export(outfile, level, namespaceprefix_, namespacedef_='',
                                              name_='bedrockDepthReference', pretty_print=pretty_print)
        if self.h800 is not None:
            namespaceprefix_ = self.h800_nsprefix_ + ':' if (UseCapturedNS_ and self.h800_nsprefix_) else ''
            self.h800.export(outfile, level, namespaceprefix_, namespacedef_='', name_='h800',
                             pretty_print=pretty_print)
        if self.h800Qindex1 is not None:
            namespaceprefix_ = self.h800Qindex1_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.h800Qindex1_nsprefix_) else ''
            self.h800Qindex1.export(outfile, level, namespaceprefix_, namespacedef_='', name_='h800Qindex1',
                                    pretty_print=pretty_print)
        if self.h800Reference is not None:
            namespaceprefix_ = self.h800Reference_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.h800Reference_nsprefix_) else ''
            self.h800Reference.export(outfile, level, namespaceprefix_, namespacedef_='', name_='h800Reference',
                                      pretty_print=pretty_print)
        if self.geologicalUnit is not None:
            namespaceprefix_ = self.geologicalUnit_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.geologicalUnit_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sgeologicalUnit>%s</%sgeologicalUnit>%s' % (namespaceprefix_, self.gds_encode(
                self.gds_format_string(quote_xml(self.geologicalUnit), input_name='geologicalUnit')), namespaceprefix_,
                                                                         eol_))
        if self.geologicalUnitQindex1 is not None:
            namespaceprefix_ = self.geologicalUnitQindex1_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.geologicalUnitQindex1_nsprefix_) else ''
            self.geologicalUnitQindex1.export(outfile, level, namespaceprefix_, namespacedef_='',
                                              name_='geologicalUnitQindex1', pretty_print=pretty_print)
        if self.geologicalMapScale is not None:
            namespaceprefix_ = self.geologicalMapScale_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.geologicalMapScale_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sgeologicalMapScale>%s</%sgeologicalMapScale>%s' % (namespaceprefix_, self.gds_encode(
                self.gds_format_string(quote_xml(self.geologicalMapScale), input_name='geologicalMapScale')),
                                                                                 namespaceprefix_, eol_))
        if self.geologicalUnitOGE is not None:
            namespaceprefix_ = self.geologicalUnitOGE_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.geologicalUnitOGE_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sgeologicalUnitOGE>%s</%sgeologicalUnitOGE>%s' % (namespaceprefix_, self.gds_encode(
                self.gds_format_string(quote_xml(self.geologicalUnitOGE), input_name='geologicalUnitOGE')),
                                                                               namespaceprefix_, eol_))
        if self.geologicalUnitReference is not None:
            namespaceprefix_ = self.geologicalUnitReference_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.geologicalUnitReference_nsprefix_) else ''
            self.geologicalUnitReference.export(outfile, level, namespaceprefix_, namespacedef_='',
                                                name_='geologicalUnitReference', pretty_print=pretty_print)
        if self.morphology is not None:
            namespaceprefix_ = self.morphology_nsprefix_ + ':' if (UseCapturedNS_ and self.morphology_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smorphology>%s</%smorphology>%s' % (namespaceprefix_, self.gds_encode(
                self.gds_format_string(quote_xml(self.morphology), input_name='morphology')), namespaceprefix_, eol_))

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def buildAttributes(self, node, attrs, already_processed):
        pass

    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'siteClassEC8':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'siteClassEC8')
            value_ = self.gds_validate_string(value_, node, 'siteClassEC8')
            self.siteClassEC8 = value_
            self.siteClassEC8_nsprefix_ = child_.prefix
        elif nodeName_ == 'siteClassEC8Qindex1':
            obj_ = siteClassEC8Qindex1.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.siteClassEC8Qindex1 = obj_
            obj_.original_tagname_ = 'siteClassEC8Qindex1'
        elif nodeName_ == 'siteClassEC8Reference':
            obj_ = siteClassEC8Reference.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.siteClassEC8Reference = obj_
            obj_.original_tagname_ = 'siteClassEC8Reference'
        elif nodeName_ == 'bedrockDepth':
            obj_ = bedrockDepth.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.bedrockDepth = obj_
            obj_.original_tagname_ = 'bedrockDepth'
        elif nodeName_ == 'bedrockDepthQindex1':
            obj_ = bedrockDepthQindex1.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.bedrockDepthQindex1 = obj_
            obj_.original_tagname_ = 'bedrockDepthQindex1'
        elif nodeName_ == 'bedrockDepthReference':
            obj_ = bedrockDepthReference.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.bedrockDepthReference = obj_
            obj_.original_tagname_ = 'bedrockDepthReference'
        elif nodeName_ == 'h800':
            obj_ = h800.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.h800 = obj_
            obj_.original_tagname_ = 'h800'
        elif nodeName_ == 'h800Qindex1':
            obj_ = h800Qindex1.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.h800Qindex1 = obj_
            obj_.original_tagname_ = 'h800Qindex1'
        elif nodeName_ == 'h800Reference':
            obj_ = h800Reference.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.h800Reference = obj_
            obj_.original_tagname_ = 'h800Reference'
        elif nodeName_ == 'geologicalUnit':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'geologicalUnit')
            value_ = self.gds_validate_string(value_, node, 'geologicalUnit')
            self.geologicalUnit = value_
            self.geologicalUnit_nsprefix_ = child_.prefix
            # validate type geologicalUnitType
            self.validate_geologicalUnit(self.geologicalUnit)
        elif nodeName_ == 'geologicalUnitQindex1':
            obj_ = geologicalUnitQindex1.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.geologicalUnitQindex1 = obj_
            obj_.original_tagname_ = 'geologicalUnitQindex1'
        elif nodeName_ == 'geologicalMapScale':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'geologicalMapScale')
            value_ = self.gds_validate_string(value_, node, 'geologicalMapScale')
            self.geologicalMapScale = value_
            self.geologicalMapScale_nsprefix_ = child_.prefix
        elif nodeName_ == 'geologicalUnitOGE':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'geologicalUnitOGE')
            value_ = self.gds_validate_string(value_, node, 'geologicalUnitOGE')
            self.geologicalUnitOGE = value_
            self.geologicalUnitOGE_nsprefix_ = child_.prefix
        elif nodeName_ == 'geologicalUnitReference':
            obj_ = geologicalUnitReference.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.geologicalUnitReference = obj_
            obj_.original_tagname_ = 'geologicalUnitReference'
        elif nodeName_ == 'morphology':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'morphology')
            value_ = self.gds_validate_string(value_, node, 'morphology')
            self.morphology = value_
            self.morphology_nsprefix_ = child_.prefix


# end class siteMorphology


class siteClassEC8Qindex1(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, value=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.value = value
        self.value_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, siteClassEC8Qindex1)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if siteClassEC8Qindex1.subclass:
            return siteClassEC8Qindex1.subclass(*args_, **kwargs_)
        else:
            return siteClassEC8Qindex1(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def hasContent_(self):
        if (
                self.value is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ', name_='siteClassEC8Qindex1',
               pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('siteClassEC8Qindex1')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'siteClassEC8Qindex1':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='siteClassEC8Qindex1')
        if self.hasContent_():
            outfile.write('>%s' % (eol_,))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='siteClassEC8Qindex1',
                                pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='siteClassEC8Qindex1'):
        pass

    def exportChildren(self, outfile, level, namespaceprefix_='',
                       namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ',
                       name_='siteClassEC8Qindex1', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.value is not None:
            namespaceprefix_ = self.value_nsprefix_ + ':' if (UseCapturedNS_ and self.value_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svalue>%s</%svalue>%s' % (
                namespaceprefix_, self.gds_format_double(self.value, input_name='value'), namespaceprefix_, eol_))

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def buildAttributes(self, node, attrs, already_processed):
        pass

    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'value' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'value')
            fval_ = self.gds_validate_double(fval_, node, 'value')
            self.value = fval_
            self.value_nsprefix_ = child_.prefix


# end class siteClassEC8Qindex1


class siteClassEC8Reference(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, literatureSource=None, FileResource=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.literatureSource = literatureSource
        self.literatureSource_nsprefix_ = None
        self.FileResource = FileResource
        self.FileResource_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, siteClassEC8Reference)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if siteClassEC8Reference.subclass:
            return siteClassEC8Reference.subclass(*args_, **kwargs_)
        else:
            return siteClassEC8Reference(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_literatureSource(self):
        return self.literatureSource

    def set_literatureSource(self, literatureSource):
        self.literatureSource = literatureSource

    def get_FileResource(self):
        return self.FileResource

    def set_FileResource(self, FileResource):
        self.FileResource = FileResource

    def hasContent_(self):
        if (
                self.literatureSource is not None or
                self.FileResource is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ',
               name_='siteClassEC8Reference', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('siteClassEC8Reference')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'siteClassEC8Reference':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='siteClassEC8Reference')
        if self.hasContent_():
            outfile.write('>%s' % (eol_,))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='siteClassEC8Reference',
                                pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='',
                         name_='siteClassEC8Reference'):
        pass

    def exportChildren(self, outfile, level, namespaceprefix_='',
                       namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ',
                       name_='siteClassEC8Reference', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.literatureSource is not None:
            namespaceprefix_ = self.literatureSource_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.literatureSource_nsprefix_) else ''
            self.literatureSource.export(outfile, level, namespaceprefix_, namespacedef_='', name_='literatureSource',
                                         pretty_print=pretty_print)
        if self.FileResource is not None:
            namespaceprefix_ = self.FileResource_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.FileResource_nsprefix_) else ''
            self.FileResource.export(outfile, level, namespaceprefix_, namespacedef_='', name_='FileResource',
                                     pretty_print=pretty_print)

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def buildAttributes(self, node, attrs, already_processed):
        pass

    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'literatureSource':
            obj_ = literatureSource.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.literatureSource = obj_
            obj_.original_tagname_ = 'literatureSource'
        elif nodeName_ == 'FileResource':
            obj_ = FileResource.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.FileResource = obj_
            obj_.original_tagname_ = 'FileResource'


# end class siteClassEC8Reference


class bedrockDepth(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, value=None, uncertainty=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.value = value
        self.value_nsprefix_ = None
        self.uncertainty = uncertainty
        self.uncertainty_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, bedrockDepth)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if bedrockDepth.subclass:
            return bedrockDepth.subclass(*args_, **kwargs_)
        else:
            return bedrockDepth(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_uncertainty(self):
        return self.uncertainty

    def set_uncertainty(self, uncertainty):
        self.uncertainty = uncertainty

    def hasContent_(self):
        if (
                self.value is not None or
                self.uncertainty is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ', name_='bedrockDepth',
               pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('bedrockDepth')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'bedrockDepth':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='bedrockDepth')
        if self.hasContent_():
            outfile.write('>%s' % (eol_,))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='bedrockDepth',
                                pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='bedrockDepth'):
        pass

    def exportChildren(self, outfile, level, namespaceprefix_='',
                       namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ',
                       name_='bedrockDepth', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.value is not None:
            namespaceprefix_ = self.value_nsprefix_ + ':' if (UseCapturedNS_ and self.value_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svalue>%s</%svalue>%s' % (
                namespaceprefix_, self.gds_format_integer(self.value, input_name='value'), namespaceprefix_, eol_))
        if self.uncertainty is not None:
            namespaceprefix_ = self.uncertainty_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.uncertainty_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%suncertainty>%s</%suncertainty>%s' % (
                namespaceprefix_, self.gds_format_integer(self.uncertainty, input_name='uncertainty'), namespaceprefix_,
                eol_))

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def buildAttributes(self, node, attrs, already_processed):
        pass

    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'value' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'value')
            ival_ = self.gds_validate_integer(ival_, node, 'value')
            self.value = ival_
            self.value_nsprefix_ = child_.prefix
        elif nodeName_ == 'uncertainty' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'uncertainty')
            ival_ = self.gds_validate_integer(ival_, node, 'uncertainty')
            self.uncertainty = ival_
            self.uncertainty_nsprefix_ = child_.prefix


# end class bedrockDepth


class bedrockDepthQindex1(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, value=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.value = value
        self.value_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, bedrockDepthQindex1)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if bedrockDepthQindex1.subclass:
            return bedrockDepthQindex1.subclass(*args_, **kwargs_)
        else:
            return bedrockDepthQindex1(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def hasContent_(self):
        if (
                self.value is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ', name_='bedrockDepthQindex1',
               pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('bedrockDepthQindex1')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'bedrockDepthQindex1':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='bedrockDepthQindex1')
        if self.hasContent_():
            outfile.write('>%s' % (eol_,))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='bedrockDepthQindex1',
                                pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='bedrockDepthQindex1'):
        pass

    def exportChildren(self, outfile, level, namespaceprefix_='',
                       namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ',
                       name_='bedrockDepthQindex1', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.value is not None:
            namespaceprefix_ = self.value_nsprefix_ + ':' if (UseCapturedNS_ and self.value_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svalue>%s</%svalue>%s' % (
                namespaceprefix_, self.gds_format_double(self.value, input_name='value'), namespaceprefix_, eol_))

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def buildAttributes(self, node, attrs, already_processed):
        pass

    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'value' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'value')
            fval_ = self.gds_validate_double(fval_, node, 'value')
            self.value = fval_
            self.value_nsprefix_ = child_.prefix


# end class bedrockDepthQindex1


class bedrockDepthReference(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, literatureSource=None, FileResource=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.literatureSource = literatureSource
        self.literatureSource_nsprefix_ = None
        self.FileResource = FileResource
        self.FileResource_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, bedrockDepthReference)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if bedrockDepthReference.subclass:
            return bedrockDepthReference.subclass(*args_, **kwargs_)
        else:
            return bedrockDepthReference(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_literatureSource(self):
        return self.literatureSource

    def set_literatureSource(self, literatureSource):
        self.literatureSource = literatureSource

    def get_FileResource(self):
        return self.FileResource

    def set_FileResource(self, FileResource):
        self.FileResource = FileResource

    def hasContent_(self):
        if (
                self.literatureSource is not None or
                self.FileResource is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ',
               name_='bedrockDepthReference', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('bedrockDepthReference')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'bedrockDepthReference':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='bedrockDepthReference')
        if self.hasContent_():
            outfile.write('>%s' % (eol_,))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='bedrockDepthReference',
                                pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='',
                         name_='bedrockDepthReference'):
        pass

    def exportChildren(self, outfile, level, namespaceprefix_='',
                       namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ',
                       name_='bedrockDepthReference', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.literatureSource is not None:
            namespaceprefix_ = self.literatureSource_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.literatureSource_nsprefix_) else ''
            self.literatureSource.export(outfile, level, namespaceprefix_, namespacedef_='', name_='literatureSource',
                                         pretty_print=pretty_print)
        if self.FileResource is not None:
            namespaceprefix_ = self.FileResource_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.FileResource_nsprefix_) else ''
            self.FileResource.export(outfile, level, namespaceprefix_, namespacedef_='', name_='FileResource',
                                     pretty_print=pretty_print)

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def buildAttributes(self, node, attrs, already_processed):
        pass

    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'literatureSource':
            obj_ = literatureSource.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.literatureSource = obj_
            obj_.original_tagname_ = 'literatureSource'
        elif nodeName_ == 'FileResource':
            obj_ = FileResource.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.FileResource = obj_
            obj_.original_tagname_ = 'FileResource'


# end class bedrockDepthReference


class h800(GeneratedsSuper):
    """This is not included in the 2.0 draft"""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, value=None, uncertainty=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.value = value
        self.value_nsprefix_ = None
        self.uncertainty = uncertainty
        self.uncertainty_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, h800)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if h800.subclass:
            return h800.subclass(*args_, **kwargs_)
        else:
            return h800(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_uncertainty(self):
        return self.uncertainty

    def set_uncertainty(self, uncertainty):
        self.uncertainty = uncertainty

    def hasContent_(self):
        if (
                self.value is not None or
                self.uncertainty is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ', name_='h800',
               pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('h800')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'h800':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='h800')
        if self.hasContent_():
            outfile.write('>%s' % (eol_,))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='h800',
                                pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='h800'):
        pass

    def exportChildren(self, outfile, level, namespaceprefix_='',
                       namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ', name_='h800',
                       fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.value is not None:
            namespaceprefix_ = self.value_nsprefix_ + ':' if (UseCapturedNS_ and self.value_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svalue>%s</%svalue>%s' % (
                namespaceprefix_, self.gds_format_integer(self.value, input_name='value'), namespaceprefix_, eol_))
        if self.uncertainty is not None:
            namespaceprefix_ = self.uncertainty_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.uncertainty_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%suncertainty>%s</%suncertainty>%s' % (
                namespaceprefix_, self.gds_format_integer(self.uncertainty, input_name='uncertainty'), namespaceprefix_,
                eol_))

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def buildAttributes(self, node, attrs, already_processed):
        pass

    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'value' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'value')
            ival_ = self.gds_validate_integer(ival_, node, 'value')
            self.value = ival_
            self.value_nsprefix_ = child_.prefix
        elif nodeName_ == 'uncertainty' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'uncertainty')
            ival_ = self.gds_validate_integer(ival_, node, 'uncertainty')
            self.uncertainty = ival_
            self.uncertainty_nsprefix_ = child_.prefix


# end class h800


class h800Qindex1(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, value=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.value = value
        self.value_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, h800Qindex1)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if h800Qindex1.subclass:
            return h800Qindex1.subclass(*args_, **kwargs_)
        else:
            return h800Qindex1(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def hasContent_(self):
        if (
                self.value is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ', name_='h800Qindex1',
               pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('h800Qindex1')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'h800Qindex1':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='h800Qindex1')
        if self.hasContent_():
            outfile.write('>%s' % (eol_,))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='h800Qindex1',
                                pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='h800Qindex1'):
        pass

    def exportChildren(self, outfile, level, namespaceprefix_='',
                       namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ', name_='h800Qindex1',
                       fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.value is not None:
            namespaceprefix_ = self.value_nsprefix_ + ':' if (UseCapturedNS_ and self.value_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svalue>%s</%svalue>%s' % (
                namespaceprefix_, self.gds_format_double(self.value, input_name='value'), namespaceprefix_, eol_))

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def buildAttributes(self, node, attrs, already_processed):
        pass

    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'value' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'value')
            fval_ = self.gds_validate_double(fval_, node, 'value')
            self.value = fval_
            self.value_nsprefix_ = child_.prefix


# end class h800Qindex1


class h800Reference(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, literatureSource=None, FileResource=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.literatureSource = literatureSource
        self.literatureSource_nsprefix_ = None
        self.FileResource = FileResource
        self.FileResource_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, h800Reference)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if h800Reference.subclass:
            return h800Reference.subclass(*args_, **kwargs_)
        else:
            return h800Reference(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_literatureSource(self):
        return self.literatureSource

    def set_literatureSource(self, literatureSource):
        self.literatureSource = literatureSource

    def get_FileResource(self):
        return self.FileResource

    def set_FileResource(self, FileResource):
        self.FileResource = FileResource

    def hasContent_(self):
        if (
                self.literatureSource is not None or
                self.FileResource is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ', name_='h800Reference',
               pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('h800Reference')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'h800Reference':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='h800Reference')
        if self.hasContent_():
            outfile.write('>%s' % (eol_,))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='h800Reference',
                                pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='h800Reference'):
        pass

    def exportChildren(self, outfile, level, namespaceprefix_='',
                       namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ',
                       name_='h800Reference', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.literatureSource is not None:
            namespaceprefix_ = self.literatureSource_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.literatureSource_nsprefix_) else ''
            self.literatureSource.export(outfile, level, namespaceprefix_, namespacedef_='', name_='literatureSource',
                                         pretty_print=pretty_print)
        if self.FileResource is not None:
            namespaceprefix_ = self.FileResource_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.FileResource_nsprefix_) else ''
            self.FileResource.export(outfile, level, namespaceprefix_, namespacedef_='', name_='FileResource',
                                     pretty_print=pretty_print)

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def buildAttributes(self, node, attrs, already_processed):
        pass

    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'literatureSource':
            obj_ = literatureSource.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.literatureSource = obj_
            obj_.original_tagname_ = 'literatureSource'
        elif nodeName_ == 'FileResource':
            obj_ = FileResource.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.FileResource = obj_
            obj_.original_tagname_ = 'FileResource'


# end class h800Reference


class geologicalUnitQindex1(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, value=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.value = value
        self.value_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, geologicalUnitQindex1)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if geologicalUnitQindex1.subclass:
            return geologicalUnitQindex1.subclass(*args_, **kwargs_)
        else:
            return geologicalUnitQindex1(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def hasContent_(self):
        if (
                self.value is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ',
               name_='geologicalUnitQindex1', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('geologicalUnitQindex1')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'geologicalUnitQindex1':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='geologicalUnitQindex1')
        if self.hasContent_():
            outfile.write('>%s' % (eol_,))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='geologicalUnitQindex1',
                                pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='',
                         name_='geologicalUnitQindex1'):
        pass

    def exportChildren(self, outfile, level, namespaceprefix_='',
                       namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ',
                       name_='geologicalUnitQindex1', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.value is not None:
            namespaceprefix_ = self.value_nsprefix_ + ':' if (UseCapturedNS_ and self.value_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svalue>%s</%svalue>%s' % (
                namespaceprefix_, self.gds_format_double(self.value, input_name='value'), namespaceprefix_, eol_))

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def buildAttributes(self, node, attrs, already_processed):
        pass

    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'value' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'value')
            fval_ = self.gds_validate_double(fval_, node, 'value')
            self.value = fval_
            self.value_nsprefix_ = child_.prefix


# end class geologicalUnitQindex1


class geologicalUnitReference(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, literatureSource=None, FileResource=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.literatureSource = literatureSource
        self.literatureSource_nsprefix_ = None
        self.FileResource = FileResource
        self.FileResource_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, geologicalUnitReference)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if geologicalUnitReference.subclass:
            return geologicalUnitReference.subclass(*args_, **kwargs_)
        else:
            return geologicalUnitReference(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_literatureSource(self):
        return self.literatureSource

    def set_literatureSource(self, literatureSource):
        self.literatureSource = literatureSource

    def get_FileResource(self):
        return self.FileResource

    def set_FileResource(self, FileResource):
        self.FileResource = FileResource

    def hasContent_(self):
        if (
                self.literatureSource is not None or
                self.FileResource is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ',
               name_='geologicalUnitReference', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('geologicalUnitReference')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'geologicalUnitReference':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='geologicalUnitReference')
        if self.hasContent_():
            outfile.write('>%s' % (eol_,))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_,
                                name_='geologicalUnitReference', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='',
                         name_='geologicalUnitReference'):
        pass

    def exportChildren(self, outfile, level, namespaceprefix_='',
                       namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ',
                       name_='geologicalUnitReference', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.literatureSource is not None:
            namespaceprefix_ = self.literatureSource_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.literatureSource_nsprefix_) else ''
            self.literatureSource.export(outfile, level, namespaceprefix_, namespacedef_='', name_='literatureSource',
                                         pretty_print=pretty_print)
        if self.FileResource is not None:
            namespaceprefix_ = self.FileResource_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.FileResource_nsprefix_) else ''
            self.FileResource.export(outfile, level, namespaceprefix_, namespacedef_='', name_='FileResource',
                                     pretty_print=pretty_print)

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def buildAttributes(self, node, attrs, already_processed):
        pass

    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'literatureSource':
            obj_ = literatureSource.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.literatureSource = obj_
            obj_.original_tagname_ = 'literatureSource'
        elif nodeName_ == 'FileResource':
            obj_ = FileResource.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.FileResource = obj_
            obj_.original_tagname_ = 'FileResource'


# end class geologicalUnitReference


class siteTopology(GeneratedsSuper):
    """or respective code, eg B2"""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, schemeA=None, schemeB=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.schemeA = schemeA
        self.schemeA_nsprefix_ = None
        self.schemeB = schemeB
        self.schemeB_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, siteTopology)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if siteTopology.subclass:
            return siteTopology.subclass(*args_, **kwargs_)
        else:
            return siteTopology(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_schemeA(self):
        return self.schemeA

    def set_schemeA(self, schemeA):
        self.schemeA = schemeA

    def get_schemeB(self):
        return self.schemeB

    def set_schemeB(self, schemeB):
        self.schemeB = schemeB

    def hasContent_(self):
        if (
                self.schemeA is not None or
                self.schemeB is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ', name_='siteTopology',
               pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('siteTopology')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'siteTopology':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='siteTopology')
        if self.hasContent_():
            outfile.write('>%s' % (eol_,))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='siteTopology',
                                pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='siteTopology'):
        pass

    def exportChildren(self, outfile, level, namespaceprefix_='',
                       namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ',
                       name_='siteTopology', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.schemeA is not None:
            namespaceprefix_ = self.schemeA_nsprefix_ + ':' if (UseCapturedNS_ and self.schemeA_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sschemeA>%s</%sschemeA>%s' % (
                namespaceprefix_,
                self.gds_encode(self.gds_format_string(quote_xml(self.schemeA), input_name='schemeA')),
                namespaceprefix_, eol_))
        if self.schemeB is not None:
            namespaceprefix_ = self.schemeB_nsprefix_ + ':' if (UseCapturedNS_ and self.schemeB_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sschemeB>%s</%sschemeB>%s' % (
                namespaceprefix_,
                self.gds_encode(self.gds_format_string(quote_xml(self.schemeB), input_name='schemeB')),
                namespaceprefix_, eol_))

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def buildAttributes(self, node, attrs, already_processed):
        pass

    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'schemeA':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'schemeA')
            value_ = self.gds_validate_string(value_, node, 'schemeA')
            self.schemeA = value_
            self.schemeA_nsprefix_ = child_.prefix
        elif nodeName_ == 'schemeB':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'schemeB')
            value_ = self.gds_validate_string(value_, node, 'schemeB')
            self.schemeB = value_
            self.schemeB_nsprefix_ = child_.prefix


# end class siteTopology


class OverallQindex(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, value=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.value = value
        self.value_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, OverallQindex)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if OverallQindex.subclass:
            return OverallQindex.subclass(*args_, **kwargs_)
        else:
            return OverallQindex(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def hasContent_(self):
        if (
                self.value is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='',
               namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ', name_='OverallQindex',
               pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('OverallQindex')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'OverallQindex':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='OverallQindex')
        if self.hasContent_():
            outfile.write('>%s' % (eol_,))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='OverallQindex',
                                pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='OverallQindex'):
        pass

    def exportChildren(self, outfile, level, namespaceprefix_='',
                       namespacedef_=' xmlns:None="https://quake.ethz.ch/quakeml/QuakeML2.0" ',
                       name_='OverallQindex', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.value is not None:
            namespaceprefix_ = self.value_nsprefix_ + ':' if (UseCapturedNS_ and self.value_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svalue>%s</%svalue>%s' % (
                namespaceprefix_, self.gds_format_double(self.value, input_name='value'), namespaceprefix_, eol_))

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def buildAttributes(self, node, attrs, already_processed):
        pass

    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'value' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'value')
            fval_ = self.gds_validate_double(fval_, node, 'value')
            self.value = fval_
            self.value_nsprefix_ = child_.prefix


# end class OverallQindex


GDSClassesMapping = {
}

USAGE_TEXT = """
Usage: python <Parser>.py [ -s ] <in_xml_file>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def get_root_tag(node):
    tag = Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = GDSClassesMapping.get(tag)
    if rootClass is None:
        rootClass = globals().get(tag)
    return tag, rootClass


def get_required_ns_prefix_defs(rootNode):
    '''Get all name space prefix definitions required in this XML doc.
    Return a dictionary of definitions and a char string of definitions.
    '''
    nsmap = {
        prefix: uri
        for node in rootNode.iter()
        for (prefix, uri) in node.nsmap.items()
        if prefix is not None
    }
    namespacedefs = ' '.join([
        'xmlns:{}="{}"'.format(prefix, uri)
        for prefix, uri in nsmap.items()
    ])
    return nsmap, namespacedefs


def parse(inFileName, silence=False, print_warnings=True):
    global CapturedNsmap_
    gds_collector = GdsCollector_()
    parser = None
    doc = parsexml_(inFileName, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'SERA_quakeml'
        rootClass = SERA_quakeml
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    CapturedNsmap_, namespacedefs = get_required_ns_prefix_defs(rootNode)
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_=namespacedefs,
            pretty_print=True)
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def parseEtree(inFileName, silence=False, print_warnings=True,
               mapping=None, nsmap=None):
    parser = None
    doc = parsexml_(inFileName, parser)
    gds_collector = GdsCollector_()
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'SERA_quakeml'
        rootClass = SERA_quakeml
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    if mapping is None:
        mapping = {}
    rootElement = rootObj.to_etree(
        None, name_=rootTag, mapping_=mapping, nsmap_=nsmap)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(str(content))
        sys.stdout.write('\n')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False, print_warnings=True):
    '''Parse a string, create the object tree, and export it.

    Arguments:
    - inString -- A string.  This XML fragment should not start
      with an XML declaration containing an encoding.
    - silence -- A boolean.  If False, export the object.
    Returns -- The root object in the tree.
    '''
    parser = None
    rootNode = parsexmlstring_(inString, parser)
    gds_collector = GdsCollector_()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'SERA_quakeml'
        rootClass = SERA_quakeml
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    if not SaveElementTreeNode:
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def parseLiteral(inFileName, silence=False, print_warnings=True):
    parser = None
    doc = parsexml_(inFileName, parser)
    gds_collector = GdsCollector_()
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'SERA_quakeml'
        rootClass = SERA_quakeml
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('#from siteXML import *\n\n')
        sys.stdout.write('import siteXML as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def main():
    args = sys.argv[1:]
    if len(args) == 1:
        parse(args[0])
    else:
        usage()


if __name__ == '__main__':
    # import pdb; pdb.set_trace()
    main()

RenameMappings_ = {
}

#
# Mapping of namespaces to types defined in them
# and the file in which each is defined.
# simpleTypes are marked "ST" and complexTypes "CT".
NamespaceToDefMappings_ = {'F:\\FROM_LAPTOP_HP\\PROJECTS\\SERA\\SITE_XML QuakeML-SERA-1.2.xsd': []}

__all__ = [
    "Analysis",
    "FileResource",
    "OverallQindex",
    "SERA_quakeml",
    "VelocityProfile",
    "affiliation",
    "altitude",
    "bedrockDepthQindex1",
    "bedrockDepthReference",
    "bedrockDepth",
    "boreholeLogsCount",
    "contact",
    "country",
    "cptLogsCount",
    "density",
    "geologicalUnitQindex1",
    "geologicalUnitReference",
    "h800Qindex1",
    "h800Reference",
    "h800",
    "identifier",
    "institution",
    "language",
    "latitude",
    "layerBottomDepth",
    "layerCount",
    "layerThickness",
    "layerTopDepth",
    "literatureSource",
    "longitude",
    "maxDistanceFromStation",
    "minDistanceFromStation",
    "person",
    "postalAddress",
    "resonanceFrequencyQindex1",
    "resonanceFrequencyReference",
    "resonanceFrequency",
    "siteCharacterizationParameters",
    "siteClassEC8Qindex1",
    "siteClassEC8Reference",
    "siteDescription",
    "siteMorphology",
    "siteOwner",
    "siteTopology",
    "sptLogsCount",
    "velocityP",
    "velocityProfileCount",
    "velocityProfileData",
    "velocityProfileQindex1",
    "velocityProfileReference",
    "velocityS30Qindex1",
    "velocityS30Reference",
    "velocityS30",
    "velocityS"
]
