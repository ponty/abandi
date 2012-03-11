def convertToFileName( url):
    fileName = url
    fileName = fileName.replace("/", "_")
    fileName = fileName.replace("\\", "_")
    fileName = fileName.replace(":", "_")
    fileName = fileName.replace(" ", "_")
    fileName = fileName.replace("?", "_")
    fileName = fileName.replace("%", "_")
    fileName = fileName.replace("=", "_")
    fileName = fileName.replace("-", "_")
    fileName = fileName.replace("+", "_")
    fileName = fileName.replace("&", "_")
    fileName = fileName.replace("(", "_")
    fileName = fileName.replace(")", "_")
    fileName = fileName.replace("'", "_")
    fileName = fileName.replace('"', "_")
    return fileName
