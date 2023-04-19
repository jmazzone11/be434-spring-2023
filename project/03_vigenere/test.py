""" Tests for vigenere.py"""

import os
import string
import re
import random
from subprocess import getstatusoutput

PRG = './vigenere.py'
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

    run([FOX], [], 'VPT XYZES QYSNP NDE NLOXH VZVT BWL PRBG SVK.')


# --------------------------------------------------
def test_fox_k():
    """ fox -k TEST """

    run([FOX], ['-k TEST'], 'MLW JNMUD UVGPG JGQ CYEIL SNXK XZX EERR WSY.')


# --------------------------------------------------
def test_fox_decode():
    """ fox --decode """

    run([FOX_OUT], ['--decode'],
        'THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.')


# --------------------------------------------------
def test_spiders():
    """ spiders """

    expected = '\n'.join(
        ["FWC'A AFTZN, ZTZFMGZ,", 'K STLT YQCHL', 'EIHBECNG.'])
    run([SPIDERS], [], expected)


# --------------------------------------------------
def test_spiders_k():
    """ spiders -k TEST"""

    expected = '\n'.join([
        "WSF'M PSJKR, WHBWIJL,", 'B OWXI LGNLI',
        'VEKNTPDR.'
    ])
    run([SPIDERS], ['-k TEST'], expected)


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
        'VPT IYJVTT PR R JWJZI',
        'VPT TSIPQCN EWVMG KIRVP',
        'KA HVPVOVTZX FH QCKYJVZXLW',
        'GVPJXVF CEVR VCZIO,—',
        '',
        "VPT ZAVGXXUK LR BWL LVCZI,",
        'CVS WYKVQCN PFXM PDEP',
        'YM HOECN VDA ARPB IV YJG IVHME', 
        'WVIPP VVMGUMKA.'
    ])
    run([BUSTLE], [], expected)


# --------------------------------------------------
def test_bustle_k():
    """ bustle -k TEST"""

    expected = '\n'.join([
        'MLW UNWLEX MF T ASMLX',
        'MLW FHVFBGK SYMIJ WXELA',
        'BW KHEIEGXWL HY MFWNWLKBIK',
        "XRSVMIV NISF XTVLA,—",
        '',
        "MLW LPIWIBRY NI XZX AISKM,",
        'TRV INXLBGK DHOI SPTC',
        'PI KATPD GHX OTGX LH NWW TZEAG',
        'NRLBE ILXKRAMR.'])
    run([BUSTLE], ['-k TEST'], expected)


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
