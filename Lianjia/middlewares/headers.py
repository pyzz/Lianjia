import random
from Lianjia.constants.headers import LIANJIA_HEADERS, WEB_USER_AGENTS

class HeadersMiddleware(object):
    def process_request(self, request, spider):
        """set headers and cookies"""
        if not bool(request.headers):
            for k, v in LIANJIA_HEADERS.iteritems():
                request.headers.setdefault(k, v)
        request.headers.setdefault('User-Agent', random.choice(WEB_USER_AGENTS))
        return None
