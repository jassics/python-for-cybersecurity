class GhConfig:
    @staticmethod
    def buildURL(url, endpoint):
        return url+endpoint
    
    @staticmethod
    def buildPATH(path, filename):
        return path+filename

    class API:
        DEV_URL= "http://127.0.0.1:8000"
        PROD_URL="https://ghbot-api.herokuapp.com"
        ENDPOINT = "/ghbot"

    class CSS:
        PARSER = "html.parser"
        OUTER_ELM = "a"
        OUTER_CLASS = "d-inline-block no-underline mb-1"
        INNER_ELM = "span"
        INNER_CLASS = "Link--secondary"

    class DefaultProfile:
        USERNAME = "deepraj1729"
        
    class IO:
        OUTPUT = "./output/"
        LOGS_PATH = "./logs/"