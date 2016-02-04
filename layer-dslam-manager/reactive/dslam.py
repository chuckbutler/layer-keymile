from charms.reactive import when, when_not, set_state
from charmhelpers.core.hookenv import config, status_set
from charmhelpers.fetch import install_remote
# by default, when starting with layer:basic - there are no states to signify
# we are ready to do anything, so we're working on a blank canvas

@when_not('dslam_manager.install')
def fetch_package():
    # first concern - we haven't checked config
    cfg = config()
    if not(cfg.get('download_url') and cfg.get('download_sum')):
        # we are not configured if this is true, message to the user
        # and return
        status_set('blocked', 'Charm is not configured, please set '
                   'download_url and download_sum') 
        return

    download_path = install_remote(cfg['download_url'], cfg['download_sum'])
    # really should be invoking an install step
    set_state('dlsam_manager.fetched')
