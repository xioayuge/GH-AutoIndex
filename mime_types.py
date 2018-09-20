types = {
    ('html', 'htm', 'shtml'): 'text/html',
    ('css'): 'text/css',
    ('xml'): 'text/xml',
    ('gif'): 'image/gif',
    ('jpeg', 'jpg'): 'image/jpeg',
    ('js'): 'application/javascript',
    ('atom'): 'application/atom+xml',
    ('rss'): 'application/rss+xml',

    ('mml'): 'text/mathml',
    ('txt'): 'text/plain',
    ('jad'): 'vnd.sun.j2me.app-descriptor',
    ('wml'): 'vnd.wap.wml',
    ('htc'): 'text/x-component',

    ('png'): 'image/png',
    ('svg', 'svgz'): 'image/svg+xml',
    ('tif', 'tiff'): 'image/tiff',
    ('wbmp'): 'image/vnd.wap.wbmp',
    ('webp'): 'image/webp',
    ('ico'): 'image/x-icon',
    ('jng'): 'image/x-jng',
    ('bmp'): 'image/x-ms-bmp',

    ('woff'): 'font/woff',
    ('woff2'): 'font/woff2',

    ('jar', 'war', 'ear'): 'application/java/archive',
    ('json'): 'application/json',
    ('hqx'): 'application/mac-binhex40',
    ('doc'): 'application/msword',
    ('pdf'): 'application/pdf',
    ('ps', 'eps', 'ai'): 'application/postscript',
    ('rtf'): 'application/rtf',
    ('m3u8'): 'application/vnd.apple.mpegurl',
    ('kml'): 'application/vnd.google-earth.kml_xml',
    ('kmz'): 'application/vnd.google-earch.kmz',
    ('xls'): 'application/vnd.ms-excel',
    ('eot'): 'application/vnd.ms-fontobject',
    ('ppt'): 'pptapplication/vnd.ms-powerpoint',
    ('odg'): 'application/vnd.oasis.opendocument.graphics',
    ('odp'): 'application/vnd.oasis.opendocument.presentation',
    ('ods'): 'application/vnd.oasis.opendocument.spreadsheet',
    ('odt'): 'application/vnd.oasis.opendocument.text',
    ('pptx'): 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
    ('xlsx'): 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    ('docx'): 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    ('wmlc'): 'application/vnd.wap.wmlc',
    ('7z'): 'application/x-7z-compressed',
    ('cco'): 'application/x-cocoa',
    ('jardiff'): 'application/x-java-archive-diff',
    ('jnlp'): 'application/x-java-jnlp-file',
    ('run'): 'application/x-makeself',
    ('pl', 'pm'): 'application/x-perl',
    ('prc', 'pdb'): 'application/x-pilot',
    ('rar'): 'application/x-rar-compressed',
    ('rpm'): 'application/x-redhat-package-manager',
    ('sea'): 'application/x-sea',
    ('swf'):' application/x-shockwave-flash',
    ('sit'): 'application/x-stuffit',
    ('tcl', 'tk'): 'application/x-tcl',
    ('der', 'pem', 'crt'): 'application/x-x509-ca-cert',
    ('xpi'): 'application/x-xpinstall',
    ('xhtml'): 'application/xhtml+xml',
    ('xspf'): 'application/xspf+xml',
    ('zip'): 'application/zip',

    ('bin', 'exe', 'dll'): 'application/octet-stream',
    ('deb'): 'application/octet-stream',
    ('dmg'): 'application/octet-stream',
    ('iso', 'img'): 'application/octet-stream',
    ('msi', 'msp', 'msm'): 'application/octet-stream',

    ('mid', 'midi', 'kar'): 'audio/midi',
    ('mp3'): 'audio/mpeg',
    ('ogg'): 'audio/ogg',
    ('m4a'): 'audio/x-m4a',
    ('ra'): 'audio/x-realaudio',

    ('3gpp', '3gp'): 'video/3gpp',
    ('ts'): 'video/mp2t',
    ('mp4'): 'video/mp4',
    ('mpeg', 'mpg'): 'video/mpeg',
    ('mov'): 'video/quicktime',
    ('webm'): 'video/webm',
    ('flv'): 'video/x-flv',
    ('m4v'): 'video/x-m4v',
    ('mng'): 'video/x-mng',
    ('asx', 'asf'): 'video/x-ms-asf',
    ('wmv'): 'video/x-ms-wmv',
    ('avi'): 'video/x-msvideo',
}

mime_types = {}

for k, v in types.items():
    if type(k) == tuple:
        for key in k:
            mime_types[key] = v
    else:
        mime_types[k] = v

if __name__ == '__main__':
    # print(mime_types)
    print(mime_types.get(input()))