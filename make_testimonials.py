#! /bin/python3

import os

list=open("testimonials.csv","r").read().split("\n,")

pics={
     "Jill Dyckman"
        }

for t in list:
    t=t.strip()
    t=t.split("\n",1)

    html=f"""<div class="image-container"><div><span>
    "{t[1]}"
    <br><i><b>
    {t[0]}
    </b></i><span></div><div>
    <img  class="testimonial_picture" src="assets/{t[0]}">
    </div></div>"""
    print(html)

