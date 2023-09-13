---
tags:
  - notes
  - slss
  - y2023
  - programming-level-1-2
---
# Headings
We create headings in Markdown using hash (#) symbols
To create subheadings, we can use multiple hash symbols
## This is a level 2 subheading
### This is a level 3 subheading
###### This is a level 6 subheading

# Modifying Text Style
## Bold and Italics
We use asterisks (\*) to modify text styling, specifically
bold and italics

e.g.
I want this **word** specifically to be bold
I want this *word* to be italicized
I want this ***word*** to be both bold and italicized

## Escape characters
**ASIDE**: If we want to place a character that is a *keyword* or
*reserved word*, and we want the LITERAL character, use
the back slash (\\)
	e.g. if we want to put an asterisk, we do this \\\*

## ~~Strikethrough~~
We can also strikethrough characters using the tilde (~)
I want to strikethrough this specific ~~word~~
~~This sentence is struck through~~
# Links
We can link things in our Markdown files
[One tool to use.](https://chat.openai.com)
Exercise:
* if you have an openai account, do the following:
	* ask chatgpt to create for you markdown code that is a link to two websites of your choice
* if you don't have chatgpt/openai, create two links to websites of your choice in the space below

e.g. [My favourite website right now](https://nyt.com)

e.g. if you use openai
Put in their code, and in italics say that it's from chatgpt
[A search engine](https://google.com) *from chatgpt*

```markdown
1. [Google](https://google.com)
2. [Steveston-London Secondary School](https://slss.sd38.bc.ca)
*from chatgpt*
```
# Images
## Method One
e.g.
![Cheetah](http://elelur.com/data_images/mammals/cheetah/cheetah-02.jpg)
# Method Two Doesn't Work
![Cheetah][cheetahpic]
[cheetahpic]: http://elelur.com/data_images/mammals/cheetah/cheetah-02.jpg

# Blockquotes
Block quotes allow us to emphasize a bigger chunk of text.
We use carets (>) to create blockquotes.

> This is an example of a blockquote
> This is line two of the blockquote
> 
> This is the fourth line; the third is blank

# Lists
We can create both unordered and ordered lists
## Unordered Lists
To create each point, we use (\*) with a space behind it
We can create sublists by placing **TABS** before the asterisk

e.g.
* dairy
	* eggs
	* milk
	* cheese
* juice

## Ordered Lists
If there is a specific order to the elements in our list,
we create ordered lists
We use numbers, followed by periods to create ordered lists

e.g.
1. Put butter into mixing bowl
2. Add sugar to butter (*hold shift to get the second line*)
   Add both brown and regular sugar
3. Use the mixer to cream the butter and sugar together

# Tables
We can organize information in tables using Markdown
We use dashes (-) and pipes (|)

Tables in Markdown require headings

e.g.

| Name        | Age        | Sign        | Superpower       |
| ---         | ---        | ---         | ---              |
| Bruce Wayne | 35         | Aquarius    | Intelligence / $ |
| Mr. Ubial   | Unaging    | All of them | Dad strength     |
| Yourself    | Your age   | Your Sign   | Super strength   |

