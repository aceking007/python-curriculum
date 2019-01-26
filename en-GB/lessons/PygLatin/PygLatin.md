---
title: PygLatin
level: Python +
language: en-GB
stylesheet: python
embeds: "*.png"
materials: ["Club Leader Resources/project-name/*.*","Project Resources/project-name-finished/*.*"]
...

# Introduction { .intro }

Pig Latin is a fun language game in which English words are altered by rearranging letters of a word and adding a new suffix.
Today we will learn to translate words by moving the first letter of the word to the end and adding an 'ay' at the end.
Thus, 'python' would become 'ythonpay' and 'latin' would become 'atinlay'.
In this project you will learn to make a Pig Latin converter using python that can translate English to Pig Latin.

<div class="trinket">
		<iframe src="https://trinket.io/embed/python/0ef746b2ca?outputOnly=true&start=result" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
</div>

#Step 1: Warm-Up { .activity}

Let's start by writing some text.

## Activity Checklist { .check}

+ Open the blank Python template Trinket: <a href="http://jumpto.cc/python-new" target="_blank_">jumpto.cc/python-new</a>. If you're reading this online, you can also use the embedded version of this trinket below.

<div class="trinket">
		<iframe src="https://trinket.io/embed/python/4eb32c4ad2?start=result" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
</div>

+ Type the following into the window that appears:

    ![screenshot](warm-up.jpg)
		The line `#!/bin/python3` just tells Trinket that we're using Python 3.
		If you want to use any previous versions of python, you can remove that line.

+ Press 'run', and you should see that the `print()` command prints everything between the quote marks `''`.

    ![screenshot](warmup-res.jpg)

+ If you make a mistake, you'll get an error message instead - telling you what went wrong!

    Try it! Delete the end quote `'` or the closing bracket `)` (or both) and see what happens.

    ![screenshot](bad-input.jpg)

+ Replace the quote or bracket and click 'run' to make sure your project works again.

## Save Your Project {.save}

__You don't need a trinket account to save your code__


# Step 2: Print the Welcome statement { .activity }

Let's start the program by welcoming people who visit.

## Activity Checklist { .check }

+ Let's print an opening statement:
	![screenshot](welcome.jpg)

## Challenge: Better intro {.challenge}
Come up with an interesting opening statement that will help people understand more about Pig Latin.

## Save your project { .save }

# Step 3: User Input { .activity }

A user is someone who uses your program to perform certain tasks. We need a word from the user to translate it.

## Activity Checklist { .check }

+ Type the following in the trinket:
	![screenshot](input.jpg)
	The input command asks the user for an input (in this case, a word) which we save in the variable word.
	The print command lets you see the word that the user entered.
	The message inside the brackets _('Enter a word:')_ is what the prompt the user sees before entering a word.

+ Note that the line inside the brackets is enclosed in an inverted comma, if you remove that you get an error.
	![screenshot](line2.jpg)

+ After experimenting for a bit with the input command, revert all the changes.

+ Now, remove the last print statement from your program and proceed.

## Save your project { .save}

# Step 4: Check the input { .activity }

To write a good program, we should be able to find any problems, even with the inputs. We need to check if the user input has proper characters.

## Activity Checklist { .check }

+ We need to check if  the input has some characters, so we will use a function to calculate the length of the input.
	Try out this function in the trinket or in a separate trinket:
	![screenshot](char.jpg)

+ We can check for the length of the word the user just entered in a same way:
	![screenshot](check.jpg)

+ Now we need to check if the length of the word is more than zero or not. We can do so by using an 'if' statement.
	![screenshot](if.jpg)
	The 'if' statement checks if a given condition is true or false and executes accordingly.
	If the condition is _'true'_, it carries out the instructions written in the _if block_.
	If the condition is _'false'_, it carries out the instructions written in the _else block_.

+ We can use the 'if' statement to check if the length of our word is zero:
	![screenshot](wordcheck.jpg)

+ See what happens when you enter no word as input:
	![screenshot](fail.jpg)

+ Now we need to confirm that the input word contains only English letters and not any numbers or special signs.
	We use another function called isalpha().
	![screenshot](tf.jpg)

+	Play around and input some more words into the isalpha() function and check what you get.

+ Now we add the isalpha() as another condition in the 'if' statement. We can add the condition by using an 'and' operator:
	![screenshot](isalpha.jpg)
	__Note that the input is invalid even if it contains some characters.
	This is because 'and' operator returns true only if both the given conditions are met.__

+ Input different words and see the effect of your code.

## Test your project { .flag}
## Save your project { .save}

# Step 5: The suffix and lowercase { .activity }

Change the case of the input and save a suffix.

## Activity Checklist { .check }

+ Make a variable to store our suffix (ay):
	![screenshot](ay.jpg)

+ Now we need to change the user input to lowercase in case someone typed in something capitalized like 'Sun'.
	We can do this by a function called 'lower()'.
	![screenshot](lower.jpg)

+ Play around with the lower() function and try out different inputs.

+ We use the lower function in our program as follows:
	![screenshot](low.jpg)
	_Note that we are carrying out the operations inside the if block._

## Test your project { .flag}
## Save your project { .save}

# Step 6: Changing the word { .activity }

This is where the real change happens

## Activity Checklist { .check }

+ First we create a variable called 'first' to store the first letter of our word:
	![screenshot](frst.jpg)

+ We create a new variable that contains the concatenation (or addition) of the three variables, 'original', 'first' and 'pyg':
	![screenshot](new.jpg)

+ Now, if we print the new word we see that it shows up everything, including the first letter which we don't want.
	![screenshot](wrong.jpg)

+ To prevent this from happening, we can tweak the code a bit:
	![screenshot](right.jpg)
	The square bracket after 'new' instructs the program to print the word starting from the second letter.
	__Remember, python starts counting from 0 onwards, thus [1:] means start from the second character and continue till the end.__

## Save your project { .save}

##Challenge: Printing the right way {.challenge}
Find another way to print the new word from the second letter onwards. Hint: You can look up iterating through strings.

# Step 7: Finishing Up { .activity }

The final step a.k.a Beautifying the code.

## Activity Checklist { .check }

+ Display a final sentence and remove the sentence displaying the user input:
	![screenshot](encode.jpg)

+ _Always remember to add comments when necessary and give proper spacing in the code to make it more readable:_
	![screenshot](final.jpg)

## Save your project { .save }
## Test your project { .flag }

## Challenge: Different translations {.challenge}
Modify your code to add different suffix to the word and also to change the word by moving the first two letters to the last.

## Challenge: Decoder {.challenge}
Using the same logic as this program, try to make a decoder that can convert PygLatin into normal English.
