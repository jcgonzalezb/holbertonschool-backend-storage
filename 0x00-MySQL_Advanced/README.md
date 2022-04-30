# MySQL - MySQL advanced

## Description of the files inside this folder:


0. A SQL script that creates a table users following these requirements:
- id, integer, never null, auto increment and primary key
- email, string (255 characters), never null and unique
- name, string (255 characters)
- If the table already exists, the script should not fail

1. A SQL script that creates a table users following these requirements:
- id, integer, never null, auto increment and primary key
- email, string (255 characters), never null and unique
- name, string (255 characters)
- country, enumeration of countries: US, CO and TN, never null
- If the table already exists, your script should not fail

2. A SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans. Column names must be: origin and nb_fans.

3. A SQL script that lists all bands with Glam rock as their main style, ranked by their longevity. Column names must be: band_name and lifespan (in years). You should use attributes formed and split for computing the lifespan.

4. A SQL script that creates a trigger that decreases the quantity of an item after adding a new order. Quantity in the table items can be negative.

5. A SQL script that creates a trigger that resets the attribute valid_email only when the email has been changed.

6. A SQL script that creates a stored procedure that adds a new correction for a student.  Procedure takes 3 inputs (in this order):
- user_id, a users.id value
- project_name, a new or already exists projects
- score, the score value for the correction

7. A SQL script that creates a stored procedure that computes and store the average score for a student. An average score can be a decimal. Procedure takes 1 input: user_id, a users.id value.

8. An index idx_name_first on the table names and the first letter of name.

9. Creates an index idx_name_first_score on the table names and the first letter of name and the score.



## Languages and Tools:

- OS: Ubuntu 20.04 LTS
- Language: Python 3.8.10
- Style guidelines: [PEP 8](https://www.python.org/dev/peps/pep-0008/)

<p align="left"> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> </p>


## Author

- Juan Camilo González <a href="https://twitter.com/juankter" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="juankter" height="30" width="40" /></a>
<a href="https://bit.ly/2MBNR0t" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="https://bit.ly/2mbnr0t" height="30" width="40" /></a>