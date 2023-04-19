""" Tests for caesar.py"""

import os
import string
import random
import re
from subprocess import getstatusoutput

PRG = './caesar.py'
FOX = './inputs/fox.txt'
FOX_OUT = './outputs/fox.txt'
SPIDERS = './inputs/spiders.txt'
SPIDERS_OUT = './outputs/spiders.txt'
BUSTLE = './inputs/bustle.txt'
BUSTLE_OUT = './outputs/bustle.txt'

# --------------------------------------------------
def random_string():
    """ Generate a random string """

    k = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))


# --------------------------------------------------
def test_exists():
    """ Program exists """

    assert os.path.isfile(PRG)


# --------------------------------------------------
def test_usage():
    """ Prints usage """

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{PRG} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_dies_bad_file():
    """ Fails on bad filename """

    bad = random_string()
    rv, out = getstatusoutput(f'{PRG} {bad}')
    assert rv != 0
    assert out.lower().startswith('usage:')
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------
def run(filenames, opts, expected):
    """ Run with a file """

    rv, out = getstatusoutput(f'{PRG} {" ".join(opts)} {" ".join(filenames)}')
    assert rv == 0
    assert out == expected


# --------------------------------------------------
def test_fox():
    """ fox """

    run([FOX], [], 'WKH TXLFN EURZQ IRA MXPSV RYHU WKH ODCB GRJ.')


# --------------------------------------------------
def test_fox_n():
    """ fox -n 4 """

    run([FOX], ['-n 4'], 'XLI UYMGO FVSAR JSB NYQTW SZIV XLI PEDC HSK.')


# --------------------------------------------------
def test_fox_decode():
    """ fox --decode """

    run([FOX_OUT], ['--decode'],
        'THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.')


# --------------------------------------------------
def test_spiders():
    """ spiders """

    expected = '\n'.join(
        ["GRQ'W ZRUUB, VSLGHUV,", 'L NHHS KRXVH', 'FDVXDOOB.'])
    run([SPIDERS], [], expected)


# --------------------------------------------------
def test_spiders_n():
    """ spiders -n 4"""

    expected = '\n'.join([
        "HSR'X ASVVC, WTMHIVW,", 'M OIIT LSYWI',
        'GEWYEPPC.'
    ])
    run([SPIDERS], ['-n 4'], expected)


# --------------------------------------------------
def test_spiders_decode():
    """ spiders --decode """

    expected = '\n'.join([
        "DON'T WORRY, SPIDERS,", 'I KEEP HOUSE',
        'CASUALLY.'
    ])
    run([SPIDERS_OUT], ['--decode'], expected)


# --------------------------------------------------
def test_bustle():
    """ bustle """

    expected = '\n'.join([
        'WKH EXVWOH LQ D KRXVH',
        'WKH PRUQLQJ DIWHU GHDWK',
        'LV VROHPQHVW RI LQGXVWULHV',
        'HQDFWHG XSRQ HDUWK,—',
        '',
        "WKH VZHHSLQJ XS WKH KHDUW,",
        'DQG SXWWLQJ ORYH DZDB',
        'ZH VKDOO QRW ZDQW WR XVH DJDLQ', 
        'XQWLO HWHUQLWB.'
    ])
    run([BUSTLE], [], expected)


# --------------------------------------------------
def test_bustle_n():
    """ bustle -n 4"""

    expected = '\n'.join([
        'XLI FYWXPI MR E LSYWI',
        'XLI QSVRMRK EJXIV HIEXL',
        'MW WSPIQRIWX SJ MRHYWXVMIW',
        "IREGXIH YTSR IEVXL,—",
        '',
        "XLI WAIITMRK YT XLI LIEVX,",
        'ERH TYXXMRK PSZI EAEC',
        'AI WLEPP RSX AERX XS YWI EKEMR',
        'YRXMP IXIVRMXC.'])
    run([BUSTLE], ['-n 4'], expected)


# --------------------------------------------------
def test_bustle_decode():
    """ bustle --decode """

    expected = '\n'.join([
        'THE BUSTLE IN A HOUSE',
        'THE MORNING AFTER DEATH',
        'IS SOLEMNEST OF INDUSTRIES',
        "ENACTED UPON EARTH,—",
        '',
        "THE SWEEPING UP THE HEART,",
        'AND PUTTING LOVE AWAY',
        'WE SHALL NOT WANT TO USE AGAIN',
        'UNTIL ETERNITY.'])
    run([BUSTLE_OUT], ['--decode'], expected)
