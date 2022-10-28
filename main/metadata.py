import metadata_parser


class getMetaData():

    def title(url):
        page = metadata_parser.MetadataParser(url=str(url), search_head_only=True)
        title = page.get_metadatas('title')
        return title[0]

    def image(url):
        page = metadata_parser.MetadataParser(url=str(url), search_head_only=True)
        image = page.get_metadatas('image')
        return image[0]

    def all(url):
        page = metadata_parser.MetadataParser(str(url), search_head_only=True)
        return str(page.metadata)
