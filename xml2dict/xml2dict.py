import json
import xml.etree.ElementTree as xmlElementTree

from xml.etree.ElementTree import ElementTree, Element


def is_list_child(tags, tag):
    """tag type
    :type tag str
    :type tags list
    :return:
    """
    i = 0
    for t in tags:
        if i > 1:
            return True
        if t == tag:
           i += 1 
    return i > 1


def append_attr_to_dict(attrib, result):
    """append xml element attrib to dict
    :param attrib: attributes
    :param result: dict
    :type result dict
    :type attrib dict
    :return: dict
    """
    for attr in attrib:
        result["@%s" % attr] = attrib[attr]
    return result


def _parse(node, result):
    """ parse xml tree to dict
    :param node:
    :type node Element
    :param result:
    :type result dict
    :return: dict
    """
    child_tag = []
    dict_child = []
    list_child = [] # filter(lambda tag: is_list_child(child_tag, tag), child_tag)

    for child in list(node):
        child_tag.append(child.tag)

        if len(list(child)) > 0:
            dict_child.append(child.tag)

    for tag in child_tag:
        if is_list_child(child_tag, tag):
            list_child.append(tag)

    if len(list(node)) == 0:
        node_text = node.text
        if node_text is None:
            node_text = append_attr_to_dict(node.attrib, {})
        result[node.tag] = node_text
        return result

    for child in list(node):
        if child.tag in list_child:
            if child.tag not in result:
                result[child.tag] = []
                append_attr_to_dict(child.attrib, result)

            result[child.tag].append(_parse(child, {}))
        elif child.tag in dict_child:
            result[child.tag] = {}
            append_attr_to_dict(child.attrib, result)

            _parse(child, result[child.tag])
        else:
            _parse(child, result)
    return result


def parser(xml):
    """parser warp
    :param xml:
    :type xml ElementTree
    :return:
    """
    return _parse(xml.getroot(), {})


if __name__ == '__main__':
    xml = xmlElementTree.parse("./test.xml")
    print(json.dumps(parser(xml)))

__all__ = ['parser']
