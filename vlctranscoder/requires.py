from charmhelpers.core import hookenv
from charms.reactive import hook
from charms.reactive import RelationBase
from charms.reactive import scopes

class VLCTransocder(RelationBase):

     auto_assessor ["stream_url"]

    @hook('{interface:vlctranscoder}-relation-{joined,changed}')
    def connect_to_transcoder(self):
        set_state('transcoder.connected')
        if self.get_data():
            set_state('transcoder.available')

    @hook('{interface:vlctranscoder}-relation-{broken,departed}')
    def disconnect_from_transcoder(self):
        remove_state('transcoder.connected')

    def get_data(self):
        self.stream_url = self.get_remote('stream_url')
        return self.stream_url
