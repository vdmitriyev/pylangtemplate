#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

__author__ = 'Viktor Dmitriyev'
__copyright__ = 'Copyright 2015, Viktor Dmitriyev'
__credits__ = ['Viktor Dmitriyev']
__license__ = 'MIT'
__version__ = '1.2.0'
__maintainer__ = '-'
__email__ = ''
__status__ = 'dev'
__date__ = '20.06.2015'
__description__ = 'Python script that change all files in project with from default language to the target one'

import os
import sys
import uuid
import time
import string
import shutil
import codecs
import tarfile
import fileinput
import importlib
from docopt import docopt
from datetime import datetime

ACCEPTED_EXTENSIONS = ['.html']
DEBUG = False


class FolderIterator():

    def iterate_through_catalog(self, rootdir=None):
        """ (str) -> (dict, dict)

            Iterating through the given catalog to identify notes.
        """

        if rootdir is None:
            rootdir = sys.argv[1]

        # notes_papers = dict()
        total_papers = dict()

        for root, _, files in os.walk(rootdir):
            for f in files:
                if root not in total_papers:
                    total_papers[root] = list()
                total_papers[root].append(f)

        return total_papers


class PrepeareForNewProject():

    def __init__(self, website_path):
        """
            Initialization of class
        """
        self.website_path = website_path

    def replace_in_file(self, proj_file, search, replace, rewrite=True):
        """
            (obj, str) -> NoneType

            Replace "search" string with "replace" string in "proj_file".
        """

        with codecs.open(proj_file, 'r', encoding='utf-8') as f:
            file_content = f.read()

        file_content = file_content.replace(search, replace)

        with codecs.open(proj_file, 'wb', encoding='utf-8') as f:
            f.write(file_content)

        # for line in fileinput.input(proj_file, inplace=True):
        #     line = line
        #     sys.stdout.write(line)

    def template_to_new(self, proj_file, lang_dict):
        """
            (obj, str) -> NoneType

            Switching from template to new specific project
        """

        for extention in ACCEPTED_EXTENSIONS:
            if (proj_file[-len(extention):].lower() == extention):
                for key in lang_dict:
                    self.replace_in_file(proj_file, key, lang_dict[key])

    def clear_directory(self, directory):
        """
            (obj, str) -> None

            Clears archive and clears given 'directory'.
        """

        def make_archive_copy(source_dir, target_filename=None):
            """Making copy of the directory before clearing it

                Args:
            """
            if target_filename is None:
                suffix = '{0}-{1}'.format(
                    datetime.fromtimestamp(time.time()).strftime('%Y%m%d-%H%M'),
                    str(uuid.uuid1())[:2])
                archive_file_path = '{0}-archive-{1}.tar.gz'.format(directory,
                                                                    suffix)
                target_filename = archive_file_path

            print('[i] creating archive of "{0}" in "{1}"'.format(
                source_dir, target_filename))

            with tarfile.open(target_filename, "w:gz") as tar:
                tar.add(source_dir, arcname=os.path.basename(source_dir))

        if os.path.exists(directory):

            make_archive_copy(source_dir=directory)

            for root, dirs, files in os.walk(directory):
                for f in files:
                    os.unlink(os.path.join(root, f))
                for d in dirs:
                    shutil.rmtree(os.path.join(root, d))

            os.rmdir(directory)

    def process(self, source_lang, target_lang, mapping_dict):
        """
            Processing the files of the project

            Args:
                source_lang (str)   : source language to be used as default.
                target_lang (str)   : target language of translation.
                mapping_dict (dict) : dictionary of translation.

            Returns:
                None
        """

        print('[i] configured website location is {0}'.format(
            self.website_path))

        target_dir = self.website_path + target_lang
        source_dir = self.website_path + source_lang

        self.clear_directory(target_dir)
        shutil.copytree(source_dir, target_dir)

        fi = FolderIterator()
        self.proj_files = fi.iterate_through_catalog(target_dir)

        for directory in self.proj_files:
            print('\t{0}'.format(directory))
            for proj_file in self.proj_files[directory]:
                print('\t{0}'.format(proj_file))
                self.template_to_new(directory + '/' + proj_file, mapping_dict)

        #os.rename(target_lang)


class Logger(object):

    def __init__(self):
        """ Initializing log file with random name"""
        self.terminal = sys.stdout
        suffix = '{0}-{1}'.format(
            datetime.fromtimestamp(time.time()).strftime('%Y%m%d-%H%M'),
            str(uuid.uuid1())[:2])
        self.log = open('logfile-{0}.log'.format(suffix), "a")
        if DEBUG:
            print('[i] saving debugging info into file "{0}"'.format(
                'logfile-{0}.log'.format(suffix)))

    def write(self, message):
        """ Overriding writing method to write to file and stdout at once"""

        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        """flush method is needed for python 3 compatibility
           handles the flush command by doing nothing
           you might want to specify some extra behavior here
        """

        pass


def main(website_path=None, dictionaries_path=None):
    """Main method that creates objects and start processing.

    Args:
        website_path (str)     : path to website that will be used as default one.
        dictionaries_path (str): path to dictionaries with translate.

    Returns:
        None
    """

    if website_path is None:
        website_path = '../'

    if dictionaries_path is None:
        dictionaries_path = 'dictionaries'

    sys.path.insert(0, dictionaries_path)

    #if DEBUG: print ('\n'.join(sys.path))

    import dictionaries as _languges

    for languge in _languges.__all__:
        current = importlib.import_module('dictionaries.{modulename}'.format(
            modulename=languge))

        print('[i] processing language {0}'.format(current.TARGET_LANGUAGE))

        pcv = PrepeareForNewProject(website_path)
        pcv.process(current.ORIGINAL_LANGUAGE, current.TARGET_LANGUAGE,
                    current.MAPPING_DICT)


if __name__ == '__main__':
    # setting system default encoding to the UTF-8
    import sys

    if sys.version_info < (3, 0, 0):
        reload(sys)
        sys.setdefaultencoding('UTF8')

    __help__ = """
    {description}
    Usage:
        pylangtemplate.py <website> <dictionaries> [--sample]
                                                   [--verbose]
                                                   [--logtofile]

        pylangtemplate.py -h | --help
        The <website> argument must be a path to folder with the website.
        The <dictionaries> argument must be a  path to folder with the dictionaries containing language mappings.

        Options:
          -h --help     Show this screen.
          --sample      Will ignore all given options and try to run sample.
          --verbose     If given, debug output is also written to the stdout.
          """

    opts = docopt(__help__.format(description=__description__))

    website_path = opts["<website>"][1:-1]
    dictionaries_path = opts["<dictionaries>"][1:-1]

    # activating logger
    if opts["--verbose"]:
        DEBUG = True

    # logging also to file
    if opts["--logtofile"]:
        sys.stdout = Logger()

    # running sample
    if opts["--sample"]:
        DEBUG = True
        main()
        exit()

    main(website_path, dictionaries_path)
