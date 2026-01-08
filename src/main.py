import os
import shutil
from string.templatelib import Template

from copystatic import copy_files_recursive
from markdown_blocks import markdown_to_html_node

dir_path_static = "./static"
dir_path_public = "./public"


def extract_title(markdown):
    lines = markdown.split("\n")

    if not lines[0].startswith("# "):
        raise Exception("No title found")

    return lines[0][2:]


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path) as f:
        markdown_file = f.read()

    with open(template_path) as f:
        template_content = f.read()

    markdown = markdown_to_html_node(markdown_file)
    the_html = markdown.to_html()

    title_extract = extract_title(markdown_file)
    new_html = template_content.replace("{{ Title }}", title_extract)
    new_html = new_html.replace("{{ Content }}", the_html)

    with open(dest_path, "w") as f:
        f.write(new_html)


def main():
    # print("Deleting public directory...")
    # if os.path.exists(dir_path_public):
    #     shutil.rmtree(dir_path_public)
    #
    # print("Copying static files to public directory...")
    # copy_files_recursive(dir_path_static, dir_path_public)

    from_path = "/home/rasmus/Projekter/Boot.dev/static-site/content/index.md"
    template_path = "/home/rasmus/Projekter/Boot.dev/static-site/template.html"
    dest_path = "/home/rasmus/Projekter/Boot.dev/static-site/public/index.html"
    generate_page(from_path, template_path, dest_path)


main()
