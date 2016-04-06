#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nose
from nose.tools import raises, assert_true, assert_equal, assert_raises

import codecs
import pylangtemplate
from pylangtemplate import main as main

website_path = '../samplewebsite/'
dictionaries_path = '..'


def test_default_setup():
    """ """

    main(website_path, dictionaries_path)


def test_default_results():
    """ """
    assert_equal.__self__.maxDiff = None
    test_str = u"""<!DOCTYPE html>
        <html lang="en">

        <head>

            <meta charset="utf-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <meta name="description" content="">
            <meta name="author" content="">

            <title>Sample Web Site</title>

            <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
            <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
            <!--[if lt IE 9]>
                <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
                <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
            <![endif]-->

        </head>

        <body>
            <center>
                <p> Текст для примера</p>
            </center>
        </body>

        </html>
        """

    import os
    file_path = os.path.join(website_path, 'ru', 'index.html')

    with codecs.open(file_path, 'r', encoding='utf-8') as f:
        file_content = f.read()
    print (file_content)
    print (test_str)
    # assert_equal(
    #     test_str.replace(' ', ''),
    #     file_content.replace(' ', ''))
