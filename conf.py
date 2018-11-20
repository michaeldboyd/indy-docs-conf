# This is used for linking and such so we link to the thing we're building
rtd_version = os.environ.get('READTHEDOCS_VERSION', 'latest')
if rtd_version not in ['stable', 'latest']:
    rtd_version = 'latest'

intersphinx_mapping = {
    'sovrin': ('http://sovrin.readthedocs.io/en/%s/' % rtd_version, None),
    'indy-sdk': ('http://indy-sdk.readthedocs.io/en/%s/' % rtd_version, None),
    'indy-node': ('http://indy-node.readthedocs.io/en/%s/' % rtd_version, None),
}

# download 
import gensidebar
gensidebar.generate_sidebar(globals(), 'sdk')

# if it didn't work, set index as masterdoc
master_doc = "builder/toc"