from flask import Flask, render_template
import yaml

bio = Flask(__name__)

with open("links.yaml") as yml:
    links_yaml = yaml.load(yml, Loader = yaml.FullLoader)

## variables con info del yaml
title = links_yaml["title"]
pic = links_yaml["picture"]
name = links_yaml["name"]
short_bio = links_yaml["shortbio"]

# Links
fb_link = links_yaml["links"]["facebook"]["link"]
ig_link = links_yaml["links"]["instagram"]["link"]
pin_link = links_yaml["links"]["pinterest"]["link"]
blog_link = links_yaml["links"]["blog"]["link"]

# Descriptions
fb_description = links_yaml["links"]["facebook"]["description"]
ig_description = links_yaml["links"]["instagram"]["description"]
pin_description = links_yaml["links"]["pinterest"]["description"]
blog_description = links_yaml["links"]["blog"]["description"]


@bio.route("/")
def linktree():
    return render_template('linktree.html', 
    links_yaml = links_yaml, title = title, 
    pic = pic, name = name, short_bio = short_bio, 
    fb_link = fb_link, ig_link = ig_link, pin_link = pin_link, blog_link = blog_link,
    fb_description = fb_description, ig_description = ig_description, pin_description = pin_description, blog_description = blog_description)

if __name__ == '__main__':
    bio.run(host="0.0.0.0", debug=True)

