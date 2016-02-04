from charms.reactive import when, when_not, set_state
from charmhelpers.core.hookenv import config, status_set, open_port
from charmhelpers.fetch import install_remote
from charmhelpers.core.templating import render
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
    install_dslam_manager(download_path)
    set_state('dlsam_manager.fetched')

def install_dslam_manager(download_path):
    #untar and install the dslam manager  + set any ACL's required 
    # create systemd / upstart job to keep service running
    # open any ports required to reach the dslam manager
    open_port(80)
    pass

# This is an illustrative method to show how to pass configuration
# from config.yaml to a jinja2 template. simply reference the keys in
# in jinja2 format {{ download_url }} as an example
def configure_dslam_manager():
    # template, destination_directory, databag 
    render('upstart', '/tmp/upstart', config())
