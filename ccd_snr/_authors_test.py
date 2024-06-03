import aastex
import ccd_snr


def test_authors():
    result = ccd_snr.authors()
    for author in result:
        assert isinstance(author, aastex.Author)
