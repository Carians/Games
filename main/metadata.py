import metadata_parser


class getMetaData():

    def title(url):
        try:
            page = metadata_parser.MetadataParser(url=str(url), search_head_only=True)
            title = page.get_metadatas('title')
            return title[0]
        except Exception as e:
            print('error metadata: '+e)
            return None


    def image(url):
        try:
            page = metadata_parser.MetadataParser(url=str(url), search_head_only=True)
            image = page.get_metadatas('image')
            return image[0]
        except Exception as e:
            print('error metadata: '+e)
            return None

    def all(url):
        try:
            page = metadata_parser.MetadataParser(str(url), search_head_only=True)
            return str(page.metadata)
        except:
            pass
        return None
