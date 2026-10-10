# collectors package
#
# Each collector module is responsible for ingesting threat data from a
# specific external source (e.g., OSINT feeds, MISP, commercial APIs).
# Example sub-modules:
#   - base.py        (abstract BaseCollector class)
#   - otx.py         (AlienVault OTX)
#   - abuse_ch.py    (abuse.ch URLhaus / MalwareBazaar)
