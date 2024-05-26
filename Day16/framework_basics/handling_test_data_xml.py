import xmltodict

# for handling xml we use normal file handling functions like read() to read the content

file_path = r"D:\SeleniumPython\Projects\FITA\pythonProject1_FITA\Day16\framework_basics\xml_file.xml"

with open(file_path) as read_xml:
    xml_content = read_xml.read()
    print(xml_content)

dict_xml = xmltodict.parse(xml_content)
for i in dict_xml['catalog'].values():
    print(i)



