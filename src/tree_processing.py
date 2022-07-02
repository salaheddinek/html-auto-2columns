import bs4
import re


def unwrap_shopify_useless_strong_tags(tree):
    for match in tree.find_all("strong"):
        tag_txt = str(match).lower().replace(" ", "")
        if 'style="font-weight:normal' in tag_txt:
            match.unwrap()
    return tree


def unwrap_tags_without_classes(tree, tag_name="div"):
    for match in tree.find_all(tag_name):
        if "class" not in match.attrs:
            if match.parent:
                p_name = match.parent.name
                if p_name not in ["body", '[document]', "html", "head"]:
                    match.unwrap()

    return tree


def remove_none_class_attributes(tree, tags_names="p"):
    search_tags = tags_names
    if isinstance(search_tags, str):
        search_tags = {search_tags}
    for search_tag in search_tags:
        for match in tree.find_all(search_tag):
            if "class" in match.attrs:
                match.attrs = {"class": match["class"]}
            else:
                match.attrs = {}
    return tree


def unwrap_tags_with_no_content(tree, tags_names="p"):
    search_tags = tags_names
    if isinstance(search_tags, str):
        search_tags = {search_tags}
    for search_tag in search_tags:
        for x in tree.find_all(search_tag):
            if len(x.get_text(strip=True)) == 0:
                x.unwrap()
    return tree


def group_consecutive_tags(tree, tags_names="p"):
    html_text = clear_spaces(str(tree))
    search_tags = tags_names
    if isinstance(search_tags, str):
        search_tags = {search_tags}
    dummy_tag = "</br dummy_attribute_remove_me_later_please>"
    for search_tag in search_tags:
        updated = True
        while updated:
            updated = False
            for bridge in ["", " "]:
                # TODO: use beautifulsoup for this issue later
                search_term = f"</{search_tag}>{bridge}<{search_tag}"
                idx = html_text.find(search_term)
                if idx == -1:
                    continue
                search_term_ext = html_text[idx + len(search_term): html_text.find(">", idx + len(search_term)) + 1]
                r_idx = html_text.rfind(f"<{search_tag}", 0, idx)
                if search_tag == "b" and html_text[r_idx + 2] == "r": # for <br> case
                    r_idx = html_text.rfind(f"<{search_tag}", 0, r_idx - 1)
                l_idx = html_text.find(f"</{search_tag}>", idx + 1)
                if l_idx == -1 or r_idx == -1:
                    print("WARNING: this should not have happened (find group_consecutive_tags)")
                l_idx += len(f"</{search_tag}>")
                # print(html_text[r_idx:l_idx])
                twin_tags = bs4.BeautifulSoup(html_text[r_idx:l_idx], "html.parser").find_all(search_tag)
                replace_with = bridge
                if len(twin_tags) != 2:
                    replace_with = f"</{search_tag}>{dummy_tag}<{search_tag} {search_term_ext}"
                elif twin_tags[0].attrs != twin_tags[1].attrs:
                    replace_with = f"</{search_tag}>{dummy_tag}<{search_tag} {search_term_ext}"

                updated = True
                html_text = html_text.replace(search_term + search_term_ext, replace_with, 1)
                break

    html_text = html_text.replace(dummy_tag, "")
    return bs4.BeautifulSoup(html_text, "html.parser")


def clear_spaces(in_html):
    res = in_html
    for pun in ["!", ",", ".", ":", ";", "?"]:
        res = res.replace(pun, pun + " ")
    pattern = re.compile("([\n])|([\ ]{2,})")
    res = re.sub(pattern, '', res)
    return res


def prettify2(in_html, indent_width=4, encoding=None, formatter="minimal"):
    tree = bs4.BeautifulSoup(in_html, "html.parser")
    r = re.compile(r'^(\s*)', re.MULTILINE)
    return r.sub(r'\1' * indent_width, tree.prettify(encoding, formatter))
