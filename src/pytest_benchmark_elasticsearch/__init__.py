__version__ = '0.0.0'

from .storage import ElasticsearchStorage

uri_example = "elasticsearch+http[s]://host1,host2/[index/doctype?project_name=Project]"
uri_prefix = "elasticsearch+"


def uri_parse(uri, **kwargs):
    netrc_file = kwargs.pop('netrc')
    args = _parse_elasticsearch_storage(uri[len("elasticsearch+"):], netrc_file=netrc_file)
    return ElasticsearchStorage(*args, **kwargs)


def add_options(addoption, prefix="benchmark-"):
    addoption(
        "--{0}netrc".format(prefix),
        nargs="?", default='', const='~/.netrc',
        help="Load elasticsearch credentials from a netrc file. Default: %(default)r.",
    )


def _parse_hosts(storage_url, netrc_file):
    # load creds from netrc file
    path = os.path.expanduser(netrc_file)
    creds = None
    if netrc_file and os.path.isfile(path):
        creds = netrc.netrc(path)

    # add creds to urls
    urls = []
    for netloc in storage_url.netloc.split(','):
        auth = ""
        if creds and '@' not in netloc:
            host = netloc.split(':').pop(0)
            res = creds.authenticators(host)
            if res:
                user, _, secret = res
                auth = "{user}:{secret}@".format(user=user, secret=secret)
        url = "{scheme}://{auth}{netloc}".format(scheme=storage_url.scheme,
                                                 netloc=netloc, auth=auth)
        urls.append(url)
    return urls


def _parse_elasticsearch_storage(string, default_index="benchmark",
                                 default_doctype="benchmark", netrc_file=''):
    storage_url = urlparse(string)
    hosts = _parse_hosts(storage_url, netrc_file)
    index = default_index
    doctype = default_doctype
    if storage_url.path and storage_url.path != "/":
        splitted = storage_url.path.strip("/").split("/")
        index = splitted[0]
        if len(splitted) >= 2:
            doctype = splitted[1]
    query = parse_qs(storage_url.query)
    try:
        project_name = query["project_name"][0]
    except KeyError:
        project_name = get_project_name()
    return hosts, index, doctype, project_name
