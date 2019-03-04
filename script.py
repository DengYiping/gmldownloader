from xml.dom import minidom
from urllib import request, error
xmldoc = minidom.parse('test.gml')
obj_list = xmldoc.getElementsByTagName('Object')
for obj in obj_list:
    obj_id = obj.getAttribute('gml:id')
    img_list = obj.getElementsByTagName('heroimage')
    logo_list = obj.getElementsByTagName('logo')
    if(len(img_list)):
        img = img_list[0].firstChild
        if(img):
            img_name = obj_id + 'I' + '.jpg'
            if(img.data != ''):
                try:
                    request.urlretrieve(img.data, img_name)
                    print('download image {} with url {}', img_name, img.data)
                except error.HTTPError:
                    pass
    if(len(logo_list)):
        logo = logo_list[0].firstChild
        if(logo):
            logo_name = obj_id + 'L' + '.jpg'
            if(logo.data != ''):
                try:
                    request.urlretrieve(logo.data, logo_name)
                    print('download logo {} with url {}', logo_name, logo.data)
                except error.HTTPError:
                    pass