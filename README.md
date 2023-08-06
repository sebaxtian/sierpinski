# sierpinski
This is a set of algorithms related to Fractal Geometry by Wacław Franciszek Sierpiński.

## How to use

Please read and execute each step below:

### Step 1

Create and use Python virtual environment:

```bash
$promt> python -m venv .venv
$promt> source .venv/bin/activate
```

### Step 2

Install all Python requirements:

```bash
$promt> python -m pip install -U pip
$promt> pip install -r requirements.txt
```

### Optional

Generate a requirements file and then install from it in another environment:

```bash
$promt> pip freeze > requirements.txt
```

---

## Sierpinski Triangle

The Sierpinski Triangle is created from an initial triangle, usually an equilateral triangle, by finding the midpoint of each side of the triangle. Then, each midpoint is connected with new lines to the other ones, creating four smaller triangles. However, the middle triangle is removed, which is the algorithm's base case. This is now a recursive process, so repeat it infinitely as many times as you want: always finding the midpoints, connecting them with new lines, removing the middle triangle, leaving three smaller identical triangles, and finally repeating the process.

This fractal has a dimension approximately equal to 1.585 and an area equal to zero.

![Sierpinski Triangle](/imgs/sierpinski_triangle.png "Sierpinski Triangle")

### This video below from Euler's Academy explain the process:
[![Watch the video](https://img.youtube.com/vi/KOTu02dMZDA/sddefault.jpg)](https://youtu.be/KOTu02dMZDA)

### My Solution using Python

Please review the python code in [triangle.py](triangle.py) and then run it

```bash
$promt> python triangle.py
```

![Sierpinski Triangle](/imgs/my_sierpinski_triangle.png "Sierpinski Triangle")

---

***That's all for now ...***

---

#### License

[GPL-3.0 License](./LICENSE)

#### About me

[https://about.me/sebaxtian](https://about.me/sebaxtian)
