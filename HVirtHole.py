#!/usr/bin/env python

######################
#
# A new main script to merge the single step files of the original
# HVSR_to_virtual_borehole scripts of Koen van Noten.
#
######################

import logging
import yaml
import pickle
import glob
import os
import numpy as np
from scipy.interpolate import interp1d


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


class HVposition(object):

    def __init__(self, x=0., y=0., z=0.):
        self.x = x
        self.y = y
        self.z = z

    def positionxy(self):
        return (self.x,self.y)


class HV(object):
    header = HVheader()
    data = HVdata()

    def __init__(self, name=str(), position=HVposition()):
        self.name = name
        self.position = position


def geopsyHVreader(filename, stationname=None, pos=None):
    readHV = HV(name=stationname, position=pos)
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
        readData.frequency = np.append(readData.frequency, [float(line.split()[0])])
        readData.amplitudes.append(HVvalue(value=float(line.split()[1]),
                                           min=float(line.split()[2]),
                                           max=float(line.split()[3])))
    readHV.data = readData

    return readHV

def geopsyCoordreader(filename: str, stations: list):
    '''

    :param filename: absolute or local path and filename
    :type: :py:class:`str`
    :param stations: List of strings with station names
    :type: :py:class:`list`

    :return: a dictionary with station names as key and HVposition() as values
    '''

    with open(filename, 'r') as f:
        lines = [line.split() for line in f.readlines() if line.split()[0] != '#']

    positiondic = {}
    for stat in stations:
        positiondic[stat] = HVposition(x=[float(line[-2]) for line in lines if stat in line][0],
                                         y=[float(line[-1]) for line in lines if stat in line][0],
                                         z=None)
    return positiondic


def xyCoordreader(filename: str, stations: list):
    # expects a comma-separated file with Name, X, Y, Z
    with open(filename, 'r') as f:
        lines = f.readlines()
    positiondic = {}
    for line in lines:
        if line.split(',')[0] in stations:
            positiondic[line.split(',')[0]] = HVposition(x=float(line.split(',')[1]),
                                                         y=float(line.split(',')[2]),
                                                         z=float(line.split(',')[3]))
    return positiondic


def arraycenter(arr: np.array):
    length = arr.shape[0]
    sum_x = np.sum(arr[:, 0])
    sum_y = np.sum(arr[:, 1])
    return (sum_x/length, sum_y/length)


def euclidean(p1, p2):
    return np.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)


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

# type of file, in which the coordinates of all sensors is stored
# up to now we can only handle X - Y (- Z) data, while elevation data is optional,
# but limits the methods to average HV values. 
# Possible parameters: 'NameXY' or 'GeopsyTable'
coord_file_type: 'GeopsyTable'

# alternative path for coordinate file if not in cwd
alt_coord_path: '.'

# coordination file name
coord_file: 'coord-table.txt'

# In the default setting, Geopsy only exports 100 frequency-amplitude samples for the computed HVSR curve.
# One can increase this number by:
#   - either increasing the sample numbers in geopsy (max = 9999)
#   - or by interpolating between the samples and improve the accuracy of picking f0
# Increasing the samples in Geopsy to 9999 gives the same results, but one might have forgotten to do this
# so this interpolation offers a nice twist to solve this.

# options: True or False
interpolate: True

# method how to weigh each station for the average HV value, choose between: "uniform", "centric", "plane"
average: 'uniform'
            '''
        )
    print('Created the "config.yaml file."')

def resampleHVs(hvlist):

    if isinstance(hvlist, list):
        hvresampled = []
        for hv in hvlist:
            hvresampled.append(resampleHV(hv))
        return hvresampled
    else:
        raise TypeError

def resampleHV(hvcurve, outsamples=15000):

    mean_ampl = np.array([ampl.value for ampl in hvcurve.data.amplitudes])
    max_ampl = np.array([ampl.max for ampl in hvcurve.data.amplitudes])
    min_ampl = np.array([ampl.min for ampl in hvcurve.data.amplitudes])

    func = interp1d(hvcurve.data.frequency, mean_ampl, 'cubic')
    freq_new = np.linspace(hvcurve.data.frequency[0], hvcurve.data.frequency[-1], outsamples)
    mean_ampl_resamp = func(freq_new)

    func = interp1d(hvcurve.data.frequency, max_ampl, 'cubic')
    max_ampl_resamp = func(freq_new)

    func = interp1d(hvcurve.data.frequency, min_ampl, 'cubic')
    min_ampl_resamp = func(freq_new)

    hvcurve.data.frequency = freq_new
    hvcurve.data.amplitudes = [HVvalue(value=mean_ampl_resamp[i],
                                       min=min_ampl_resamp[i],
                                       max=max_ampl_resamp[i]) for i in range(len(mean_ampl_resamp))]
    hvcurve.header.amplitude_at_f0 = mean_ampl_resamp[np.argmax(mean_ampl_resamp)]
    hvcurve.header.f0_from_windows = HVvalue(value=freq_new[np.argmax(mean_ampl_resamp)],
                                             min=freq_new[np.argmax(min_ampl_resamp)],
                                             max=freq_new[np.argmax(max_ampl_resamp)])
    return hvcurve


def averageHV(indata, method=None):
    '''
    Function to estimate the f0 and amplitude(f0) values averaged over
    a whole array.
    :param indata: List of HV curves
    :type indata: :py:class:`list`
    :param method: method how to weigh the average choices: [uniform, centric, plane]

    :return: an HV object? or 4 variables?
    '''

    # calculate (mass) center of array
    centerpos = arraycenter(np.array([hv.position.positionxy() for hv in indata]))

    if method == 'uniform':
        f0_ave = np.mean([hv.header.f0_from_windows.value for hv in indata])
        ampl_ave = np.mean([hv.header.amplitude_at_f0 for hv in indata])
        f0_err = np.std([hv.header.f0_from_windows.value for hv in indata])
        ampl_err = np.std([hv.header.amplitude_at_f0 for hv in indata])
        # alternatively use the standard error of mean?
        # f0_err = np.std([hv.header.f0_from_windows.value for hv in indata])/np.sqrt(len(indata))
        # ampl_err = np.std([hv.header.amplitude_at_f0 for hv in indata])/np.sqrt(len(indata))

    elif method == 'centric':
        # calculate minimum interstation distance (as weighting factor)
        mindist = min([min([euclidean(hv1.position.positionxy, hv2.position.positionxy) for hv1 in indata if hv1 != hv2]) for hv2 in indata])
        weigh = lambda pos: mindist/euclidean(pos, centerpos)
        f0_ave = np.average([hv.header.f0_from_windows.value for hv in indata], [weigh(hv.position.positionxy) for hv in indata])
        ampl_ave = np.average([hv.header.amplitude_at_f0 for hv in indata], [weigh(hv.position.positionxy) for hv in indata])

        # Now I just miss, how to estimate the errors

    # elif method == 'plane':
    #
    else:
        raise ValueError

    return centerpos, f0_ave, ampl_ave, f0_err, ampl_err


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
        return
    if glob.glob(config['store_dir'] + '/*.log') == []:
        print('no geopsy .log files found! Program stops now.')
        return

    store = {}
    store['statlist'] = [path.split('.hv')[0].split(config['store_dir'] + '/')[1] for path in filelist]

    # now read coordinate file (so far only x and y? otherwise might be a bit annoying to change)
    # and add the HVposition() to the database

    # print(config['alt_coord_path'])
    # if os.path.isfile(config['coord_file']):
    #     config['alt_coord_path'] = './'
    # else:
    #     raise LookupError('alt_coord_path and/or coord_file are not properly assigned in the config file!')

    if config['coord_file_type'].lower() == 'geopsytable':
        store['coordinates'] = geopsyCoordreader(filename=config['alt_coord_path'] + config['coord_file'],
                                                 stations=store['statlist'])
    elif config['coord_file_type'].lower() == 'namexy':
        store['coordinates'] = xyCoordreader(filename=config['alt_coord_path'] + config['coord_file'],
                                             stations=store['statlist'])
    else:
        raise NameError('Only "NameXY" or "GeopsyTable" are allowed for "coord_file_type"')

    # with open('store.yaml', 'w') as f:
    #     yaml.dump(store, f)

    with open('store.pkl', 'wb') as f:
        pickle.dump(store, f)

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
        with open('store.pkl', 'rb') as f:
            store = pickle.load(f)
    except FileNotFoundError:
        print('"store.yaml" file not found! please run the "store"-process first')
        quit()

    input_data = []
    for statname in store['statlist']:
        # print('reading file = ' + statname + '.hv')
        input_data.append(geopsyHVreader(filename=config['store_dir'] + '/' + statname + '.hv',
                                         stationname=statname))
    print('loaded {0} .hv files'.format(len(input_data)))

    if config['interpolate']:
        input_data = resampleHVs(input_data)
        print('successfully interpolated!')
    else:
        print('Just use basic data with {0} frequency samples.'.format(input_data[0].data.frequency.size))

    for hv in input_data:
        hv.position = store['coordinates'][hv.name]

    # if there are more than one hv file given, we could have different averaging options (different weighting schemes)
    # the output could then be stored in the header and give back to store.yaml (without data)
    ave_out = averageHV(input_data, config['average'])

    print('\nThe final HV-value of the array is averaged with {0} weights'. format(config['average']))
    print('center of array: {0:.2f},{1:.2f} (x,y)'.format(ave_out[0][0], ave_out[0][1]))
    print('f0: {0:.3f} +/-{1:.3f}'.format(ave_out[1], ave_out[3]))
    print('amplitude(f0): {0:.2f} +/-{1:.2f}'.format(ave_out[2], ave_out[4]))

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser('HVSR data into a virtual borehole.', add_help=True)
    parser.add_argument('--log', required=False, default='INFO')

    sp = parser.add_subparsers(dest='cmd')
    init_parser = sp.add_parser('init',
                                help='Creates a config file (config.yaml). Please run first!')
    init_parser.add_argument('--force',
                             default=False,
                             help='force overwrite')

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
        if args.force:
            createConfigFile(args)
        elif os.path.isfile('config.yaml'):
            print('\nThe config file already exists.')
            print('If you want to overwrite use the --force True option.')
        else:
            createConfigFile(args)

    elif args.cmd == 'store':
        store(args, config)
    elif args.cmd == 'f0':
        fZero(args, config)
    else:
        parser.print_help()

    print('\nHVirtHole terminates.\n')
