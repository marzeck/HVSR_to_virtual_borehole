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

def createConfigFile(args):
    print(args._get_kwargs())
    #[('cmd', 'init'), ('log', 'INFO')]

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
            '''
        )

def store(args):
    print(args.filename)
    print(args.store_dir)
    print(args._get_kwargs())
    #[('cmd', 'store'), ('filename', 'HVSR-database'), ('force', False), ('log', 'INFO'), ('store_dir', 'stores')]

    statlist = glob.glob(args.store_dir + '/*.hv')
    print(statlist)
    

    # if args.append == True:
    #     # read existing file and check which data is missing
    #     with open('{0}.csv'.format(args.filename), 'r') as f:



if __name__=='__main__':
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
                              help='super directory where to search/create stores. Default: stores',
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

    if args.cmd == 'init':
        createConfigFile(args)
    elif args.cmd == 'store':
        store(args)
    else:
        parser.print_help()

