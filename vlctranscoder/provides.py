from charmhelpers.core import hookenv
from charms.reactive import hook
from charms.reactive import RelationBase
from charms.reactive import scopes


class VLCTransocder(RelationBase):

     @hook('{interface:vlctranscoder}-relation-{joined,changed}')
     def connect_to_transcoder(self):
         set_state('transcoder.connected')

     @hook('{interface:vlctranscoder}-relation-{broken,departed}')
     def disconnect_from_transcoder(self):
         remove_state('transcoder.connected')

    def configure(self, stream_url):
        self.set_remote('stream_url', stream_url)
