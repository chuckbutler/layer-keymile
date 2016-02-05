from charms.reactive import when, when_not
from charmhelpers.core import fetch

@when_not('keymile.downloaded')
def download_payload():
    fetch.install_remote('http://git.io/weave') 
