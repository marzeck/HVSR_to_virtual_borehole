#!/usr/bin/env python

######################
#
# A new main script to merge the single step files of the original
# HVSR_to_virtual_borehole scripts of Koen van Noten.
#
######################

import logging
import yaml
import glob
import numpy as np


class HVvalue(object):

    def __init__(self, value=float(), max=float(), min=float()):
        self.value = value
        self.max = max
        self.min = min


class HVheader(object):
    windows_total = int
    windows_used = int
    f0_from_average = float
    f0_from_windows = HVvalue  # create object with min, max and value
    amplitude_at_f0 = float


class HVdata(object):

    def __init__(self, frequency=np.array([])):
        self.frequency = frequency
        self.amplitudes = []

    def add_amplitude(self, values=HVvalue()):
        self.amplitudes.append(values)


class HV(object):
    header = HVheader
    data = HVdata


def geopsyHVreader(filename):
    readHV = HV()
    readHeader = HVheader()
    readData = HVdata()
    with open(filename, 'r') as f:
        lines = f.readlines()

    readHeader.windows_total = float(lines[1].split()[-1])
    readHeader.windows_used = float(lines[3].split()[-1])
    readHeader.f0_from_average = float(lines[2].split()[-1])
    readValue = HVvalue()
    readValue.value = float(lines[4].split()[-3])
    readValue.min = float(lines[4].split()[-2])
    readValue.max = float(lines[4].split()[-1])
    readHeader.f0_from_windows = readValue
    readHeader.amplitude_at_f0 = float(lines[5].split()[-1])
    readHV.header = readHeader

    for line in lines[9:]:
        readData.frequency = np.append(readData.frequency, [line.split()[0]])
        readData.amplitudes.append(HVvalue(value=float(line.split()[1]),
                                           min=float(line.split()[2]),
                                           max=float(line.split()[3])))

    return readHV


def createConfigFile(args):

    #######################
    #
    # Purpose:
    # Before the start of the program a config file will be created.
    # This step aims to reduce the amount of user interaction with each
    # call from the commandline, as the config parameters are read and stored
    # through this config file.
    #
    #######################

    with open('config.yaml', 'w') as f:
        f.write(
            '''
            # yaml config file to communicate parameters, paths, filenames, etc.
            # between user and program. Please change according to you needs.
            # But keep in mind the YAML syntax.
            
            # directory to search for .hv and .log files to construct file-database
            store_dir:  'stores'
            '''
        )
    print('Created the "config.yaml file."')


def store(args, config):
    # print(args.filename)
    # print(args.store_dir)
    # print(args._get_kwargs())
    # [('cmd', 'store'), ('filename', 'HVSR-database'), ('force', False), ('log', 'INFO'), ('store_dir', 'stores')]

    if config.get('store_dir') is None:
        config['store_dir'] = args.store_dir
        print('variable "store_dir" not set in the config file and automatically set to {0}'.format(args.store_dir))

    filelist = glob.glob(config['store_dir'] + '/*.hv')
    if filelist == []:
        print('No hv files found in {0}! Program stops now.'.format(config['store_dir']))
        quit()
    if glob.glob(config['store_dir'] + '/*.log') == []:
        print('no geopsy .log files found! Program stops now.')
        quit()

    database = {}
    database['statlist'] = [path.split('.hv')[0].split(config['store_dir'] + '/')[1] for path in filelist]
    with open('store.yaml', 'w') as f:
        yaml.dump(database, f)

    # in the following, loop over the stations and read hv and log file headers to retrieve necessary information
    # in order to construct database.
    # --> for that check, what are necessary information for following processing steps (e.g., f0)
    # - check for what we need geolocations, maybe we can get them form geopsy .coord file

    # if args.append == True:
    #     # read existing file and check which data is missing
    #     with open('{0}.csv'.format(args.filename), 'r') as f:


def fZero(args, config):

    if config.get('store_dir') is None:
        config['store_dir'] = args.store_dir
        print('variable "store_dir" not set in the config file and automatically set to {0}'.format(args.store_dir))

    try:
        store_stream = open('store.yaml', 'r')
        store = yaml.load(store_stream, Loader=yaml.SafeLoader)
    except FileNotFoundError:
        print('"store.yaml" file not found! please run the "store"-process first')
        quit()

    input_data = []
    for statname in store['statlist']:
        print('reading file = ' + statname + '.hv')
        input_data.append(geopsyHVreader(filename=config['store_dir'] + '/' + statname + '.hv'))
    print(len(input_data))
    print(input_data[0].header)
    quit()


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser('HVSR data into a virtual borehole.', add_help=True)
    parser.add_argument('--log', required=False, default='INFO')

    sp = parser.add_subparsers(dest='cmd')
    init_parser = sp.add_parser('init',
                                help='Creates a config file (config.yaml). Please run first!')

    store_parser = sp.add_parser('store',
                                 help='Creates a store/database for HV file handling.')
    store_parser.add_argument('--filename',
                              help='name of csv file to store HV file infos into',
                              default='HVSR-database')
    store_parser.add_argument('--append',
                              help='you want to append files to existing data base [False]',
                              choices=[True, False],
                              default=False)
    store_parser.add_argument('--super-dir',
                              dest='store_dir',
                              help='Super directory where to search files. If set in "config.yaml", this argument ' + \
                                   'will be ignored. Default: stores',
                              default='stores')
    store_parser.add_argument('--force',
                              action='store_true',
                              default=False,
                              help='force overwrite')

    fZero_parser = sp.add_parser('f0',
                                 help='Extracts the f0 values from the HV files.')

    borehole_parser = sp.add_parser('borehole',
                                    help='Transforms the HV results into a virtual borehole.')

    hvPolarity_parser = sp.add_parser('polarity',
                                      help='Extracts the polarity information from the HV data.')

    args = parser.parse_args()

    logging.basicConfig(level=args.log.upper())

    try:
        config_stream = open('config.yaml', 'r')
        config = yaml.load(config_stream, Loader=yaml.SafeLoader)
    except FileNotFoundError:
        print('"config.yaml" file not found! please run the "init"-process first')
        quit()

    if args.cmd == 'init':
        createConfigFile(args)
    elif args.cmd == 'store':
        store(args, config)
    elif args.cmd == 'f0':
        fZero(args, config)
    else:
        parser.print_help()
