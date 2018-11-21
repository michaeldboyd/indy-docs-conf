import os
def write_if_changed(fname, contents):
    
    try:
        with open(fname, 'r') as fp:
            old_contents = fp.read()
    except:
        old_contents = ''
        
    if old_contents != contents:
        with open(fname, 'w') as fp:
            fp.write(contents)

def generate_sidebar(conf, conf_api):
    
    # determine 'latest' or 'stable'
    # if not conf.do_gen:
    do_gen = os.environ.get('SIDEBAR', None) == '1' or conf['on_rtd']
    version = conf['rtd_version']
    
    lines = [
        '', '.. DO NOT MODIFY! THIS PAGE IS AUTOGENERATED!', ''
    ]

    def toctree(name, depth):
        lines.extend(['.. toctree::',
                        '    :caption: %s' % name,
                        '    :maxdepth: %d' % depth,
                        ''])

    def endl():
        lines.append('')

    def write(desc, link):
        if conf_api == 'sovrin':
            args = desc,  link
        # elif not do_gen:
        #     return
        else:
            args = desc, 'https://sovrin.readthedocs.io/en/%s/%s.html' % (version, link)
            
        lines.append('    %s <%s>' % args)

    def write_api(project, desc, link):
        if project != conf_api:
            # if do_gen:
            args = desc, project, version, link
            lines.append('    %s <https://sovrin.readthedocs.io/projects/%s/en/%s/%s.html>' % args)
        else:
            lines.append('    %s <%s>' % (desc, link))
    

    toctree('Sovrin', 2)
    write('Release Notes', 'release-notes')
    write('Build Instructions', 'build-scripts/ubuntu-1604/README')

    toctree('Repositories', 2)
    write_api('node', 'Indy Node', 'index')
    write_api('sdk', 'Indy SDK', 'index')
    endl()

    write_if_changed('toc.rst', '\n'.join(lines))

def get_intersphinx_mapping(version):
    return {
        'sovrin': ('http://sovrin.readthedocs.io/en/%s/' % version, None),
        'indy-sdk': ('http://indy-sdk.readthedocs.io/en/%s/' % version, None),
        'indy-node': ('http://indy-node.readthedocs.io/en/%s/' % version, None),
    }