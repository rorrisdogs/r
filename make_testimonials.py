#! /bin/python3

import os

out=open("testimonials.html.base","r").read()

list=open("testimonials.csv","r").read().split("\n,")

out+="<!-- begin testimonials -->"

for t in list:
    t=t.strip().replace("’","'").replace("“","\"").replace("”","\"")
    t=t.split("\n",1)
    message=t[1].ljust(130,"\t")

    html=f"""<div class="image-container"><div><span>
    "{message}"
    <br><i><b>
    {t[0]}
    </b></i><span></div><div>
    <img  class="testimonial_picture" src="assets/{t[0]}">
    </div></div>"""
    print(html)
    out+=html+"\n"


out+="</body>\n"

open("testimonials.html","w").write(out)

