""" Tests for substitution.py"""

import os
import string
import random
import re
from subprocess import getstatusoutput

PRG = './substitution.py'
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

    run([FOX], [], 'VYL NFCRU SJMOD TMX AFIZK MBLJ VYL WHGQ EMP.')


# --------------------------------------------------
def test_fox_s():
    """ fox -s 4 """

    run([FOX], ['-s 4'], 'GTP KBADY JFXSR EXZ WBOIU XNPF GTP QHVL MXC.')


# --------------------------------------------------
def test_fox_decode():
    """ fox --decode """

    run([FOX_OUT], ['--decode'],
        'THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.')


# --------------------------------------------------
def test_spiders():
    """ spiders """

    expected = '\n'.join(
        ["EMD'V OMJJQ, KZCELJK,", 'C ULLZ YMFKL', 'RHKFHWWQ.'])
    run([SPIDERS], [], expected)


# --------------------------------------------------
def test_spiders_s():
    """ spiders -s 4"""

    expected = '\n'.join([
        "MXR'G SXFFL, UIAMPFU,", 'A YPPI TXBUP',
        'DHUBHQQL.'
    ])
    run([SPIDERS], ['-s 4'], expected)


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
        'VYL SFKVWL CD H YMFKL',
        'VYL IMJDCDP HTVLJ ELHVY',
        'CK KMWLIDLKV MT CDEFKVJCLK',
        'LDHRVLE FZMD LHJVY,—',
        '',
        "VYL KOLLZCDP FZ VYL YLHJV,",
        'HDE ZFVVCDP WMBL HOHQ',
        'OL KYHWW DMV OHDV VM FKL HPHCD', 
        'FDVCW LVLJDCVQ.'
    ])
    run([BUSTLE], [], expected)


# --------------------------------------------------
def test_bustle_s():
    """ bustle -s 4"""

    expected = '\n'.join([
        'GTP JBUGQP AR H TXBUP',
        'GTP OXFRARC HEGPF MPHGT',
        'AU UXQPORPUG XE ARMBUGFAPU',
        "PRHDGPM BIXR PHFGT,—",
        '',
        "GTP USPPIARC BI GTP TPHFG,",
        'HRM IBGGARC QXNP HSHL',
        'SP UTHQQ RXG SHRG GX BUP HCHAR',
        'BRGAQ PGPFRAGL.'])
    run([BUSTLE], ['-s 4'], expected)


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
